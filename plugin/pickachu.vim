"Script: Pickachu
"Version: 0.0.1
"Copyright: Copyright (C) 2018 Doug Beney
"Licence: 
"Website: https://dougie.io

if !has('python3')
	echo "You need Vim Python3 support to use this plugin. If you're using NeoVim, try running `pip3 install neovim` to resolve this issue."
endif


if !exists("g:pickachu_default_command")
	let g:pickachu_default_command = "zenity"
endif

if !exists("g:pickachu_default_date_format")
	let g:pickachu_default_date_format = "%m/%d/%Y"
endif

if !exists("g:pickachu_default_color_format")
	let g:pickachu_default_color_format = "hex"
endif

command! -nargs=* Pickachu call Pickachu(<f-args>)

python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))

function! Pickachu(...)
python3 << EOF
from pickachu.main import MainFunction
MainFunction()
EOF
endfunction
