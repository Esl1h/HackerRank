import re

Regex_Pattern = r'^[A-Za-z]*[s]$'
print(str(bool(re.search(Regex_Pattern, input()))).upper())

Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]*' # Do not delete 'r'.
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())



Regex_Pattern = r'^[A-Za-z]*[s]$' # Do not delete 'r'.
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())



Regex_Pattern = r'^[0-9]+[A-Z]+[a-z]+$' # Do not delete 'r'.
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())



# Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.
Regex_Pattern = r"(?<=[13579])\d"
import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))



#Write a regex which can match all the occurences of characters which are not immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U).
Regex_Pattern = r"(?<![aoueiAEIOU])." # Do not delete 'r'.
import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# Your task is to write a regex which will match word starting with vowel (a,e,i,o, u, A, E, I , O or U).
# The matched word can be of any length. The matched word should consist of letters (lowercase and uppercase both) only.
# The matched word must start and end with a word boundary.
Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b' # Do not delete 'r'.
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())



#  should have 3 or more consecutive repetitions of ok.
Regex_Pattern = r'okokok([ok]*)' # Do not delete 'r'.
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())



# must start with Mr., Mrs., Ms., Dr. or Er.. The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).
Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$' # Do not delete 'r'.
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
