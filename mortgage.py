#Created and maintained by Harsh Jivani
#Mortgage Calculator
#COPYRIGHT 2019. ASK FOR PERMISSION BEFORE COPYING

def main():
	print(' (1) - Befefit of paying CC upfront w/ lower rate!\n' + \
		' (2) - Is saving money at closing BETTER option?\n' + \
		' (3) - Exit app')
	userSelection = raw_input('Please select option (1), (2) or (3): ')
	if userSelection == '1':
		option1()
	elif userSelection == '2':
		option2()
	elif userSelection == '3':
		exit()
	else:
		main()

def option1():
	print("\n**** Befefit of paying CC upfront w/ lower rate! ****\n")
	closingCost = raw_input('What is the CC of home w/ lower rate: ')
	closingCost = float(closingCost)
	#print(closingCost)

	zeroClsoingPI = raw_input("What is the Monthly P&I for zero CC ONLY: ")
	zeroClsoingPI = float(zeroClsoingPI)

	higherClsoingPI = raw_input("What is the Monthly P&I for higher CC: ")
	higherClsoingPI = float(higherClsoingPI)

	#Mathematical Formula
	diff = float((higherClsoingPI - zeroClsoingPI) * 12)
	years = float(closingCost / diff)
	yr = abs(years)
	yr = round(yr, 2)
	print('\nPaying CC upfront and getting lower rate will not begin' + \
		' to work to your advantage until the loan has been in place for little' + \
			' over %s years.' % yr)

def option2():
	print("\n**** Is saving money at closing BETTER option? ****\n")
	print('Option 1')
	rate1 = raw_input('What is loan 1 RATE: ')
	rate1 = float(rate1)
	cc1 = raw_input('What is loan 1 CC: ')
	cc1 = float(cc1)
	pi1 = raw_input('What is loan 1 Monthly P&I: ')
	pi1 = float(pi1)

	print('\nOption 2')
	rate2 = raw_input('What is loan 2 RATE: ')
	rate2 = float(rate2)
	cc2 = raw_input('What is loan 2 CC: ')
	cc2 = float(cc2)
	pi2 = raw_input('What is loan 2 Monthly P&I: ')
	pi2 = float(pi2)

	if cc1 <= 0 and cc2 <= 0:
		cc1 = abs(cc1)
		cc2 = abs(cc2)

		closingCostDiff = (cc1 - cc2)
		closingCostDiff = float(closingCostDiff)

		piDiff = (pi1 - pi2)
		piDiff = float(piDiff)
		piDiff = abs(piDiff)

		months = closingCostDiff / piDiff
		months = float(months)
		monthsToYears = months / 12
		monthsToYears = float(monthsToYears)
		monthsToYears = abs(monthsToYears)
		monthsToYears = round(monthsToYears, 1)
		print('If you going to keep your loan for MORE THAN {} years'.format(monthsToYears) + \
			' then its worth getting the LOWER RATE')
	elif (cc1 <= 0 and cc2 >= 0) or (cc1 >= 0 and cc2 <= 0):
		if cc1 <= 0 and cc2 >= 0:
			cc1 = abs(cc1)
			closingCostDiff = (cc1 - cc2)
			closingCostDiff = float(closingCostDiff)
			#closingCostDiff = abs(closingCostDiff)

			piDiff = (pi1 - pi2)
			piDiff = float(piDiff)
			piDiff = abs(piDiff)

			months = closingCostDiff / piDiff
			months = float(months)
			monthsToYears = months / 12
			monthsToYears = float(monthsToYears)
			monthsToYears = abs(monthsToYears)
			monthsToYears = round(monthsToYears, 1)
			print('Keep your loan until {} years'.format(monthsToYears) + \
				' and choose the HIGHER RATE')
		else:
			cc2 = abs(cc2)
			closingCostDiff = (cc1 - cc2)
			closingCostDiff = float(closingCostDiff)
			#closingCostDiff = abs(closingCostDiff)

			piDiff = (pi1 - pi2)
			piDiff = float(piDiff)
			piDiff = abs(piDiff)

			months = closingCostDiff / piDiff
			months = float(months)
			monthsToYears = months / 12
			monthsToYears = float(monthsToYears)
			monthsToYears = abs(monthsToYears)
			monthsToYears = round(monthsToYears, 1)
			print('Keep your loan until {} years'.format(monthsToYears) + \
				' and choose the HIGHER RATE')
	else:
		closingCostDiff = (cc1 - cc2)
		closingCostDiff = float(closingCostDiff)

		piDiff = (pi1 - pi2)
		piDiff = float(piDiff)
		piDiff = abs(piDiff)

		months = closingCostDiff / piDiff
		months = float(months)
		monthsToYears = months / 12
		monthsToYears = float(monthsToYears)
		monthsToYears = round(monthsToYears, 1)
		print('If you going to keep your loan for MORE THAN {} years'.format(monthsToYears) + \
			' then its worth getting the LOWER RATE')

if __name__ == '__main__':
	main()