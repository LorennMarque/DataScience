from stable_baselines3 import PPO
from environment import AutoEnv

# Cargar el entorno y el modelo
env = AutoEnv()
model = PPO.load("auto_agent")

# Probar el modelo
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()

    if done:
        obs = env.reset()
