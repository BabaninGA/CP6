try:
	print("Введите кол-во элементов массива")
	n=int(input())
except ValueError:
	print("Обозначение кол-ва элементов массива не может содержать ничего кроме целых чисел")
	exit()
if n>=0:
	if n>=2:
		array=[0]*n
		for i in range(n):
			try:
				print("Введите элемент массива")
				array[i]=float(input())
			except ValueError:
				print("Элементами массива в данном случае могут быть только числа")
				exit()
		print("Массив:",array)
		min=array[0]
		for i in range(1,n):
			if array[i]<min:
				min=array[i]
		print("Наименьшее число:",min)
		
		try:
			print("Введите DELTA")
			d=float(input())
		except ValueError:
			print("DELTA может быть только числом")
			exit()
		k=0
		if d>0:
			for i in range(0,n):
				if array[i]-min==d:
					k+=1
			if k>=1:
				k=str(k)
				print("Количество элементов в заданном массиве, отличающихся от минимального на DELTA:"+k)
			else:
				print("В массиве нет элементов отличающихся от минимального на DELTA")
		elif d==0:
			for i in range(0,n):
				if array[i]==min:
					k+=1
			k-=1
			if k>=1:
				k=str(k)
				print("Количество элементов в заданном массиве, отличающихся от минимального на DELTA:"+k)
			else:
				print("В массиве нет элементов отличающихся от минимального на DELTA")
		else:
			print("Числа могут отличаться друг от друга только на положительное число или ноль")
	else:
		print("В массиве, чтобы его проверить на данное условие, должно быть хотя бы 2 элемента")
else:
	print("Количество элементов в массиве не может быть отрицательным")