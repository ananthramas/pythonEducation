
student_list = ["Komali", "Navin & Navya","Udeepth",  "Akshar","Adityamithran"]

# Index starts from 0

long_name = student_list[0]

for student_name in student_list :
  if len(student_name) > len(long_name) :
    long_name = student_name

print(long_name)
  
