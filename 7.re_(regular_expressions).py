# Regular expressions ( regex )
# user@email.com
# pattern = text + @ + text + .com

# (555) - 555 - 555
# r'(\d\d\d) - \d\d\d - \d\d\d'
# r'(\d{3}) - \d{3} - \d{4})'

import re

text = "The agent's phone number is 408-555-1234. Call Soon"

pattern ='phone'
print(re.search(pattern, text))

pattern2 = 'Not in text'
print(re.search(pattern2, text))

match = re.search(pattern, text)
print(match.span())  # (12, 17)

print(match.start()) # 12
print(match.end())   # 17

#####################################################################################

text = 'my phone once, my phone twich'
match_phone = re.search('phone', text)
print(match_phone)

matches = re.findall('phone', text)
print(matches) # ['phone', 'phone']
print(len(matches)) # 2

######################################################################################

for match in re.finditer('phone', text): # itterates throw text and returns all phones
    print(match)         # span of phone
    print(match.group()) # actual phone

