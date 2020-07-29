import random

#A function to shuffle all the characters of a string
def shuffle(string):
    random.shuffle(TempList)
    return ''.join(TempList)

#Main program starts here
uppercase_letter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercase_letter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercase_letter1=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
lowercase_letter2=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
first_digit= chr(random.randint(48,57))#Generate a random number between 0 and 9 (based on ASCII code)
second_digit= chr(random.randint(48,57)) #Generate a random number between 0 and 9 (based on ASCII code)
punctuation1= chr(random.randint(128,152)) #Generate a random punctuation sign (based on ASCII code)
punctuation2= chr(random.randint(128,152)) #Generate a random punctuation sign (based on ASCII code)

#Generate password using all the characters, in random order
TempList= list(uppercase_letter1+uppercase_letter2 + lowercase_letter1 + lowercase_letter2 + first_digit +second_digit + punctuation1 + punctuation2)
password = shuffle(TempList)

#Ouput
print (password)
