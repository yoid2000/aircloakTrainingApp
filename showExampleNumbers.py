from demoConfig import getExampleList

examples = getExampleList()

for i in range(len(examples)):
    ex = examples[i]
    if len(ex['cloak']['sql']) == 0:
        continue
    print(f"---------- Example {i} -------------------")
    print('cloak:')
    print(ex['cloak']['sql'])
    print('---')
    print('native')
    print(ex['native']['sql'])
