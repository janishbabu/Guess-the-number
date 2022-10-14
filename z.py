import random
number = random.randint(0, 100)
print(number)
count = 0
while count < 5:
    guess = int(input('Enter your guess number'))
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
print('corrct answer is ', number)