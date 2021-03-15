class State:
    def __init__(self, state, ancestor, target):
        self.state = state
        self.f = None
        self.g = None
        self.ancestor = ancestor
        self.target = target
        self.count()

    def __repr__ (self):

        repr_str = "{}, {}, {}, {}".format(self.state, self.f, self.g, self.ancestor.state if self.ancestor != None else None)
        return repr_str


    def count(self):

        if self.ancestor == None:
            self.g = 0
        else:
            self.g = self.ancestor.get_d() + 1

        self.f = self.g + self.__heuristic(self.state, self.target)


    def __heuristic(self, start, target):

        x_dist = abs(start[0] - target[0])
        y_dist = abs(start[1] - target[1])

        return x_dist + y_dist


    def get_d(self):

        return self.g





#################

# numbers = {'second': 2, 'first': 1, 'third': 3, 'Fourth': 4}
# print(list(numbers))


# a = State([0, 1], None, [2, 2])
# b = State([0, 0], a, [2, 2])
# c = State([0, 2], a, [2, 2])
# d = State([1, 1], a, [2, 2])

# openn = {"[0, 1]": a, "[0, 0]": b, "[0, 2]": c, "[1, 1]": d}
# print(openn.values())
# print()

# def getKey(state):
#     return state.f

# adresses = sorted(openn.values(), key=getKey)
# print(adresses)
# print(adresses[1].state)

