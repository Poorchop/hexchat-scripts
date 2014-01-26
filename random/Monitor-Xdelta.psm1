# First import the module
# 
# PS> Import-Module Monitor-Xdelta.psm1
# 
# 
# To start monitoring:
# 
# PS> $job = Begin-XdeltaMonitor .
# 
# 
# To end monitoring:
# 
# PS> End-XdeltaMonitor $job
# 
# ... or just close the PS window to stop the monitoring

function Begin-XdeltaMonitor (
	[Parameter(Mandatory = $true)]
	[string] $Directory,
	
	[Parameter()]
	[switch] $DontRunOnExisting = $false
) {
	$watcher = New-Object System.IO.FileSystemWatcher -ArgumentList $Directory,'*.xdelta'
	
	Register-ObjectEvent -InputObject $watcher -EventName 'Created' -Action {
		Process-Xdelta -FilePath $args[1].FullPath
	}
	
	if (-not $DontRunOnExisting) {
		Get-ChildItem -Path . -Include *.xdelta | %{ Process-Xdelta $_.FullName }
	}
}

function End-XdeltaMonitor (
	[Parameter(Mandatory = $true)]
	$Job
) {
	UnRegister-Event -SubscriptionId $Job.Id
}

function Process-Xdelta (
	[Parameter(Mandatory = $true)]
	[string] $FilePath
) {
	Write-Host "[$(Get-Date)] $FilePath"
	
	Write-Host $(xdelta3 -d $FilePath)
	
	Remove-Item $FilePath
}
