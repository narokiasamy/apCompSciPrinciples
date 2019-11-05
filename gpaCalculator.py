# these are the statements that gather the data on the kind of GPA  user would like to see 
print ("What kind of GPA would you like to view? (enter without honors points, with honors points, or hope GPA)")

userInput = str(input())

# this is the function which converts the raw scores into numbers on the 4.0 scale
def calcNumberGrade():
  if (grade >= 90):
    numberGrade = 4.0
  elif (grade >= 80):
    numberGrade = 3.0
  elif (grade >= 70):
    numberGrade = 2.0
  else:
    numberGrade = 1.0
  return numberGrade

# this conditional takes in the user input on what kind of GPA they would like to view and uses it calculate the GPA, making adjustments based on what the grades are
if (userInput == "without honors points"): 
  print ("Type out the six grades for your six classes (with no honors points, raw grade only)")
  numberGradeTotal = 0
  numberGrade = 0
  for i in range (6):
    grade = int(input())
    x = calcNumberGrade()
    numberGradeTotal = numberGradeTotal + x
  withoutHonorsPoints = numberGradeTotal / 6
  print (float(withoutHonorsPoints))
  if (withoutHonorsPoints >= 3.72):
    print ("You qualified for the zell miller scholarship!")
elif (userInput == "with honors points"):
  print ("Type out the six grades for your six classes (with no honors points, raw grade only)")
  numberGradeTotal = 0
  numberGrade = 0
  for i in range (6):
    grade = int(input()) + 7
    x = calcNumberGrade()
    numberGradeTotal = numberGradeTotal + x
  withHonorsPoints = numberGradeTotal / 6
  print (float(withHonorsPoints))
elif (userInput == "hope gpa"):
  apClasses = int(input("Enter the number of AP classes you are taking (only if you don't already have an A in this class):"))
  print ("Type out the six grades for your six classes (with no honors points, raw grade only)")
  numberGradeTotal = 0
  numberGrade = 0
  for i in range (6):
    grade = int(input())
    x = calcNumberGrade()
    numberGradeTotal = numberGradeTotal + x
  numberGradeTotal = numberGradeTotal + (apClasses * 0.5)
  hopeScholarship = numberGradeTotal / 6
  print (float(hopeScholarship))