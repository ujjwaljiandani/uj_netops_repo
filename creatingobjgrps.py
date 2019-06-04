import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.0.0.8/api/'
username= 'ignw'
password = 'ignw'

resp = requests.get(f'{url}interfaces/physical/',auth=(username, password), verify=False)
print(f'Response:{resp}')
print(f'Status Code:{resp.status_code}')

resp_dict = json.loads(resp.text)

ints_qty = resp_dict['rangeInfo']['total']
ints_names = []
ints_ips = {}

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

for i in range(len(resp_dict['items'])):
	try:
		name = resp_dict['items'][i].get('name')
		key = resp_dict['items'][i]['ipAddress']['ip']['value']
		value = resp_dict['items'][i]['ipAddress']['netMask']['value']
		ints_ips[name] = key+' '+value
	except:
		pass

print(f'Int IPS:{ints_ips}')
