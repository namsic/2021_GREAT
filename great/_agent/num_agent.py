import gym

import random


class DQNAgent(object):


    def __init__(self, action_space):
        self.action_space = action_space
        self.epsilon = 0.05


    def random_act(self, observation):
        return self.action_space.sample()


    def greedy_act(self, observation):
        pass


    def act(self, observation, epsilon):
        e = random.random()
        if e > self.epsilon:
            action = self.random_act(observation)
        else:
            action = self.greedy_act(observation)
        return action


if __name__ == '__main__':
    env = gym.make('great:numbergame-v0')
    agent = DQNAgent(env.action_space)

    episode_count = 10
    iteration = 200

    for ep in range(episode_count):
        print('- Episode', ep+1)

        ob = env.reset()
        cumulative_reward = 0
        done = False
        for i in range(iteration):
            action = agent.random_act(ob)
            ob, reward, done = env.step(action)
            cumulative_reward += reward
            if done:
                break

        env.render()
        print('Success:', done)
        print('State  :', ob)
        print('Reward :', cumulative_reward)
        print()
