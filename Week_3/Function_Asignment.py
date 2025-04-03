'''Create a function named calculate_discount(price, discount_percent) 
that calculates the final price after applying a discount. 
The function should take the original price (price) and the discount 
percentage (discount_percent) as parameters. If the discount is 20% or higher,
apply the discount; otherwise, return the original price.
 
Using the calculate_discount function, prompt the user to enter the 
original price of an item and the discount percentage. Print the final 
price after applying the discount, or if no discount was applied, print the original price.'''

def calclate_discount (a,b):
    if b <= 20:
        return (a)
    else :
        y= 1 - (b/100)
        return(a*y)


price = int(input("What is the price: "))
discount = int(input("What is the discount: "))

print(calclate_discount(price,discount))
