from py_extras import change_stmt


def make_change(cost, amount_given):
  twenties = 0, tens = 0, ones = o, quarters = 0, dimes = 0, nickels = 0, pennies = 0
    change = amount_given - cost
    while change is >= 20 
    twenties = twenties + 1
    change = change - 20
    change = amount_given - cost
    while change is >= 10
    tens = tens + 1    
    change = change - 10
    change = amount_given - cost
    while change is >= 1
    ones = ones + 1
    change = change - 1
    change = amount_given - cost
    while change is >= .25
    quarters = quarters + 1
    change = change - .25
    change = amount_given - cost
    while change is >= .10
    dimes = dimes + 1
    change = change - .10
    change = amount_given - cost
    while change is >= .05
    nickels = nickels + 1
    change = change - .05
    change = amount_given - cost
    while change is >= .01
    pennies = pennies + 1
    change = change - .01
    change = amount_given - cost
    change_stmt()
        # Consider using variables that match the variables used in the call to change_stmt() below

    # This will be the final statement of make_change() and will return the appropriate string
    return change_stmt(twenties, tens, fives, ones, quarters, dimes, nickels, pennies)


if __name__ == '__main__':
    # Test your code with this first 
    # Change the cost and paid values to try different inputs
    cost = 45.33
    paid = 77.22
    s = make_change(cost, paid)
    print(s)

    # After you are satisfied with your results, use input() calls to prompt the user for values:
    # cost = float(input("Cost of the items: "))
    # paid = float(input("Amount paid: "))
    # print(make_change(cost, paid))
