import pygame
import sys

# Inicializamos pygame
pygame.init()

# Dimensiones de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Configuración de colores
SKY_BLUE = (135, 206, 235)  # Fondo (cielo)
ROAD_GRAY = (50, 50, 50)    # Camino
RED = (255, 0, 0)           # Auto (círculo)
GREEN = (0, 255, 0)         # Inicio
BLUE = (0, 0, 255)          # Fin

# Configuramos la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Auto con Reinforcement Learning")

# Posición del inicio y fin
start_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, 0, 100, 12)  # Inicio
end_rect = pygame.Rect(SCREEN_WIDTH // 2 + 250, SCREEN_HEIGHT // 2 - 50, 12, 100)  # Fin

# Dimensiones del camino
vertical_road_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, 0, 100, SCREEN_HEIGHT // 2)
horizontal_road_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50, 300, 100)

# Posición inicial del "auto" (círculo) - centrado en el inicio
circle_x = start_rect.centerx
circle_y = start_rect.bottom + 10  # Justo debajo del inicio para mayor claridad
circle_radius = 20

# Velocidad del auto
speed = 5

# Función para reiniciar la posición del auto
def reset_to_start():
    global circle_x, circle_y
    circle_x = start_rect.centerx
    circle_y = start_rect.bottom + 10

# Bucle principal
clock = pygame.time.Clock()

while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detectamos las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Mover hacia arriba
        circle_y -= speed
    if keys[pygame.K_s]:  # Mover hacia abajo
        circle_y += speed
    if keys[pygame.K_a]:  # Mover hacia la izquierda
        circle_x -= speed
    if keys[pygame.K_d]:  # Mover hacia la derecha
        circle_x += speed

    # Dibujamos el fondo
    screen.fill(SKY_BLUE)  # Fondo azul cielo

    # Dibujamos el camino en forma de L
    pygame.draw.rect(screen, ROAD_GRAY, vertical_road_rect)  # Parte vertical del camino
    pygame.draw.rect(screen, ROAD_GRAY, horizontal_road_rect)  # Parte horizontal del camino

    # Dibujamos el inicio y el fin del circuito
    pygame.draw.rect(screen, GREEN, start_rect)  # Inicio
    pygame.draw.rect(screen, BLUE, end_rect)    # Fin

    # Dibujamos el auto (círculo)
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

    # Verificamos si el auto toca los bordes
    car_rect = pygame.Rect(circle_x - circle_radius, circle_y - circle_radius, circle_radius * 2, circle_radius * 2)

    # Si el auto sale del camino
    if not (vertical_road_rect.colliderect(car_rect) or horizontal_road_rect.colliderect(car_rect)):
        print("¡Choque! Reiniciando...")
        reset_to_start()

    # Verificamos si el auto llega al final
    if car_rect.colliderect(end_rect):
        print("¡Llegaste al final!")
        reset_to_start()

    # Actualizamos la pantalla
    pygame.display.flip()
    clock.tick(60)  # Limitamos a 60 FPS
