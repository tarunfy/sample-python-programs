# We can add commas too for big number cuz then we can ezily read them 
# First add underscores then simply format then while printing I mean convert them to commas

num1 = 10_000_000
num2 = 10_00_000_000

total = num1 + num2

print(f'{total:,}')