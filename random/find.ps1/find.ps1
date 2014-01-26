param (
	[Parameter(Mandatory = $true)]
	[string[]] $Name,

	[Parameter(Mandatory = $true)]
	[string[]] $Pattern,

	[Parameter()]
	[switch] $IgnoreCase = $false,
	
	[Parameter()]
	[ValidateSet('AllInLine', 'AllInFile', 'Any')]
	[string] $MatchMode = 'AllInLine',
	
	[Parameter()]
	[switch] $OnlyMatching = $false
)

Add-Type -Language CSharp -TypeDefinition @"
	public class MatchInfoEqualityComparer : System.Collections.Generic.IEqualityComparer<Microsoft.PowerShell.Commands.MatchInfo>
	{
		public bool Equals(Microsoft.PowerShell.Commands.MatchInfo x, Microsoft.PowerShell.Commands.MatchInfo y)
		{
			return x.Path == y.Path && x.LineNumber == y.LineNumber;
		}
	
		public int GetHashCode(Microsoft.PowerShell.Commands.MatchInfo obj)
		{
			return obj.LineNumber;
		}
	}
"@ -ReferencedAssemblies Microsoft.PowerShell.Commands.Utility

Add-Type -Language CSharp -TypeDefinition @"
	public class MatchResult
	{
		public System.IO.FileInfo File { get; private set; }
		public int LineNumber { get; private set; }
		public string Line { get; private set; }
		
		public MatchResult(System.IO.FileInfo file, int lineNumber, string line) {
			File = file;
			LineNumber = lineNumber;
			Line = line;
		}
	}
"@ -ReferencedAssemblies Microsoft.PowerShell.Commands.Utility

if ($(Get-FormatData -TypeName MatchResult) -eq $null) {
	Update-FormatData -PrependPath ($(Split-Path $script:MyInvocation.MyCommand.Path) + '\find-results.format.ps1xml') 2>$null
}

$equalityComparer = New-Object MatchInfoEqualityComparer

Get-ChildItem -Path * -Include $Name -Recurse -Force | ?{ $_ -is [System.IO.FileInfo] } | %{
	$file = $_;
  
	[System.Collections.Generic.ICollection[Microsoft.PowerShell.Commands.MatchInfo]] $result = $null;
	
	if ($MatchMode -eq 'Any') {
		$params = @{
			Pattern = $Pattern
		}
		if (-not $IgnoreCase) {
			$params.CaseSensitive = $true
		}

		[Microsoft.PowerShell.Commands.MatchInfo[]] $currentResult = Select-String @params $file
		$result = $currentResult
	}
	else {
		$Pattern | %{
			$params = @{
				Pattern = $_
			}
			if (-not $IgnoreCase) {
				$params.CaseSensitive = $true
			}

			[Microsoft.PowerShell.Commands.MatchInfo[]] $currentResult = Select-String @params $file
			if ($currentResult -eq $null) {
				$currentResult = New-Object Microsoft.PowerShell.Commands.MatchInfo[] 0
			}
			
			if ($result -eq $null) {
				$result = New-Object System.Collections.Generic.HashSet[Microsoft.PowerShell.Commands.MatchInfo] -ArgumentList $currentResult,$equalityComparer
			}
			else {
				switch ($MatchMode) {
					'AllInFile' {
						if ($result.Count -gt 0 -and $currentResult.Length -gt 0) {
							$result.UnionWith($currentResult)
						}
						else {
							$result.Clear()
							return
						}
					}
					
					'AllInLine' {
						if ($result.Count -gt 0 -and $currentResult.Length -gt 0) {
							$result.IntersectWith($currentResult)
						}
						else {
							$result.Clear()
							return
						}
					}
				}
			}
		}
	}
	
	if ($result.Count -gt 0) {
		if ($OnlyMatching) {
			$result | %{
				New-Object -TypeName MatchResult -ArgumentList $file,$_.LineNumber,$_.Matches[0].Value
			}
		}
		else {
			$result | %{
				New-Object -TypeName MatchResult -ArgumentList $file,$_.LineNumber,$_.Line
			}
		}
	}
}
