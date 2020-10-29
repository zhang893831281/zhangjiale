# 一 调用库
import pygame
import sys
import time
import random
from pygame.locals import *

# 二 设置初始化
# 初始化PYgame
pygame.init()
fpsClock = pygame.time.Clock()

# 创建pygame显示层
playSurface = pygame.display.set_mode((640,480))
# 定义标题
pygame.display.set_caption('Snake GO!')
# 加载资源图片，game.ico在最后的文件中
image = pygame.image.load("F:\workhome\蛇.jpg")
# 设置图标
pygame.display.set_icon(image)

# 三 定义颜色变量
redColour = pygame.Color(255,0,0)
blackColour = pygame.Color(0,0,0)
whiteColour = pygame.Color(255,255,255)
greyColour = pygame.Color(155,155,155)
LightColour = pygame.Color(220,220,220)

# 定义gameover函数
def gameOver(playsurface,score):
# 显示gameove并定义字体及大小
    gameOverFont = pygame.font.Font('arial.ttf',72)
    gameOverSurf = gameOverFont.render('GAME OVER',True,greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320,125)
    playSurface.blit(gameOverSurf,gameOverRect)
# 显示分数并定义
    scoreFont = pygame.font.Font('arial.ttf',48)
    scoreSurf = scoreFont.render('SCORE:'+ str(score),True,greyColour)
    scoreRect =scoreSurf.get_rect()
    scoreRect.midtop = (320,125)
    playSurface.blit(scoreSurf,scoreRect)
    pygame.display.flip() #刷新界面
# 休眠五秒后关闭
    time.sleep(15)
    pygame.quit()
    sys.exit()

# 蛇和树莓
# 一  初始化位置
# 初始化变量
snakePosition = [100,100] #蛇头位置
sankeSegments = [[100,100],[80,100],[60,100]]#初始长度为三个单位
raspberryPosition = [300,300]  #树莓位置
raspberrySpawned = 1  #树莓个数
direction = 'right'  #初始方向
changeDirection = direction
score = 0 #初试分数为0 

# 键盘输入判断蛇运动
# 检测到例如按键等pygame事件
for event in pygame.event.get():
    if  event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        # 判断键盘方向
        if event.key == K_RIGHT or event.key == ord('d'):
            changeDirection = 'right'
        if event.key == K_LEFT or event.key == ord('a'):
            changeDirection = 'left'
        if event.key == K_UP or event.key == ord('w'):
            changeDirection = 'up'
        if event.key == K_DOWN or event.key == ord('sd'):
            changeDirection = 'down'
        if event.key == K_ESCAPE:   #按esc退出游戏
            pygame.event.post(pygame.event.Event(QUIT))
#贪吃蛇有一个运动特点，不能往相反方向移动
        if changeDirection == 'right' and not direction == 'left':
            changeDirection = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            changeDirection = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            changeDirection = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            changeDirection = changeDirection
# 根据键盘的输入方向转动蛇头，将蛇头的当前位置添加到蛇身上
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
             snakePosition[0] += 20
        if direction == 'up':
            snakePosition[0] += 20
        if direction == 'down':
            snakePosition[0] += 20
#将蛇头的位置加入列表中
sankeSegments.insert(0,list(snakePosition))
#判断是否吃点树莓
if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
    raspberrySpawned = 0
else:
     sankeSegments.pop()  #每次将最后一节蛇身提出列表
#重新生成树莓
if raspberrySpawned ==0:
    x = random.randrange(1,32)
    y = random.randrange(1,24)
    raspberryPosition = [int(x*20),int(y*20)]
    raspberrySpawned = 1
    score += 1
# 刷新显示层
playSurface.fill(blackColour)
for position in sankeSegments[1:]:     #蛇身为白色
    pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
    pygame.draw.rect(playSurface,LightColour,Rect(snakePosition[0],snakePosition[1],20,20))
    pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0],raspberryPosition[1],20,20))
    pygame.display.flip()

#判断是否死亡
if snakePosition[0] >620 or snakePosition[0] <0:  #超出左右边界
    gameOver(playSurface,score)
if snakePosition[1] >460 or snakePosition[1] <0:  #超出上下边界
    gameOver(playSurface,score)
for snakeBody in sankeSegments[1:]:     #蛇碰到自己身体
    if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
        gameOver(playSurface,score)
 
#控制速度
#长度越长，游戏速度越快
if len(snakeSegments) <40:
    speed = 6 + len(snakeSements)//4
else:
    speed = 16
fpsClock.tick(speed)






