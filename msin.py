# dla 'ola' zwroci 'lo', dla 'kacper': 'epcak'
def odwracanie(string):
	newString = string[0:-1]
	newString = list(newString)#zamiana na tablice
	newString.reverse()
	newString = ''.join(newString)#laczenie w stronga
	return (newString)

print(odwracanie("alicja"))
