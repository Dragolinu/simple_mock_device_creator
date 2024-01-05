import string
from operator import itemgetter
from tabulate import tabulate
from pprint import pprint
from random import choice

def solicitate_mock(num_devices=1 , num_subnets=1):
	
#devices list create
	created_mocks=list()


	if num_devices >254 or num_subnets > 254 :
		print("maximum subnets created")

	for subnet_indexing in range (1, num_subnets+1):
		for device_indexing in range (1, num_devices+1):

			#created devices Dictionary

			mockdevice = dict()

			#parameters to generate.

		mockdevice["nome do dispositivo:"] = (choice(["a1","a2","a3"]))
		mockdevice["versao:"] = (choice(["v1","v2","v3"]))
		mockdevice["sistema operacional:"] = (choice(["xp","linux","windows"]))
		mockdevice["ip"] = "192.168."+str(device_indexing)+"."+ str(subnet_indexing+1)
		created_mocks.append(mockdevice)
		
	return created_mocks



##main function caller
if __name__ == '__main__' :
	devices = solicitate_mock(num_devices=10, num_subnets=10)
	print("\nTabulated Version printed:")
	print(tabulate(devices, headers="keys", tablefmt="grid"))

#this is part of a python study.
