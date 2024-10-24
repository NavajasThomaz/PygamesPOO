import pygame
import os

class Actor:
    """Um Ator é um objeto que pode ser colocado ou instanciado no mundo.
    """
    def __init__(self, path, heigth, width, speed, transform, x=0, y=0):
        # Configurações do jogador
        self.facing_right = True
        self.transform = transform
        self.speed = speed
        self.jump = 15
        self.gravity = 0.5
        self.velocity_y = 0
        self.x = x
        self.y = y
        self.sprite_index = 0
        self.sprite_timer = 0
        self.sprite_interval = 100  # Tempo em milissegundos entre os quadros
        self.height = heigth
        self.width = width
        self.on_ground = True
        if path:
            try:
                self.sprite_images = [pygame.image.load(os.path.join(path, image)) for image in os.listdir(path)]
                self.sprite_images = [pygame.transform.scale(image, (width, heigth)) for image in self.sprite_images]
            except Exception as e:
                print(e)
        self.current_sprite = self.sprite_images[0]
            
    def update(self, clock):
        # Atualizar animação do sprite
        self.sprite_timer += clock.get_time()
        if self.sprite_timer >= self.sprite_interval:
            self.sprite_timer = 0
            self.sprite_index = (self.sprite_index + 1) % len(self.sprite_images)
            self.current_sprite = self.sprite_images[self.sprite_index]
            
        # Aplicar gravidade
        if self.transform == 'dinamico':
            self.velocity_y += self.gravity
            self.y += self.velocity_y
  
class Pawn(Actor):
    """Um Peão é um Ator que consegue possuido e receber entradas de um controlador.
    """
    def __init__(self):
        super().__init__(None, 100, 70, 5, 'dinamico')

class Character(Pawn):
    """Um Personagem é um tipo de Peão que possui a habilidade de andar pelo mundo.
    """
    def __init__(self, width=70, height=100):
        self.walking = False
        self.jumping = False
        self.load_sprites(width, height)
        self.sprite_images = self.idle_queue
        super().__init__()
        
    def load_sprites(self, width, height):
        self.collision_queue = [pygame.image.load(os.path.join('Classes\\Brave_Boy\\Player_actions\\Collision', image)) for image in os.listdir('Classes\\Brave_Boy\\Player_actions\\Collision')]
        self.collision_queue = [pygame.transform.scale(image, (width, height)) for image in self.collision_queue]
        
        self.flying_queue = [pygame.image.load(os.path.join('Classes\\Brave_Boy\\Player_actions\\Flying', image)) for image in os.listdir('Classes\\Brave_Boy\\Player_actions\\Flying')]
        self.flying_queue = [pygame.transform.scale(image, (width, height)) for image in self.flying_queue]
        
        self.gameover_queue = [pygame.image.load(os.path.join('Classes\\Brave_Boy\\Player_actions\\GameOver', image)) for image in os.listdir('Classes\\Brave_Boy\\Player_actions\\GameOver')]
        self.gameover_queue = [pygame.transform.scale(image, (width, height)) for image in self.gameover_queue]
        
        self.idle_queue = [pygame.image.load(os.path.join('Classes\\Brave_Boy\\Player_actions\\Idle', image)) for image in os.listdir('Classes\\Brave_Boy\\Player_actions\\Idle')]
        self.idle_queue = [pygame.transform.scale(image, (width, height)) for image in self.idle_queue]
        
        self.jump_queue = [pygame.image.load(os.path.join('Classes\\Brave_Boy\\Player_actions\\Jump', image)) for image in os.listdir('Classes\\Brave_Boy\\Player_actions\\Jump')]
        self.jump_queue = [pygame.transform.scale(image, (width, height)) for image in self.jump_queue]
        
        self.jumpfall_queue = [pygame.image.load(os.path.join('Classes\\Brave_Boy\\Player_actions\\Jump-Fall', image)) for image in os.listdir('Classes\\Brave_Boy\\Player_actions\\Jump-Fall')]
        self.jumpfall_queue = [pygame.transform.scale(image, (width, height)) for image in self.jumpfall_queue]
        
        self.run_queue = [pygame.image.load(os.path.join('Classes\\Brave_Boy\\Player_actions\\Run', image)) for image in os.listdir('Classes\\Brave_Boy\\Player_actions\\Run')]
        self.run_queue = [pygame.transform.scale(image, (width, height)) for image in self.run_queue]
        
        self.shoot_queue = [pygame.image.load(os.path.join('Classes\\Brave_Boy\\Player_actions\\Shoot', image)) for image in os.listdir('Classes\\Brave_Boy\\Player_actions\\Shoot')]
        self.shoot_queue = [pygame.transform.scale(image, (width, height)) for image in self.shoot_queue]
        
        self.shootbazooka_queue = [pygame.image.load(os.path.join('Classes\\Brave_Boy\\Player_actions\\Shoot-Bazooka', image)) for image in os.listdir('Classes\\Brave_Boy\\Player_actions\\Shoot-Bazooka')]
        self.shootbazooka_queue = [pygame.transform.scale(image, (width, height)) for image in self.shootbazooka_queue]
        
        self.slash_queue = [pygame.image.load(os.path.join('Classes\\Brave_Boy\\Player_actions\\Slash', image)) for image in os.listdir('Classes\\Brave_Boy\\Player_actions\\Slash')]
        self.slash_queue = [pygame.transform.scale(image, (width, height)) for image in self.slash_queue]

    def update_player(self, clock):
        if self.walking:
            if self.on_ground:
                self.sprite_images = self.run_queue
            else:
                self.sprite_images = self.jumpfall_queue
        elif self.jumping:
            self.sprite_images = self.jump_queue
        elif self.on_ground and not self.jumping and not self.walking:
            self.sprite_images = self.idle_queue
        self.update(clock)

class Player_Controller(Actor):
    """Um Controlador de Player é um Ator responsável por controlar o Peão usado pelo Player.
    """
    def __init__(self, Pawn, Gamemode):
        self.pawn = Pawn
        self.gamemode = Gamemode
    
    def input(self):
        # Teclas pressionadas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pawn.x -= self.pawn.speed
            self.pawn.facing_right = False
            self.pawn.walking = True
        elif keys[pygame.K_RIGHT]:
            self.pawn.x += self.pawn.speed
            self.pawn.facing_right = True
            self.pawn.walking = True
        else:
            self.pawn.walking = False
        if keys[pygame.K_SPACE] and self.pawn.on_ground:
            self.pawn.velocity_y = -self.pawn.jump
            self.pawn.jumping = True
            self.pawn.on_ground = False
        else:
            self.pawn.jumping = False
        
class Game_Mode_Base:
    """Modo de Jogo define o game sendo jogado, suar regras, pontuações e etc.
    """
    def __init__(self):
        pass
    
class Enemy(Actor):
    def __init__(self, heigth, width, speed, type=0, level=1, loot=[[1,1]]):
        PATH = os.path.join('Classes\\Villains', os.listdir('Classes\\Villains')[type])
        super().__init__(PATH, heigth, width, speed, transform='dinamico')
        self.type = type
        self.level = level
        self.loot = loot
        
    def follow_player(self, player):
        if self.x < player.x:
            self.x += self.speed
        elif self.x > player.x:
            self.x -= self.speed
    
class Item(Actor):
    def __init__(self):
        pass

class Mapa:
    def __init__(self, path):
        with open(os.path.join('Maps', path), "r") as file:
            self.map = file.readlines
    
class Tile(Actor):
    def __init__(self, type, x, y):
        PATH = os.path.join('Classes\\Background', os.listdir('Classes\\Background')[type])
        super().__init__(PATH, 80, 80, 'static', x, y)
        