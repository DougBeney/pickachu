import vim
from datetime import datetime

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# name:				 processors.py
# description: this file contains functions that process data
#							 from the runapp function (in app.py).
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

DEFAULT_DATE_FORMAT = vim.eval("g:pickachu_default_date_format")
DEFAULT_COLOR_FORMAT = vim.eval("g:pickachu_default_color_format")

def dateProcessor(input, format=DEFAULT_DATE_FORMAT):
	try:
		dateObj = datetime.strptime(input, '%m/%d/%Y')
	except(ValueError):
		dateObj = datetime.strptime(input, '%m/%d/%y')
	return dateObj.strftime(format)

def colorProcessor(input, format=DEFAULT_COLOR_FORMAT):
	# The system color picker returned an rgba value
	if 'rgba' in input:
		strip = input.strip('rgba)(')
		array = strip.split(',')
		# Round the alpha value to two decimal placed
		array[3] = round(float(array[3]), 2)
		rgba_string = "rgba("
		values = ",".join(str(x) for x in array)
		rgba_string += values + ")"
		return rgba_string
	# The system color picker returned an rgb value
	elif 'rgb' in input:
		# RGB as input
		if format == 'rgb':
			return input
		else:
			# Strip 'rgb' and parenthesis
			strip = input.strip('rgb)(')
			array = strip.split(',')

			if format == 'hex':
				hex = '#%02x%02x%02x' % (int(array[0]), int(array[1]), int(array[2]))
				return hex.upper()
			elif format == 'rgba':
				rgba_string = "rgba("
				array.append(1)
				values = ",".join(str(x) for x in array)
				rgba_string += values + ")"
				return rgba_string
		return array
	# The system olor picker returned a hex
	elif '#' in input:
		# If there is a '#' in input,
		# they are most likely using Qarma instead of Zenity
		# or any other program that outputs hex
		if format == 'hex':
			return input
		else:
			hex = input.lstrip('#')
			rgb_array = tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))

			if format == 'rgb':
				rgb_string = "rgb("
				for i in range(0, len(rgb_array)):
					rgb_string += str(rgb_array[i])
					if i < len(rgb_array) - 1:
						rgb_string += ", "
					else:
						rgb_string += ")"
				return rgb_string
			elif format == 'rgba':
				rgba_string = "rgba("
				for i in range(0, len(rgb_array)):
					rgba_string += str(rgb_array[i])
					if i < len(rgb_array) - 1:
						rgba_string += ", "
					else:
						rgba_string += ", 1)"
				return rgba_string
	return None
