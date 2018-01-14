import sys
import vim
import subprocess
from datetime import datetime

DEFAULT_COMMAND = vim.eval("g:pickachu_default_command")

DEFAULT_DATE_FORMAT = vim.eval("g:pickachu_default_date_format")
DEFAULT_COLOR_FORMAT = vim.eval("g:pickachu_default_color_format")

def dateProcessor(input, format=DEFAULT_DATE_FORMAT):
	try:
		dateObj = datetime.strptime(input, '%m/%d/%Y')
	except(ValueError):
		dateObj = datetime.strptime(input, '%m/%d/%y')
	return dateObj.strftime(format)

def colorProcessor(input, format=DEFAULT_COLOR_FORMAT):
	if 'rgba' in input:
		# RGBA as input
		strip = input.strip('rgba)(')
		array = strip.split(',')
		array[3] = round(float(array[3]), 2)
		rgba_string = "rgba("
		values = ",".join(str(x) for x in array)
		rgba_string += values + ")"
		return rgba_string
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
					if i < len(array) - 1:
						rgb_string += ", "
					else:
						rgb_string += ")"
				return rgb_string
			elif format == 'rgba':
				rgba_string = "rgba("
				for i in range(0, len(rgb_array)):
					rgba_string += str(rgb_array[i])
					if i < len(array) - 1:
						rgba_string += ", "
					else:
						rgba_string += ", 1)"
				return rgba_string
	return None

# # # # # # # # # # # # # # # # # # # # # # # # # # #

apps = {
	'date': {
		'cmd': '--calendar',
		'processor': dateProcessor,
		'options': [
			'--date-format=%m-%d-%Y'
		]
	},
	'file': {
		'cmd': '--file-selection',
	},
	'color': {
		'cmd': '--color-selection',
		'processor': colorProcessor
	}
}

def runApp(choosenApp, format=None):
	app = apps.get(choosenApp, None)
	if app:
		output = None
		try:
			command_array = [DEFAULT_COMMAND, app['cmd']]
			if app.get('options', False):
				for option in app['options']:
					command_array.append(option)
			# Logging
			command_array.append('2> /tmp/pickachu_log')
			output = subprocess.check_output(command_array).decode('utf-8')
		except:
			return None

		if app.get('processor', None):
			if format:
				return app['processor'](output.rstrip(), format)
			else:
				return app['processor'](output.rstrip())
		else:
			return output.rstrip()
	else:
		print("App does not exist.")

# # # # # # # # # # # # # # # # # # # # # # # # # # #

def MainFunction():
	arglength = int(vim.eval('a:0'))

	CHOOSEN_APP = 'color'
	CHOOSEN_FORMAT = None

	if arglength > 0:
		CHOOSEN_APP = vim.eval('a:1')

	if arglength > 1:
		CHOOSEN_FORMAT = vim.eval('a:2')

	if not CHOOSEN_APP:
		CHOOSEN_APP = 'color'
	output = runApp(CHOOSEN_APP, CHOOSEN_FORMAT)

	# Vim!
	if output:
		pos_y, pos_x = vim.current.window.cursor
		vim.current.line = vim.current.line[:pos_x+1] + output + vim.current.line[pos_x+1:]
		vim.current.window.cursor = (pos_y, pos_x + len(output))
	else:
		print('Pickachu - Canceled')

