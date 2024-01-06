#module_calling_example

from tabulate import tabulate
import creator.py
import string
from operator import itemgetter
from tabulate import tabulate
from pprint import pprint
from random import choice
# add number of devices by chanong the number on Num_devices and num_subnets
if __name__ == '__main__' :
	devices = (util.solicitate_mock(num_devices=10, num_subnets=10))

print("\nTabulated Version:")
print(tabulate(devices, headers="keys", tablefmt="grid"))
