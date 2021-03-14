class AI:
    def __init__(self, snake):
        self.open = list()
        self.closed = list()
        self.path = list()
        self.snake = snake


    def A_star(self, start, target):

        if not self.open:
            self.__count([start], [start, 0], target)
            exp_states = self.__expand(start)
            self.__count(exp_states, [start, 0], target)
            
        while self.open:

            self.open.sort(key = lambda x:x[1]) # Sorts list according to f
            best = self.open.pop(0) # Pops first item from the list
            exp_states = self.__expand(best[0])
            self.__count(exp_states, [best[0], best[2]], target)
            self.closed.append(best)

            for state in self.open:
                if state[0] == target:
                    self.closed.append(state)
                    self.__find_path(state[0], state[3][0])
                        
                    return self.path[::-1]

        print("Path not found")


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
        # snake_body = [[2, 29], [3, 29]] # This was for testing
        correct = list()

        for state in exp_states:
            out_of_map = state[0] < 0 or state[0] > 44 or state[1] < 0 or state[1] > 29 
            if not (state in snake_body or out_of_map):
                correct.append(state)

        return correct


    # (stav i, hodnota f(i), hodnota g(i), předchůdce stavu i)
    # f(i) = g(i) + h(i)        - h(i) = heuristic function
    # g(j) = g(i) + c(i,j)      - c(i, j) = 1
    def __count(self, exp_states, ancestor, target): # exp_states = [[0, 0], [2, 0], [1, 1]], ancestor = [], target = [x, y]
        
        for state in exp_states:
            cnt_state = list()
            g = ancestor[1] + 1
            f = g + self.__heuristic(state, target)

            for item in [state, f, g, ancestor]:
                cnt_state.append(item)

            if not self.open:
                self.open.append(cnt_state)

            for index, open_state in enumerate(self.open, start = 1):
                if cnt_state[0] == open_state[0]:
                    if cnt_state[3] < open_state[3]:
                        open_state = cnt_state
                        break
                    else:
                        break

                else:
                    if index == len(self.open):
                        self.open.append(cnt_state)


    # Manhattan heuristic for 4 directional movement
    def __heuristic(self, start, target):

        x_dist = abs(start[0] - target[0])
        y_dist = abs(start[1] - target[1])

        return x_dist + y_dist


    def __find_path(self, current, ancestor):

        self.path.append(current)
        found = False
        while not found:

            for state in self.closed:
                if state[0] == ancestor and state[2] == 1:
                    self.path.append(state[0])
                    self.closed.remove(state)
                    found = True

                elif state[0] == ancestor:
                    self.path.append(state[0])
                    current = state[0]
                    ancestor = state[3][0]
                    self.closed.remove(state)

        print("Path found!")


# a = AI("ahoj")
# print(a.A_star([0, 29], [7, 25]))



