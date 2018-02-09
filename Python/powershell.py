import winrm
import json
session = winrm.Session('192.168.178.123', auth=('admin','admin'))
result = session.run_ps("Get-ChildItem | Select-Object -Property Name,Mode | ConvertTo-Json")
out=result.std_out.decode("utf-8")
obj = json.loads(out)
for item in obj:
    print(item['Name']+" "+item['Mode'])