# Using zip function to loop over two or more lists at once like you can see below its so ezzzzz but one thing to remember is that we should have same length of list which have some relation with each other
 
names = ['Tarun', 'Varun', 'Astrallics', 'gramps', 'Ricky', 'Gore']
roles = ['Member', 'Co-leader', 'Leader', 'Admin', 'Elite', 'Exclusive']
nicks = ['dog', 'cat', 'egale', 'simp', 'tard', 'toxic']

for name, role, nick in zip(names, roles, nicks):
    # role = roles[index]
    print(f'{name} is our clan\'s {role} and his nick is {nick}')

