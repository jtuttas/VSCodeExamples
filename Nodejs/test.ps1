param (
    $filter
)
$sb = {
    param (
        $filter="*"
    )   
    Get-ADGroup -Filter $filter | Select-Object -Property DistinguishedName,Name | ConvertTo-Json -Depth 3
}
#Write-Host "Filter ist $filter"
$username = "admin"
$password = "admin" | ConvertTo-SecureString -AsPlainText -Force
$cred = new-object -TypeName System.Management.Automation.PSCredential -argumentlist $username, $password
Invoke-Command -ScriptBlock $sb -Credential $cred -Authentication Negotiate -ComputerName 192.168.178.123 -ArgumentList $filter
