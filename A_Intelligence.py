

class AI:
    def __init__(self, snake):
        self.open = list()
        self.closed = list()
        self.snake = snake


    def A_star(self, start, target):

        if not self.open:
            self.open.append(start) 

        

        print(self.open)


    # Expannd state - returns list of possible states
    def __expand(self, state):

        exp_states = list()

        for axis in range(len(state)):
            for direction in [-1, 1]:
                if axis == 0:
                    exp_states.append([state[axis] + direction, state[1]])
                else:
                    exp_states.append([state[0], state[axis] + direction])

        return self.__check_expanded(exp_states)


    # Removes map borders and snake occipied nodes from exp_states
    def __check_expanded(self, exp_states):
 
        snake_body = self.snake.get_body()
        correct = list()

        for state in exp_states:
            out_of_map = state[0] < 0 or state[0] > 44 or state[1] < 0 or state[1] > 29 
            if not (state in snake_body or out_of_map):
                correct.append(state)

        return correct


    def heuristic(self, start, target):

        x_dist = abs(start[0] - target[0])
        y_dist = abs(start[1] - target[1])

        return x_dist + y_dist



a = AI("ahoj")

# a.A_star([1, 1], [2, 3])



