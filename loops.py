#LOOPS

#1. For loop
# Iterates over  a sequence  (strings,lists,dictionaries)
# Syntax
#for  variable in interable:
  #code block

#Example
courseUnit = "Principles of Programming"
marks = [90,60,100]
for item in courseUnit:
    print(item)

#Using a list
for mark in marks:
    print(mark)
    

#2. While Loop
#Continue executing the code block as long as a condition is true

#Syntax
#while condition:
  #code block

 
#Example
#print numbers from 1 to 8  
#(1-8) #9 to make 8 inclusive 
number = 1
while number <=8:
    print(number) 
    number += 1

#3. range() Function
#Generates an iterable sequence of numbers
#Syntax
# range(start,stop,step)

#Example 1 (Basic Approach)
for num in range(6): #0-5 #Numbers from 0 to 5 (0,1,2,3,4,5)
    print(num)

#Example 2
for num in range(3,7): # 3-6 (3,4,5,6)
    print(num)

#Example 3
for num in range(1,11,2): # Odd numbers (1,3,5,7,9)
    print(num)

#Example 4
for num in range(2,11,2): # Even numbers (2,4,6,8,10)
    print(num)



#Read about break and  continue

