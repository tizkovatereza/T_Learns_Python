last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 


subjects = ["physics","calculus","poetry","history"]
grades = [98
,97
,85
,88]

gradebook = [["physics",	98],["calculus",	97],["poetry",	85],["history",	88]]

unicorn1 = ["computer science", 100]
gradebook.append(unicorn1)

unicorn2 = ["visual arts", 93]
gradebook.append(unicorn2)

gradebook[-1][1] = 98

gradebook[2].remove(85)
potery_sublist = gradebook[2]
print(potery_sublist)
potery_sublist.append("Pass")

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)


print(subjects)
print(grades)
print(gradebook)
