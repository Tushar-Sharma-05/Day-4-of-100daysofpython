import random
people = input("Give me everybody's name seperated by a comma\n")
list_of_people = people.split(",")
# lengthoflist = len(list_of_people)
# choice = random.randint(0,lengthoflist-1)
person_whowill_pay = random.choice(list_of_people)
print(person_whowill_pay,"is going to pay todays bill!!")