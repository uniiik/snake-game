
from turtle import *
from random import randrange
from freegames import square,vector
#these modules we have downloaded to use in games

#we will need three elements
foods=vector(0,0)
snakkee=[vector(10,0)]
target=vector(0,-10)
#target defines the direction of graph
def change(x,Y):
    target.x=x
    target.y=y
#it is about boundaries values , so if game crosses boundary row then it is considered as illegal move
def inside(head):
   return -200<head.x<190 and -200 <head.y <190



def move():
    head=snakkee[-1].copy()#we will give forward movement value
    head.move(target)

    if not inside(head) or head in snakkee:#if snakkee hits its own body then also user is out
        square(head.x , head.y ,9,'red')
        update()
        return

    snakkee.append()#

    if head==foods:#if snakkee hits foods then score will add
        print("snakkee",len(snakkee))

        foods.x=randrange(-15,15)*10

        foods.y=randrange(-15,15)*10

    else:

        snakkee.pop(0)

    clear()

    for body in snakkee:

        square(body.x,body.y,9,'green')

    square(foods.x,foods.y,9,'red')

    update()

    ontimeter(move,100)

    hideturtle()

    tracer(False)

    listen()

    onkey(lambda:changes(10,0),'right')

    onkey(lambda:changes(-10,0),'left')

    onkey(lambda:changes(0,10),'up')
    onkey(lambda:changes(0,-10),'down')

    move()
    done()
