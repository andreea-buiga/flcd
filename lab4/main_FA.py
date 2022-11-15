from FA import FA


def print_menu():
    print("\n")
    print("-" * 30)
    print("choose what you want to display:")
    print("\t• 1 • the set of states")
    print("\t• 2 • the alphabet")
    print("\t• 3 • all transitions")
    print("\t• 4 • the initial state")
    print("\t• 5 • the final states")
    print("\t• 6 • check sequence")
    print("\t• 0 • to exit")
    print("-" * 20)


def menu():
    fa = FA("./FA_input/FA_identifier.in")
    while True:
        try:
            print_menu()
            option = int(input("your choice >> "))
            if option == 1:
                print(fa.get_FA_Q())
            elif option == 2:
                print(fa.get_FA_E())
            elif option == 3:
                print(fa.get_FA_d())
            elif option == 4:
                print(fa.get_FA_q0())
            elif option == 5:
                print(fa.get_FA_F())
            elif option == 6:
                seq = input("give sequence to verify >> ")
                if fa.check_sequence(seq):
                    print("✔ sequence accepted by FA")
                else:
                    print("❌ NOT accepted by FA")
            elif option == 0:
                return
            else:
                print("wrong option!")
        except Exception as e:
            print(e)


menu()
