from pico2d import *
import game_framework
import game_framework
import title_mode

image = None

logo_start_time = 0.0

def init():
    #여기서 이미지를 로드, 초기 세팅
    global image, logo_start_time
    image = load_image('tuk_credit.png')

    logo_start_time = get_time()


def update():
    #시간 체크를 해주고
    global logo_start_time
    if get_time() - logo_start_time >=2.0:
        logo_start_time = get_time()
        game_framework.change_mode(title_mode)

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
    #입력 버퍼는 다 지웠다?
    events = get_events()

def pause():
    pass
def resume():
    pass