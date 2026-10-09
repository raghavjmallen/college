import sys
f=open("grades.txt", "r")
line= f.readline()
print(line)
line= f.readline()
maxmarks=line.split()
maxmarks.pop(0)
maxmarks=list(map(int,maxmarks))
print(maxmarks)
line= f.readline()
weightage=line.split()
weightage.pop(0)
weightage=list(map(int,weightage))
print(weightage)
quizhash={}
midsemhash={}
finalhash={}
wtotalhash={}
line= f.readline()
while line:
    marks=line.split()
    name=marks.pop(0)
    quizhash[name]=int(marks[0])
    midsemhash[name]=int(marks[1])
    finalhash[name]=int(marks[2])
    line= f.readline()
for name in quizhash.keys():
    wtotalhash[name]=quizhash[name]*(weightage[0]/maxmarks[0])+midsemhash[name]*(weightage[1]/maxmarks[1])+finalhash[name]*(weightage[2]/maxmarks[2])

print(quizhash)
print(midsemhash)
print(finalhash)
for name, wtotal in wtotalhash.items():
    print(name, wtotal)
grade = ""
for name, marks in wtotalhash.items():
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B+"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else: 
        grade = "F"
    print(name, marks, grade)
