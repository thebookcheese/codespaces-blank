from faker import Faker
Fake = Faker()

import re


rep = {"e": "caviar", "a": "bens", "n":'union of soviet socialist republics'} # define desired replacements here

# use these three lines to do the replacement

def Replace(text, rep):
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)  
    print(text)
    return text



with open('input.txt', 'r') as f:
    text = f.read()
    ReplacedText = Replace(text, rep)

with open('output.txt', 'w') as f:
    a = ReplacedText.split('.')
    f.write('')

with open('output.txt', 'w') as f:
    for i in a:
        f.write(i + '\n')