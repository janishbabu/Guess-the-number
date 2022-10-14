import random
number = random.randint(0, 100)
print(number)
count = 0
while count < 5:
    guess = (input('Enter your guess number'))
    if type(guess) == int:
        if guess < number:
            print('Your Guess was Low')
            count = count+1
            print('you guess chance is :', 5-count)
        if guess > number:
            print('Your Guess was High')
            count = count + 1
            print('your Guess chance is:', 5-count)
        if guess == number:
            print('Congratulations Your answer is correct')
            break
    else:
        print('please enter valid number')
        break
print('corrct answer is ', number)
