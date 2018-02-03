import vim
from . import apps

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# name:        main.py
# description: This file evaluates the command arguments
#              provided by the user, calls the runApp function,
#              and inserts valid output to the user's buffer.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

DEFAULT_APP = vim.eval('g:pickachu_default_app')


def MainFunction():
	# This section is for getting the
	# arguments from the user's Vim
	# command.
	arglength = int(vim.eval('a:0'))
	CHOOSEN_APP = DEFAULT_APP
	CHOOSEN_FORMAT = None
	if arglength > 0:
		CHOOSEN_APP = vim.eval('a:1')
	if arglength > 1:
		CHOOSEN_FORMAT = vim.eval('a:2')

	# We run apps.py's runApp function to get an output.
	output = apps.runApp(CHOOSEN_APP, CHOOSEN_FORMAT)

	# Now, if runApp gave us an output, we can use the
	# Vim API to print the output to the user's buffer.
	if output:
		pos_y, pos_x = vim.current.window.cursor
		vim.current.line = vim.current.line[:pos_x+1] + output + vim.current.line[pos_x+1:]
		vim.current.window.cursor = (pos_y, pos_x + len(output))
	else:
		print('Pickachu - Canceled')
