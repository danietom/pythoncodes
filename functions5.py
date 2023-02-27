def grading(marks):
    if((marks>=70) and (marks<=100)):
        print("Grade A")
    elif((marks>=60) and(marks<=69)):
        print("Grade B")
    elif((marks>=50) and(marks<=59)):
        print("Grade C")
    elif((marks>=40) and(marks<=49)):
        print("Grade D")
    elif((marks>=0) and(marks<=39)):
        print("Grade E")
    else:
        print("INVALID GRADE.")
grading(80)
grading(65)
grading(55)
grading(45)
grading(35)
grading(5)
grading(800)
