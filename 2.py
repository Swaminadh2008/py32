email = input()
student_id = input()

email_valid = email.endswith("@college.edu")
id_valid = len(student_id) == 8 and student_id.isdigit()

if email_valid and id_valid:
    print("Valid Student Record")
else:
    print("Invalid Student Record")