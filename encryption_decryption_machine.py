
# coding: utf-8

# ## Encryption Decryption Machine
# ### Created by: Jamila Smith-Dell
# #### April 3, 2021

# #### Import the relevant libraries

# In[1]:


import math
import random


# #### Create a function that can check if p and q are prime or not
# 
# I will use user input to define p and q so I'll need a way to make sure the numbers are actually prime and q is actually greater than p.

# In[2]:


def prime_check(number):
    
    """
    This function checks if a number is prime or not, 
    if the number is greater than 1, and if q is greater than p.
    
    Arguments: 
    - Any number
    
    Outputs:
    - Error message if the number is not prime or not greater than 1
    - Error message if q is less than p
    - Success message if the number is prime
    - The boolean of the 'check' variable if the number is prime or not
    
    """
    
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(f'{number} is not a prime number, please choose again!')
                check = False
                break
            else:
                print(f'{number} is a prime number, perfect!')
                check = True
                break
    else:
        print(f'{number} is not greater than 1, please choose again.')
        check = False
        
    return check


# #### Ask the user for a prime number
# This while loop will run the prime_check function above to check the user input and prompt for them to input another number if needed.

# In[3]:


p = 1

while p != "q":
    p = input('Please type "q" to quit. Please select a prime number (p): ')
    if p =='q':
        break
    else: 
        p = int(p)
        check = prime_check(p)
        if check == False:
            p = int(input('Sorry! Please select an a prime number (p) greater than 1: '))
        else: 
            check = True
            while check:
                q = int(input('\nPlease select a prime number (q), greater than p: '))
                if q > p:
                    check = prime_check(q)
                    if check == False:
                        q = int(input('\nPlease select an actual prime number (q), greater than p: '))
                    else:
                        break
            print(f'\nGreat job! p = {p} and q = {q}')            
            break


# #### Ask the user for a value for e
# I will then use a series of if statements to make sure phi_n is not divisible by e and e is greater than 1 and less than phi_n.

# In[4]:


if p and q:
    n = p * q
    phi_n = int((p - 1) * (q - 1))
else: 
    default_p = 13
    default_q = 17
    n = default_p * default_q
    phi_n = int((default_p - 1) * (default_q - 1))

e = input(f'Please type "q" to quit. Please choose a number greater than 1 and less than {phi_n}: ')

check_e = True

while check_e:
    if e == "q":
        break
    else:
        e = int(e)
        if e > 1 and e < 10:
            if e < phi_n:
                if math.gcd(phi_n, e):
                    print(f'Awesome! There is no greatest common divisor between {phi_n} and {e}: .')
                    break
                else:
                    print('')
                    e = int(input(f'Something is wrong. Please choose a different value for e. '))
            else:
                e = int(input(f'Something is wrong. Please choose a different value for e. '))
        else:
            e = int(input(f'Please choose a value for e that is less than 10. '))


# #### Calculate the private key (d)
# Check to make sure all numbers are integers.

# In[5]:


i = random.randint(1,100)

d = int((i * phi_n + 1) / e)

print(f'\np = {p} \nq = {q} \nn = {n} \nphi_n = {phi_n}         \ne = {e} \nd = {d} \ni = {i}') 


# #### Encrypt using a public key
# The c_list is the list of cipher values.

# In[ ]:


letters = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    ' ': 27,
    '.': 28,
    "'": 29,
    "’": 30,
          }

c_list = [] #cipher list

for letter in letters:
    c = (letters[letter] ** e) % n
    c_list.append(c)
    
# print(c_list) #just to check that it worked


# #### Test Encryption
# User inputs the message that they want encrypted. The result is printed without spaces or punctiation.

# In[ ]:


encryption = input('What message do you want to encrypt? ').lower()

encrypt_list = []

for value in encryption:
    c = (letters[value] ** e) % n
    encrypt_list.append(c)

encrypt_list_str = []

for value in encrypt_list:
    encrypt_list_str.append(str(value))
    
encryption_result = ''.join(encrypt_list_str)
print(f'\nYour encryption was successful, here is the result: {encryption_result}.')


# #### Test Decryption
# The recipient of the encrypted message can then check to see what the message is.

# In[ ]:


decryption_list = []
values_list = list(letters.keys())

for number in encrypt_list:
    if number in c_list:
        position = c_list.index(number)
        decryption_list.append(values_list[position])
        
# print(decryption_list) #just to check

raw_decryption = ''.join(decryption_list)
decryption_sentences = raw_decryption.split('. ')

new_sentences = []
for sentence in decryption_sentences:
    new_sentences.append(sentence.capitalize())

decryption = '. '.join(new_sentences)

decrypt_request = input('Type "q" to quit. Would you like to decrypt this secure message (y/n)? ')

while decrypt_request:
    if decrypt_request == 'n':
        print('Sorry! You must type "y" to decrypt this message. ')
        decrypt_request = input('Would you like to decrypt this secure message (y/n)? ')
    elif decrypt_request == 'y':
        print(f'\nYour decryption was successful! The message is: \n\n\t{decryption}')
        break
    elif decrypt_request == 'q':
        break
    else:
        print('Please type either "y" or "n".')
        decrypt_request = input('Would you like to decrypt this secure message (y/n)? ')

