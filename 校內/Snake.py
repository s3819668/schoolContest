# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()


#import random as rd
#T=rd.randint(1,99)
#G=0
#while G!=T:
#    G=eval(input("終極密碼請猜(1-99):"))
#    if G<T:
#        print("猜大一點")
#    elif G>T:
#        print("猜小一點")
#    else:
#        print("猜中了!!")

#M=eval(input("請輸入一整數M以判定1*2*3*4*...*N>=M"))
#N=1
#S=1
#while S<M:
#    N+=1
#    S*=N
#print("%d! = %d >= %d"%(N,S,M))

#sum1=0
#count=0
#for i in range(1,1001):
#    if i%3==0 and i%5==0:
#        print(i, end=" ")
#        sum1+=i
#        count+=1
#print()
#print("總和:%d, 個數:%d"%(sum1,count))
#
#sum1=0
#count=0
#for i in range(3,1001,3):
#    if i%5==0:
#        print(i, end=" ")
#        sum1+=i
#        count+=1
#        
#print()
#print("總和:%d, 個數:%d"%(sum1,count))
#
#list1=[]
#for i in range(1,1001):
#    if i%3==0 and i%5==0:
#        list1.append(i)
#print(list1,sum(list1),len(list1))

#a=eval(input("輸入三角形的第一邊長:"))
#b=eval(input("輸入三角形的第一邊長:"))
#c=eval(input("輸入三角形的第一邊長:"))
#
#if a+b>c and a+c>b and b+c>a:
#    print("%d %d %d 可構成三角形"%(a,b,c))
#else:
#    print("%d %d %d 無法構成三角形"%(a,b,c))
#    if a+b<=c:
#        print("因為%d+%d<=%d"%(a,b,c))
#    if a+c<=b:
#        print("因為%d+%d<=%d"%(a,c,b))
#    if b+c<=a:
#        print("因為%d+%d<=%d"%(b,c,a))

#num=eval(input("輸入一整數:"))
#if num%2==1:
#    print("%d為奇數"%num)
#else:
#    print("%d為偶數"%num)

#a=3
#if a<=3:
#    print("GOOD")
#    print("GOOD")
#    print("GOOD")
#
#
#b=eval(input("SCORE"))
#if b>=60:
#    print("GOOD")
#else:
#    print("BAD")