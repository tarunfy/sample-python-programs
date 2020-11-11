# Using enumerate function when we need a counter while we looping over something

names = ['Corey', 'Tarun', 'Varun', 'Chris', 'Astallics']


# count = 0
for index, name in enumerate(names, start=1):
    print(index, name)
    # count += 1