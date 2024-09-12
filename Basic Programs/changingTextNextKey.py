def CustomCaesarCipher(key,message):
    if(key<0):
        print("Invalid")
    else:
        strEm=""
        for i in range(len(message)):
            ch=message[i]
            if(ch.isupper()):
                strEm=strEm+chr( (ord(ch)+key-65)%26 + 65 )
            elif(ch.islower()):
                strEm=strEm+chr((ord(ch)+key-97)%26 + 97)
            elif(ch.isdigit()):
                strEm=strEm+ str(int(strEm))+key
            elif(ch.isspace()):
                strEm+=" "
            elif(ch=="-"):
                strEm+="-"
    print(strEm)   

message=input("Enter a string:")
key=int(input("Enter a num:"))
CustomCaesarCipher(key,message)


