import string
import random
import re
print ('\n  welcome to the password generator')

def register (user, pwd=None) :
    while True:
        pwd = input('type your password : ')
        if len(pwd) < 8:
            print("Make sure your password is at lest 8 letters")
            continue
        elif re.search('[0-9]', pwd) is None:
            print("Make sure your password has a number in it")
            continue
        elif re.search('[A-Z]', pwd) is None:
            print("Make sure your password has a capital letter in it")
            continue
        else:
            print("Your password seems fine")
            break
    pwdc = input(' please confirm your password : ')
    while pwd != pwdc :
        pwdc = input(' please confirm your main password : ')
        if pwdc == pwd :
            break
    with open('passwords.txt', 'a') as f :
        f.write( user + "|" + pwd + '\n')
    print("your account is created successfully")

def login () :
    user = input('\n please type your user name : ')
    test = False
    with open('passwords.txt', 'r') as f:
                while True:
                    for line in f.readlines():
                        data = line.rstrip()
                        usert, pwdt = data.split("|")
                        if user != usert:
                            continue
                        elif user == usert:
                            pwd = input('\n please type your password : ')
                            essays = 3
                            test = True
                            if pwd == pwdt:
                                print('welcome ' + user)
                                break
                            elif pwd != pwdt and essays > 0:
                                pwd = input('\n the password is incorrect ! try again : ')
                                essays -= 1
                                continue
                            elif pwd != pwdt and essays == 0:
                                print('you are out of essays')
                                break
                    if test == False :
                        print(" the user name is not correct !")
                        break

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()"+'1234567890')
def alea():
    password = []
    for i in range(15):
        password.append(random.choice(characters))
        random.shuffle(password)
        pwd = ("".join(password))
    print("your password is : " + pwd)
    with open('passwords.txt', 'a') as f:
        f.write(user + "|" + pwd + '\n')
    print("your account is created successfully")

def validate():
    while True:
        pwd = input('type your password : ')
        if len(pwd) < 8:
            print("Make sure your password is at lest 8 letters")
            continue
        elif re.search('[0-9]', pwd) is None:
            print("Make sure your password has a number in it")
            continue
        elif re.search('[A-Z]', pwd) is None:
            print("Make sure your password has a capital letter in it")
            continue
        else:
            print("Your password seems fine")
            return pwd


while True :
    print('\n for login press A')
    print('\n for signing in press B')
    choice = input('\n A or B :  ')
    choice = choice.upper()
    if choice == 'A' :
       login()
       continue
    elif choice == 'B':
        user = input(' please type your user name : ')
        while True :
            ts  = input (' press T to type your password or press S if you want a strong password :')
            ts = ts.upper()
            if ts == 'S' :
               alea()
               break
            elif ts == 'T' :
              register(user)
              break
    else :
       print(" please type a valid choice")
       continue