import gym
from gym import spaces
import numpy as np

class AutoEnv(gym.Env):
    def __init__(self):
        super(AutoEnv, self).__init__()
        self.observation_space = spaces.Box(low=np.array([0, 0]), high=np.array([800, 600]), dtype=np.float32)
        self.action_space = spaces.Discrete(4)  # [izquierda, derecha, arriba, abajo]
        self.reset()

    def reset(self):
        self.auto_x = 400
        self.auto_y = 580
        self.done = False
        return np.array([self.auto_x, self.auto_y], dtype=np.float32)

    def step(self, action):
        if action == 0:
            self.auto_x -= 5
        elif action == 1:
            self.auto_x += 5
        elif action == 2:
            self.auto_y -= 5
        elif action == 3:
            self.auto_y += 5

        reward = -1
        if self.auto_y < 0 or self.auto_x < 350 or self.auto_x > 450:
            reward = -50
            self.done = True
        elif self.auto_x > 650 and 250 < self.auto_y < 350:
            reward = 100
            self.done = True

        return np.array([self.auto_x, self.auto_y], dtype=np.float32), reward, self.done, {}

    def render(self, mode="human"):
        print(f"Auto en posición: ({self.auto_x}, {self.auto_y})")
