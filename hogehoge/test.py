from turtle import *
shape("turtle")
n = int(input('ピラミッドの段数を入力してください。'))
for i in range(n):
    forward(100)
    left(45)
    forward(100)
    left(45)
    forward(100)
    left(45)
    forward(100)
done()