from Brave_Boy import Sprite_Queue

class Player_sprite_manager:
    def __init__(self):
        self.collision_queue = Sprite_Queue('Brave_Boy\\Player_actions\\Collision')
        self.flying_queue = Sprite_Queue('Brave_Boy\\Player_actions\\Flying')
        self.gameover_queue = Sprite_Queue('Brave_Boy\\Player_actions\\GameOver')
        self.idle_queue = Sprite_Queue('Brave_Boy\\Player_actions\\Idle')
        self.jump_queue = Sprite_Queue('Brave_Boy\\Player_actions\\Jump')
        self.jumpfall_queue = Sprite_Queue('Brave_Boy\\Player_actions\\Jump-Fall')
        self.run_queue = Sprite_Queue('Brave_Boy\\Player_actions\\Run')
        self.shoot_queue = Sprite_Queue('Brave_Boy\\Player_actions\\Shoot')
        self.shootbazooka_queue = Sprite_Queue('Brave_Boy\\Player_actions\\Shoot-Bazooka')
        self.slash_queue = Sprite_Queue('Brave_Boy\\Player_actions\\Slash')