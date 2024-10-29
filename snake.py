import pygame
import random

pygame.init()

# Configuração da tela
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Cores
color_red = (255, 0, 0)
color_light_green = (170, 215, 81)
color_dark_green = (162, 209, 73)
color_snake = (128, 0, 128)
color_text = (255, 255, 255)

# Configurações da cobra
snake_size = 10
speed = 8

# Fonte para exibir a contagem
font = pygame.font.Font(None, 25)

# Função principal do jogo
def game():
    x = width // 2
    y = height // 2
    dx = snake_size
    dy = 0

    # Comprimento inicial da cobra
    snake_body = []
    snake_length = 4

    # Contador de maçãs comidas
    apples_eaten = 0

    # Posicionamento inicial da maçã
    apple_x = random.randint(0, (width - snake_size) // 10) * 10
    apple_y = random.randint(0, (height - snake_size) // 10) * 10

    clock = pygame.time.Clock()
    running = True

    while running:
        # Checando eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Movimentação da cobra
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -snake_size
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = snake_size
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -snake_size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = snake_size

        # Atualizando a posição da cobra
        x += dx
        y += dy

        # Verificando colisão com a borda
        if x < 0 or x >= width or y < 0 or y >= height:
            running = False

        # Comer a maçã
        if x == apple_x and y == apple_y:
            apple_x = random.randint(0, (width - snake_size) // 10) * 10
            apple_y = random.randint(0, (height - snake_size) // 10) * 10
            snake_length += 1
            apples_eaten += 1

        # Atualizando o corpo da cobra
        snake_body.append([x, y])
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Verificando colisão com o próprio corpo
        for part in snake_body[:-1]:
            if part == [x, y]:
                running = False

        # Renderização do chão em xadrez
        for line in range(0, height, snake_size):
            for column in range(0, width, snake_size):
                if (line // snake_size + column // snake_size) % 2 == 0:
                    color_cell = color_light_green
                else:
                    color_cell = color_dark_green
                pygame.draw.rect(screen, color_cell, pygame.Rect(column, line, snake_size, snake_size))

        # Renderização da cobra e maçã
        for part in snake_body:
            pygame.draw.rect(screen, color_snake, pygame.Rect(part[0], part[1], snake_size, snake_size))
        pygame.draw.rect(screen, color_red, pygame.Rect(apple_x, apple_y, snake_size, snake_size))

        # Renderização do contador de maçãs comidas
        score_text = font.render(f"Apples: {apples_eaten}", True, color_text)
        screen.blit(score_text, (10, 10))  # Posição do texto no canto superior esquerdo

        # Atualiza a tela
        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()

game()
