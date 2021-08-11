from gym.envs.registration import register

register(
    id='numbergame-v0',
    entry_point='great._env:NumberGame',
)
