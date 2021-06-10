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

clear = lambda: os.system('clear')

class logs(object):
	def __init__(self, val1, val2, operationVal):
		self.val1 = val1
		self.val2 = val2
		self.operationVal = operationVal

	def to_json(self):
		#vraceni vsech operaci ve formatu json objektu
		return { "val1": "{}".format(self.val1), "val2":"{}".format(self.val2), "operationVal": "{}".format(self.operationVal) }

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
		with open('data.json', 'w', encoding='utf-8') as fp:
    			fp.write(json.dumps(jsonData).replace('\\', '')[1:len(jsonData) + 1])


		htmlContent = '<!DOCTYPE html> <html lang="cs"> <head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>PythonCalculator</title> <meta name="author" content="Filip Kalousek https://twentio.cz"> </head> <body> <style> @import url("https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap"); *, ::after, ::before 😔 box-sizing: border-box; padding: 0; margin: 0; ☺ body 😔 margin: 0; font-family: "Roboto Mono", monospace; background: rgb(11, 12, 17); ☺ body .content 😔 display: flex; flex-direction: column; justify-content: center; align-items: center; max-width: 90%; margin: 0 auto; margin-top: 1rem; ☺ body .content h1 😔 color: rgb(249,229,211); text-transform: uppercase; letter-spacing: 6px; margin-bottom: 2rem; ☺ body .content ul 😔 list-style: none; color: rgb(255, 255, 255); ☺ body .content ul li 😔 text-align: center; ☺ body .content ul li:not(:last-of-type) 😔 margin-bottom: 1rem; ☺ body footer 😔 padding: 2rem 0; display: flex; align-items: center; justify-content: center; ☺ body footer .copy 😔 color: rgb(255, 255, 255); display: flex; ☺ body footer .copy a 😔 color: rgb(255, 255, 255); margin-left: 1rem; ☺ </style> <div id="app"> <div class="content"> <h1>HISTORY LOG</h1> <ul> <li v-for="(log, index) in $root.logsList.logs"> <p class="operation" v-if="log.operationVal == &#39;+&#39;"> 😔😔index + 1☺☺. 😔😔log.val1☺☺ 😔😔log.operationVal☺☺ 😔😔log.val2☺☺ = <b>😔😔parseInt(log.val1) + parseInt(log.val2)☺☺</b> </p> <p class="operation" v-else-if="log.operationVal == &#39;-&#39;"> 😔😔index + 1☺☺. 😔😔log.val1☺☺ 😔😔log.operationVal☺☺ 😔😔log.val2☺☺ = <b>😔😔parseInt(log.val1) - parseInt(log.val2)☺☺</b> </p> <p class="operation" v-else-if="log.operationVal == &#39;*&#39;"> 😔😔index + 1☺☺. 😔😔log.val1☺☺ 😔😔log.operationVal☺☺ 😔😔log.val2☺☺ = <b>😔😔parseInt(log.val1) * parseInt(log.val2)☺☺</b> </p> <p class="operation" v-else-if="log.operationVal == &#39;/&#39;"> 😔😔index + 1☺☺. 😔😔log.val1☺☺ 😔😔log.operationVal☺☺ 😔😔log.val2☺☺ = <b>😔😔parseInt(log.val1) / parseInt(log.val2)☺☺</b> </p> <p class="operation" v-else-if="log.operationVal == &#39;?&#39; || log.operationVal == &#39;help&#39;"> 😔😔index + 1☺☺. Vyžádal jsi pomoc a tím našel všechny skryté funkce, jsi borec. 👍 </p> <p class="operation" v-else-if="log.operationVal == &#39;//&#39;"> 😔😔index + 1☺☺. √😔😔log.val1☺☺ = <b>😔😔Math.sqrt(parseInt(log.val1))☺☺</b> </p> <p class="operation" v-else-if="log.operationVal == &#39;**&#39;"> 😔😔index + 1☺☺. 😔😔log.val1☺☺ na 😔😔log.val2☺☺ = <b>😔😔Math.pow(parseInt(log.val1),parseInt(log.val2))☺☺</b> </p> <p class="operation" v-else-if="log.operationVal == &#39;log&#39;"> 😔😔index + 1☺☺. Hezky pěkně, víš jak si ukázat logy přímo v programu. 😎 </p> <p class="operation" v-else-if="log.operationVal == &#39;export&#39;"> 😔😔index + 1☺☺. Tak našel jsi easter egg na export, to z tebe dělá největšího frajera na světě! 🤘 </p> <p class="operation" v-else> 😔😔index + 1☺☺. Sorry, ale fakt tuhle operaci neznám: 😔😔log.operationVal☺☺ </p> </li> </ul> </div> </div> <footer> <div class="copy"> vytvořil <a href="https://github.com/kaldaf" target="_blank">Filip Kalousek</a> </div> </footer> <script src="https://cdn.jsdelivr.net/npm/vue@2"></script> <script> var app = new Vue(😔 el : "#app", data: 😔 logsList: [] ☺, mounted() 😔 var str = ''\''+ json.dumps(jsonData).replace('\\', '')[1:len(jsonData) + 1] + '' '\'; str = JSON.parse(str); this.logsList = str; ☺, ☺) </script> </body> </html>'

		with open('index.html', 'w', encoding='utf-8') as fp:
			fp.write(htmlContent.replace('☺','}').replace('😔','{'))
		print('Tvé odpovědi úspěšně uloženy.')
		specialOperation = True
	elif operation == 'clear':
		speacialOperation = True

		for i in range(0, 5):
			time.sleep(0.9)
			print('Konzole se čistí {}...'.format(str(5 - i)))
			if i == 4:
				time.sleep(0.9)
				print('Konzole úspěšně vyčištěna ✅.')
				time.sleep(0.9)
		clear()
		specialOperation = True
	elif operation == 'exit' or operation == 'quit':
		specialOperation = True
		print('\033[1;31,40mTo už je konec? No nic nezbývá mi nic jiného než se rozloučit.')
		exitMessages = ['budeš mi chybět moc', 'fakt moc', 'nechceš si to ještě rozmyslet?', 'tak čau..']
		time.sleep(2)
		clear()
		for index, val in enumerate(exitMessages):
			print('\033[1;31;40m'+val)
			time.sleep(1.5)
			clear()
		os._exit(0);
	else:
		print('\033[1;31;40mBohužel, tuhle operaci "{}" zatím neznám, snad se jí naučím.'.format(operation) + '\n')
		historyLog.append(logs(0, 0, operation))
		specialOperation = True

	if specialOperation == False:
		print('\033[1;31;40mAktuální výsledek je: {}'.format(result) + '\n')

	specialOperation = False

	if saveResults == False:
		result = 0
