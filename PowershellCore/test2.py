import subprocess
import json
data = subprocess.getoutput("pwsh test2.ps1")
obj = json.loads(data)
for item in obj:
    print(item['Name'])
