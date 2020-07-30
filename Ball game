from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return (mylist)

def user_guess():
    
    guess=''
    
    while guess not in ['1', '2', '3']:
        
        guess = input("The ball is located at either the 1st, 2nd, or 3rd ball. Guess 1, 2 or 3")
        
    return int(guess)

def check_guess(gamelist,guess):
    if gamelist[guess-1]== 'o':
        print ('Correct!')
        print (gamelist)
    else:
        print ('Wrong guess!')
        print(gamelist)
        
# INITIAL LIST
initiallist = ['','o','']

#SHUFFLE LIST
mixed_list = shuffle_list(mylist)

# GUESS
guess = user_guess()

# CHECK GUESS
check_guess(mixed_list,guess)
