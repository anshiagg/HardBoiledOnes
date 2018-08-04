import csv
from models.course import *

'''
class_code = 0
activity = 1
status = 2
day = 3 
start_time = 4 
hour = 5 
course = 6
'''

course_dictionary = {}

def build_class(is_lecture, start_time, hours, day):
    if is_lecture:
        return Lecture(start_time, hours, day)

    else:
        return Tutorial(start_time, hours, day)


with open("MockData.txt", 'r') as file:
    spamreader = csv.reader(file, delimiter='|')
    title=True
    for row in spamreader:
        if title:
            title = False
            continue

        course_code = row[6]
        activity = row[1]

        new_class = build_class(activity == "Lecture", row[4], row[5], row[3])

        if course_code not in course_dictionary:
            course_dictionary[course_code] = Course(course_code, None, [])

        
        if activity == "Lecture":
            course_dictionary[course_code].Lecture = new_class

        else:
            course_dictionary[course_code].tutorials.append(new_class)

print (course_dictionary)