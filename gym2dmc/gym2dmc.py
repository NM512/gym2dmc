from dm_env import specs, Environment, TimeStep, StepType


class Gym2DMC(Environment):
    """Convert a Gym environment to a DMC environment"""

    def __init__(self, gym_env) -> None:
        """Initializes a new Gym2DMC wrapper

        Args:
            gym_env (GymEnv): The Gym environment to convert.
        """
        gym_obs_space = gym_env.observation_space
        self._observation_spec = specs.BoundedArray(
            shape=gym_obs_space.shape,
            dtype=gym_obs_space.dtype,
            minimum=gym_obs_space.low,
            maximum=gym_obs_space.high,
            name='observation'
            )
        gym_act_space = gym_env.action_space
        self._action_spec = specs.BoundedArray(
            shape=gym_act_space.shape,
            dtype=gym_act_space.dtype,
            minimum=gym_act_space.low,
            maximum=gym_act_space.high,
            name='action'
            )
        self._gym_env = gym_env

    def step(self, action):
        obs, reward, done, *_ = self._gym_env.step(action)

        if done:
            step_type = StepType.LAST
            discount = 0.0
        else:
            step_type = StepType.MID
            discount = 1.0

        return TimeStep(step_type=step_type,
                        reward=reward,
                        discount=discount,
                        observation=obs)

    def reset(self):
        # to fix
        obs = self._gym_env.reset()[0]
        return TimeStep(step_type=StepType.FIRST,
                        reward=None,
                        discount=None,
                        observation=obs)

    def render(self):
        return self._gym_env.render()

    def observation_spec(self):
        return self._observation_spec

    def action_spec(self):
        return self._action_spec