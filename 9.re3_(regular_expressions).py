import re

print(re.search(r'cat',' The cat is here'))
re.search(r'cat',' The dog is here')

# Or operator |
print(re.search(r'cat|dog', 'The cat is here')) # Will search for cat or dog

# The Wildcard Character
print(re.findall(r'.at', 'The cat in a hat sat there')) # ['cat', 'hat', 'sat']
print(re.findall(r'...at', 'The cat in a hat splat there')) # ['e cat', 'a hat', 'splat']
# One or more non-whitespace that ends with 'at'
re.findall(r'\S+at',"The bat went splat") # ['bat', 'splat']

# Starts with and Ends With
print(re.findall(r'^\d','1 is a number')) # Starts
print(re.findall(r'\d$','The number is 2')) # Ends

################################################################################################################

phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+' # + occurs one or more time
print(re.findall(pattern, phrase)) # Every single characters that was not a number

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
clean = (re.findall(r'[^!.? ]+',test_phrase)) # There's a space after ? that will remove all the blank spaces
print(' '.join(clean)) # Get everything together

################################################################################################################

text = 'Only find the hyper-words in this sentence. But you do not know how long-ish they are'
pattern2 = r'[\w]+-[\w]'
print(re.findall(pattern2, text))

################################################################################################################

#          Parenthesis for Multiple Options
# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
textone = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|erpillar)', textone))
print(re.search(r'cat(fish|nap|erpillar)', texttwo))
print(re.search(r'cat(fish|nap|erpillar)', textthree))
