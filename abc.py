# ADDING TWO DICTIONARIES 

d1 = {"Tarun":"qt", "Shubham":"kys", "Cringe":"faggot"}
d2 = {"Astrallics":"American", "Richard":"Russian", "Taylor":"Australian"}

# METHOD 1:
# d3 = d1.copy()
# d3.update(d2)
# print(d3)

# METHOD 2:
# d3 = {**d1, **d2}
# print(d3)

# METHOD 3: (new python 3.9.0)
d3 = d1 | d2
print(d3)

