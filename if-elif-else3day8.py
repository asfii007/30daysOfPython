#Write a Python program that asks the user to enter their exam score (0–100).

#If the score is 90 or above, print "Grade: A"

#If the score is 80–89, print "Grade: B"

#If the score is 70–79, print "Grade: C"

#If the score is 60–69, print "Grade: D"

#If the score is below 60, print "Grade: F"
score=int(input("enter your score here:"))
if score>=90 and score<=100:
    print("grade: A")
elif score>=80 and score<=89:
    print("grade:B")
elif score>=70 and score<=79:
    print("grade:C")
elif score>=60 and score<=69:
    print("grade:D")
else:
    print("grade: F")    

#ANOTHER VERSION:it rejects scores that are not between 0 and 100


score = int(input("Enter your exam score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score! Please enter a number between 0 and 100.")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
