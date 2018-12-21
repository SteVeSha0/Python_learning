import random
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('your number is too low.')
    elif guess > secret_number:
        print('your number is too high.')
    else:
        break

if guess == secret_number:
    print('Good! you find the right number! the right number is : ' + str(secret_number) + '!' )
else:
    print('Nope, you failed. the right number is ' + str(secret_number) + '!')