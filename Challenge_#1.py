#Author: Michael McCoy
#Date: 6/4/2018
#Website: www.slashdba.com
#LinkedIn: https://www.linkedin.com/in/michael-p-mccoy/


#Function Definition
def list_sum_k(num_list, k):
    result = 'No'
    length = num_list.__len__()
    length = length - 1

    x = 0
    while x < length:
        y = x + 1
        print( 'x = ' + str(x) + '   y = ' + str(y))
        while y <= length:
            print('Checking ' + str(num_list[x]) + str(' and ') + str(num_list[y]))
            if (num_list[x] + num_list[y] == k):
                result = 'Yes'
            y = y + 1
        x = x + 1
        y = x
        print(' ')
    print(result)



#Driver
num_list = [1,2,5,1,10,11,14,7]
k = 6
list_sum_k(num_list, k)
