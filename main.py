import keyword
import re
# Don't remove the above imports, you will need this for checking keywords and valid identifiers


var1 = input()
pattern = r'^[a-zA-Z_]\w*$'

# Hint: the search is a method of the re object, if you are unsure how to use it, look for the documentation online

if(keyword.iskeyword(var1)):
  print(var1)
else:
  print(var1 + "IS NOT VALID")

