import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Dimensiones del entorno
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Parámetros del auto (agente)
circle_x = SCREEN_WIDTH // 2
circle_y = 10
circle_radius = 20

# Parámetros de Q-Learning
actions = [0, 1, 2, 3]  # [Izquierda, Derecha, Arriba, Abajo]
q_table = np.zeros((SCREEN_WIDTH // 10, SCREEN_HEIGHT // 10, len(actions)))
learning_rate = 0.1
discount_factor = 0.9
epsilon = 1.0
epsilon_decay = 0.995
min_epsilon = 0.01

# Puntajes
total_score = 0
score_history = []

# Dimensiones del camino
vertical_road_x = SCREEN_WIDTH // 2 - 50
vertical_road_width = 100
horizontal_road_y = SCREEN_HEIGHT // 2 - 50
horizontal_road_width = 300

# Posición del inicio y fin
start_x = SCREEN_WIDTH // 2 - 50
start_y = 0
end_x = SCREEN_WIDTH // 2 + 250
end_y = SCREEN_HEIGHT // 2 - 50

# Obtener el estado actual
def get_state():
    return circle_x // 10, circle_y // 10

# Reiniciar la posición del auto
def reset_to_start():
    global circle_x, circle_y
    circle_x = SCREEN_WIDTH // 2
    circle_y = 10
    return get_state()

# Realizar una acción
def take_action(action):
    global circle_x, circle_y
    if action == 0:  # Izquierda
        circle_x = max(circle_x - 10, 0)
    elif action == 1:  # Derecha
        circle_x = min(circle_x + 10, SCREEN_WIDTH)
    elif action == 2:  # Arriba
        circle_y = max(circle_y - 10, 0)
    elif action == 3:  # Abajo
        circle_y = min(circle_y + 10, SCREEN_HEIGHT)

# Calcular la recompensa
def calculate_reward():
    if circle_x < vertical_road_x or circle_x > vertical_road_x + vertical_road_width:
        return -50, True  # Penalización por salir del camino
    if circle_y < horizontal_road_y or circle_y > horizontal_road_y + vertical_road_width:
        return -50, True  # Penalización por salir del camino
    if end_x < circle_x < end_x + 10 and end_y < circle_y < end_y + 100:
        return 100, True  # Recompensa por llegar al final
    return -1, False  # Penalización mínima por moverse

# Configurar la figura de Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, SCREEN_WIDTH)
ax.set_ylim(0, SCREEN_HEIGHT)
ax.invert_yaxis()  # Invertir el eje Y para que (0,0) esté en la esquina superior izquierda

# Dibujar el camino
ax.fill_betweenx([0, SCREEN_HEIGHT], vertical_road_x, vertical_road_x + vertical_road_width, color="gray")
ax.fill_between([vertical_road_x, vertical_road_x + horizontal_road_width], horizontal_road_y,
                horizontal_road_y + vertical_road_width, color="gray")

# Dibujar inicio y fin
start_rect = plt.Rectangle((start_x, start_y), 100, 10, color="green")
end_rect = plt.Rectangle((end_x, end_y), 10, 100, color="blue")
ax.add_patch(start_rect)
ax.add_patch(end_rect)

# Dibujar el auto
car_circle = plt.Circle((circle_x, circle_y), circle_radius, color="green")
ax.add_patch(car_circle)

# Actualización de la animación
state = reset_to_start()

def update(frame):
    global state, total_score, epsilon, circle_x, circle_y

    # Elegir acción (exploración vs explotación)
    if random.uniform(0, 1) < epsilon:
        action = random.choice(actions)  # Explorar
    else:
        action = np.argmax(q_table[state[0], state[1]])  # Explotar

    # Realizar la acción
    take_action(action)
    new_state = get_state()
    reward, done = calculate_reward()

    # Actualizar la Q-Table
    best_future_q = np.max(q_table[new_state[0], new_state[1]])
    q_table[state[0], state[1], action] += learning_rate * (reward + discount_factor * best_future_q -
                                                            q_table[state[0], state[1], action])

    # Actualizar estado y puntajes
    state = new_state
    total_score += reward
    if done:
        reset_to_start()

    # Actualizar el auto en la figura
    car_circle.center = (circle_x, circle_y)
    return car_circle,

# Crear la animación
ani = FuncAnimation(fig, update, frames=1000, interval=50, blit=True)

plt.show()
