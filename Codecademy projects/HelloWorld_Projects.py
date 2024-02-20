###########################################################################################################################################################################
# Project 1

Twitter: @tereza_tizkova
# Fun Fact: I am boring.

LetterT = """
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
        TTT
        TTT
        TTT
        TTT
        TTT
        TTT
        TTT
        TTT
        TTT
"""
        
                
print(LetterT + LetterT)

###########################################################################################################################################################################
# Project 2

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

#In order to be a business, we should also be calculating sales tax. Let’s store that in a variable as well. Define the variable sales_tax and set it equal to .088. That’s 8.8%.

sales_tax = .088

# Our first customer is making their purchase! Let’s keep a running tally of their expenses by defining a variable called customer_one_total. Since they haven’t purchased anything yet, let’s set that variable equal to 0 for now.
customer_one_total = 0


#We should also keep a list of the descriptions of things they’re purchasing. Create a variable called customer_one_itemization and set that equal to the empty string "". We’ll tack on the descriptions to this as they make their purchases
customer_one_itemization = ""

#Our customer has decided they are going to purchase our Lovely Loveseat! 
customer_one_total += lovely_loveseat_price

#Let’s start keeping track of the items our customer purchased. Add the description of the Lovely Loveseat to customer_one_itemization.
customer_one_itemization += lovely_loveseat_description

#Our customer has also decided to purchase the Luxurious Lamp! 

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description


customer_one_tax = customer_one_total * sales_tax
customer_one_total += sales_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total")
print(customer_one_total)



































