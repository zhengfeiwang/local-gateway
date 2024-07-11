# interception.ps1
# This script manages the interception setup, allowing you to start and stop mitmproxy and the system proxy

param (
    [string]$action = "start"
)

# Define variables
$proxyAddress = "127.0.0.1:8080"
$registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"

# Function to set system proxy
function Set-SystemProxy {
    Set-ItemProperty -Path $registryPath -Name ProxyServer -Value $proxyAddress
    Set-ItemProperty -Path $registryPath -Name ProxyEnable -Value 1

    # Notify the system about the proxy settings change
    $internetSettings = New-Object -ComObject InternetExplorer.Application
    $internetSettings.Quit()
}

# Function to unset system proxy
function Unset-SystemProxy {
    Set-ItemProperty -Path $registryPath -Name ProxyEnable -Value 0

    # Notify the system about the proxy settings change
    $internetSettings = New-Object -ComObject InternetExplorer.Application
    $internetSettings.Quit()
}

# Main script logic
if ($action -eq "start") {
    Set-SystemProxy
} elseif ($action -eq "stop") {
    Unset-SystemProxy
} else {
    Write-Output "Invalid action. Use 'start' or 'stop'."
}
