# Howard Miller
run = True
def decoder(password):
    # empty string of the old encoded password
    old_password = ""

    # iterates over the password for each character
    for dig in password:
        # subtracts 3 from each character
        new_digit = int(dig) - 3

        # if the new digit is negative add 10
        if new_digit < 0:
            old_password += str(new_digit+10)
            # goes to the top of the loop
            continue

        # adds this string to the old_password string
        old_password += str(new_digit)

    # returns the old password
    return old_password

while run == True:
    raw = input("Enter value to encode: ")
    print(decoder(raw))