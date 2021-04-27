## IMPORTS
from random import randint, choice
import sale_tax

#-------------------------MAIN TASK--------------------------------------------
"""
"""
def use_sale_tax():
    # calculate_tax
    # data = [[randint(10,100), choice(list(sale_tax.PROVINCE)), choice(sale_tax.HOURS+[-15,33])] for _ in range(randint(3,10))]
    # for elem in data: print(*elem,'total:',sale_tax.calculate_tax(*elem))
    # calculate_income
    data = [choice([-100,200,3000,19000,60000,35000]) for _ in range(randint(3,10))]
    for elem in data:
        try:
            print(elem,'total tax to pay:',sale_tax.calculate_income(elem))
        except sale_tax.IncomeTooLow as e:
            print(elem, e)
#-------------------------BEYOND THE TASK--------------------------------------

if __name__ == '__main__':
    use_sale_tax()
