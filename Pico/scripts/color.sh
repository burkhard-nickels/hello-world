
# ---------------------
# Beispiel aus dem Netz:
# vim -E -s -c "let g:html_no_progress=1" -c "syntax on" -c "set ft=c" -c "runtime syntax/2html.vim" -cwqa myfile.c
# 
# ls -l /usr/share/vim/vim82/syntax/html*
# ls -l /usr/share/vim/vim82/syntax/2html*
# Ich habe die Datei 2html.vim editiert: Ich habe die Zeilen mit "underline" auskommentiert.
#
# In vim:
# :colorscheme <Ctrl+d>, shows available color schemes
# :colorscheme blue
# :colorscheme default
#     morning, evening, murphy, delek
# => leider ist die Ausgabe des Code farblich anders als in vim.
# --------------------

file=$1
vim -E -s -c "let g:html_no_progress=1" -c "syntax on" -c "set nu" -c "colorscheme default" -c "set syntax=python" -c "set ft=python" -c "runtime syntax/2html.vim" -cwqa $file

# -c "runtime syntax/2html.vim"

