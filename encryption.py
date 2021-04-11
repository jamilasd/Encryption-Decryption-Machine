
# coding: utf-8

# ## Encryption Machine
# ### Created by: Jamila Smith-Dell
# #### April 11, 2021
# ![Windows](encryption_image.png)

# ## Import the relevant libraries

# In[1]:


import math
import random
import string


# ## Function that checks if numbers are prime or not
# This function will be used to check if the user inputted values for p and q are actually prime. If not, it will notify the user that the number is not prime so they can choose again.

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
    
    if number >= 13:
        for i in range(2, number):
            if number % i == 0:
                print(f'{number} is not a prime number.')
                check = False
                break
            else:
                print(f'{number} is a prime number, perfect!')
                check = True
                break
    else:
        print(f'{number} is not greater than 13.')
        check = False
        
    return check


# ## Ask the user for prime numbers: p & q
# This while loop will run the prime_check function above to check the user input and prompt for them to input another number if needed.

# In[3]:


p = 1

while p != "q":
    p = input('Please type "q" to quit. Please select a prime number (p) that is greater than or equal to 13: ')
    if p =='q':
        break
    else: 
        p = int(p)
        check = prime_check(p)
        if check == False:
            p = int(input('Please select a prime number (p) greater than or equal to 13: '))
        else: 
            check = True
            while check:
                q = int(input('\nPlease select a prime number (q), greater than p (i.e. 17): '))
                if q > p:
                    check = prime_check(q)
                    if check == False:
                        q = int(input('\nPlease select a (q) that is greater than p and is prime (i.e. 17): '))
                    else:
                        break
            print(f'\nGreat job! p = {p} and q = {q}\n')            
            break


# ## Ask the user for a value for e
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

e = input(f'Please type "q" to quit. Please choose a number greater than 1 and less than {phi_n} (i.e. 5): ')

check_e = True

while check_e:
    if e == "q":
        break
    else:
        e = int(e)
        if e > 1 and e < 10:
            if e < phi_n:
                if math.gcd(phi_n, e):
                    print(f'Awesome! There is no greatest common divisor between {phi_n} and {e}.\n')
                    break
                else:
                    print('')
                    e = int(input(f'Something is wrong. Please choose a different value for e (i.e. 5). '))
            else:
                e = int(input(f'Something is wrong. Please choose a different value for e (i.e. 5). '))
        else:
            e = int(input(f'Please choose a value for e that is less than 10 (i.e. 5). '))


# ## Function to calculate the private key (d)
# Calculate the private key and check to make sure all other importnant encryption variables are integers.

# In[5]:


def private_key():
    """
    This function creates the private key (d) for the encryption machine
    and calculates the n and phi_n values as well.
    
    Arguments: 
    - None. It uses the values of p, q, and e from the user input above
    
    Outputs:
    - Prime numbers: p and q
    - Private key: d
    - Other encryption variables: e, n, phi_n, and i
    """
    i = random.randint(1,100)

    d = int((i * phi_n + 1) / e)
    
    return p, q, n, phi_n, e, d, i


# In[6]:


private_key()


# ## Create the Public Key
# 'Letters' is a dictionary with string keys mapped to integer values. The c_list is the list of cipher values that are calculated using the integer values from the dictionary. We will use the c_list as the public key from here on out.

# In[7]:


letters = {}
value = 0


for letter in string.ascii_lowercase:
    value += 1
    letters[letter] = value

#add common punctuation
punctuation = [' ','.',"’","'","!","?","/",",",'"',":"]


for punct in punctuation:
    value += 1
    letters[punct] = value

c_list = [] #cipher list

for letter in letters:
    c = (letters[letter] ** e) % n
    c_list.append(c)


# ## Encryption
# Here the user will input the message that they want encrypted. The result will then be printed as a list that should be copied over to the decryption machine for decryption.

# In[8]:


def return_encryption():
    """
    This function creates the encryption list from the message the user 
    provides using the cipher list and letters dictionary. 
    
    Arguments: 
    - User input for the message to encrypt
    
    Outputs:
    - A message telling the use that they encryption was successful
    - List of calculated encryption values
    
    """
    
    encryption = input('What message do you want to encrypt? ').lower()

    encrypt_list = []

    for value in encryption:
        c = (letters[value] ** e) % n
        encrypt_list.append(c)

    encrypt_list_str = []

    for value in encrypt_list:
        encrypt_list_str.append(str(value))

    encryption_result = ' '.join(encrypt_list_str)
    print(f'\nYour encryption was successful! Here is the result: {encrypt_list} \n\n\n')
    
    return encrypt_list


# In[9]:


return_encryption()


# In[10]:


print('Please copy this encryption list, run the decryption.py file, and paste the encryption list when prompted.')
print(f'\n\n\n')

