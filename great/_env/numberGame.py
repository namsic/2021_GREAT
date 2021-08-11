import gym
from gym import error, spaces

class NumberGame(gym.Env):
    metadata = {'render.modes": ["human"]}
    def __init__(self):
        self.action_space = spaces.Discrete(2)

        self.reset()


    def reset(self):
        # Initializes self.state and returns initial observation

        self.state = {
            'current': 0
        }
        self.state['distance'] = self.get_distance()
        return self.state


    def step(self, action):
        remaining_distance = min(self.state['distance'])

        amount = 1 if action else -1
        self.state['current'] += amount
        self.state['distance'] = self.get_distance()

        done = bool(
            self.state['current'] >= 10 or 
            self.state['current'] <= -10 
        )

        if min(self.state['distance']) < remaining_distance:
            reward = 1.0
        elif min(self.state['distance']) > remaining_distance:
            reward = -1.0
        else:
            reward = 0

        return self.state, reward, done  #, info


    def render(self):
        for i in range(-12, 13):
            if i == self.state['current']:
                print('O', end='')
            elif abs(i) == 10:
                print('X', end='')
            else:
                print('+', end='')


    def get_distance(self):
        distance = (
            abs(-10 - self.state['current']), 
            abs(10 - self.state['current'])
        )
        return distance
