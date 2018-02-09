$out= Get-ChildItem | Select-Object -Property Mode,Name,Length
$out | ConvertTo-Json