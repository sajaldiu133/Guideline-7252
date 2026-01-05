# in page_1 
""" 1.simple print 
    2.data_type
    3.Variable declaration
    4.Arithetic operation(short)
"""

                     #  in this page_2 

  #                      1.  Variable (3. type , 4.type conversion #  )
  #                      2.  Taking input (5.input)


"""  3. TYPE """

# 3.1 code
n = 1  
print(type(n))            #SAME for other data type 
            #Output int 
            

""" 4. TYPE CONVERSION """

# 4.1 code (int - float)
a = 15      
b= float(a)

print(type(a))
print(type(b))   # same as float to int

# 4.2 code (str - int)

a = "16"
b = int(a)
print(b)
print(type(a))
print(type(b))     #same as str - float

# 4.3 code(bool type)

print(bool(0)) # False
"""      ( 0 hole always False asbe )  """

print(bool("")) # False 
""" ("") double quotation er vitore kono  value na thakle False """


print(bool(1)) # True 
   
   #Value , space , number , special charrectr  """
       #  agulo thakle answe True Hoi """"

print(bool("@")) # True

print(bool("-")) #True
  
print(bool("hi"))   # True



#     5. input 

#5.1 code
      
user = input("Enter Anything : ")# eta basically string akare input nei 

""" input jodi 10 neo ata str show korbe """
print(user)
print(type(user))

#5.2 code
"""Float / int data type input """

user1 = int(input("Enter Number "))
print(type(user1))
                         # data type int e asbe same as float 

    
#simple math (sum)

#wrong way
a = input("Enter number a = ")
b = input("Enter number b = ")
sum = a + b
print(sum) #  jodi input 3 , 1 deya hoi 
#              output  ""  31 ""

#right_way
a = int(input("Enter number a = "))
b = int(input("Enter number b = "))
sum = a + b
print(sum) 

          # jodi input 3,1  deya hoi
#           output = 4