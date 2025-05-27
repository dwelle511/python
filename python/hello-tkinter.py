import turtle as t
cols=['blue','black','red']

def drawpolygon(n,size):
    for i in range(n):
        t.pencolor(cols[i%len(cols)])
        t.forward(size)
        t.left(360/n)
t.setup(500,200)
t.speed(3)

t.pu()
t.goto(-50,-170)

t.pd()
for i in range(3,13):
    drawpolygon(i,200)