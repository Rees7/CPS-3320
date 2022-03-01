
num = int(input('Please enter a number:'))
while 1:
    if (num > 0):
        print('This number is positive')
        if num%2==0 or num%3==0 or num%4==0:
            print('This number is multiple of 2, 3, 4')
        else:
            print('This number is not multiple of 2, 3, 4')

        print('End of Program')
        break
    else:
        print('the number is not positive')
        num = int(input("Please re-enter a number:"))

