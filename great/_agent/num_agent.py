import gym

class RandomAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space


    def act(self, observation, reward, done):
        return self.action_space.sample()


if __name__ == '__main__':
    env = gym.make('great:numbergame-v0')
    agent = RandomAgent(env.action_space)

    repeat = 100
    reward = 0
    done = False

    ob = env.reset()
    env.render()
    for i in range(repeat):
        print(i+1)
        action = agent.act(ob, reward, done)
        ob, reward, done = env.step(action)
        env.render()
        if done:
            break
    print('done :', done)
    print(ob)
