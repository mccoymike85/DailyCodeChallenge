#Author: Michael McCoy
#Date: 6/5/2018
#Website: www.slashdba.com
#LinkedIn: https://www.linkedin.com/in/michael-p-mccoy/

#Function Definition
def list_smallest_positive(num_list):
    num_list_unsorted = num_list
    num_list.sort()

    i = 0
    smallest_positive = -1
    smallest_positive_non_existing = -1
    num_search = -1

    for x in num_list:
        if(x >= 0 and smallest_positive == -1):
            smallest_positive = num_list[i]
        i = i + 1

    if(smallest_positive == -1):
        smallest_positive_non_existing = 0

    while(smallest_positive_non_existing == -1):
        num_search = num_search + 1
        print(num_search)
        if(num_search not in num_list):
            smallest_positive_non_existing = num_search

    print(num_list_unsorted)
    print('Smallest Positive Non-Existing Number In List: ' + str(smallest_positive_non_existing))


#Driver
num_list = [1,2,3,0]
list_smallest_positive(num_list)
