import click
import csv_parser
import re

@click.command()
@click.option('--currency', prompt='Enter country code (ISO 4217)',  help='country code (ISO 4217)')
def main(currency):
	"""
	Displays whether currecy code input is supported or not

	Input 
		- currency: String of country code

	"""

	if re.fullmatch('[a-z]{3}', str(currency).lower()) :
		
		# Get sorted list 
		sorted_list = csv_parser.sort_file_contents("Cheap.Stocks.Internationalization.Currencies.csv")

		# Check if currency is supported
		result = csv_parser.currency_present(sorted_list, currency)

		# Print result
		if result:
			print("The currency with code [" +currency +"] is supported")
		else:
			print("The currency with code [" +currency +"] is not supported")
			
	else :
		print("Input for currency is invalid . Try again")

if __name__ == '__main__':
    main()