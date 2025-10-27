start= int(input("enter the start range "))
end = int(input("enter the end range "))
skip=int(input("enter the number you want to skip "))
while skip>end or skip<start:
    print("invalid inpute ")
    skip = int(input("you have enter number out or range please re enter :"))
else:
    for num in range(start,end):
        if num==skip:
            continue
        print(num)