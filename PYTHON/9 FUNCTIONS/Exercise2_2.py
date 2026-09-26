counter = 10 # global variable 

def show_counter():
    print(counter)

show_counter() # show you the value of the global variable because you are not modifying its valor inside the function


#Using the global function inside the function you can modify the original value of the global variable

counter = 10 #global variable 

def increase():
    global counter 
    counter = counter + 1
    print(counter)

increase()


#The same example but not using the global function inside the function, that makes an error because you need the function global 

counter = 10 #global variable 

def increase():
    counter 
    counter = counter + 1
    print(counter)

increase()