class applicatonEx(Exception):
    def __init__(self, value):
        self.value = value
        print(self.value)