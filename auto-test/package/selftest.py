import json
data='{"data": [{"groupname": "default", "latestversion": "2.0.1011.0", "devices": [{"status": "1", "devicename": "TIM-PC", "assettag": "", "ip": "10.21.144.80", "lastcontacttime": "1504166869", "version": "2.0.1011.0", "command": {}, "deviceid": "4B6206E22FB54BA389C5", "os": "Windows 7 32Bit"}]}]}'
print data
json2=json.loads(data)
print json2
print json2['data'][0]['devices'][0]['deviceid']