max=26
def getch():
    ch=input("Encrypt or decrypt(E/D)?:")
    if(ch=='D' or ch=='d' or ch=='e' or ch=='E'):
        return ch
    else:
        print("Enter E or D Only")
        getch()

def getmsg():
    msg=input("Enter your msg:")
    return msg



def logic(ch,msg,key):
    if ch=='d':
        key = -key
    final=''

    for x in msg:
        if x.isalpha():
            num=ord(x)
            num+=key

            if x.isupper():
                if num>ord('Z'):
                    num -=26
                elif num <ord('A'):
                    num+=26
            elif x.islower():
                if num > ord('z'):
                    num -=26
                elif num <ord('a'):
                    num+=26

            final+=chr(num)
        else:
            final+=x
    return final

ch=getch()
msg=getmsg()
key=25
print('Your translated text is:')
print(logic(ch, msg, key))
