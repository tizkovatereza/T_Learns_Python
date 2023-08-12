name = "Unicorn"
question = "Are unicorns real?"
answer = ""

import random
#Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:
random_number = random.randint(1,9)

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
else:
      answer = "Error"


print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)
  


#Yes - definitely
#It is decidedly so
#Without a doubt
#Reply hazy, try again
#Ask again later
#Better not tell you now
#My sources say no
#Outlook not so good
#Very doubtful





#[Name] asks: [Question]
#Magic 8-Ball’s answer: [Answer]

#Joe asks: Is this real life?
#Magic 8-Ball's answer: Better not tell you now
