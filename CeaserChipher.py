# A python program to illustrate Caesar Cipher Technique
def encrypt(text, S):
    result = ""
    
    # traversing the text 
    for i in range(len(text)):
        char = text[i]

        # Encryption for UpperCase Character 
        if (char.isupper()):
            result += chr((ord(char) + S - 65) % 26 + 65)
        # Encryption for LowerCase Character 
        else:
            result += chr((ord(char) + S - 97) % 26 + 97)
    # Returning the result 
    return result    # //output should Produce ATTACKATONCE -------- EXXEGOEXSRGI



# A python program to illustrate Caesar Cipher Technique
def decrypt(text, S):
    result = ""
    
    # traversing the text 
    for i in range(len(text)):
        char = text[i]

        # Decryption for UpperCase Character 
        if (char.isupper()):
            result += chr((ord(char) - S - 65) % 26 + 65)

        # Decryption for LowerCase Character 
        else:
            result += chr((ord(char) - S - 97) % 26 + 97)

    # Returning the result 
    return result    # //output should Produce  EXXEGOEXSRGI ------------ ATTACKATONCE


# Finally Calling the function 
text = "EXXEGOEXSRGI"
s = 4
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + decrypt(text,s))
