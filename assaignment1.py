#!/bin/python3

fib0=0          #this is the variable to start at 0
p=0             #this is a place holder for fib0
fib1=0        #this is the variable to start at 1
sum1=0          #variable equaling fib1 and fib0 

#print("ok here we go")  #just some random thing i thought would be cool before the loop starts
#while sum1<50:   #while loop idk 
 #   print(sum1)     #prints everytime the loop finishes
 #   if sum1<50:         #begins all the math to start adding variables
  #      sum1=fib1+fib0  #self explanatory
   #     p=fib1              #holds the value of fib1 before it gets added to fib2
    #    fib1=fib0+fib1      #adds fib0-1
     #   fib0=p              #gives fib0 the falue of p which was fib1 before math
        



import argparse             #imports argparse
parser= argparse.ArgumentParser()   #begins the module
parser.add_argument("num",help="please type a int here",type=int) #adds the argument for num
args = parser.parse_args()                       #variable args holds the parse argument   
print(args.num)                                 #prints args with the variable argument num
filename= input("where would like me to write this file to\n")
f=open(filename,"w")                            #opens krm-hw to write to
fib1=args.num                                   #variables 
dib0=args.num
print("do you want to overwrite?")
answer=input("yes or no\n")                       #userinput to overwrite or not
if answer=="no":
    f.close()
    print("no? ok canceling")
        
elif answer=="yes":
    print("yes?, ok here we go")
    while sum1<1000000:          #condensed the above code into this and added writing to file
        print(sum1)                             
        sum1=fib1+fib0
        p=fib1
        fib1=fib0+fib1
        fib0=p
        f.write(str(sum1))
        f.write(",")

else:
    print("invalid input....")
    print("goodbye.")
