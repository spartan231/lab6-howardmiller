#decode function
run = True


def decode(inpu):
    ret = ""
    for i in range(0, len(inpu)):
        temp_num = int(inpu[i]) - 3 #basic decode (Raw)
        if temp_num < 0:
            ret += str((10-abs(temp_num))) #full decode (final)
        else:
            ret += str((temp_num))
    return ret


while run == True:
    raw = input("Enter value to encode: ")
    print(str(decode(raw)))