import sys
input = sys.stdin.readline

checklist = [0]*4
mylist = [0] * 4
checksecret = 0

def myadd(c):
    global checklist, mylist, checksecret
    if c == 'A':
        mylist[0] += 1
        if mylist[0] == checklist[0]:
            checksecret += 1
    elif c == 'C':
        mylist[1] += 1
        if mylist[1] == checklist[1]:
            checksecret += 1
    elif c == 'G':
        mylist[2] += 1
        if mylist[2] == checklist[2]:
            checksecret += 1
    elif c == 'T':
        mylist[3] += 1
        if mylist[3] == checklist[3]:
            checksecret += 1
            
def myremove(c):
    global checklist, mylist, checksecret
    if c == 'A':
        if mylist[0] == checklist[0]:
            checksecret -= 1
        mylist[0] -= 1
    elif c == 'C':
        if mylist[1] == checklist[1]:
            checksecret -= 1
        mylist[1] -= 1
    elif c == 'G':
        if mylist[2] == checklist[2]:
            checksecret -= 1
        mylist[2] -= 1
    elif c == 'T':
        if mylist[3] == checklist[3]:
            checksecret -= 1
        mylist[3] -= 1
        
s, p = map(int, input().split())
result = 0
A = list(input())
checklist = list(map(int, input().split()))

for i in range(4):
    if checklist[i] == 0:
        checksecret += 1

for i in range(p):
    myadd(A[i])

if checksecret == 4:
    result += 1
     
for i in range(p, s):
    j = i-p
    myadd(A[i])
    myremove(A[j])
    if checksecret == 4:
        result += 1

print(result)