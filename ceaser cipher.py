"""\t\t\t\t\tJai Maa"""
"""\t\t\t\tMy First poject"""
class ceasercipher():
    def __init__(self,plain_text_message,key):
        self.plain_text_message=plain_text_message
    
    
    
    def Encryption(self,plain_text_message,key):
        self.plain_text_message=plain_text_message
        self.key=key
        self.encrypted_text=""
        for i in range(len(self.plain_text_message)):
            if ord(self.plain_text_message[i]==32):
                self.encrypted_text +=chr(ord(self.plain_text_message[i]))
        
            elif (ord(self.plain_text_message[i]+key))>122:
                temp=(ord(self.plain_text_message[i]+key))-122
                self.encrypted_text +=chr(96+temp)
            
            elif (ord(self.plain_text_message[i]+key)>90) and (ord(self.plain_text_message[i])<=96):
                temp=(ord(self.plain_text_message[i])+key)-90
                self.encrypted_text +=chr(ord(self.plain_text_message[i])+key)
        return(self.encrypted_text)       
    
    
    def decryption(self,Encrypted_message,key):
        self.Encrypted_message=Encrypted_message

print("You Have this Choices \n1.encryption \n2.decryption")
a=int(input("Enter The Choice"))
if   a==1:
    y=input("Enter The Messsage:")
    b=int(input("Enter your key(1-26):"))
    x=ceasercipher(y,b)
    print("Your Encrypted Message is:",x.Encryption(y,b))
elif a==2:
    print("Your decrypted message is:")
else:
    print("Wrong choice please chose correct")

     
  

    
    
           

