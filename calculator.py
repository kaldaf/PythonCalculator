import os
import time
import math
import json

result = 0
firtsVal = 0
secondVal = 0
saveResults = False
saveResultMessageShowed = False
specialOperation = False
historyLog = []

class logs(object):
	def __init__(self, val1, val2, operationVal):
		self.val1 = val1
		self.val2 = val2
		self.operationVal = operationVal

	def to_json(self):
		#vraceni vsech operaci ve formatu json objektu
		return { "val1": self.val1, "val2": self.val2, "operationVal": "{}".format(self.operationVal) }

	def show(self):
		#vypsani vsech operaci
		if self.operationVal == '?' or self.operationVal == 'help':
			print('Našel jsi nabídku kde je vše vysvětlené, snad to už chápeš.')
		elif self.operationVal == 'null':
			print('Vynuloval jsi výsledek.')
		elif self.operationVal == 'log':
			print('Jsi frajer, našel jsi vše zalogované.')
		elif self.operationVal == 'export':
			print('Jde vidět že jsi mega O.G. tester nebo jen koukáš do zdrojáku.')
		elif self.operationVal == '//':
			print('√{} = {}'.format(self.val1, math.sqrt(self.val1)))
		elif self.operationVal == '+':
			print('{} {} {} = {}'.format(self.val1, self.operationVal, self.val2, self.val1 + self.val2))
		elif self.operationVal == '-':
			print('{} {} {} = {}'.format(self.val1, self.operationVal, self.val2, self.val1 - self.val2))
		elif self.operationVal == '/':
			print('{} {} {} = {}'.format(self.val1, self.operationVal, self.val2, self.val1 / self.val2))
		elif self.operationVal == '*':
			print('{} {} {} = {}'.format(self.val1, self.operationVal, self.val2, self.val1 * self.val2))
		elif self.operationVal == '**':
			print('{} na {} = {}'.format(self.val1, self.val2, self.val1 ** self.val2))
		else:
			print('Nechci říct, že jsi hlupák... 🤐')
			print('Ale fakt tuhle operaci neznám: {}'.format(self.operationVal))

#setup pracovani s hodnotami
	if saveResultMessageShowed == False:

		print('Budeme ukládat výsledky?')
		answer = input('y/n: ')

		if answer == 'y':
			saveResults = True
			print('Volba uložena. \n')
		elif answer == 'n':
			saveResults = False
			print('Volba uložena. \n')
		else:
			print('\033[1;31;40mBohužel takovou odpověď neberu, radši to uložíme.')
			saveResults = True
		saveResultMessageShowed = True

while True:

	print('\033[1;32;40mJakou operaci budeme dělat?')
	print('+, -, *, /, **, //, null')
	operation = input('\033[1;33;40mOperace: ').strip()

	if operation == '+':
		firstVal = float(input('\n\033[1;37;40mZadej 1. číslo: '))
		secondVal = float(input('Zadej 2. číslo: '))
		result += firstVal + secondVal
		historyLog.append(logs(firstVal, secondVal, operation))
	elif operation == '-':
		firstVal = float(input('\n\033[1;37;40mZadej 1. číslo: '))
		secondVal = float(input('Zadej 2. číslo: '))
		result += firstVal - secondVal
		historyLog.append(logs(firstVal, secondVal, operation))
	elif operation == '*':
		firstVal = float(input('\n\033[1;37;40mZadej 1. číslo: '))
		secondVal = float(input('Zadej 2. číslo: '))
		result += firstVal * secondVal
		historyLog.append(logs(firstVal, secondVal, operation))
	elif operation == '/':
		firstVal = float(input('\n\033[1;37;40mZadej 1. číslo: '))
		secondVal = float(input('Zadej 2. číslo: '))
		result += firstVal / secondVal
		historyLog.append(logs(firstVal, secondVal, operation))
	elif operation == '**':
		firstVal = float(input('\n\033[1;37;40mZadej 1. číslo: '))
		secondVal = float(input('Zadej 2. číslo: '))
		result += firstVal ** secondVal
		historyLog.append(logs(firstVal, secondVal, operation))
	elif operation == '//':
		firstVal = float(input('\n\033[1;37;40mZadej číslo k odmocnění: '))
		secondVal = 0
		result += math.sqrt(firstVal)
		historyLog.append(logs(firstVal, 0, operation))
	elif operation == 'null':
		result = 0
		print('\033[1;33;40mVýsledek byl vynulován. \n')
		specialOperation = True
		historyLog.append(logs(0, 0, operation))
	elif operation == '?' or operation == 'help':
		print('\n\033[1;34;40mOperace "+" znamená sčítání. \nOperace "-" znamená odčítání.')
		print('Operace "*" znamená násobení. \nOperace "/" znamená dělení.')
		print('Operace "**" znamená mocnění. \nOperace "//" znamená odmocnění.')
		print('Operace "null" znamená vynulování výsledku.')
		print('Operace 01101100 01101111 01100111 znamená vypsání všech dosavadních úkonů.')
		print('Operace 01100101 01111000 01110000 01101111 01110010 01110100 znamená uložení úkonů do tvaru json. \n')
		specialOperation = True
		historyLog.append(logs(0, 0, operation))
	elif operation == 'log':
		historyLog.append(logs(0, 0, operation))
		print('\033[1;34;40mGratuluji, našel jsi easter egg! \n')
		for log in historyLog:
			log.show()
		specialOperation = True
	elif operation == 'export':
		historyLog.append(logs(0,0,operation))
		print('\033[1;34;40mVypadá to že jsi asi koukal do zdrojáku, no neva já ti uložím tvoje odpovědi... \n')

		#list convert to json
		listToExport = [obj.to_json() for obj in historyLog]
		jsonData = json.dumps({"logs": listToExport})

		#save json objects to json file
		with open('data.json', 'w', encoding='utf-8') as f:
    			json.dump(jsonData, f, ensure_ascii=False, indent=4)

		print('Tvé odpovědi úspěšně uloženy.')
		specialOperation = True
	elif operation == 'clear':
		speacialOperation = True
		clear = lambda: os.system('clear')

		for i in range(0, 5):
			time.sleep(0.9)
			print('Konzole se čistí {}...'.format(str(5 - i)))
			if i == 4:
				time.sleep(0.9)
				print('Konzole úspěšně vyčištěna ✅.')
				time.sleep(0.9)
		clear()
		specialOperation = True
	else:
		print('\033[1;31;40mBohužel, tuhle operaci {} zatím neznám, snad se jí naučím.'.format(operation) + '\n')
		historyLog.append(logs(0, 0, operation))
		specialOperation = True

	if specialOperation == False:
		print('\033[1;31;40mAktuální výsledek je: {}'.format(result) + '\n')

	specialOperation = False

	if saveResults == False:
		result = 0
