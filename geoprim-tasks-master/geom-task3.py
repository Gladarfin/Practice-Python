import graphics as gr

window = gr.GraphWin("MIPT Graphics module practice", 640, 480)

#небо
def draw_sky(color):
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(640, 200))
    sky.setFill(color)
    sky.draw(window)

#земля
def draw_ground(color):
    ground = gr.Rectangle(gr.Point(0, 200), gr.Point(640, 480))
    ground.setFill(color)
    ground.draw(window)

#солнце
def draw_sun():
    sun = gr.Circle(gr.Point(530, 110), 50)
    sun.setFill('yellow')
    sun.draw(window)

#домик

def draw_roof():    
    #крыша
    vertices = [gr.Point(100, 250), gr.Point(200, 140), gr.Point(300, 250)]
    roof = gr.Polygon(vertices)
    roof.setFill('#B22222')
    roof.setWidth(3)
    roof.draw(window)


def draw_body():
    #стены
    body = gr.Rectangle(gr.Point(110, 250), gr.Point(290, 410))
    body.setFill('#FFDF83')
    body.setWidth(3)
    body.draw(window)


def draw_window():
    #окно
    #рама
    window_border = gr.Rectangle(gr.Point(155, 285), gr.Point(245, 375))
    window_border.setFill('brown')
    window_border.draw(window)
    #стекла
    home_window = gr.Rectangle(gr.Point(160, 290), gr.Point(240, 370))
    home_window.setFill('#99CCFF')
    home_window.draw(window)
    #еще рама
    window_inside_border = gr.Line(gr.Point(200, 290), gr.Point(200, 375))
    window_inside_border.setWidth(6)
    window_inside_border.setOutline('brown')
    window_inside_border.draw(window)
    window_inside_border2 = gr.Line(gr.Point(155, 330), gr.Point(245, 330))
    window_inside_border2.setWidth(6)
    window_inside_border2.setOutline('brown')
    window_inside_border2.draw(window)

def draw_house():
    draw_roof()
    draw_body()
    draw_window()
    
   
#дерево
def draw_tree():
    trunk = gr.Rectangle(gr.Point(400, 370), gr.Point(410, 430))
    trunk.setFill('#663300')
    trunk.setWidth(3)
    trunk.draw(window)

    vertices_tree1 = [gr.Point(300, 370), gr.Point(405, 300), gr.Point(500, 370)]
    vertices_tree1 = gr.Polygon(vertices_tree1)
    vertices_tree1.setFill('#003300')
    vertices_tree1.setWidth(3)
    vertices_tree1.draw(window)

    vertices_tree2 = [gr.Point(330, 330), gr.Point(405, 270), gr.Point(480, 330)]
    vertices_tree2 = gr.Polygon(vertices_tree2)
    vertices_tree2.setFill('#003300')
    vertices_tree2.setWidth(3)
    vertices_tree2.draw(window)

    vertices_tree3 = [gr.Point(360, 290), gr.Point(405, 240), gr.Point(450, 290)]
    vertices_tree3 = gr.Polygon(vertices_tree3)
    vertices_tree3.setFill('#003300')
    vertices_tree3.setWidth(3)
    vertices_tree3.draw(window)                       

def draw_cloud(x, y, radius):
    temp_x = x
    for i in range(0, 2, 1):
        cloud_piece = gr.Circle(gr.Point(x, y), radius)
        cloud_piece.setFill('#ecf0f1')
        cloud_piece.draw(window)
        x += radius
    y += radius
    x = temp_x - 15
    for j in range(0, 3, 1):
        cloud_piece = gr.Circle(gr.Point(x, y), radius)
        cloud_piece.setFill('#ecf0f1')
        cloud_piece.draw(window)
        x += radius


def draw_picture():
    draw_sky('#0585E6')
    draw_ground('#024B16')
    draw_sun()
    draw_house()
    draw_tree()
    draw_cloud(530, 120, 30)
    draw_cloud(130, 50, 35)
    draw_cloud(330, 150, 25)

    
draw_picture()

window.getMouse()

window.close()
