import re


pattern = 'this'
text = 'Is this real?'

match = re.search(pattern, text)

if match:
    print(f'Found at {match.start()}')
else:
    print('Not found!')


