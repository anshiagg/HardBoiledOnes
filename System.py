from Post import Post
from Requests import Request

class System:
    def __init__(self):
        self._post   = []
        self._request    = []

    def addPost(self, post):
        self._post.append(post)

    def addRequest(self, request):
        self._post.append(request)

    def removePost(self, post):
        self._post.remove(post)

    def removeRequest(self, request):
        self._request.remove(request)

    @property
    def post_list(self):
        return self._post
    @property
    def request_list(self):
            return self._request