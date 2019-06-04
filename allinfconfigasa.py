import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.0.0.8/api/'
username= 'ignw'
password = 'ignw'

payload1 = '''
{
  "securityLevel": 50,
  "kind": "object#GigabitInterface",
  "channelGroupMode": "active",
  "flowcontrolLow": -1,
  "name": "outside",
  "duplex": "auto",
  "forwardTrafficSFR": false,
  "hardwareID": "GigabitEthernet0/1",
  "mtu": 1500,
  "lacpPriority": -1,
  "flowcontrolHigh": -1,
  "ipAddress": {
    "ip": {
      "kind": "IPv4Address",
      "value": "203.0.113.1"
    },
    "kind": "StaticIP",
    "netMask": {
      "kind": "IPv4NetMask",
      "value": "255.255.255.192"
    }
  },
  "flowcontrolOn": false,
  "shutdown": true,
  "interfaceDesc": "Uplink to internet",
  "managementOnly": false,
  "channelGroupID": "",
  "speed": "auto",
  "forwardTrafficCX": false,
  "flowcontrolPeriod": -1
}
'''

payload2 = '''
{
  "securityLevel": 40,
  "kind": "object#GigabitInterface",
  "channelGroupMode": "active",
  "flowcontrolLow": -1,
  "name": "newsecurityzone",
  "duplex": "auto",
  "forwardTrafficSFR": false,
  "hardwareID": "GigabitEthernet0/2",
  "mtu": 1500,
  "lacpPriority": -1,
  "flowcontrolHigh": -1,
  "ipAddress": {
    "ip": {
      "kind": "IPv4Address",
      "value": "192.168.1.1"
    },
    "kind": "StaticIP",
    "netMask": {
      "kind": "IPv4NetMask",
      "value": "255.255.255.0"
    }
  },
  "flowcontrolOn": false,
  "shutdown": true,
  "interfaceDesc": "Uplink to LAB",
  "managementOnly": false,
  "channelGroupID": "",
  "speed": "auto",
  "forwardTrafficCX": false,
  "flowcontrolPeriod": -1
}
'''

headers = {'Content-Type': 'application/json'}

resp = requests.put(f'{url}interfaces/physical/GigabitEthernet0_API_SLASH_1',auth=(username, password), data=payload1, headers=headers, verify=False)
print(f'Response:{resp}')
print(f'Status Code:{resp.status_code}')
print(resp.text)

resp = requests.put(f'{url}interfaces/physical/GigabitEthernet0_API_SLASH_2',auth=(username, password), data=payload2, headers=headers, verify=False)
print(f'Response:{resp}')
print(f'Status Code:{resp.status_code}')
print(resp.text)

