#CONDITIONAL STATEMENTS

# Conditional statements are used to execute code only if certain conditions are met. 
# They allow programs to make decisions and respond differently based on different inputs or states.
# The primary conditional statements in Python are if, elif, and else

# Keywords in python, (reversed words )  # Operators (logical,comparison etc)

# if statement (run a block of code only if a condition is true)
#Mind about indentation


# Syntax 
#if condition:
  #statement

#Practical Example
age = 24 #Greater or equal to 18 (condition) # You are eligible for voting!!
ageTwo = 15
if ageTwo >= 18: 
  print("You are eligible for voting!!")

else: #Else Statememts  
  print("You are not eligible for voting!!")

#Multiple conditions
#Student grade ranges
#90 - 100 - A
#80 - 89 - B
#70 - 79 - C
#60 - 69 - D
#50 - 59 - E
#Below 40 - failed

mark = int(input("Enter your mark scored: "))

if (mark >=90 and mark <=100):
  print("A")

elif(mark >=80 and mark <=89):
   print("B")

elif(mark >=70 and mark <=79):
   print("C")

elif(mark >=60 and mark <=69):
   print("D")

elif(mark >=50 and mark <=59):
   print("E") 

else:
     print("Failed") 

# marks = [] 
# totalMarks  = input("")

# while running == True:
#    #append the marks
#    #varible to store all marks, lists [60,70,50,80]
#    #provide a condition for the number of marks to be entered
   
# #[60, 90], [60,70,50,80]




  

 
