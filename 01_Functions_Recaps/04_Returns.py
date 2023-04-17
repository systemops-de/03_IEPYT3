# Function without return *
def greeting1(first_name):
    print("Hallo", first_name)

# With single return
def greeting2(first_name):
    print("Hallo", first_name)
    return "True"


# With Multi- Return --> Tuple
def greeting3(first_name):
    print("Hallo", first_name)
    return "True", "Hallo", 30, 12.3




# Cosumer
greeting1("Thomas")

single_return = greeting2("Thomas")


multi_return_tuple = greeting3("Lena")
print(type(multi_return_tuple), multi_return_tuple)

# Using Unpacking --> directly to 4x different variables
a, b, c, d = greeting3("Lena") # 4x values as returns --> in 4x Containers
print(a, b, c, d)


 

