class Or:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

class And:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

class Implies:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

class Not:
    def __init__(self, arg1):
        self.arg1 = arg1