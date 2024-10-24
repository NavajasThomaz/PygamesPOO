import pygame
import sys
from Classes import Enemy, Mapa, Character, Player_Controller, Game_Mode_Base

class Game:
    def __init__(self):
        # Inicialização do Pygame
        pygame.init()
        
        # Loop principal do jogo
        self.running = True
        self.clock = pygame.time.Clock()
        
        
        # Configurações da tela
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Jogo de Plataforma 2D com Animação")

        # Cores e fonte
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.font = pygame.font.Font(None, 36)
        self.initial_screen()

    def is_button_clicked(self, mouse_pos, button_rect):
        return button_rect.collidepoint(mouse_pos)

    def initial_screen(self):
        
        green_long_button_image = pygame.image.load('Classes\\GuI\\Empty Buttons\\Green-Long.png')
        green_long_button_image = pygame.transform.scale(green_long_button_image, (400, 90))
        grey_long_button_image = pygame.image.load('Classes\\GuI\\Empty Buttons\\Grey-Long.png')
        grey_long_button_image = pygame.transform.scale(grey_long_button_image, (400, 90))
        orange_long_button_image = pygame.image.load('Classes\\GuI\\Empty Buttons\\Orange-Long.png')
        orange_long_button_image = pygame.transform.scale(orange_long_button_image, (400, 90))
        red_long_button_image = pygame.image.load('Classes\\GuI\\Empty Buttons\\Red-Long.png')
        red_long_button_image = pygame.transform.scale(red_long_button_image, (400, 90))
        
        start_button_rect = green_long_button_image.get_rect()
        start_button_rect.topleft = (self.width // 2 - start_button_rect.width // 2, self.height // 3 + start_button_rect.height)
        start_text_surface = self.font.render('New Game', True, self.BLACK)
        start_text_rect = start_text_surface.get_rect(center=start_button_rect.center)
        
        load_button_rect = orange_long_button_image.get_rect()
        load_button_rect.topleft = (self.width // 2 - load_button_rect.width // 2, self.height // 3 + load_button_rect.height * 2)
        load_text_surface = self.font.render('Load Game', True, self.BLACK)
        load_text_rect = load_text_surface.get_rect(center=load_button_rect.center)
        
        survival_button_rect = red_long_button_image.get_rect()
        survival_button_rect.topleft = (self.width // 2 - survival_button_rect.width // 2, self.height // 3 + survival_button_rect.height * 3)
        survival_text_surface = self.font.render('Survival', True, self.BLACK)
        survival_text_rect = survival_text_surface.get_rect(center=survival_button_rect.center)
        
        quit_button_rect = grey_long_button_image.get_rect()
        quit_button_rect.topleft = (self.width // 2 - quit_button_rect.width // 2, self.height // 3 + quit_button_rect.height * 4)
        quit_text_surface = self.font.render('Quit', True, self.BLACK)
        quit_text_rect = quit_text_surface.get_rect(center=quit_button_rect.center)
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.is_button_clicked(event.pos, start_button_rect):
                        print("Botão iniciar clicado!")
                    elif self.is_button_clicked(event.pos, load_button_rect):
                        print("Botão load clicado!")
                    elif self.is_button_clicked(event.pos, survival_button_rect):
                        self.level('level1.txt')
                    elif self.is_button_clicked(event.pos, quit_button_rect):
                        self.running = False
                        
            # Desenhar tudo
            self.screen.fill(self.WHITE)
            
            self.screen.blit(green_long_button_image, start_button_rect.topleft)
            self.screen.blit(start_text_surface, start_text_rect.topleft)
            
            self.screen.blit(orange_long_button_image, load_button_rect.topleft)
            self.screen.blit(load_text_surface, load_text_rect.topleft)
            
            self.screen.blit(red_long_button_image, survival_button_rect.topleft)
            self.screen.blit(survival_text_surface, survival_text_rect.topleft)
            
            self.screen.blit(grey_long_button_image, quit_button_rect.topleft)
            self.screen.blit(quit_text_surface, quit_text_rect.topleft)
            
            pygame.display.flip()
            pygame.time.Clock().tick(60)

        pygame.quit()
        sys.exit()
        
    def level(self, path):
        mapa = Mapa(path)
        
        # Plataforma
        platform_width = self.width
        platform_height = 20
        platform_x = 0
        platform_y = self.height - platform_height

        self.gamemode = Game_Mode_Base()
        self.inimigo = Enemy(97.9, 133.2, 1)
        self.player = Character()
        self.player_controller = Player_Controller(self.player, self.gamemode)


        # Direção do jogador
        facing_right = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.inimigo.update(self.clock)
            self.inimigo.follow_player(self.player)
            
            self.player_controller.input()
            self.player.update_player(self.clock)
            
            # Colisão com o chão
            if self.inimigo.y + self.inimigo.height > platform_y:
                self.inimigo.y = platform_y - self.inimigo.height
                self.inimigo.velocity_y = 0
                self.inimigo.on_ground = True
                
            # Colisão com o chão
            if self.player.y + self.player.height > platform_y:
                self.player.y = platform_y - self.player.height
                self.player.velocity_y = 0
                self.player.on_ground = True
                
            # Desenhar tudo
            self.screen.fill(self.WHITE)
        
            enemy_current_sprite = self.inimigo.current_sprite
            player_current_sprite = self.player.current_sprite
        
            if not self.player.facing_right:
                player_current_sprite = pygame.transform.flip(player_current_sprite, True, False)
                
            self.screen.blit(enemy_current_sprite, (self.inimigo.x, self.inimigo.y))
            self.screen.blit(player_current_sprite, (self.player.x, self.player.y))
            pygame.draw.rect(self.screen, self.BLACK, (platform_x, platform_y, platform_width, platform_height))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

game = Game()