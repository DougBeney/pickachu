import vim
import subprocess
from . import processors

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# name:        apps.py
# description: this function contains a dictionary object
#              where you can easily add new apps with processor
#              functions to handle their output. Note: a
#              processor is optional.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

ZENITY_COMMAND = vim.eval("g:pickachu_default_command")
# Note: This is not the final date format that displays on
#       the users' buffer. This is the format we force
#       Zenity/Qarma to provide us.
RETURNED_DATE_FORMAT = "%m/%d/%Y"
if ZENITY_COMMAND == 'qarma':
	RETURNED_DATE_FORMAT = "MM/dd/yy"

apps = {
	'date': {
		'cmd': ZENITY_COMMAND,
		'processor': processors.dateProcessor,
		'options': [
			'--calendar',
			'--date-format=' + RETURNED_DATE_FORMAT
		]
	},
	'file': {
		'cmd': ZENITY_COMMAND,
		'options': [
            '--file-selection'
        ]
	},
	'color': {
		'cmd': ZENITY_COMMAND,
		'options': [
			'--color-selection'
    ],
		'processor': processors.colorProcessor
	}
}

def runApp(choosenApp, format=None):
	app = apps.get(choosenApp, None)
	if app:
		output = None
		try:
			command_array = [app['cmd']]
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
