totalMark = int(input("Enter the total marks : "))

marks = {
    "firstSub": 100, 
    "secSub": 100, 
    "thirdSub": 100
}

firstSubMark = int(input("Enter the marks for first subject. "))
secondSubMark = int(input("Enter the marks for second subject. "))
thirdSubMark = int(input("Enter the marks for third subject. "))

marks.update({"firstSub": (firstSubMark/totalMark) * 100, "secSub": (secondSubMark/totalMark) * 100, "thirdSub": (thirdSubMark/totalMark) * 100})

if(marks["firstSub"]< 33 or marks["secSub"]<33 or marks['thirdSub']<33): 
    print("The person failed because he failed in one subject. ")
else: 
    if(((marks["firstSub"] + marks["secSub"] + marks["thirdSub"]) / 4) <40): 
        print("The person failed in average marks. ")
    else: 
        print("The person passed. ")