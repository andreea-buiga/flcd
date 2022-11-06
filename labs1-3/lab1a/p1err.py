def maxNumber(n1, n2, n3):
    if (n1 >= n2 and n1 >= n3):
        return n1
    
    if (n2 >= n1 and n2 >= n3):
        return n2

    if (n3 >= n1 and n3 >= n2):
        return n3

# 1) using input instead of READ
n1 🡠 int(input("n1 🡠 "))
n2 🡠 int(READ("n2 🡠 "))
# 2) using equal intead of arrow 🡠
n3 = int(READ("n3 🡠 "))

print_this_please(n1, n2, n3)
print_this_please(maxNumber(n1, n2, n3))
quod erat demonstrandum