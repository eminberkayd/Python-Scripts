"""
Simple Password Generator 
You can customize the password.
"""


import random #necessary for randomly chosen passwords
import string


uppercaseLetters = string.ascii_uppercase
lowercaseLetters = string.ascii_lowercase
digits = string.digits
symbols = "!'^+%&/()=?#${[]}"

upper,lower,nums,syms = True, True, True, False # Change True with False when you want to not include that type of characters

all="" #creating an empty string

if upper:
    all+=uppercaseLetters
if lower:
    all+=lowercaseLetters
if nums:
    all+=digits
if syms:
    all+=symbols

length = 12 #You can change the length of the password from here
psw = []
for i in range(length):
    password="".join(random.sample(all,length))

print(password)

