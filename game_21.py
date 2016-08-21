from random import randint

cart = [x for x in range(2,12)]
a = 0
b = 0

while True:
	ch1 = input("Будите брать карту? y/n")
	if ch1 == "y":
		r = randint(0, len(cart) - 1)
		choose1 = cart[r]
		a += choose1
		if a > 21:
			print("Вы проиграли!")
			break
		elif a == 21:
			print("21 ска!Вы выйграли")
			break
	elif ch1 == "n":
		print("Ну ок....многое теряешь")
		print("Вы набрали %d очков" %a )
		break

print("Теперь ходит ваш противник")
while True:
	r = randint(0, len(cart) - 1)
	choose2 = cart[r]
	b += choose2
	r2 = randint(0,2)
	if r2 == 0:
		print("Ваш противник набрал %d очков" %b)
		if a > b:
				print("Вы выйграли!")
				break
		elif b == 21:
			print("Ваш противник набрал 21!")
			break
		else:
			print("Вы проиграли")
			break
	elif r2 == 1:	
		if b > 21:
			print("Вы выйграли!Он набрал > 21 очков")
			break
		elif a == 21:
			print("21 ска!Вы проиграли!")
			break






