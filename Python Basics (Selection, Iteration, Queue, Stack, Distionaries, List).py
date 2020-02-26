#Selection

print("what is your name")
name = input("enter your name")
length = len(name)
print(length)
if length > 7 :
    print("your name is lengthy")
elif    length < 5:
    print("your name is short")
else:
    print("beautiful name")
 

# Iteration
for i in range(1, 6):
    print(i)

i =1
while i < 6:
    print(i)
    i += 1   

# Built-in stuffs
string = "Prasanna Dhungel"
print(string[2:6])
print(string.capitalize)
print(string.join("!rame!"))     

#count no of 'a' in a name
count = 0
username = input("Please enter your name ")
for i in range(1, len(username)):
    if username[i] == 'a':
        count += 1
print("no of e's is:" , count ) 

# Using lists
fruits = ['Apple', 'Orange', 'Litchi', 'Banana', 'lemon']
print(fruits[1])
fruits.append('rice')
print(fruits)
fruits.__delitem__(1)
print(fruits)
if 'Apple' in fruits:
    print("apple is present")

if len(fruits) < 10:
    print("space left")
fruits.clear()
fruits.append("cheery")
fruits.pop()
fruits2 = fruits.copy()
fruits.insert(2, "pomegranate")
fruits.reverse()
fruits.sort()
fruits.remove()
print(fruits)    


# Using Dictionaries
students = {'sid1': 'prasanna', 'sid2': 'dhungel'}
print(students['sid2'])
print(students.values())
for item in students.keys():
    print(item , " {0} has a id: ".format("daju") , students[item])

students.update({'sid2': 'damna'})
students.update({'sid3': 'paat', 'sid4': 'manxe'})
print(len(students))
del students['sid3']
print(students)
students.clear()
print(students)  


#Stack
MyStack = []
StackSize = 3
def DisplayStack():
    print("Stack currently contains:")
    for Item in MyStack:
        print(Item)

def Push(Value):
 if len(MyStack) < StackSize:
    MyStack.append(Value)
 else:
    print("Stack is full!")

def Pop():
 if len(MyStack) > 0:
    MyStack.pop()
 else:
    print("Stack is empty.")

Push(1)
Push(2)
Push(3)
DisplayStack()
input("Press any key when ready...")
Push(4)
DisplayStack()
input("Press any key when ready...")
Pop()
DisplayStack()
input("Press any key when ready...")
Pop()
Pop()
Pop()
DisplayStack()   

# Queue
import queue
studentline = queue.Queue(3)
print(studentline.empty())
studentline.put("prasanna")
studentline.put("punam")
studentline.put("prajita")
print(studentline.full())
print(studentline.get())
print(studentline.get())
print(studentline.get())
print(studentline.empty())   

# Dequeue
import collections
MyDeque = collections.deque("abcdef", 10)
print("Starting state:")
for Item in MyDeque:
 print(Item, end=" ")
print("\r\n\r\nAppending and extending right")
MyDeque.append("h")
MyDeque.extend("ij")
for Item in MyDeque:
 print(Item, end=" ")
print("\r\nMyDeque contains {0} items."
 .format(len(MyDeque)))
print("\r\nPopping right")
print("Popping {0}".format(MyDeque.pop()))
for Item in MyDeque:
 print(Item, end=" ")
print("\r\n\r\nAppending and extending left")
MyDeque.appendleft("a")
MyDeque.extendleft("bc")
for Item in MyDeque:
 print(Item, end=" ")
print("\r\nMyDeque contains {0} items."
 .format(len(MyDeque)))
print("\r\nPopping left")
print("Popping {0}".format(MyDeque.popleft()))
for Item in MyDeque:
 print(Item, end=" ")
print("\r\n\r\nRemoving")
MyDeque.remove("a")
for Item in MyDeque:
 print(Item, end=" ")   
 
