from PIL import Image

def expand2square(img, background_color):
    width, height = img.size
    if width == height:
        return img
    elif width > height:
        result = Image.new(img.mode, (width, width), background_color)
        result.paste(img, (0, (width - height) // 2))
        return result
    else:
            result = Image.new(img.mode, (height, height), background_color)
            result.paste(img, ((height - width) // 2, 0))
    return result

def transparentToSquare(img, background_color):
    width, height = img.size
    paste_coords = (0,0)
    square_width = width
    if width != height:
        img_orientation = 'landscape' if width > height else 'portrait'
        square_width = width if width > height else height
        lower_dim = width if width < height else height
        paste_coords = (0,(square_width - lower_dim)//2) if img_orientation == 'landscape' else ((square_width - lower_dim)//2,0)
    result = Image.new('RGBA', (square_width, square_width), background_color)
    result.paste(img,paste_coords,img)
    return result


                      
           
           
           