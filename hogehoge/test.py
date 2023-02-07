from turtle import *
shape("turtle")
n = int(input('ピラミッドの段数を入力してください。'))
if n == 1:
 for n in range(3):
    left(120)
    forward(100)
elif n == 2:
    left(120)
    forward(50)
    left(120)
    forward(50)
    left(120)
    forward(100)
done()