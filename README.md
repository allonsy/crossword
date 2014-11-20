Crossword
=========

Author: Allonsy
email: linuxbash8@gmail.com

Crossword, a simple crossword helper. 

Call crossword either from your shell or by using the python utility

usage:
./crossword word [word]...

or 

python crossword.py word [word]...

where word is a pattern with the given letters filled in and any blanks are replace by '.'
For example,

./crossword "d.g" would return dog, dug, dig, etc...

You can give the program as many arguments as you want. 
Don't forget to encapsulate your word with quotes otherwise your shell may exapand the periods to pattern match

Don't forget to download the dict.db file from the github

Questions? Bugs? email me at linuxbash8@gmail.com
