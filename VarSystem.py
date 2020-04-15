class VarSystem:
    def __init__(self):
        self.vars = {}

    def set_var(self, name, res):
        name = name.replace(' ', '')
        res = res.replace(' ', '')
        try:
            res = int(res)
        except:
            try:
                res = int(self.vars.get(res))
            except:
                pass
        self.vars.update({name: res})
    def print_var(self):
        return self.vars.keys()

    def get_var(self, name):
        try:
            return self.vars.get(name)
        except:
            pass