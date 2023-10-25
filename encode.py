# Howard Miller
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

