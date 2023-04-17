
## *Args: Beliebiger Anzahl von Werte Arguments --> Tuple
def demo_args(*container):
    for val in container:
        print(val)

demo_args(1,2)

demo_args(1, 2, "Apfel", "Banana")

demo_args(1, "Mango", True, ["A", "B"])
print()


###################################################


### **KWArgs ( Keyword Argument) : Beliebiger Anzahl von Values UND Parameter Bezeichnung --> Dictionary

def show_information(first_name, last_name, **kwargs):
    print(first_name, last_name, kwargs)
    for key,val in kwargs.items():
        print(key , val)


# Consumer
show_information("Thomas", "Meier", car = "VW")

show_information("Sara", "Meier", car = "VW", color = "Black")

show_information("Ingo", "Meier", kinderanzahl = 2, wife = "Lena")

show_information("Frank", "Meier")

####################################################


def greeting(first_name, last_name, city = "Berlin", *args, **kwargs):
    print(first_name, last_name, city, args, kwargs)



# Consumer
greeting("Thomas", "Meier")
greeting("Sara", "Meier", "Hannover")
greeting("Lena", "Meier", "Hannover",1,2,3)
greeting("Ingo", "Meier", "Hannover",1,2,3,4,5,6)
greeting("Frank", "Meier", "Hannover",1,2, car ="VW")
greeting("Frank", "Meier", "Hannover",1,2,3, color ="Black")
greeting("Frank", "Meier", "Hannover",1,2,3,4,5, kinder =2, housenr = 60)