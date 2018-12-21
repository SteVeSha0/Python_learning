def collatz(number):   
    if number%2 == 0 :
        number = number // 2
        print(int(number))
        return number
    else:
        number = 3 * number + 1
        print(int(number))
        return number

def user_input():
    input_number = input()
    try:
        int(input_number)
    except ValueError:
        print('Please input a int type number !')
    return input_number

number = int(user_input())

while number != 1:
    number = collatz(number)
