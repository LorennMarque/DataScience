from stable_baselines3 import PPO
from environment import AutoEnv
from stable_baselines3.common.env_checker import check_env

# Cargar el entorno
env = AutoEnv()
check_env(env)  # Verifica que el entorno es válido

# Crear y entrenar el modelo
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

# Guardar el modelo
model.save("auto_agent")
print("Modelo entrenado y guardado como 'auto_agent'.")
