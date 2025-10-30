#[0]은 배경
#[1]은 그 위에
world = [[],[]]

#월드에 객체 추가
def add_object(o, depth=0):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return


#월드 전체의 객체들을 업데이트
def update():
    for layer in world:
        for o in layer:
            o.update()

    #월드 전체의 객체들을 그린다.
def render():
    for layer in world:
        for o in layer:
            o.draw()

