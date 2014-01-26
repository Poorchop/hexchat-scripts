function Stream (
	[Parameter(Mandatory = $true)]
	[string] $FileName,
	
	[Parameter()]
	[string] $Arguments = '',
	
	[Parameter(ValueFromPipeline = $true)]
	[System.IO.Stream] $InputStream = $null,
	
	[Parameter()]
	[switch] $OutputStream = $false
) {
	$processStartInfo = New-Object System.Diagnostics.ProcessStartInfo
	$processStartInfo.FileName = $FileName
	$processStartInfo.Arguments = $Arguments
	$processStartInfo.RedirectStandardInput = ($InputStream -ne $null)
	$processStartInfo.RedirectStandardOutput = $OutputStream
	$processStartInfo.UseShellExecute = $false
	$processStartInfo.WorkingDirectory = $PWD

	$process = [System.Diagnostics.Process]::Start($processStartInfo)

	if ($OutputStream) {
		$process.StandardOutput.BaseStream
	}

	if ($InputStream -ne $null) {
		$processInputStream = $process.StandardInput.BaseStream
		
		$InputStream.CopyTo($processInputStream)
		
		$processInputStream.Close()
	}

	$process.WaitForExit()
}

# Stream 'F:\Visual Studio\Test\Test\bin\Debug\Test.exe' -Arguments 'D:\*.ps1' -OutputStream | Stream 'F:\Visual Studio\Test\Test\bin\Debug\Test.exe' -OutputStream | Stream 'F:\Visual Studio\Test\Test\bin\Debug\Test.exe'
