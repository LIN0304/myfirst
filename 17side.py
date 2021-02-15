import turtle
pensixe=int(input('penwide'))
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
turtle.pencolor('white')
n=int(input('請輸入正n邊形'))
x=(n-2)*180/n
turtle.goto(0, 0)
turtle.speed(2)
a=0
b=int(input('請輸入正n邊形邊長'))#input n side
t.pensize(3)#pen wide

while True:
    if a%2==0:
        turtle.color('green')
        a=a+1
    else:
        turtle.color('red')
        a=a+1

    turtle.forward(b)
    turtle.right(180-x)

turtle.done
