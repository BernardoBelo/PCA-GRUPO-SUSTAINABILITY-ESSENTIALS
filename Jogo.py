import pygame
from pygame.locals import *
from sys import exit
from random import *
from os import *

pygame.init()
pygame.mixer.init()

largura = 640
altura = 480

pontos = 0

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sustainability Essentials')
fonte = pygame.font.SysFont('arial', 35, True, False)

imagem_fundo = pygame.image.load('fundo.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

relogio = pygame.time.Clock()

som_fundo = pygame.mixer.Sound('sons/musica_fundo.wav')
som_fundo.set_volume(0.1)
som_coletavel = pygame.mixer.Sound('sons/coleta.wav')
som_coletavel.set_volume(1)
som_inimigo = pygame.mixer.Sound('sons/perda.wav')
som_inimigo.set_volume(0.4)

def exibe_mensagem(msg, tamanho, cor):
    escrita = pygame.font.SysFont('arial', tamanho, True, False)
    recado = f'{msg}'
    mensagem_formatada = escrita.render(recado, True, cor)
    som_inimigo.play()
    return mensagem_formatada
    
def reiniciar_jogo():
    global pontos, colisao_inimigo
    pontos = 0
    colisao_inimigo = False
    inimigo1.rect.x = largura - randrange(30, 600, 30)
    inimigo1.rect.y = randrange(0, 480, 20)
    inimigo2.rect.x = largura - randrange(30, 600, 30)
    inimigo2.rect.y = randrange(0, 480, 20)
    inimigo3.rect.x = largura - randrange(30, 600, 30)
    inimigo3.rect.y = randrange(0, 480, 20)
    inimigo4.rect.x = largura - randrange(30, 600, 30)
    inimigo4.rect.y = randrange(0, 480, 20)

coletavel1_pos_x = randint(20, 580)
coletavel1_pos_y = randint(0, 435)

coletavel2_pos_x = randint(20, 580)
coletavel2_pos_y = randint(0, 435)

coletavel3_pos_x = randint(20, 580)
coletavel3_pos_y = randint(0, 435)

coletavel4_pos_x = randint(20, 580)
coletavel4_pos_y = randint(0, 435)

coletavel5_pos_x = randint(20, 580)
coletavel5_pos_y = randint(0, 435)

coletavel6_pos_x = randint(20, 580)
coletavel6_pos_y = randint(0, 435)

coletavel7_pos_x = randint(20, 580)
coletavel7_pos_y = randint(0, 435)

coletavel8_pos_x = randint(20, 580)
coletavel8_pos_y = randint(0, 435)

coletavel9_pos_x = randint(20, 580)
coletavel9_pos_y = randint(0, 435)

coletavel10_pos_x = randint(20, 580)
coletavel10_pos_y = randint(0, 435)

coletavel11_pos_x = randint(20, 580)
coletavel11_pos_y = randint(0, 435)

coletavel12_pos_x = randint(20, 580)
coletavel12_pos_y = randint(0, 435)

coletavel13_pos_x = randint(20, 580)
coletavel13_pos_y = randint(0, 435)

coletavel14_pos_x = randint(20, 580)
coletavel14_pos_y = randint(0, 435)

coletavel15_pos_x = randint(20, 580)
coletavel15_pos_y = randint(0, 435)

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('personagem/sprite_0.png'))
        self.sprites.append(pygame.image.load('personagem/sprite_1.png'))
        self.sprites.append(pygame.image.load('personagem/sprite_2.png'))
        self.sprites.append(pygame.image.load('personagem/sprite_3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (512 / 4, 512 / 4))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = 256, 360
        self.up = False
        self.left = False
        self.right = False
        self.down = False
        self.jump = False
    def cima(self):
        self.up = True
    def esquerda(self):
        self.left = True
    def direita(self):
        self.right = True
    def baixo(self):
        self.down = True
    def pula(self):
        self.jump = True
    def update(self):
        if self.up == True:
            if self.rect.y <= 480:
                self.up = False
            self.rect.y -= 13
        if self.left == True:
            if self.rect.x <= 640:
                self.left = False
            self.rect.x -= 13
        if self.right == True:
            if self.rect.x >= -640:
                self.right = False
            self.rect.x += 13
        if self.down == True:
            if self.rect.y >= -480:
                self.down = False
            self.rect.y += 13
        if self.jump == True:
            if self.rect.y <= 368 & self.rect.y >= 367:
                self.jump = False
            self.rect.y -= 35
        if self.rect.y >= 369:
            self.rect.y = 369
        if self.rect.y <= -19:
            self.rect.y = -19
        if self.rect.x >= 539:
            self.rect.x = 539
        if self.rect.x <= -29:
            self.rect.x = -29
        self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (512 / 4, 512 / 4))

grupo_personagem = pygame.sprite.Group()
personagem = Personagem()
grupo_personagem.add(personagem)

class Inimigo1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('inimigos/Cortar_Arvore/sprite_0.png'))
        self.sprites.append(pygame.image.load('inimigos/Cortar_Arvore/sprite_1.png'))  
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = largura - randrange(30, 600, 30)
        self.rect.y = randrange(0, 480, 20)
    def update(self):
        self.atual = self.atual + 0.2
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (64, 64))
        if self.rect.topright[0] < 0:
            self.rect.x = largura
            self.rect.y = randrange(0, 480, 20)
        self.rect.x -= 5

grupo_inimigo = pygame.sprite.Group()
inimigo1 = Inimigo1()
grupo_inimigo.add(inimigo1)

class Inimigo2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('inimigos/Lata_Lixo/sprite_0.png'))
        self.sprites.append(pygame.image.load('inimigos/Lata_Lixo/sprite_1.png'))  
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = largura - randrange(30, 600, 30)
        self.rect.y = randrange(0, 480, 20)
    def update(self):
        self.atual = self.atual + 0.2
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (64, 64))
        if self.rect.topright[0] < 0:
            self.rect.x = largura
            self.rect.y = randrange(0, 480, 20)
        self.rect.x -= 5 

inimigo2 = Inimigo2()
grupo_inimigo.add(inimigo2)

class Inimigo3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('inimigos/Latao_Fogo/sprite_0.png'))
        self.sprites.append(pygame.image.load('inimigos/Latao_Fogo/sprite_1.png'))  
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (150, 70))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = largura - randrange(30, 600, 30)
        self.rect.y = randrange(0, 480, 20)
    def update(self):
        self.atual = self.atual + 0.2
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (150, 70))
        if self.rect.topright[0] < 0:
            self.rect.x = largura
            self.rect.y = randrange(0, 480, 20)
        self.rect.x -= 5 

inimigo3 = Inimigo3()
grupo_inimigo.add(inimigo3)

class Inimigo4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('inimigos/Nuclear/sprite_0.png'))
        self.sprites.append(pygame.image.load('inimigos/Nuclear/sprite_1.png'))  
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = largura - randrange(30, 600, 30)
        self.rect.y = randrange(0, 480, 20)
    def update(self):
        self.atual = self.atual + 0.2
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (64, 64))
        if self.rect.topright[0] < 0:
            self.rect.x = largura
            self.rect.y = randrange(0, 480, 20)
        self.rect.x -= 5 

inimigo4 = Inimigo4()
grupo_inimigo.add(inimigo4)

class Coletavel1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/CaixaGrande/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/CaixaGrande/sprite_1.png'))
        self.sprites.append(pygame.image.load('coletaveis/CaixaGrande/sprite_2.png'))
        self.sprites.append(pygame.image.load('coletaveis/CaixaGrande/sprite_3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (54, 57))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel1_pos_x, coletavel1_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (54, 57))
        self.rect.topleft = coletavel1_pos_x, coletavel1_pos_y

grupo_coletavel1 = pygame.sprite.Group()
coletavel1 = Coletavel1()
grupo_coletavel1.add(coletavel1)

class Coletavel2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/CaixaPizza/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/CaixaPizza/sprite_1.png'))
        self.sprites.append(pygame.image.load('coletaveis/CaixaPizza/sprite_2.png'))
        self.sprites.append(pygame.image.load('coletaveis/CaixaPizza/sprite_3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (62, 53))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel2_pos_x, coletavel2_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (62, 53))
        self.rect.topleft = coletavel2_pos_x, coletavel2_pos_y

grupo_coletavel2 = pygame.sprite.Group()
coletavel2 = Coletavel2()
grupo_coletavel2.add(coletavel2)

class Coletavel3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/CopoIsopor/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/CopoIsopor/sprite_1.png'))
        self.sprites.append(pygame.image.load('coletaveis/CopoIsopor/sprite_2.png'))
        self.sprites.append(pygame.image.load('coletaveis/CopoIsopor/sprite_3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (30, 57))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel3_pos_x, coletavel3_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (30, 57))
        self.rect.topleft = coletavel3_pos_x, coletavel3_pos_y

grupo_coletavel3 = pygame.sprite.Group()
coletavel3 = Coletavel3()
grupo_coletavel3.add(coletavel3)

class Coletavel4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/GarrafaPet/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/GarrafaPet/sprite_1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (18, 51))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel4_pos_x, coletavel4_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (18, 51))
        self.rect.topleft = coletavel4_pos_x, coletavel4_pos_y

grupo_coletavel4 = pygame.sprite.Group()
coletavel4 = Coletavel4()
grupo_coletavel4.add(coletavel4)

class Coletavel5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/GarrafaVidro1/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/GarrafaVidro1/sprite_1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (19, 58))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel5_pos_x, coletavel5_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (19, 58))
        self.rect.topleft = coletavel5_pos_x, coletavel5_pos_y

grupo_coletavel5 = pygame.sprite.Group()
coletavel5 = Coletavel5()
grupo_coletavel5.add(coletavel5)

class Coletavel6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/GarrafaVidro2/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/GarrafaVidro2/sprite_1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (18, 60))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel6_pos_x, coletavel6_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (18, 60))
        self.rect.topleft = coletavel6_pos_x, coletavel6_pos_y

grupo_coletavel6 = pygame.sprite.Group()
coletavel6 = Coletavel6()
grupo_coletavel6.add(coletavel6)

class Coletavel7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/Jornal/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/Jornal/sprite_1.png'))
        self.sprites.append(pygame.image.load('coletaveis/Jornal/sprite_2.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/Jornal/sprite_3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (55, 40))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel7_pos_x, coletavel7_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (55, 40))
        self.rect.topleft = coletavel7_pos_x, coletavel7_pos_y

grupo_coletavel7 = pygame.sprite.Group()
coletavel7 = Coletavel7()
grupo_coletavel7.add(coletavel7)

class Coletavel8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/LataRefri/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/LataRefri/sprite_1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (21, 48))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel8_pos_x, coletavel8_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (21, 48))
        self.rect.topleft = coletavel8_pos_x, coletavel8_pos_y

grupo_coletavel8 = pygame.sprite.Group()
coletavel8 = Coletavel8()
grupo_coletavel8.add(coletavel8)

class Coletavel9(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/LatasFerro/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/LatasFerro/sprite_1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (49, 53))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel9_pos_x, coletavel9_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (49, 53))
        self.rect.topleft = coletavel9_pos_x, coletavel9_pos_y

grupo_coletavel9 = pygame.sprite.Group()
coletavel9 = Coletavel9()
grupo_coletavel9.add(coletavel9)

class Coletavel10(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/PoteVidro/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/PoteVidro/sprite_1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (25, 48))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel10_pos_x, coletavel10_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (25, 48))
        self.rect.topleft = coletavel10_pos_x, coletavel10_pos_y

grupo_coletavel10 = pygame.sprite.Group()
coletavel10 = Coletavel10()
grupo_coletavel10.add(coletavel10)

class Coletavel11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/ProdutoLimpeza1/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/ProdutoLimpeza1/sprite_1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (42, 64))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel11_pos_x, coletavel11_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (42, 64))
        self.rect.topleft = coletavel11_pos_x, coletavel11_pos_y

grupo_coletavel11 = pygame.sprite.Group()
coletavel11 = Coletavel11()
grupo_coletavel11.add(coletavel11)

class Coletavel12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/ProdutoLimpeza2/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/ProdutoLimpeza2/sprite_1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (38, 51))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel12_pos_x, coletavel12_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (38, 51))
        self.rect.topleft = coletavel12_pos_x, coletavel12_pos_y

grupo_coletavel12 = pygame.sprite.Group()
coletavel12 = Coletavel12()
grupo_coletavel12.add(coletavel12)

class Coletavel13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/SacoPapelao/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/SacoPapelao/sprite_1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (39, 58))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel13_pos_x, coletavel13_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (39, 58))
        self.rect.topleft = coletavel13_pos_x, coletavel13_pos_y

grupo_coletavel13 = pygame.sprite.Group()
coletavel13 = Coletavel13()
grupo_coletavel13.add(coletavel13)

class Coletavel14(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/Spray/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/Spray/sprite_1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (20, 47))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel14_pos_x, coletavel14_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (20, 47))
        self.rect.topleft = coletavel14_pos_x, coletavel14_pos_y

grupo_coletavel14 = pygame.sprite.Group()
coletavel14 = Coletavel14()
grupo_coletavel14.add(coletavel14)

class Coletavel15(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/Xicara/sprite_0.png'))                        
        self.sprites.append(pygame.image.load('coletaveis/Xicara/sprite_1.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32, 44))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = coletavel15_pos_x, coletavel15_pos_y
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32, 44))
        self.rect.topleft = coletavel15_pos_x, coletavel15_pos_y

grupo_coletavel15 = pygame.sprite.Group()
coletavel15 = Coletavel15()
grupo_coletavel15.add(coletavel15)

while True:
    relogio.tick(30)
    tela.fill((PRETO))
    pontuacao = f'Pontos: {pontos}'
    texto_formatado_pontuacao = fonte.render(pontuacao, True, (BRANCO))

    colisao_inimigo = pygame.sprite.spritecollide(personagem, grupo_inimigo, False, pygame.sprite.collide_mask)

    colisao_coletavel1 = pygame.sprite.spritecollide(personagem, grupo_coletavel1, False, pygame.sprite.collide_mask)
    colisao_coletavel2 = pygame.sprite.spritecollide(personagem, grupo_coletavel2, False, pygame.sprite.collide_mask)
    colisao_coletavel3 = pygame.sprite.spritecollide(personagem, grupo_coletavel3, False, pygame.sprite.collide_mask)
    colisao_coletavel4 = pygame.sprite.spritecollide(personagem, grupo_coletavel4, False, pygame.sprite.collide_mask)
    colisao_coletavel5 = pygame.sprite.spritecollide(personagem, grupo_coletavel5, False, pygame.sprite.collide_mask)
    colisao_coletavel6 = pygame.sprite.spritecollide(personagem, grupo_coletavel6, False, pygame.sprite.collide_mask)
    colisao_coletavel7 = pygame.sprite.spritecollide(personagem, grupo_coletavel7, False, pygame.sprite.collide_mask)
    colisao_coletavel8 = pygame.sprite.spritecollide(personagem, grupo_coletavel8, False, pygame.sprite.collide_mask)
    colisao_coletavel9 = pygame.sprite.spritecollide(personagem, grupo_coletavel9, False, pygame.sprite.collide_mask)
    colisao_coletavel10 = pygame.sprite.spritecollide(personagem, grupo_coletavel10, False, pygame.sprite.collide_mask)
    colisao_coletavel11 = pygame.sprite.spritecollide(personagem, grupo_coletavel11, False, pygame.sprite.collide_mask)
    colisao_coletavel12 = pygame.sprite.spritecollide(personagem, grupo_coletavel12, False, pygame.sprite.collide_mask)
    colisao_coletavel13 = pygame.sprite.spritecollide(personagem, grupo_coletavel13, False, pygame.sprite.collide_mask)
    colisao_coletavel14 = pygame.sprite.spritecollide(personagem, grupo_coletavel14, False, pygame.sprite.collide_mask)
    colisao_coletavel15 = pygame.sprite.spritecollide(personagem, grupo_coletavel15, False, pygame.sprite.collide_mask)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                personagem.pula()
            if event.key == K_r:
                reiniciar_jogo()
            if event.key == K_m:
                som_fundo.play(-1)
    if pygame.key.get_pressed()[K_w]:
        personagem.cima()
    if pygame.key.get_pressed()[K_a]:
        personagem.esquerda()
    if pygame.key.get_pressed()[K_d]:
        personagem.direita()
    if pygame.key.get_pressed()[K_s]:
        personagem.baixo()
    if colisao_coletavel1:
        coletavel1_pos_x = randrange(20, 580, 10)
        coletavel1_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel2:
        coletavel2_pos_x = randrange(20, 580, 10)
        coletavel2_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel3:
        coletavel3_pos_x = randrange(20, 580, 10)
        coletavel3_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel4:
        coletavel4_pos_x = randrange(20, 580, 10)
        coletavel4_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel5:
        coletavel5_pos_x = randrange(20, 580, 10)
        coletavel5_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel6:
        coletavel6_pos_x = randrange(20, 580, 10)
        coletavel6_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel7:
        coletavel7_pos_x = randrange(20, 580, 10)
        coletavel7_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel8:
        coletavel8_pos_x = randrange(20, 580, 10)
        coletavel8_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel9:
        coletavel9_pos_x = randrange(20, 580, 10)
        coletavel9_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel10:
        coletavel10_pos_x = randrange(20, 580, 10)
        coletavel10_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel11:
        coletavel11_pos_x = randrange(20, 580, 10)
        coletavel11_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel12:
        coletavel12_pos_x = randrange(20, 580, 10)
        coletavel12_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel13:
        coletavel13_pos_x = randrange(20, 580, 10)
        coletavel13_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel14:
        coletavel14_pos_x = randrange(20, 580, 10)
        coletavel14_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    if colisao_coletavel15:
        coletavel15_pos_x = randrange(20, 580, 10)
        coletavel15_pos_y = randrange(0, 435, 10)
        pontos = pontos + 1
        som_coletavel.play()
    tela.blit(imagem_fundo, (0, 0))
    tela.blit(texto_formatado_pontuacao, (435, 10))
 
    grupo_personagem.draw(tela)
    grupo_inimigo.draw(tela)
    grupo_coletavel1.draw(tela)
    grupo_coletavel2.draw(tela)
    grupo_coletavel3.draw(tela)
    grupo_coletavel4.draw(tela)
    grupo_coletavel5.draw(tela)
    grupo_coletavel6.draw(tela)
    grupo_coletavel7.draw(tela)
    grupo_coletavel8.draw(tela)
    grupo_coletavel9.draw(tela)
    grupo_coletavel10.draw(tela)
    grupo_coletavel11.draw(tela)
    grupo_coletavel12.draw(tela)
    grupo_coletavel13.draw(tela)
    grupo_coletavel14.draw(tela)
    grupo_coletavel15.draw(tela)

    if colisao_inimigo:
        tela.fill((PRETO))
        game_over = exibe_mensagem('GAME OVER', 40, (VERMELHO))
        tela.blit(game_over, (largura // 2 - 135, altura // 2 - 100))     
        motivacao1 = exibe_mensagem('Poxa, você perdeu! Mas não desanime.', 20, (BRANCO))
        tela.blit(motivacao1, (largura // 2 - 200, altura // 2 - 40))
        motivacao2 = exibe_mensagem('A sustentabilidade é uma atitude de todos precisamos adotar.', 20, (BRANCO))
        tela.blit(motivacao2, (largura // 2 - 295, altura // 2 - 20))        
        motivacao3 = exibe_mensagem('É uma luta diária que todos nós devemos tomar partido.', 20, (BRANCO))
        tela.blit(motivacao3, (largura // 2 - 268, altura // 2 + 0))        
        motivacao4 = exibe_mensagem('Não desanime dessa batalha para mantermos o planeta vivo!', 20, (BRANCO))
        tela.blit(motivacao4, (largura // 2 - 290, altura // 2 + 20))        
        restart = exibe_mensagem('Pressione R para reiniciar', 20, (AMARELO))
        tela.blit(restart, (largura // 2 - 133, altura // 2 + 80))
    else:
        grupo_personagem.update()
        grupo_inimigo.update()
        grupo_coletavel1.update()
        grupo_coletavel2.update()
        grupo_coletavel3.update()
        grupo_coletavel4.update()
        grupo_coletavel5.update()
        grupo_coletavel6.update()
        grupo_coletavel7.update()
        grupo_coletavel8.update()
        grupo_coletavel9.update()
        grupo_coletavel10.update()
        grupo_coletavel11.update()
        grupo_coletavel12.update()
        grupo_coletavel13.update()
        grupo_coletavel14.update()
        grupo_coletavel15.update()

    pygame.display.flip()