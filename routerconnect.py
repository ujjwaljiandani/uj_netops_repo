import pexpect
import re

username = 'ignw'
password = 'ignw'
device_ip = '10.0.0.5'

#connection = pexpect.spawn("ssh "+username+"@"+device_ip)
connection = pexpect.spawn(f'ssh {username}@{device_ip}')
#print(connection)
#print(type(connection))

connection.expect('Are you sure you want to continue connecting (yes/no)?')
connection.sendline('yes')
connection.expect('Password:')
connection.sendline(password)
