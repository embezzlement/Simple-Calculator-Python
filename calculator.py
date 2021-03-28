from colorama import init
init(convert=True)
from os import system, name
from time import sleep
import time
import os

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def addition_func(x, y):
	return x + y

def add():
	os.system('Title: Addition')
	clear()
	g = f"""
	┌────────────┐
	|---Adding---|
	└────────────┘
	"""
	print(g)

	try:
		file = open("logs.txt", "a")
		fn = float(input("\nFirst Number: "))
		sn = float(input("\nSecond Number: "))
		print(f"\n{fn} + {sn} =", addition_func(fn, sn))
		file.write("\n"+f"[{fn}] + [{sn}] = {addition_func(fn, sn)}")
		sleep(2.0)
		file.close()
		main()


	except ValueError:
		print("Invalid. ")
		sleep(1.0)
		clear()
		add()

def subtraction_func(x, y):
	return x - y

def subtract():
	os.system('Title: Subtraction')
	clear()
	g = f"""
	┌─────────────────┐
	|---Subtraction---|
	└─────────────────┘
	"""
	print(g)

	try:
		file = open("logs.txt", "a")
		fn = float(input("\nFirst Number: "))
		sn = float(input("\nSecond Number: "))
		print(f"\n{fn} - {sn} =", subtraction_func(fn, sn))
		file.write("\n"+f"[{fn}] - [{sn}] = {subtraction_func(fn, sn)}")
		sleep(2.0)
		file.close()
		main()

	except ValueError:
		print("Invalid. ")
		sleep(1.0)
		clear()
		subtract()

def multiplication_func(x, y):
	return x * y

def multiply():
	os.system('Title: Multiplication')
	clear()
	g = f"""
	┌────────────────────┐
	|---Multiplication---|
	└────────────────────┘
	"""
	print(g)

	try:
		file = open("logs.txt", "a")
		fn = float(input("\nFirst Number: "))
		sn = float(input("\nSecond Number: "))
		print(f"\n{fn} x {sn} =", multiplication_func(fn, sn))
		file.write("\n"+f"[{fn}] x [{sn}] = {multiplication_func(fn, sn)}")
		sleep(2.0)
		file.close()
		main()

	except ValueError:
		print("Invalid. ")
		sleep(1.0)
		clear()
		multiply()


def division_func(x, y):
	return x / y


def division():
	os.system('Title: Division')
	clear()
	g = f"""
	┌──────────────┐
	|---Division---|
	└──────────────┘
	"""
	print(g)

	try:
		file = open("logs.txt", "a")
		fn = float(input("\nFirst Number: "))
		sn = float(input("\nSecond Number: "))
		print(f"\n{fn} / {sn} =", division_func(fn, sn))
		file.write("\n"+f"[{fn}] / [{sn}] = {division_func(fn, sn)}")
		sleep(2.0)
		file.close()
		main()

	except ValueError:
		print("Invalid. ")
		sleep(1.0)
		clear()
		division()


def main():
	os.system('Title: Main Page')
	clear()
	calc_screen = f"""
	            ╔════════════════╗
	            ║---Calculator---║
	╔═══════════╩════════════════╩════════════╗
	║(Add) - [Add Current 2 Numbers]          ║
	║(Subtract) - [Subtract Current 2 Numbers]║
	║(Multiply) - [Multiply Current 2 Numbers]║
	║(Division) - [Divide Current 2 Numbers]  ║
	╚═════════════════════════════════════════╝
	"""
	print(calc_screen)

	choice = input("Choice: ")
	
	if choice == "Add" or choice == "add":
		add()

	elif choice == "Subtract" or choice == "subtract":
		subtract()

	elif choice == "Multiply" or choice == "multiply":
		multiply()

	elif choice == "Division" or choice == "division":
		division()

	else:
		print("Invalid. ")
		sleep(1.5)
		main()

main()

if '__name__' == '__main__':
	main()