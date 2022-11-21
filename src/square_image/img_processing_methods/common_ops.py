from PIL import Image

def resize_method(img, target_size): #resizes the image by maintaing the aspect ratio
    width,height=img.size
    if width == height:
        return img
    
    elif  height > width :
            width=int((width/height) *target_size)
            height = target_size
            img=img.resize((width,height),Image.BILINEAR)
            return img
    else:
            height=int((height/width) *target_size)
            width =target_size
            img =img.resize((width,height),Image.BILINEAR)
    return img




                      
           
           
           