from pico2d import *
import game_framework
import game_framework
import play_mode

image = None


def init():
    #여기서 이미지를 로드, 초기 세팅
    global image
    image = load_image('title.png')

def update():
    #시간 체크를 해주고
    pass

def draw():
    #이미지를 그려준다
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def finish():
    global image
    del image

def handle_events():
    #현재까지 들어온 이벤트들을 받아온다. 그리고 아무것도 하지 않는다.
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)

def pause():
    pass
def resume():
    pass