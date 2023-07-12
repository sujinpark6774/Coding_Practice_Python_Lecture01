class Node:
    def __init__(self, value = 0, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class BrowserHistory(object):

    def __init__(self, homepage):
        self.head = self.current = Node(value = homepage)

    def visit(self, url):
        self.current.next = Node(value = url, prev = self.current)
        self.current = self.current.next
        return None

    def back(self, steps):
        while steps > 0 and self.current.prev is not None:
            steps -= 1
            self.current = self.current.prev
        return self.current.value

    def forward(self, steps):
        while steps > 0 and self.current.next is not None:
            steps -= 1
            self.current = self.current.next
        return self.current.value


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")       # You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com")     # You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com")      # You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1)                   # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1)                   # You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1)                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com")     # You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2)                # You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2)                   # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7)                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"