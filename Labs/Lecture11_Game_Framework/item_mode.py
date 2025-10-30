from pico2d import *


import game_framework
import game_world
from pannel import Pannel


def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel, 2)

def finish():
    global pannel
    game_world.remove_object(pannel)
    del pannel

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def handle_events():
    event_list = get_events()
    for event in event_list:
          if event.type == SDL_QUIT:
               game_framework.quit()
          elif event.type == SDL_KEYDOWN:
               if event.key == SDLK_ESCAPE:
                   game_framework.pop_mode()
               elif event.key == SDLK_0:
                # import play_mode here to avoid circular import problems
                import play_mode
                play_mode.boy.item = None
                 game_framework.pop_mode()
               elif event.key == SDLK_1:
                import play_mode
                play_mode.boy.item = 'Ball'
                 game_framework.pop_mode()
               elif event.key == SDLK_2:
                import play_mode
                play_mode.boy.item = 'BigBall'
                 game_framework.pop_mode()

def pause():
    pass
def resume():
    pass
