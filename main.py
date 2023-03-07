# Robert Meekins
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(unencoded):
    encoded = ""
    #1234
    for i in unencoded:
        encoded += str((int(i) + 3) % 10)
    return encoded


def main():
    while True:
        print_menu()
        choice = input("Please enter an option: ")
        if choice == '3':
            break
        if choice == '1':
            password = input("Please enter your password to encode: ")
            password = encode(password)
            #print(password)
            print("Your password has been encoded and stored!")


if __name__ == '__main__':
    main()
