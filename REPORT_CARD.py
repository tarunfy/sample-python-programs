report_card = []
sub = ["phy", "chem", "maths", "cs", "eng", "phyedu"]
Tmarks = 0
#marks = []
for i in range(1, len(sub) + 1):
    #print("enter the marks of", i)
    markss = int(input("marks: "))
    #marks.append(markss)
    Tmarks = Tmarks + markss

perc = (Tmarks/600)*100

Grade = " "

if perc > 80 and perc <= 100:
    Grade = "A"
elif perc > 50 and perc <=80:
    Grade = "B"
else:
    Grade = "C"


s = {}
for x in range(1, len(sub)+1):
    key = input("enter the subject: ")
    value = int(input("enter the marks: "))
    s.update({key: value})
report_card.append(s)

num_elem2 = 1 
t = {}
for y in range(1, num_elem2 + 1):
    key = "Total marks"
    value = Tmarks
    t.update({key: value})
report_card.append(t)

num_elem3 = 1 
p = {}
for z in range(1, num_elem3 + 1):
    key = "Percentage"
    value = perc
    p.update({key: value})
report_card.append(p)

num_elem4 = 1 
g = {}
for f in range(1, num_elem4 + 1):
    key = "Grade"
    value = Grade
    g.update({key: value})
report_card.append(g)

print("THE REPORT CARD IS", report_card)


    
    

    
