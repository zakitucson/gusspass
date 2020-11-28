trupass = "123@zaki"
trys = 5
putpass = input("Please Guss The Password: ")
while putpass != trupass:
    trys -= 1
    print("The Password Is Wrong!")
    putpass = input("Please Guss The Password: ")
    if trys == 0 and putpass == trupass:
        print("Tru Pass Wellcom")
        break
    
    if trys == 0:
        print("No More Chance Come Later!")
        break
else:
    print("tru pass")