import sys
import vim
import subprocess
from datetime import datetime

DEFAULT_DATE_FORMAT = vim.eval("g:pickachu_default_date_format")
DEFAULT_COLOR_FORMAT = vim.eval("g:pickachu_default_color_format")


def dateProcessor(input, format=DEFAULT_DATE_FORMAT):
    dateObj = datetime.strptime(input, '%m/%d/%Y')
    return dateObj.strftime(format)

def colorProcessor(input, format=DEFAULT_COLOR_FORMAT):
    if 'rgb' in input:
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
                for i in range(0, len(array)):
                    rgba_string += str(array[i])
                    if i < len(array) - 1:
                        rgba_string += ", "
                    else:
                        rgba_string += ")"
                return rgba_string


        return array
    return None

# # # # # # # # # # # # # # # # # # # # # # # # # # #

apps = {
    'date': {
        'cmd': '--calendar',
        'processor': dateProcessor
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
            output = subprocess.check_output(['zenity', app['cmd']]).decode('utf-8')
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

