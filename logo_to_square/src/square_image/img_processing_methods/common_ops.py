from PIL import Image

def resize_method(img): #resizes the image by maintaing the aspect ratio
    width,height=img.size

    if width == height:
        return img
    
    elif  height > width :
            width=int((width/height) *400)
            height = 400
            img=img.resize((width,height),Image.BILINEAR)
            return img
    else:
            height=int((height/width) *400)
            width =400
            img =img.resize((width,height),Image.BILINEAR)
    return img





                      
           
           
           