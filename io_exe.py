# 1
def user_message():
    user_message=input("enter a message:")
    return user_message
# 2
def Encode_message(user_message):
    key = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'," ":" " }
    user_message=user_message.upper()
    e_message=""
    for l in user_message:
            l = key[l]
            e_message+=l
    return e_message
# 3
def save_to_file(Encode_message):
    with open("secret.txt","w") as f:
        f.write(Encode_message)

user_message1=user_message()
Encode_message1=Encode_message(user_message1)
save_to_file1=save_to_file(Encode_message1)
# 4
def read_emessage():
    with open ("secret.txt") as f :
        return(f.read())
        
read_emessage1=read_emessage()
# 5
def decode_message(read_emessage1):
    input("Message decoder")
    key = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'," ":" " }
    e_message=""
    for l in read_emessage1:
            l = key[l]
            e_message+=l
    return e_message
print("Encrypted message",read_emessage1)
print(decode_message(read_emessage1))

        
    
