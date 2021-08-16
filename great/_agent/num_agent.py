import random
from collections import namedtuple, deque

import gym
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


Transition = namedtuple('Transition', ('state', 'action', 'next_state', 'reward'))


class ReplayMemory(object):


    def __init__(self, capacity):
        self.memory = deque([], maxlen=capacity)


    def push(self, *args):
        ''' Save transition '''
        self.memory.append(Transition(*args))


    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)


    def __len__(self):
        return len(self.memory)


class Network(nn.Module):
    ''' Network for numbergame '''


    def __init__(self, hidden_layer):
        super(Network, self).__init__()
        self.l1 = nn.Linear(1, hidden_layer)
        self.l2 = nn.Linear(hidden_layer, 1)


    def forward(self, x):
        x = F.relu(self.l1(x))
        x = self.l2(x)
        return x


class gymAgent(object):


    def __init__(self, env):
        self.env = env
        self.model = Network(8)
        self.memory = ReplayMemory(10000)


    def random_act(self, observation):
        return self.env.action_space.sample()


    def greedy_act(self, observation):
        ob_tensor = torch.FloatTensor(observation)
        return self.model(ob_tensor)


    def select_act(self, observation):
        e = random.random()
        self.epsilon = 1
        if e > self.epsilon:
            action = self.random_act(observation)
        else:
            action = self.greedy_act(observation)
        return action


    def run(self, episode_count=10, iteration=200):
        for ep in range(episode_count):
            print('- Episode', ep+1)

            ob, reward, done = self.run_episode(iteration)

            self.env.render()
            print('State  :', ob)
            print('Reward :', reward)
            print('Success:', done)
            print()


    def run_episode(self, iteration):
        ob = self.env.reset()
        cumulative_reward = 0
        done = False

        for step in range(iteration):
            act = self.greedy_act(ob)
            print('act:', act) 
            act = int(act)
            next_ob, reward, done = self.env.step(act)
            cumulative_reward += reward

            self.memory.push(ob, act, next_ob, cumulative_reward)
            print('ob:', ob)
            print('next_ob:', next_ob)
            print('cumulative_reward', cumulative_reward)

            ob = next_ob

            if done:
                break
        return ob, cumulative_reward, done


    def learn():
        batch_size = 64
        if len(self.memory) < batch_size:
            return


if __name__ == '__main__':
    env = gym.make('great:numbergame-v0')
    agent = gymAgent(env)

    agent.run(episode_count=1, iteration=10)
