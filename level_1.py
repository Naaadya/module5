class StringVar:
    def __init__(self,s):
        self.s = s
    def get_s(self):
        return self.s
    def set_s(self,a):
        self.s = a
p = StringVar('gont')
print(p.get_s())
p.set_s('v')
print(p.get_s())
