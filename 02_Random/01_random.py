import random  #  standard library



# Float
print(random.random()) # 0 - 1
print(random.uniform(5, 10)) 

# Integer
print(random.randint(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10, 2)) # [1, 3, ---, 9] Ungerade


# choice(s)
# ~~~~~~~~~~~~~~

teilnehmer_list = ["Thomas" , "Ingo", "Sara", "Lena"]

print(random.choice(teilnehmer_list)) # random single choice


# Choices --> With duplicate
print(random.choices(teilnehmer_list, k = 2)) # random multi choice
print(random.choices(teilnehmer_list, k = 10)) # random multi choice


# sample---> without duplicate
print(random.sample(teilnehmer_list, k = 3)) # random multi choice


# Shuffling -> mix the order
# ~~~~~~~~~~~
numbers = [ 1, 2, 3, 4, 5]

print(numbers)

random.shuffle(numbers) # --> in-place --> changes to original container

print(numbers)

print()
##########################
# Example: generate 5x random integers between 0 and 30 without duplicate

print(random.sample( range(0, 31) , k = 5))