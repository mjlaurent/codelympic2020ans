#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'interpolate' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY instances
#  3. FLOAT_ARRAY price
#

def interpolate(n, instances, price):
    # Interger "<=0" check and collecting position 
    remove_list = []
    for index in range(len(price)):
        if price[index] <= 0:
            remove_list.append(index)
    
    # Remove overwritten price
    price = [i for i in price if i > 0]

    # Remove instances / quantities associated with removed price
    iteration = 0
    for remove_instances in remove_list:
        if iteration == 0:
            instances.pop(remove_instances)
        else:
            remove_instances = remove_instances - iteration
            instances.pop(remove_instances)
        iteration = iteration + 1

    # Check for exactly the same quantity in the price list
    if n in instances:
        value = "{0:.2f}".format(price[instances.index(n)])
        
    # Check if the price list length is only 1 / only has 1 quantity
    elif len(price) == 1:
        value = "{0:.2f}".format(price[0])
        
    # Check if the quantities is not in the instaces list
    elif n not in instances:
        # Check if the n is bigger than the largest instances
        if n > instances[-1]:
            instances_1 = instances[-1]
            instances_2 = instances[-2]
            price_1 = price[-1]
            price_2 = price[-2]
        
        # Check if the n is smaller than the smallest instances
        elif n < instances[0]:
            instances_1 = instances[0]
            instances_2 = instances[1]
            price_1 = price[0]
            price_2 = price[1]

        # Check if the n lies in between two instances
        else:
            instances.append(n)
            instances.sort()
            index = instances.index(n)
            instances_1 = instances[index+1]
            instances_2 = instances[index-1]
            price_1 = price[index]
            price_2 = price[index-1]
        
        # Linear equation calculation
        slope = (price_1 - price_2 ) / (instances_1 - instances_2)
        constant = price_1 - (slope * instances_1)
        value = (slope * n) + constant
        value = "{0:.2f}".format(value)

    # Return statement
    return str(value)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    instances_count = int(input().strip())

    instances = []

    for _ in range(instances_count):
        instances_item = int(input().strip())
        instances.append(instances_item)

    price_count = int(input().strip())

    price = []

    for _ in range(price_count):
        price_item = float(input().strip())
        price.append(price_item)

    result = interpolate(n, instances, price)

    fptr.write(result + '\n')

    fptr.close()
