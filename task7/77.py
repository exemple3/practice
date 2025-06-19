letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

a = input()
if (len(a) == 6 and
    a[0] in letters and
    a[1] in digits and
    a[2] in digits and
    a[3] in digits and
    a[4] in letters and
    a[5] in letters):
    print("Yes")
else:
    print("No")
