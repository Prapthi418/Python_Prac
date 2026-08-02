def greet(): 
    print("Hello pratham") 
    print("welcome to python") 

greet() 

def greet(): 
    print("Hello") 

greet() 

def calculate_total(): 
    price = 1000 
    tax = price * 0.18 
    total = price + tax     
    print(total) 
calculate_total() 

#Parameters vs Arguments 
def greet(name):
    print(f"Hello {name}") 
greet("Pratham") 

#Multiple parameters 
def introduce(name,age): 
    print(f"my name is {name} and I am {age} years old") 
introduce("Pratham",20) 

#Print vs Return 
def add(a,b): 
    print(a+b) 
add(5,10) 

def add(a,b): 
    return a + b 
result = add(5,10)  
final_result = result * 2   
print(final_result) 

#Function execution with return 
def add(a,b): 
    result = a + b 
    return result 

answer = add(10,20) 
print(answer) 

def test(): 
    print("A") 
    return  
    print("B")   
test() 

def calculate_square(number): 
    return number * number 
result = calculate_square(5)  
print(result)   
