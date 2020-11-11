# Ways to unpack different values in python:

#Normal
# items = (1,2)

# print(items)


#unpacking 
a, _ = (1,2) #underscore is used to tell that we aren't using the other value i.e. 2 in this case

print(a)
# print(b)

c,d,*e = (3,4,5,6,2) #asterick use krke hamne e ko [5,6,2] values dedi
print(c)
print(d)
print(e)

print('\n')

m,r,*_ = (13,24,45,66,82) #asterick aur underscore use krke hamne 4 ke bad ki sari values ko ignore kardiya
print(m)
print(r)

print('\n')

l,n,*j,z = (37,41,53,62,21) #l & n ko values 1,2 mili fhir n ko uske age ki sari mili par ab z use krdiya to hamne last value ko z ko asign kardiya to j to sari values milengi except last one 
print(l)
print(n)
print(j)
print(z)




