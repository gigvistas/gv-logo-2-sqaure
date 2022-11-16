from PIL import Image
from colorthief import ColorThief
from img_processing_methods.method_padding import expand2square, transparentToSquare
from img_processing_methods.is_transparent import has_transparency
from img_processing_methods.resize_ar import resize_method
from img_processing_methods.get_bg import get_bg_color



def squareify(img_path,filename):
    img = Image.open(img_path)
    img=resize_method(img) #resize original image to 400 * lower dimension - maintaining aspect ratio
   
    if has_transparency(img):
        color_thief = ColorThief(img_path)
        
        # get the dominant color
        # param quality: quality settings 1 to 10 
        # 1 is the highest quality, the biggerthe number, 
        # the faster a color will be returned but the greater 
        # the likelihood that it will not be accurate

        dominant_color = color_thief.get_color(quality=10)
        if dominant_color >(150,150,150):
            img=img.convert('RGBA')
            im_new = transparentToSquare(img,(0,0,0))
            im_new.save('assets/'+filename+'_square.webp',quality=95)

        else:
            img=img.convert('RGBA')
            im_new =transparentToSquare(img,(255,255,255))
            im_new.save('assets/'+filename+'_square.webp', quality=95)

    else:
        if img.mode != 'RGB':
            img=img.convert('RGB')
        bg_color = get_bg_color(img)
        im_new = expand2square(img, bg_color)
        newsize = (400, 400)
        im_new = im_new.resize(newsize)
        im_new.save('assets/'+filename+'_square.webp', quality=95)
      

squareify('assets/tc29.jpg','tc27.jpg')


