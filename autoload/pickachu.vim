python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))

function! pickachu#Main(...)
python3 << EOF
from pickachu.main import MainFunction
MainFunction()
EOF
endfunction
