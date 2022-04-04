def to_usd(my_price):
    """
    This is a docstring. It tells us what this function is about. 
    Invoke like this: to_usd(99.999)
    """
    return '${:,.2f}'.format(my_price)

if __name__=="__main__":
    # nesting code in the main condition will
    #allow other scripts to cleanly import
    #without running this code

    #this code still gets run when we invoke the script from the command line
    price = input("Please choose a price like 4.9999")

    print(to_usd(float(price)))
