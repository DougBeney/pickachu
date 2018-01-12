"Script: Pickachu
"Version: 0.0.1
"Copyright: Copyright (C) 2018 Doug Beney
"Licence: 
"Website: https://dougie.io

if !has('python3')
	echo "You need Vim Python3 support to use this plugin. If you're using NeoVim, try running `pip3 install neovim` to resolve this issue."
endif

let g:pickachu_default_date_format = "%m/%d/%Y"
let g:pickachu_default_color_format = "hex"

python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))

command! -nargs=* Pickachu call Pickachu(<f-args>)

function! Pickachu(...)
python3 << EOF
from pickachu import MainFunction
MainFunction()
EOF
endfunction
