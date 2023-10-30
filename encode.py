# Howard Miller
from decoder import decoder

run = True

def encoder(password):
    # empty string of the new encoded password
    new_password = ""

    # iterates over the password for each character
    for dig in password:
        # adds 3 to each character
        new_digit = int(dig) + 3

        # checks to see if the new value is greater than 9
        if new_digit > 9:
            # subtracts 10 from that value
            new_password += str(new_digit-10)
            # restarts the loop
            continue

        # adds this new digit to the new password string
        new_password += str(new_digit)

    # returns the new_password
    return new_password

while run == True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    option = input("Please enter an option: ")

    if option == "1":
        raw = input("Please enter your password to encode: ")
        encoded_password = encoder(raw)
        print("Your password has been encoded and stored!\n")

    elif option == "2":
        print(f"The encoded password is {encoded_password}, and the original password is {decoder(encoded_password)}.\n")

    elif option == "3":
        run = False