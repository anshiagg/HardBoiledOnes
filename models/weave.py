def weave_timetable(my_courses, friend_courses):

	time_together = 60;
	for course1 in my_courses:
		for course2 in friend_courses:
			if (course1.lecture.start_time == course2.lecture.start_time):
				if (course1.lecture.hours > course2.lecture.hours):
					time_together -= course1.lecture.hours
				else:
					time_together -= course2.lecture.hours
			elif (course1.lecture.start_day == course2.lecture.start_day):
				if (course1.lecture.start_time < course2.lecture.start_time):
					smaller_time = course1.lecture
					bigger_time = course2.lecture
				else
					smaller_time = course2.lecture
					bigger_time = course1.lecture

				i = 1
				temp = smaller_time.start_time
				while (i < smaller_time.hours) 
					temp += timedelta(hours = 1)
					if (temp == bigger_time.start_time):
						time_together -= smaller_time.hours - i
						bigger_end_time = bigger_time.start_time + (timedelta(hours = bigger_time.hours))
						smaller_end_time = smaller_time.start_time + (timedelta(hours = smaller_time.hours))
						if (bigger_end_time > smaller_time):
							time_together -= bigger_end_time - smaller_end_time
						break

				else:
					time_together -= course1.lecture.hours
					time_together -= course2.lecture.hours


