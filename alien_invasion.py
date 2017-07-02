import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group   # 导入编组中的精灵，精灵就是游戏中的角色
from game_stats import GameStats


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    ship = Ship(ai_setting, screen)
    stats = GameStats(ai_setting)
    bullets = Group()
    pygame.display.set_caption('alien invasion')
    aliens = Group()  # 利用编组
    gf.create_fleet(ai_setting, screen, ship, aliens)
    while True:  # 主循环的函数简单清新，职责单一
        gf.check_event(ai_setting, screen, ship, bullets)
        bullets.update()
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, screen, ship, aliens,bullets)
        gf.update_screen(ai_setting, screen, ship, aliens, bullets)


run_game()
