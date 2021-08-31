import argparse
from PIL import Image, ImageDraw

output_file="output.png"

def get_dice(val,size):
    dice={1:"----x----",2:"x-------x",3:"x---x---x",4:"x-x---x-x",5:"x-x-x-x-x",6:"x-xx-xx-x"}

    val_normalized=max(round(12*(val/255)),1)   
    dot_size=size/8
    col="black" if val_normalized<=6 else "white"
    dot_col="white" if col=="black" else "black"
    val_normalized=val_normalized-6 if val_normalized>6 else val_normalized

    img=Image.new("RGB",(size,size),color=col)
    dots=ImageDraw.Draw(img)
    dots.rectangle((0,0,size,size),outline=dot_col)
    x=y=0

    for r in range(3):
        for c in range(3):
            if dice[val_normalized][r*3+c]=="x":
                # x
                if c==0:
                    x=size/5
                elif c==1:
                    x=size/2
                elif c==2:
                    x=size-size/5
                # y
                if r==0:
                    y=size/5
                elif r==1:
                    y=size/2
                elif r==2:
                    y=size-size/5

                dots.ellipse((x-dot_size/2,y-dot_size/2,x+dot_size,y+dot_size),fill=dot_col)
    
    return img

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Convert a picture into Dice")
    parser.add_argument("source", help="Source image file")
    parser.add_argument("-d", default="50", help="Dice size", metavar="DiceSize")
    parser.add_argument("-x", default="100", help="Maximum Width in Dice", metavar="MaxWidth")
    parser.add_argument("-y", default="100", help="Maximum Height in Dice", metavar="MaxHeight")
    args = vars(parser.parse_args())
    source_file=args["source"]
    dice_size=int(args["d"])
    max_width=int(args["x"])
    max_height=int(args["y"])

    img=Image.open(source_file).convert("L")
    img.thumbnail((max_width,max_height),Image.ANTIALIAS)

    img_new=Image.new("RGB",(img.width*dice_size,img.height*dice_size))

    for y in range(img.height):
        for x in range(img.width):
            img_new.paste(get_dice(img.getpixel((x,y)),dice_size),(x*dice_size, y*dice_size))


    img_new.save("output.png")
