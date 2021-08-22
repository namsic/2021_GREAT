import numpy as np
import gym

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy


class gymAgent(object):


    def __init__(self, env):
        self.env = env


    def init_dqn(self):
        oss = self.env.observation_space.shape
        asn = self.env.action_space.n
        model = Sequential()
        model.add(Flatten(input_shape=(1,) + oss))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(asn, activation='linear'))
        model.summary()

        self.dqn = DQNAgent(
            model = model, 
            nb_actions = self.env.action_space.n, 
            memory = SequentialMemory(limit=10000, window_length=1), 
            policy = EpsGreedyQPolicy()
        )
        self.dqn.compile(Adam(lr=1e-1), metrics=['mae'])


    def random_act(self, observation):
        return self.env.action_space.sample()


    def run(self, mode=0):
        if mode == 1:
            self.init_dqn()
            self.dqn.fit(env, nb_steps=1000, visualize=False)
            self.dqn.test(self.env, nb_episodes=episode_count, visualize=True)
            return

        ob = self.env.reset()
        cumulative_reward = 0

        for step in range(30):
            act = self.random_act(ob)
            ob, reward, done, _ = self.env.step(act)
            cumulative_reward += reward
            self.env.render()

            if done:
                break
        print('reward:', cumulative_reward)


if __name__ == '__main__':
    env = gym.make('great:numbergame-v0')
    agent = gymAgent(env)

    print('0: random_action')
    print('1: dqn')
    mode = int(input('>>> '))
    agent.run(mode)
