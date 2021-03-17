from stt import State

class AI:
    def __init__(self, snake):
        self.open = dict()
        self.closed = dict()
        self.path = list()
        self.snake = snake


    def A_star(self, start, target):

        if not self.open:
            self.__count([start], None, target)

        while self.open:

            best = self.__sort_and_pick()
            key = str(best.state)
            self.open.pop(key)
            self.closed[key] = best
            exp_states = self.__expand(best.state)
            self.__count(exp_states, best, target)

            for key in self.open:
                value = self.open[key]
                if value.state == target:
                    self.open.pop(key)
                    self.closed[key] = value
                    self.__find_path(value)

                    return self.path[::-1]

        print("Path not found")
        

    def __sort_and_pick(self):

        adresses = sorted(self.open.values(), key=self.getKey)
        return adresses[0]


    def getKey(self, state):

        # return state.f
        return state.get_f()


    # (state i, value f(i), value g(i), ancestor i)
    # f(i) = g(i) + h(i)        - h(i) = heuristic function
    # g(j) = g(i) + c(i,j)      - c(i, j) = 1
    def __count(self, exp_states, ancestor, target): # exp_states = [[0, 0], [2, 0], [1, 1]], ancestor = adress to ancestor, target = [x, y]
        
        for state in exp_states:
            temp = State(state, ancestor, target)

            if str(state) in self.closed.keys():
                continue

            if str(state) in self.open.keys():
                compared_state = self.open[str(state)]
                if temp.get_d() < compared_state.get_d():
                    self.open[str(state)] = temp
                continue

            else:
                self.open[str(state)] = temp


    # Expannd state - returns list of possible states
    def __expand(self, state): # state = [x, y]

        exp_states = list()

        for axis in range(len(state)):
            for direction in [-1, 1]:
                if axis == 0:
                    exp_states.append([state[axis] + direction, state[1]])
                else:
                    exp_states.append([state[0], state[axis] + direction])

        return self.__check_expanded(exp_states)
        

    # Removes map borders and snake occipied nodes from exp_states
    def __check_expanded(self, exp_states): # exp_states = [[x, y], [x, y], [x, y], [x, y]]
 
        snake_body = self.snake.get_body()
        # snake_body = [[0, 1], [1, 0]] # This was for testing
        correct = list()

        for state in exp_states:
            out_of_map = state[0] < 0 or state[0] > 44 or state[1] < 0 or state[1] > 29 
            if not (state in snake_body or out_of_map):
                correct.append(state)

        return correct


    def __find_path(self, current):

        anc = current.ancestor
        if anc == None:
            print("Path found!")
            return

        self.path.append(current.state)
        self.__find_path(anc)


