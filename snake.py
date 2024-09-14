import pygame
import time
import random

# Inicializar o pygame
pygame.init()

# Definir as cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (213, 50, 80)
PRETO = (0, 0, 0)
AZUL = (50, 153, 213)

# Definir a largura e altura da tela
LARGURA = 800
ALTURA = 600
TAMANHO_CELULA = 20
FPS = 15

# Inicializar a tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo da Cobrinha')

# Fonte para a pontuação
fonte = pygame.font.SysFont(None, 35)

def exibir_pontuacao(pontuacao):
    texto = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    tela.blit(texto, [0, 0])

def desenhar_cobrinha(tamanho_celula, lista_cobrinha):
    for segmento in lista_cobrinha:
        pygame.draw.rect(tela, VERDE, [segmento[0], segmento[1], tamanho_celula, tamanho_celula])

def mensagem(texto, cor):
    fonte_mensagem = pygame.font.SysFont(None, 50)
    mensagem = fonte_mensagem.render(texto, True, cor)
    tela.blit(mensagem, [LARGURA / 6, ALTURA / 3])

def jogo():
    game_over = False
    game_fim = False

    x1 = LARGURA / 2
    y1 = ALTURA / 2

    x1_alteracao = 0
    y1_alteracao = 0

    lista_cobrinha = []
    comprimento_cobrinha = 1

    comida_x = round(random.randrange(0, LARGURA - TAMANHO_CELULA) / 20.0) * 20.0
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_CELULA) / 20.0) * 20.0

    relogio = pygame.time.Clock()

    while not game_over:

        while game_fim:
            tela.fill(AZUL)
            mensagem("Você perdeu! Pressione Q para sair ou C para jogar novamente", VERMELHO)
            exibir_pontuacao(comprimento_cobrinha - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True
                    game_fim = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_fim = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_alteracao = -TAMANHO_CELULA
                    y1_alteracao = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_alteracao = TAMANHO_CELULA
                    y1_alteracao = 0
                elif evento.key == pygame.K_UP:
                    y1_alteracao = -TAMANHO_CELULA
                    x1_alteracao = 0
                elif evento.key == pygame.K_DOWN:
                    y1_alteracao = TAMANHO_CELULA
                    x1_alteracao = 0

        if x1 >= LARGURA or x1 < 0 or y1 >= ALTURA or y1 < 0:
            game_fim = True
        x1 += x1_alteracao
        y1 += y1_alteracao
        tela.fill(AZUL)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_CELULA, TAMANHO_CELULA])
        cabeca_cobrinha = []
        cabeca_cobrinha.append(x1)
        cabeca_cobrinha.append(y1)
        lista_cobrinha.append(cabeca_cobrinha)
        if len(lista_cobrinha) > comprimento_cobrinha:
            del lista_cobrinha[0]

        for segmento in lista_cobrinha[:-1]:
            if segmento == cabeca_cobrinha:
                game_fim = True

        desenhar_cobrinha(TAMANHO_CELULA, lista_cobrinha)
        exibir_pontuacao(comprimento_cobrinha - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, LARGURA - TAMANHO_CELULA) / 20.0) * 20.0
            comida_y = round(random.randrange(0, ALTURA - TAMANHO_CELULA) / 20.0) * 20.0
            comprimento_cobrinha += 1

        relogio.tick(FPS)

    pygame.quit()
    quit()

if __name__ == "__main__":
    jogo()
