from scanner import Scanner


def print_menu():
    print("choose program to scan:")
    print("1 | p1.txt")
    print("2 | p2.txt")
    print("3 | p3.txt")
    print("4 | p1err.txt")


done = False
files = ["./p1.txt", "./p2.txt", "./p3.txt", "./p1err.txt"]
print_menu()
while not done:
    option = int(input("\n\n>> my option: "))
    if option == 1 or option == 2 or option == 3 or option == 4:
        scanner = Scanner(option)
        scanner.set_option(option)
        print(f"Scanning {files[option - 1]}...")
        scanner.scan(files[option - 1])
        print(scanner.get_message())
    elif option == 0:
        done = True
    else:
        print("bad command!")
