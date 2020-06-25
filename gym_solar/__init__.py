from gym.envs.registration import register

register(
    id='solar-v0',
    entry_point='gym_solar.envs:SolarEnv',
)
register(
    id='solar-extrahard-v0',
    entry_point='gym_solar.envs:SolarExtraHardEnv',
)
