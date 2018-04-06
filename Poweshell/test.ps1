Write-Host "Powershell Version: $($PSVersionTable.PSVersion)" -BackgroundColor DarkBlue
for ($i = 0,$i -lt 5; $i++) {
    Write-Host "$i Works";
    Write-Host "test"
}