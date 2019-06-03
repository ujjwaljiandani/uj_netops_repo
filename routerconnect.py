import pexpect
import re

username = 'ignw'
password = 'ignw'
device_ip = '10.0.0.5'

connection = pexpect.spawn("ssh "+username+"@"+device_ip)
print(connection)
print(type(connection))
