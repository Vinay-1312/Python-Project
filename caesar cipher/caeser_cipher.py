# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 16:44:37 2022

@author: DELL
"""

def Encrypt(message,shiftnumber):
    new_message = ""
    for i in message:
        encrypt_letter_value = ord(i) + shiftnumber
        ### for uppercase and lowercase 
        
        if (ord(i) >= 97 and ord(i)<=122):
            limit = 122
        else:
            limit = 90
        
            
       
        if (ord(i) == 32):
            encrypt_letter_value = 32 
        else:
             if encrypt_letter_value > limit:
                 encrypt_letter_value = encrypt_letter_value - 26
            
        new_message = new_message + chr(encrypt_letter_value)
    return new_message

    pass

def Decrypt(message,shiftnumber):
    new_message = ""
    for i in message:
        if (ord(i) >= 97 and ord(i)<=122):
            limit = 97
        else:
            limit = 65
        dcrypt_letter_value = ord(i) - shiftnumber
        
        if (ord(i) == 32):
            dcrypt_letter_value = 32 
        else:
            if dcrypt_letter_value < limit:
                dcrypt_letter_value = dcrypt_letter_value + 26
        new_message = new_message + chr(dcrypt_letter_value)
    return new_message

    pass

shift_number = int(input("enter a shift number"))
message = input("enter message")

encrypted_message = Encrypt(message,shift_number)
dcrypted_message = Decrypt(encrypted_message,shift_number)
print(encrypted_message)
print(dcrypted_message)

print()


