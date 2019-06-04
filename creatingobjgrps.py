import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.0.0.8/api/'
username= 'ignw'
password = 'ignw'

resp = requests.get(f'{url}interfaces/physical/',auth=(username, password), verify=False)
#resp = requests.get(f'{url}i/api/interfaces/physical/GigabitEthernet0_API_SLASH_1',auth=(username, password), verify=False)
#resp = requests.get(f'{url}i/api/interfaces/physical/GigabitEthernet0_API_SLASH_2',auth=(username, password), verify=False)
print(f'Response:{resp}')
print(f'Status Code:{resp.status_code}')
print(dir(resp))

resp_dict = json.loads(resp.text)

ints_qty = resp_dict['rangeInfo']['total']
ints_names = []
ints_ips = []

for i in resp_dict['items']:
	ints_names.append(i['name'])
	ints_ips.append(i['ipAddress'])

print('Inf Names:')
print(ints_names)
print('Inf IPs:')
print(ints_ips)	
payload = '''
{
	"host": {
		"kind": "IPv4Address",
		"value": "{}.{}.{}.{}"
	},
	"kind": "object#NetworkObj",
	"name": "leGoogle",
	"objectId": "leGoogle"
}
'''


