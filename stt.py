class State:
    def __init__(self, state, ancestor, target):
        self.state = state
        self.__f = None
        self.__g = None
        self.ancestor = ancestor
        self.target = target
        self.__count()

    def __repr__ (self):

        repr_str = "{}, {}, {}, {}".format(self.state, self.__f, self.__g, self.ancestor.state if self.ancestor != None else None)
        return repr_str


    def __count(self):

        if self.ancestor == None:
            self.__g = 0
        else:
            self.__g = self.ancestor.get_d() + 1

        self.__f = self.__g + self.__heuristic(self.state, self.target)


    def __heuristic(self, start, target):

        x_dist = abs(start[0] - target[0])
        y_dist = abs(start[1] - target[1])

        return x_dist + y_dist


    def get_d(self):

        return self.__g


    def get_f(self):

        return self.__f