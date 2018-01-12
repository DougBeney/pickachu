"Script: Pickachu
"Version: 0.0.1
"Copyright: Copyright (C) 2018 Doug Beney
"Licence: 
"Website: https://dougie.io

let g:pickachu_default_cal_format = "%m/%d/%Y"
let g:pickachu_default_color_format = "hex"

if !has('python3')
	echo "You need Vim Python3 support to use this plugin. If you're using NeoVim, try running `pip3 install neovim` to resolve this issue."
endif

command! -nargs=* Pickachu call Pickachu(<f-args>)

function! Pickachu(...)
	py3file pickachu.py
endfunction

