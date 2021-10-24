import random  



def computer_guess(x):
    low = 1   # we need to set the range that we will be dealing with 
    high = x   # until the user can rovid some feedback we need to be able to tell the computer if its too high or too low or correct 
    feedback = ''   # so we need a feedback variable, right now we just need something to work with so ''
    # correct = c 
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)   # if the comp gets it wrong then it guesses again using a random number between low and high.... within the bounds of what we know is correct 
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? '.lower())
        if feedback == 'h':
            high = guess - 1   # if it is too high then minus one 
        elif feedback == 'l':
            low = guess + 1  # if it is too low then + one
            
    print(f'Yay! The computer guessed your number {guess}, correctly! ')  # guess was the last number 
    

computer_guess(10)

# guess(10)  