import pexpect
import re

username = 'ignw'
password = '1111ignw'
device_ip = '10.0.0.5'

#connection = pexpect.spawn("ssh "+username+"@"+device_ip)
connection = pexpect.spawn(f'ssh {username}@{device_ip}')
#print(connection)
#print(type(connection))

connection.expect('Password:')
connection.sendline(password)
