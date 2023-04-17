# Too Bad
print("Hallo Mohamed")
print("Welches BKG hast du ?")
print("Python Vorkenntnisse ?\n")

print("Hallo Thomas")
print("Welches BKG hast du ?")
print("Python Vorkenntnisse ?\n")

print("Hallo Ingo")
print("Welches BKG hast du ?")
print("Python Vorkenntnisse ?\n")

print("Hallo Sara")
print("Welches BKG hast du ?")
print("Python Vorkenntnisse ?\n")

print("Hallo Lena")
print("Welches BKG hast du ?")
print("Python Vorkenntnisse ?\n")

##############################################################
# With Loops

tn_list = ["Mohamed", "Thomas", "Ingo", "Sara", "Lena"]

for teilnehmende in tn_list:
    print("Hallo", teilnehmende)
    print("Welches BKG hast du ?")
    print("Python Vorkenntnisse ?\n")


###############################################################
# with function

def greeting(teilnehmende:str):
    print("Hallo", teilnehmende)
    print("Welches BKG hast du ?")
    print("Python Vorkenntnisse ?\n") 


### Consumer --> should send the name of each TN

tn_list = ["Mohamed", "Thomas", "Ingo", "Sara", "Lena"]

for teilnehmende in tn_list:
    greeting(teilnehmende)


############################################################

def greet_all_people(teilnehmer_list:list):
    for teilnehmende in teilnehmer_list:
        print("Hallo", teilnehmende)
        print("Welches BKG hast du ?")
        print("Python Vorkenntnisse ?\n") 

### Consumer: ---> sends the list of all PT and i will do the rest
tn_list = ["Mohamed", "Thomas", "Ingo", "Sara", "Lena"]
greet_all_people(tn_list)

