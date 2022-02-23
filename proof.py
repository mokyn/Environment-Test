from classes.logic import *

class Proof:

    def __init__(self):
        self.env = [{}]
        self.depth = 0
        self.currAssumption = []
        self.steps = []

    def env(self):
        return self.env[self.depth]

    def IntroGroup(self, group):
        default = {"contains":[], "all":[]}
        self.env()[group] = default
        self.steps.append([group])

    def IntroGroupElement(self, elem, group):
        default = {"in":[group]}
        self.env()[elem] = default
        self.env()[group]["contains"].append(elem)
        self.steps.append([elem])
        self.steps.append([group,"contains",elem])
    
    def getProps(self, elem):
        d = self.env()[elem]
        for group in self.env()[elem]["in"]:
            d.update(self.env()[group]["all"])
        return d

    def IntroAssumptionSubproof(self, assumption):
        self.currAssumption.append(assumption)
        self.env.append(self.env().copy())
        self.depth += 1


    def ConcludeSubproof(self):
        self.depth -= 1
        assumed = self.currAssumption.pop()
        conclusion = self.steps[-1]
        spot = self.env()
        for level in conclusion[:-1]:
            spot=conclusion[level]
        spot.append(Implies(assumed,conclusion[-1]))
