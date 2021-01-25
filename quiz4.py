from random import *

# print(" -- 당첨자 발표 -- ")
# chicken = randint(1, 20)
# print(f"치킨 당첨자 : {chicken}")

# coffee = list(range(1, 20))
# coffee.remove(chicken)
# shuffle(coffee)
# print(f"커피 당첨자 : {sample(coffee, 3)}")

users = range(1, 21)
print(type(users)) #range
users = list(users)
print(type(users)) #list

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print(winners)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
