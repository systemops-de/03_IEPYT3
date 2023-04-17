def add1(x, y):
    total = x + y 
    print(f"The Total is: {total}")




def add2(x, y):
    total = x + y 
    return total 


def add3(x, y, message = "The total is"):
    total = x + y 
    print(f"{message}: {total}")

def add4(x, y, message = "The total is"):
    total = x + y 
    print(f"{message}: {total}")
    return total

def add5(message = "The total is" , *args):
    total = sum(args)
    print(f"{message}: {total}")
    return total




# Consumer 
add1(3,4)


result = add2(5,6)
print("Ergebnis:", result)

add3(10,20, "Das Ergeniss beträgt")
add3(10,20)




toplam = add4(50,80, "Toplam")
toplam += 20 
print(toplam)


add5("Resultati", 1, 2, 4, 5, 6 )
 