import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.0.0.8/api/'
username= 'ignw'
password = 'ignw'

payload1 = '''
{
  "securityLevel": 100,
  "kind": "object#GigabitInterface",
  "channelGroupMode": "active",
  "flowcontrolLow": -1,
  "name": "inside",
  "duplex": "auto",
  "forwardTrafficSFR": false,
  "hardwareID": "GigabitEthernet0/0",
  "mtu": 1500,
  "lacpPriority": -1,
  "flowcontrolHigh": -1,
  "ipAddress": {
    "ip": {
      "kind": "IPv4Address",
      "value": "10.255.255.1"
    },
    "kind": "StaticIP",
    "netMask": {
      "kind": "IPv4NetMask",
      "value": "255.255.255.240"
    }
  },
  "flowcontrolOn": false,
  "shutdown": true,
  "interfaceDesc": "Uplink to core",
  "managementOnly": false,
  "channelGroupID": "",
  "speed": "auto",
  "forwardTrafficCX": false,
  "flowcontrolPeriod": -1
}
'''

headers = {'Content-Type': 'application/json'}

resp = requests.put(f'{url}interfaces/physical/GigabitEthernet0_API_SLASH_0',auth=(username, password), data=payload1, headers=headers, verify=False)
print(f'Response:{resp}')
print(f'Status Code:{resp.status_code}')
print(resp.text)
