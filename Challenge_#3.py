#Author: Michael McCoy
#Date: 6/5/2018
#Website: www.slashdba.com
#LinkedIn: https://www.linkedin.com/in/michael-p-mccoy/

#Function Definition
def myFunction (input_array):
    length = input_array.__len__()
    i = 0
    other_array = []

    for value in input_array:
        x = 0
        total = 1

        while (x < length):
            if (x != i):
                total = total * input_array[x]
            x = x + 1

        i = i + 1
        other_array.append(total)

    print('Original Array')
    print(input_array)
    print('')
    print('Final Array')
    print(other_array)
    print(' ')


#Driver
input_array = [1,5,6,2]
myFunction(input_array)

