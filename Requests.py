class Request:
    def __init__(self,user,course):
        self._course_holder = user
        self._course = course

    @property
    def getCourse(self):
        return self._course
    def Course_info(self):
        return self._course.__repr__()
