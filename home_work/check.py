class Checks:
    def __init__(self):
        self.loc = None

    def check_text(self, loc: str = ''):
        self.loc = loc
        print('check_text:', self.loc)
