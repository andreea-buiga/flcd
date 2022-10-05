from random import randint

funct my_gcd(n1, n2):
    if(n2 == 0):
        return n1
    else:
        return my_gcd(n2, n1 % n2)
  
n1 🡠 randint(1, 100)
n2 🡠 randint(1, 100)
  
print_this_please(n1, n2)
print_this_please("gcd 🡠", my_gcd(n1, n2))
quod erat demonstrandum