
from PIL import Image

def has_transparency(im): # checks for transparency in an image
    if im.mode == "P":
        if im.info.get("transparency", None) is not None:
          return True
        transparent = im.info.get("transparency", -1)
        for _, index in im.getcolors():
            if index == transparent:
                return True
    elif im.mode == "RGBA":
        extrema = im.getextrema()
        if extrema[3][0] < 255:
            return True

    return False

def transparent_to_square(img, background_color): #converts a transparent bg image into square
    
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
