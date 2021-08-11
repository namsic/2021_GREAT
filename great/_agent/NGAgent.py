import gym

class RandomAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space


    def act(self, observation, reward, done):
        return self.action_space.sample()

if __name__ == '__main__':
    env = gym.make('number-game_v0')
    agent = RandomAgent(env.action_space)

    repeat = 100
    reward = 0
    done = False

    for i in range(repeat):
        action = agent.act(ob, reward, done)
        ob = env.reset()
        ob, reward, done = env.step(action)
        if done:
            break
