import re

Regex_Pattern = r'^[A-Za-z]*[s]$'
print(str(bool(re.search(Regex_Pattern, input()))).upper())

