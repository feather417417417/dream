from turtle import *
shape("turtle")
n = int(input('ピラミッドの段数を入力してください。'))
if n == 1:
 for n in range(3):
    forward(100)     
    left(120)
elif n == 2:
 for n in range(3):
    forward(50)
    left(120)
    continue
right(120)
for n in range(3):
    forward(50)
    left(120)
    continue
forward(50)
left(120)
forward(50)
for n in range(3):
    forward(50)
    left(120)
done()