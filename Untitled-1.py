print("=============================================================================")
print("Shipping Calculator")
print("=============================================================================")

choice = "y"
while choice.lower() == "y":

        
        
    costOrdered = float(input("Cost of items ordered: \t"))  
   
    if costOrdered < 0:
        print("You must enter a positive number. Please try again.")
        continue
   
        print()
    elif costOrdered < 0 and costOrdered < 3000:
        shipping = costOrdered * 0.03
        print("Shipping Cost: \t", shipping)
        total = costOrdered + shipping
        print("Total Cost: \t", total)
    elif costOrdered < 4999:
        shipping = costOrdered * 0.04
        print("Shipping Cost: \t", shipping)
        total = costOrdered + shipping
        print("Total Cost: \t", total)
    elif costOrdered < 7499:
        shipping = costOrdered * 0.05
        print("Shipping Cost: \t", shipping)
        total = costOrdered + shipping
        print("Total Cost: \t", total)
    else:
        shipping = 0

    print()

       #test if user wants to continue
    choice = input("Continue (y/n)?: ")
    print()
print("=============================================================================")    
print("Bye!")

