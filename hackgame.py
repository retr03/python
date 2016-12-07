user = 'admin'
password = 'password'
user1 = input('enter the username:')

while user1 == user:
	print('correct user')
	break
else:
	print('try again')

user2 = input('enter the paswword:')

while user2 == password:
	print('access granted')
	break
else:
        print('try again')

a = 'a)1. access the files.'            
b = 'b)2. hack targets'
c = 'c)3. ddos'
d = 'd)4. notes'
e = 'e)5. generate a new ip or mac adress'
f = 'f)6. quit/log out'
g = 'g)7. hack wifi'
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

action = input('hacker:\\admin =>..')


if action == a:
        print('would you like a text file or a picture file or a video file?')
        files =('enter the directroty e.g C:\\users\bob\desktop\text.txt')

while 'a' == 'a':
        input('this file is empty')
        break 

if action == 'b':
       targets = input('type in targets ip')
       list = ['10101010101010 loading.....']
       print(list * 100)
       print('this is ' + targets + 'machine')
       des=input('do you want to fry their system with a deadly virus y:n:')
       if des == 'y':
                           print(list*100)
                           print('system fried')
                           botnet = 0
                           botnet + 100
                           print('your botnet has' + str(botnet) + 'power')
if  action == 'c':
        website = input('type in the web address of your target')
        list2 = [1,0,0,1,0,1,0]
        print(list2 * 100)
        print('website down')

if action == 'd':
        note = input('type press enter when done')

import random

do_you = input('mac or ip')
if action == 'e' and do_you == 'ip':
                ip = [167,67,678,0]
                random.shuffle(ip)
                print(ip)
do_you = input('mac or ip')

if do_you == 'mac':
        mac = ['a','c','b','v','f','e,' 'j','6','7','5','4']
        random.shuffle(mac)
        print(mac)

if action == f:
        quit()
else:
        print('are you sure')

if action == 'g':
        ssid = input('enter the name of the target network')
        load = 'cracking ...'
        print(load *100)
        print('sucsessfully cracked network')
else:
        print('fail')


