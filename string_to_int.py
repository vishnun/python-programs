def is_valid_digit(digit):
	return 0 <= digit <= 9


def str_to_int(num_str):
	num_str, sign = get_sign(num_str)
	value = 0
	for digit in num_str:
		digit = ord(digit) - ord('0')
		if is_valid_digit(digit):
			value = value * 10 + digit
		else:
			return "Not a number"
	if sign == '-':
		value = -value
	return value


def get_sign(num_str):
	sign = '+'
	if num_str[0] == '-' or num_str[0] == '+':
		sign = num_str[0]
		num_str = num_str[1:]
	return num_str, sign
