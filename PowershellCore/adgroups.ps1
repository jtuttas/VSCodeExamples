$sb = {
    Get-ADGroup -Filter *
}
$c = Get-Credential Administrator
Invoke-Command -ComputerName 192.168.178.123 -ScriptBlock $sb -Credential $c