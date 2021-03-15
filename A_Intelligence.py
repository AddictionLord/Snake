from stt import *

class AI:
    def __init__(self, snake):
        self.open = dict()
        self.closed = list()
        self.path = list()
        self.snake = snake


    def A_star(self, start, target):

        if not self.open:
            self.__count([start], None, target)
            exp_states = self.__expand(start)
            self.__count(exp_states, self.open[str(start)], target)

        # while self.open:

        for i in self.open:
            print(i, "\t", self.open[i])

        print()

        adresses = sorted(self.open.values(), key=self.getKey)
        for i in adresses:
            print(i)
        # print(adresses)

        #     self.open.sort(key = lambda x:x[1]) # Sorts list according to f
        #     best = self.open.pop(0) # Pops first item from the list
        #     exp_states = self.__expand(best[0])
        #     self.__count(exp_states, [best[0], best[2]], target)
        #     self.closed.append(best)

        #     for state in self.open:
        #         if state[0] == target:
        #             self.closed.append(state)
        #             self.__find_path(state[0], state[3][0])
                        
        #             return self.path[::-1]

        # print("Path not found")

    def getKey(self, state):
        return state.f

    # (stav i, hodnota f(i), hodnota g(i), předchůdce stavu i)
    # f(i) = g(i) + h(i)        - h(i) = heuristic function
    # g(j) = g(i) + c(i,j)      - c(i, j) = 1
    def __count(self, exp_states, ancestor, target): # exp_states = [[0, 0], [2, 0], [1, 1]], ancestor = adress to ancestor, target = [x, y]
        
        for state in exp_states:
            temp = State(state, ancestor, target)

            if not self.open:
                self.open[str(state)] = temp

            else:
                if str(state) in self.open.keys():
                    compared_state = self.open[str(state)]
                    if temp.get_d() < compared_state.get_d():
                        self.open[str(state)] = temp

                    break

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
 
        # snake_body = self.snake.get_body()
        snake_body = [[2, 29], [3, 29]] # This was for testing
        correct = list()

        for state in exp_states:
            out_of_map = state[0] < 0 or state[0] > 44 or state[1] < 0 or state[1] > 29 
            if not (state in snake_body or out_of_map):
                correct.append(state)

        return correct





    # Manhattan heuristic for 4 directional movement
    # def __heuristic(self, start, target):

    #     x_dist = abs(start[0] - target[0])
    #     y_dist = abs(start[1] - target[1])

    #     return x_dist + y_dist


    def __find_path(self, current, ancestor):

        self.path.append(current)
        found = False
        for i in self.closed:
            print(i)
            
        while not found:

            for state in self.closed:
                if state[0] == ancestor and state[2] == 1:
                    print(1)
                    self.path.append(state[0])
                    self.closed.remove(state)
                    found = True

                elif state[0] == ancestor:
                    print(2)
                    self.path.append(state[0])
                    current = state[0]
                    ancestor = state[3][0]
                    self.closed.remove(state)

        print("Path found!")


a = AI("ahoj")
print(a.A_star([0, 1], [7, 25]))



