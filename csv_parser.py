import csv
import operator

def sort_file_contents(filename):
	"""
	Read contents of file a parses it

	Input 
		- file_name: String of filename of file containing supported currencies 

	Return
		List of supported currencies sorted alphabetically by currency code
	"""

	with open(filename, 'r') as file:
		reader = csv.reader(file)
		return sorted(reader, key=operator.itemgetter(2), reverse=False) 


def raw_file_contents(file_name):
	"""
	Read contents of file a parses it

	Input 
		- file_name: String of filename of file containing supported currencies 

	Return
		List of supported currencies sorted alphabetically by currency code
	"""

	with open(filename, 'r') as file:
		reader = csv.reader(file)
		return  list(reader)

def currency_present(currency_list, currency_code):
	"""
	Checks if currency code is in list

	Input 
		- currency_list: List of supported currencies
		- currency_code: String of currency in question 

	Return
		Boolean whether currency is supported or not
	"""

	for row in currency_list:
		if len(row[-1]) == 3 and row[-1].lower() == currency_code.lower():
			return True
	return False

