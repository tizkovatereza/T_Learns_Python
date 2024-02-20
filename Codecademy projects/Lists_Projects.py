last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 


subjects = ["physics","calculus","poetry","history"]
grades = [98
,97
,85
,88]

gradebook = [["physics",	98],["calculus",	97],["poetry",	85],["history",	88]]

unicorn1 = ["computer science", 100]
gradebook.append(unicorn1)

unicorn2 = ["visual arts", 93]
gradebook.append(unicorn2)

gradebook[-1][1] = 98

gradebook[2].remove(85)
potery_sublist = gradebook[2]
print(potery_sublist)
potery_sublist.append("Pass")

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)


print(subjects)
print(grades)
print(gradebook)


################################################################################################################################################

# Your code below:

toppings = ["pepperoni",
"pineapple",
"cheese",
"sausage",
"olives",
"anchovies",
"mushrooms"]

prices = [2,
6,
1,
3,
2,
7,
2]

num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

print("Number of occurences of 2 in the prices is: " + str(num_two_dollar_slices))
print("Length of toppings list is: " + str(num_pizzas))

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = [[2,"pepperoni"],[6,"pineapple"],[1,"cheese"],[3,	"sausage"],[2,	"olives"],[7,"anchovies"],[	2, "mushrooms"]]

pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop(-2)
pizza_and_prices.apend[2.5, "peppers"]


print(pizza_and_prices)
print("The cheapest pizza is: " + str(cheapest_pizza))
print("The priciest pizza is: " + str(priciest_pizza))























