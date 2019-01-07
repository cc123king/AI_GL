from PIL import ImageDraw,ImageFont,Image,ImageFilter
import random
def zm_sz():
    i =random.randint(1,3)
    if i == 1:
        return chr(random.randint(48,57))
    elif i==2:
        return chr(random.randint(65,90))
    else:
        return chr(random.randint(97,122))




def randcolor():
    return (random.randint(127,255),random.randint(127,255),random.randint(127,255))

def randcolor2():
    return (random.randint(0,127),random.randint(0,127),random.randint(0,127))

def dr():
    width=30*4
    height=30
    image=Image.new('RGB',(width,height),(255,255,255))
    font=ImageFont.truetype('DejaVuSans.ttf',18)
    draw=ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=randcolor())

    l = []
    for t in range(4):

        item=zm_sz()
        l.append(item)
        draw.text((30*t+8,8),item,font=font,fill=randcolor2())

    image=image.filter(ImageFilter.DETAIL)
    image.save('/home/king/PycharmProjects/AI_gl/static/picture/yzm.jpg','jpeg')
    return l




if __name__=='__main__':
    l=dr()