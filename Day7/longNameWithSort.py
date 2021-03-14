student_list = ["Komali", "Navin & Navya","Udeepth",  "Akshar","Adityamithran"]
# Index starts from 0

print("---- Before sorting--")

for student_name in student_list :
      print(student_name)

#Sort in descending
sorted_student_list = sorted(student_list, key=len, reverse=True)

for student_name in sorted_student_list :
  if len(student_name) !=len(sorted_student_list[0]) : # Break if student name length is difrent break loop
        break
  print(student_name)

