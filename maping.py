from PIL import Image

def getPerimeter(x,y):
   ToRight=0
   ToLeft=0
   ToDown=0
   ToUp=0
   FromRight = 0
   FromLeft = 0
   FromDown = 0
   FromUp = 0
   Xway=x
   Yway=y
   perimeter=[]
   val, dummy = image.getpixel(Xway,Yway)
   while (val > 105):
       valLeft, dummyL = image.getpixel(Xway-1, Yway)
       valRight, dummyR = image.getpixel(Xway + 1, Yway)
       valUp , dummyU = image.getpixel(Xway, Yway+1)
       valDown, dummyD = image.getpixel(Xway, Yway - 1)
       if (valLeft < 105 or  valRight < 105 or valUp < 105 or valDown < 105):
           perimeter.append((Xway,Yway))
           ToRight = 0
           ToLeft = 0
           ToDown = 0
           ToUp = 0
           if(valLeft > 105 and FromLeft==0):
               ToLeft = -1
               FromRight=1
               Xway=Xway + ToLeft
               continue
           if(valRight > 105 and FromRight==0):
                ToRight = 1
                FromLeft=1
                Xway = Xway + ToRight
                continue
           if(valUp > 105 and FromUp==0):
                ToUp = 1
                FromDown=1
                Yway = Yway + ToUp
                continue
           if(valDown > 105 and FromDown==0):
                ToDown = -1
                FromUp=1
                Yway = Yway + ToDown
                continu

perimeter = []
UP   =  1
DOWN = -1
LEFT = -1
RIGHT=  1

def snowflack(x,y,TwospotsCF ):
    Whitespot=40
    Xway = x
    Yway = y
    if(Xway + 1<Xsize and Yway + 1<Ysize ):
        valLeft,f,u = MyImage[Xway - 1, Yway    ]
        valRight,f,u= MyImage[Xway + 1, Yway    ]
        valUp,f,u   = MyImage[Xway    , Yway + 1]
        valDown,f,u = MyImage[Xway    , Yway - 1]
    else:
        valLeft,f,u = 255
        valRight,f,u = 255
        valUp,f,u = 255
        valDown,f,u = 255
    Oneblackspot    = 'NO'
    Twoblackspot    = 'NO'
    Threeblackspots = 'NO'
    Noblackspots    = 'NO'
    if((valLeft  < Whitespot) and (valUp   >Whitespot and valRight >Whitespot and valDown  >Whitespot)): Oneblackspot='1L'
    if((valUp    < Whitespot) and (valLeft >Whitespot and valRight >Whitespot and valDown  >Whitespot)): Oneblackspot='1U'
    if((valRight < Whitespot) and (valLeft >Whitespot and valUp    >Whitespot and valDown  >Whitespot)): Oneblackspot='1R'
    if((valDown  < Whitespot) and (valLeft >Whitespot and valUp    >Whitespot and valRight >Whitespot)): Oneblackspot='1D'

    if((valLeft  < Whitespot and valUp   < Whitespot) and (valRight > Whitespot and valDown > Whitespot)): Twoblackspot='LU'
    if((valRight < Whitespot and valUp   < Whitespot) and (valLeft  > Whitespot and valDown > Whitespot)): Twoblackspot= 'UR'
    if((valLeft  < Whitespot and valDown < Whitespot) and (valRight > Whitespot and valUp   > Whitespot)): Twoblackspot='DL'
    if((valRight < Whitespot and valDown < Whitespot) and (valLeft  > Whitespot and valUp   > Whitespot)): Twoblackspot='RD'

    if((valLeft  < Whitespot and valUp    < Whitespot and valRight < Whitespot) and (valDown  > Whitespot)): Threeblackspots='3D'
    if((valUp    < Whitespot and valRight < Whitespot and valDown  < Whitespot) and (valLeft  > Whitespot)): Threeblackspots='3L'
    if((valRight < Whitespot and valDown  < Whitespot and valLeft  < Whitespot) and (valUp    > Whitespot)): Threeblackspots='3U'
    if((valDown  < Whitespot and valLeft  < Whitespot and valUp    < Whitespot) and (valRight > Whitespot)): Threeblackspots='3R'

    if( TwospotsCF !='NO' and
       (valLeft  > Whitespot and valUp  > Whitespot and valRight  > Whitespot and valDown > Whitespot)):
        Noblackspots='C2'
    if( TwospotsCF =='NO' and
       (valLeft  > Whitespot and valUp  > Whitespot and valRight  > Whitespot and valDown  > Whitespot)):Noblackspots='C1'

    if(Oneblackspot     != 'NO'): return Oneblackspot
    if(Twoblackspot     != 'NO'): return Twoblackspot
    if(Threeblackspots  != 'NO'): return Threeblackspots
    if(Noblackspots     != 'NO'): return Noblackspots

def MarkAndGo(x,y,CameFrom,TwospotsCF):
    Xway = x
    Yway = y
    ComeFrom='NO'
    Checksnowflack=snowflack(Xway,Yway,TwospotsCF)
    if(Checksnowflack == '1L' or Checksnowflack == '1R' ):
        perimeter.append((Xway,Yway))
        if(CameFrom == 'UP'):
            Yway= Yway + DOWN
            ComeFrom='UP'
        if (CameFrom == 'DOWN'):
            Yway = Yway + UP
            ComeFrom = 'DOWN'
    if(Checksnowflack == '1U' or Checksnowflack == '1D' ):
        perimeter.append((Xway, Yway))
        if (CameFrom == 'RIGHT'):
            Xway = Xway + LEFT
            ComeFrom = 'RIGHT'
        if (CameFrom == 'LEFT'):
            Xway = Xway + RIGHT
            ComeFrom = 'LEFT'
    if(Checksnowflack == 'LU'):
        perimeter.append((Xway, Yway))
        if (CameFrom == 'RIGHT'):
            Yway = Yway + DOWN
            ComeFrom = 'UP'
        if (CameFrom == 'DOWN'):
            Xway = Xway + RIGHT
            ComeFrom = 'LEFT'
        TwospotsCF='LU'
    if(Checksnowflack == 'UR'):
        perimeter.append((Xway, Yway))
        if (CameFrom == 'LEFT'):
            Yway = Yway + DOWN
            ComeFrom = 'UP'
        if (CameFrom == 'DOWN'):
            Xway = Xway + LEFT
            ComeFrom = 'RIGHT'
        TwospotsCF = 'UR'
    if(Checksnowflack == 'RD'):
        perimeter.append((Xway, Yway))
        if (CameFrom == 'UP'):
            Xway = Xway + LEFT
            ComeFrom = 'RIGHT'
        if (CameFrom == 'LEFT'):
            Yway = Yway + UP
            ComeFrom = 'DOWN'
        TwospotsCF = 'RD'
    if(Checksnowflack == 'DL'):
        perimeter.append((Xway, Yway))
        if (CameFrom == 'UP'):
            Xway = Xway + RIGHT
            ComeFrom = 'LEFT'
        if (CameFrom == 'RIGHT'):
            Yway = Yway + UP
            ComeFrom = 'DOWN'
        TwospotsCF = 'DL'
    if(Checksnowflack == '3L'):
        Xway=Xway+LEFT #should mark pixel as black
        ComeFrom = 'RIGHT'
        perimeter.append((Xway, Yway))
    if(Checksnowflack == '3U'):
        Yway = Yway + UP  # should mark pixel as black
        ComeFrom = 'DOWN'
        perimeter.append((Xway, Yway))
    if(Checksnowflack == '3R'):
        Xway = Xway + RIGHT  # should mark pixel as black
        ComeFrom = 'LEFT'
        perimeter.append((Xway, Yway))
    if(Checksnowflack == '3D'):
        Yway = Yway + DOWN  # should mark pixel as black
        ComeFrom = 'UP'
        perimeter.append((Xway, Yway))
    if(Checksnowflack == 'C1'):
        #suppose to come back by its own but i still dont know
        'x' is 'x'
    if(Checksnowflack == 'C2'):
        perimeter.append((Xway, Yway))
        if(TwospotsCF == 'LU' and CameFrom == 'LEFT'):
            Yway = Yway + UP
            ComeFrom = 'DOWN'
        if(TwospotsCF == 'LU' and CameFrom == 'UP'):
            Xway = Xway + LEFT
            ComeFrom = 'RIGHT'
        if(TwospotsCF == 'UR' and CameFrom == 'UP'):
            Xway = Xway + RIGHT
            ComeFrom = 'LEFT'
        if(TwospotsCF == 'UR' and CameFrom == 'RIGHT'):
            Yway = Yway + UP
            ComeFrom = 'DOWN'
        if(TwospotsCF == 'RD' and CameFrom == 'RIGHT'):
            Yway = Yway + DOWN
            ComeFrom = 'UP'
        if(TwospotsCF == 'RD' and CameFrom == 'DOWN'):
            Xway = Xway + RIGHT
            ComeFrom = 'LEFT'
        if (TwospotsCF == 'DL' and CameFrom == 'DOWN'):
            Xway = Xway + LEFT
            ComeFrom = 'RIGHT'
        if (TwospotsCF == 'DL' and CameFrom == 'LEFT'):
            Yway = Yway + DOWN
            ComeFrom = 'UP'
        TwospotsCF = 'NO'
    return (Xway,Yway,ComeFrom,TwospotsCF)
'''
def towhare(x,y):
    Checksnowflack = snowflack(x, y, 'R')
    if(Checksnowflack=='C2'):
        return'DOWN'
        '''
def start(x,y):
    xgo=x
    ygo=y
    towhare='DOWN'
    TwospotsCF='NO'
    for i in range (0,1000):
        xgo, ygo, towhare,TwospotsCF=MarkAndGo(xgo,ygo,towhare,TwospotsCF)

def nextAtom():
    findMaxX=perimeter
    size=len(perimeter)
    next=0
    for i in range(0,size-1):
        x,y=findMaxX[i]
        if(x>=next):
            next=x
    return next

def nextLine():
    findMinY = perimeter
    size = len(perimeter)
    next = Ysize
    for i in range(0, size - 1):
        x, y = findMinY[i]
        if (y <= next):
            next = y
    return next
def search(x,y):
    for Y in range(y -1, 1, -1):
        for X in range(x, Xsize):
            for CheckY in range(Y,Y-15,-1):
                val, f, u = MyImage[X,CheckY]
                if(val > 105):
                    if((X,CheckY) in perimeter):
                          continue
                    else:
                        perimeter.clear()
                        return (X,CheckY)



image = Image.open("test_detect.jpg")
MyImage = image.load()
Xsize, Ysize = image.size
x,y = search(0,Ysize)
start(x,y)
count=len(perimeter)
newImg = Image.new('L', (Xsize, Ysize))
for i in range (0,count):
    newImg.putpixel(perimeter[i],255)
newImg.save("new.jpg")
nextY = Ysize
for j in range(0,40):
    if(j==28):
       print("v")
    nextX=nextAtom()
    if (nextX >= Xsize - 20):
        nextY=nextLine()
        nextX=0
    x,y=search(nextX,nextY)
    start(x,y)
    count = len(perimeter)
    newImg = Image.open('new.jpg')
    for i in range(0, count):
        newImg.putpixel(perimeter[i], 255)
    newImg.save("new.jpg")

print("end")







