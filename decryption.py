
# coding: utf-8

# ## Decryption Machine
# ### Created by: Jamila Smith-Dell
# #### April 11, 2021
# 
# ![Windows](decryption_image.png)

# ## Import the relevant libraries

# In[9]:


import math
import random
import string


# ## Import relevant variables from the Encryption Machine
# In order to bring over the shared variables between the encryption and decryption machines, I will ask which prime numbers the user chose for the encryption.

# In[8]:


p = int(input('For the encryption, what number did you choose for p? '))
q = int(input('For the encryption, what number did you choose for q? '))
e = int(input('For the encryption, what number did you choose for e? '))

n = q * p

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

print(f'\nGreat! p = {p}, q = {q}, e = {e}\n')


# ## Decryption
# Here the user will provide the list they got at the end of the encryption process and will receive a decrypted message in return once they opt to decrypt the message. I'm assuming the message is private, and in everyday circumstances, you wouldn't want a secure message to print unless you're ready.

# In[ ]:


def decryption():
    """
    This function decrypts the encryption list from the encryption machine 
    back to a message that is readable. 
    
    Arguments: 
    - User input for the encryption list that will be decrypted
    
    Outputs:
    - A user input prompt asking the user if they want to decrypt the private message
    - String with the message that was decrypted which is the original message that was 
    provided to the encryption machine
    """
    
    encrypt_result = input('What message are you trying to decrypt? Hint, please paste the encryption result here: ')
    encrypt_result = encrypt_result.replace('[','').replace(']','').replace(' ','').split(',')
    
    print(f'\n\n')

    encrypt_list = []
    
    for value in encrypt_result:
        value_int = int(value)
        encrypt_list.append(value_int)
    
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
            print(f'\nYour decryption was successful! The message is: \n\n\t{decryption}\n')
            break
        elif decrypt_request == 'q':
            break
        else:
            print('Please type either "y" or "n".')
            decrypt_request = input('Would you like to decrypt this secure message (y/n)? ')
            
    return decryption


# In[ ]:


decryption()

