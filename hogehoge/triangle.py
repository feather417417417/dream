from turtle import *
shape("turtle")
# n = int(input('ピラミッドの段数を入力してください。'))
n = 5
def triangle(n):
   for n in range(3):
      forward(50)
      if n != 2:
         left(120)

def triangle2(n) :
 for n in range(4):
    forward(50)
    left(120)
         
#1段目
if  n == 1:
 for n in range(3):
    forward(100)     
    left(120)

#2段目
elif n == 2:
 for n in range(3):
    forward(50)
    left(120)
    continue
 right(120)
 for n in range(4):
    forward(50)
    left(120)
    continue
 forward(50)
 for n in range(3):
    forward(50)
    left(120)

#3段目
elif n == 3:
 for n in range(3):
   forward(50)
   left(120)
   continue
 right(120)
 for n in range(4):
    forward(50)
    left(120)
    continue
 forward(50)
 for n in range(3):
    forward(50)
    left(120)  
    continue
 right(180)
 forward(50)
 right(60)    
 for n in range(3):
    left(120) 
    forward(50) 
    continue
 for n in range(2):
    left(120) 
    forward(50) 
 for n in range(3):
    forward(50)
    left(120)  
    continue
 forward(50) 
 for n in range(3):
    forward(50)
    left(120)      
    
#4段目    
elif n == 4:
 for n in range(3):
   forward(50)
   left(120)
   continue
 right(120)
 for n in range(4):
    forward(50)
    left(120)
    continue
 forward(50)
 for n in range(3):
    forward(50)
    left(120)  
    continue
 right(180)
 forward(50)
 right(60)    
 for n in range(5):
    left(120) 
    forward(50) 
    continue  
 for n in range(3):
    forward(50)
    left(120)  
    continue
 forward(50) 
 for n in range(3):
    forward(50)
    left(120)   
    continue
 right(180)
 forward(100)
 left(60)
 for n in range(4):
    forward(50)
    left(120)  
    continue
 forward(50)
 for n in range(3):
    forward(50)
    left(120)  
    continue
 forward(50)
 for n in range(3):
    forward(50)
    left(120) 
    continue 
 forward(50)
 for n in range(3):
    forward(50)
    left(120)    
    continue

#5段目
elif n == 5:
 triangle(n)
 triangle2(n)
 forward(50)
 
 for n in range(3):
    forward(50)
    left(120)  
    continue
 right(180)
 forward(50)
 right(60)
     
 for n in range(4):
    left(120) 
    forward(50) 
    continue
 left(120)
 forward(50) 
 
 for n in range(3):
    forward(50)
    left(120)  
    continue
 forward(50)
  
 triangle(n)
 right(60)
 forward(100)
 left(60)
 
 for n in range(4):
    forward(50)
    left(120)  
    continue
 forward(50)
 
 triangle(n)
 left(120) 
 forward(50)
 
 triangle(n)
 left(120) 
 forward(50)
 
 triangle(n)
 right(60)
 forward(150)
 left(60)
 
 triangle2(n)
 forward(50)
 
 triangle(n)
 left(120) 
 forward(50)
 
 triangle(n)
 left(120) 
 forward(50)
 
 triangle(n)
 left(120)
 forward(50)
 
 triangle(n)
 right(60)
 forward(200)

done()