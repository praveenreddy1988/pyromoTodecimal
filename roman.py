
def value(r):
	if (r == 'I'):
		return 1
	if (r == 'V'):
		return 5
	if (r == 'X'):
		return 10
	return -1


def romanToDecimal(roman_numbers):

	decimal_numbers =[]
	for number in roman_numbers:
		res = 0
		i = 0
		#number = I
		#print("number is --------",number)
		#print("length of number-------- ",len(number))
		while (i < len(number)):
			#value("I")
			#print("i is ----------",i)
			#print("number first iteration...",number[i])
			n1 = value(number[i])
			#n1 = 1
			#print("n1---------- ",n1)


			if (i + 1 < len(number)):
				#print("i is ------------",i)
				#print("number second iteration...",number[i+1])
				n2 = value(number[i + 1])
				#print("n2----------------- ",n2)

				if (n1 >= n2):
					res = res + n1
					i = i + 1
					#print("res---------- ",res)
					#print("i------------ ",i)
				else:
					res = res + n2 - n1
					i = i + 2
					decimal_numbers.append(res)
					#print("res in else-------- ",res)
					#print("i in else---------- ",i)
			else:
				res = res + n1
				i = i + 1
				decimal_numbers.append(res)
				#print("final res is ------- ",res)


	return decimal_numbers



print("Integer form of Roman Numeral I to X")
#roman_numbers = ["II"]
roman_numbers = ["I","II","III","IV","V","VI","VII","VIII","IX","X"]
#print(romanToDecimal(roman_numbers))

val = input("Enter a value of Roman number--")
#print(val)
print(romanToDecimal([val]))
