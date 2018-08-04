from abc import ABC
from datetime import datetime


class Course:
	def __init__(self, course_code, lecture, tutorials):
	self._course_code = course_code
	self._lecture = lecture
	self._tutorials = tutorials

	@property
	def course_code(self):
		return self._course_code

	@property
	def lecture(self):
		return self._lecture

	@property
	def tutorials(self):
		return self._tutorials

	@lecture.setter
	def lecture(self, lecture):
		self._lecture = lecture

	@tutorials.setter
	def tutorials(self, tutorials):
		self._tutorials = tutorials
	
class Class:
	def __init__(self, start_time, hours, day):

		self.start_time = start_time
		self.hours = hours
		self.day = day

class Lecture(Class):
	def __init__(self, start_time, hours, day):
		super().__init__(self, start_time, hours, day)
	

class Tutorial(Class):
	def __init__(self, start_time, hours, day):
		super().__init__(self, start_time, hourse, day)
