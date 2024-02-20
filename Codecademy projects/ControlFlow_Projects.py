name = "Unicorn"
question = "Are unicorns real?"
answer = ""

import random
#Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:
random_number = random.randint(1,10)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "Why are you asking such dumb questions? Dont you have work to do?"
else:
      answer = "Error"

if name == "":
  print("Question:" + question)
else:
  print(name + " asks: " + question)

print("Magic 8-Ball's answer: " + answer)
  


#[Name] asks: [Question]
#Magic 8-Ball’s answer: [Answer]

#Joe asks: Is this real life?
#Magic 8-Ball's answer: Better not tell you now


weight = 1.5

#Ground Shipping


if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20


print("Cost: " + str(cost_ground))

cost_premium_ground = 125.00

print("Premium Cost: " + str(cost_premium_ground))


##############################################################################################################


#Drone Shipping
if weight <= 2:
  drone_shipping = weight * 4.5 + 0
elif weight <= 6:
  drone_shipping = weight * 9.0 + 0
elif weight <= 10:
  drone_shipping = weight * 12.0 + 0
else:
  drone_shipping = weight * 14.25 + 0

print("Drone Shipping Cost: " + str(drone_shipping))


