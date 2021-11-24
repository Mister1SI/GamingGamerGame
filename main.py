#print('Text inverter!')
#while True:
#	a = input('Enter your text: ')
#	print(a[::-1] + "\n")
#	if a == 'break':
#		break
from time import sleep
interacting = True
def buy():
	buyStock = input('Enter the symbol of the stock you want to buy: ').upper()
	try:
		index = symbols.index(buyStock)
		print(index)
	except:
		print('Invalid')
	try:
		buyAmount = int(input('How many would you like to buy? '))
	except:
		print('Invalid')
	if (buyAmount * prices[index]) < money:
		print('Bought ' + str(buyAmount) + ' stocks of ' + names[index])
day = 0
money = 1000
gameRunning = True
symbols = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'FB', 'TSLA', 'WMT', 'INTL', 'NVDA', 'AMD']
names = ['Apple', 'Google', 'Microsoft', 'Amazon', 'Facebook', 'Tesla', 'Walmart', 'Intel Corp.', 'NVIDIA Corp.', 'Advanced Micro Devices']
quantities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
prices = [100.0, 200.0, 150.0, 80.0, 190.0, 70.0, 12.4, 260.0, 130.0, 230.0]
print('Stock Market Game!\n====================')
while gameRunning:
	interacting = True
	print('Day: ' + str(day))
	i = 0
	while i < len(symbols):
		print(names[i] + '(' + symbols[i] + ') = $' + str(prices[i]) + '  (' + str(quantities[i]) + ')')
		i += 1
	while interacting:
		print('Type \"buy\" to buy a stock, \"sell\" to sell stocks, and \"next\" or just hit enter to skip the day. To end the game, type \"end\"')
		choice = input('Your choice: ')
		if choice == 'buy':
			buy()
		elif choice == 'sell':
			print('Selling...')
		elif choice == 'next' or choice == '':
			print('Passing...')
			interacting = False
		elif choice == 'end':
			interacting = False
			gameRunning = False
		else:
			print('Unknown input! Passing day...')
			interacting = False
	print()
	sleep(1)
	day += 1