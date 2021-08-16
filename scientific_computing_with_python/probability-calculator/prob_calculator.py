import copy
import random
# Consider using the modules imported above.

class Hat:
    contents = []

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(f'{key}')

    def draw(self, amount):
        if amount > len(self.contents):
            contents_copy = copy.copy(self.contents)
            self.contents.clear()
            return contents_copy

        drawn = []
        for i in range(amount):
            num = random.randint(0, len(self.contents) - 1)
            drawn.append(self.contents.pop(num))  
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        expected_balls_copy = copy.deepcopy(expected_balls)

        drawn = hat_copy.draw(num_balls_drawn)
        for j in drawn:
            if j in expected_balls_copy:
                expected_balls_copy[j] += -1

        if all(v <= 0 for v in expected_balls_copy.values()):
            success_count += 1

    probability = success_count / num_experiments

    return probability
