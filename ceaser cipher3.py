print("You have option:\n1.Encryption\n2.Decryption")
def Encryption():
    message=input("Enter Your message:")
    key=int(input("Enter The key(1-26):"))
    Encrypted_text=""
    for i in message:
        if (i.isalpha()==True):
            y=ord(i)+key
            if(y>122):
                z=y-122
                z=z+96
                Encrypted_text+=chr(z)
            else:
                Encrypted_text +=chr((y))
        else:
            Encrypted_text+=i
    return Encrypted_text
def Decryption():
    message=input("Enter Your message:")
    key=int(input("Enter The key(1-26):"))
    Encrypted_text=""
    for i in message:
        if (i.isalpha()==True):
            y=ord(i)-key
            if(y<97):
                z=122-key+1
                Encrypted_text +=chr(z)
            else:    
                Encrypted_text +=chr((y))
        else:
            Encrypted_text+=i
    return Encrypted_text
a=int(input("Please Chose you option:"))
if a==1:
    b=Encryption()
    print(b)
elif(a==2):
    c=Decryption()
    print(c)
else:
    print("Wrong Input")        