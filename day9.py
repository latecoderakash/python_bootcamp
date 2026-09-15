#dictionary
# names = {
# #     "a" : "Akash",
# #     "s" : "Swapnil",
# # }

# print(names["s"])
# print(names["a"])

#wipe dictionary values

# names = {}
# print(names)

#loop thorugh dictionary

# for key in names:
#     print(key)
#     print(names[key])

# Grading program
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# student_grades = {}
# for key in student_scores:
#     if student_scores[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] > 80 and student_scores[key] <= 90:
#             student_grades[key] = "Excceds Expectations"
#     elif student_scores[key] > 70 and student_scores[key] <= 80:
#                 student_grades[key] = "Acceptable"
#     elif student_scores[key] <= 70:
#                 student_grades[key] = "fail"
# print(student_grades)

#nesting

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

travel_log ={
    "India": ["Luknow","Noida"],
    "Singapore": ["A","B"]
}
print(travel_log["India"][1])