stack = []


def push(item):
	stack.append(item)


def peek():
	return stack[len(stack) - 1]


def pop():
	return stack.pop()


def print_stack():
	print "\n\n"
	for item in list(reversed(stack)):
		print "| {} |".format(item)

	print "```````"


def menu():
	while True:
		print "1. Push\n2. Pop\n3. Print\n4. Exit"
		choice = input("Enter the choice: ")
		if choice == 1:
			item = raw_input("Enter the value: ")
			push(item)
		elif choice == 2:
			print pop()
		elif choice == 3:
			print_stack()
		elif choice == 4:
			break
		else:
			print "Enter the correct option !"
