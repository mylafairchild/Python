#Salary calculator. 2.7% state, 33% fed taxes. This is old Python2 booooooooo

salary = 55.00
st_tax = 0.027
fed_tax = 0.033

salary = salary + salary * st_tax
total = salary + salary * fed_tax

print("%.2f" % total)
