import gym
from gym import error, spaces
import numpy as np

class NumberGame(gym.Env):
    metadata = {'render.modes": ["human"]'}
    def __init__(self):
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=-15, high=15, shape=(1,), dtype=np.int64)

        self.reset()


    def reset(self):
        # Initializes self.state and returns initial observation

        self.state = 0
        return self.state


    def step(self, action):
        ''' 
        input: action
        0 : decrement(-1)
        1 : no change(+0)
        2 : increment(+1)
        
        ouput: observation, reward, done
        '''

        self.state += action -1

        # The reward decreases with every step because the goal is to reach the destination quickly
        reward = -1

        done = bool(
            self.state >= 10 or 
            self.state <= -10 
        )

        info={'state': self.state}
        return self.state, reward, done, info


    def render(self, mode='human'):
        '''
        example output:
        --+---------+---O-----+--
        + : goal(10, -10), starting_point(0)
        O : current number
        '''


        print('[', end='')
        for i in range(-12, 13):
            if i == self.state:
                print('O', end='')
            elif abs(i) == 0 or abs(i) == 10:
                print('+', end='')
            else:
                print('-', end='')
        print(']')

