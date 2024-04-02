#Here we have a couple of lists, each list is dedicated to a particular student's test grades for this semester



#Students
jeff_grades = [87,90,86,79,88,22]

lisa_grades = [92,94,89,90,86,23]

george_grades = [73,82,85,74,78,21]

kendra_grades = [63,38,72,65,54,23]

#There was a mistake with the system and it accidentally added a really low test grade for all of the students, can you remove the lowest test grade from all of the student lists?
jeff_grades.remove(22)
lisa_grades.remove(23)
george_grades.remove(21)
kendra_grades.remove(23)

#As a part of a bonus grade, we are allowing each student to drop their lowest score so they can have a better average grade, can you remove the lowest test grade from each list? But make sure the grade is printed out!

#print(jeff_grades.pop(3))
#print(lisa_grades.pop(4))
#print(george_grades.pop(0))
#print(kendra_grades.pop(1))

print("This grade was just deleted: " + str(jeff_grades.pop(jeff_grades.index(min(jeff_grades)))))
print("This grade was just deleted: " + str(lisa_grades.pop(lisa_grades.index(min(lisa_grades)))))
print("This grade was just deleted: " + str(george_grades.pop(george_grades.index(min(george_grades)))))
print("This grade was just deleted: " + str(kendra_grades.pop(kendra_grades.index(min(kendra_grades)))))

#Kendra has decided that she is going to drop the class after seeing her average, can you remove all of her test grades and print her list?

kendra_grades.clear()
print(kendra_grades)




