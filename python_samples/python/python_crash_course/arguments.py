def add_pizza_toppings(*toppings):
    print('Make a pizza with the below toppings:')
    for num,topping in enumerate(toppings):
        num+=1
        print str(num)+'.'+ str(topping)
    print("end of function")
    print('\n')


#add_pizza_toppings('pepperoni','capsicum','tomato')
#add_pizza_toppings('plain cheese')

'''=================================================================='''

def default(cat,dog,parrot):
    print 'cat =',cat,'\n','dog =', dog,'\n','parrot =',parrot
    print('end of function')
    print('\n')


default(parrot='tweety',cat='tom',dog='garfield')
