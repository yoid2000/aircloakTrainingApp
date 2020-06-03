import requests
from demoConfig import getExampleList

# Modify following with the domain that you want to use
urlBase = 'http://localhost:8070/'
urlTraining = urlBase + 'training'
urlCache = urlBase + 'cache/'

examples = getExampleList()

for i in range(len(examples)):
    ex = examples[i]
    if 'skip' in ex and ex['skip'] is True:
        continue
    if len(ex['cloak']['sql']) == 0:
        continue
    url = urlCache + str(i)
    r = requests.get(url)
    print(f"---------- Example {i} -------------------")
    print(r.text)
