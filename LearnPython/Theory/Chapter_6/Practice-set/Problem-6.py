enteredMarks = int(input("Enter the marks : "))
marksSchema = {
  enteredMarks >= 90 or enteredMarks == 100:"Ex" , 
  enteredMarks >= 80 and enteredMarks < 90: "A", 
  enteredMarks >= 70 and enteredMarks < 80: "B" , 
  enteredMarks >=60 and enteredMarks < 70: "C"  , 
  enteredMarks >= 50 and enteredMarks < 60: "D",
  enteredMarks < 50 :  "F"
}

print(f"The obtained grade is : {marksSchema[True]}")