import graphics as gr

window = gr.GraphWin("MIPT Graphics module practice", 640, 480)

#небо
sky = gr.Rectangle(gr.Point(0, 0), gr.Point(640, 200))
sky.setFill('#2CA2FD')
sky.draw(window)

#земля
ground = gr.Rectangle(gr.Point(0, 200), gr.Point(640, 480))
ground.setFill('#0B6623')
ground.draw(window)

#солнце
sun = gr.Circle(gr.Point(60, 70), 50)
sun.setFill('yellow')
sun.draw(window)

#домик
#крыша
vertices = [gr.Point(400, 250), gr.Point(500, 140), gr.Point(600, 250)]
roof = gr.Polygon(vertices)
roof.setFill('#B22222')
roof.setWidth(3)
roof.draw(window)

#стены
body = gr.Rectangle(gr.Point(410, 250), gr.Point(590, 410))
body.setFill('#FFDF83')
body.setWidth(3)
body.draw(window)

#окно
#рама
window_border = gr.Rectangle(gr.Point(455, 285), gr.Point(545, 375))
window_border.setFill('brown')
window_border.draw(window)
#стекла
home_window = gr.Rectangle(gr.Point(460, 290), gr.Point(540, 370))
home_window.setFill('#99CCFF')
home_window.draw(window)
#еще рама
window_inside_border = gr.Line(gr.Point(500, 290), gr.Point(500, 375))
window_inside_border.setWidth(6)
window_inside_border.setOutline('brown')
window_inside_border.draw(window)

window_inside_border2 = gr.Line(gr.Point(455, 330), gr.Point(545, 330))
window_inside_border2.setWidth(6)
window_inside_border2.setOutline('brown')
window_inside_border2.draw(window)

#дерево
trunk = gr.Rectangle(gr.Point(200, 370), gr.Point(210, 430))
trunk.setFill('#663300')
trunk.setWidth(3)
trunk.draw(window)

vertices_tree1 = [gr.Point(100, 370), gr.Point(205, 300), gr.Point(300, 370)]
vertices_tree1 = gr.Polygon(vertices_tree1)
vertices_tree1.setFill('#003300')
vertices_tree1.setWidth(3)
vertices_tree1.draw(window)

vertices_tree2 = [gr.Point(130, 330), gr.Point(205, 270), gr.Point(280, 330)]
vertices_tree2 = gr.Polygon(vertices_tree2)
vertices_tree2.setFill('#003300')
vertices_tree2.setWidth(3)
vertices_tree2.draw(window)

vertices_tree3 = [gr.Point(160, 290), gr.Point(205, 240), gr.Point(250, 290)]
vertices_tree3 = gr.Polygon(vertices_tree3)
vertices_tree3.setFill('#003300')
vertices_tree3.setWidth(3)
vertices_tree3.draw(window)

#облако1
cloud_piece1 = gr.Circle(gr.Point(330, 50), 20)
cloud_piece1.setFill('#ecf0f1')
cloud_piece1.draw(window)

cloud_piece2 = gr.Circle(gr.Point(350, 50), 20)
cloud_piece2.setFill('#ecf0f1')
cloud_piece2.draw(window)

cloud_piece3 = gr.Circle(gr.Point(320, 70), 20)
cloud_piece3.setFill('#ecf0f1')
cloud_piece3.draw(window)

cloud_piece4 = gr.Circle(gr.Point(340, 70), 20)
cloud_piece4.setFill('#ecf0f1')
cloud_piece4.draw(window)

cloud_piece5 = gr.Circle(gr.Point(360, 70), 20)
cloud_piece5.setFill('#ecf0f1')
cloud_piece5.draw(window)

#облако2
cloud_piece1 = gr.Circle(gr.Point(330, 50), 20)
cloud_piece1.setFill('#ecf0f1')
cloud_piece1.draw(window)

cloud_piece2 = gr.Circle(gr.Point(350, 50), 20)
cloud_piece2.setFill('#ecf0f1')
cloud_piece2.draw(window)

cloud_piece3 = gr.Circle(gr.Point(320, 70), 20)
cloud_piece3.setFill('#ecf0f1')
cloud_piece3.draw(window)

cloud_piece4 = gr.Circle(gr.Point(340, 70), 20)
cloud_piece4.setFill('#ecf0f1')
cloud_piece4.draw(window)

cloud_piece5 = gr.Circle(gr.Point(360, 70), 20)
cloud_piece5.setFill('#ecf0f1')
cloud_piece5.draw(window)

#облако
cloud_piece1 = gr.Circle(gr.Point(330, 50), 20)
cloud_piece1.setFill('#ecf0f1')
cloud_piece1.draw(window)

cloud_piece2 = gr.Circle(gr.Point(350, 50), 20)
cloud_piece2.setFill('#ecf0f1')
cloud_piece2.draw(window)

cloud_piece3 = gr.Circle(gr.Point(320, 70), 20)
cloud_piece3.setFill('#ecf0f1')
cloud_piece3.draw(window)

cloud_piece4 = gr.Circle(gr.Point(340, 70), 20)
cloud_piece4.setFill('#ecf0f1')
cloud_piece4.draw(window)

cloud_piece5 = gr.Circle(gr.Point(360, 70), 20)
cloud_piece5.setFill('#ecf0f1')
cloud_piece5.draw(window)

window.getMouse()

window.close()
