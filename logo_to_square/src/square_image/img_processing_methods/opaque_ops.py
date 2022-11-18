from PIL import Image

def get_bg_color(im): # gets the background colour of the and rgb image 
    px = im.load()
    width, height = im.size
    
    # get colors at 5px at 4 corners
    top_left = px[4,4]
    
    top_right = px[width-6,4]
    
    bottom_left = px[4,height-6]
    bottom_right = px[width-6,height-6]

    avg_color = get_avg_color(top_left, top_right, bottom_left, bottom_right)
    return avg_color

def get_avg_color(tl, tr, bl, br): # calcluates the average value of "rgb" of the corner pixels
    sum_of_all = [sum(tup) for tup in zip(tl, tr, bl, br)]
    avg_rgb = tuple(item // 4 for item in sum_of_all)
    return avg_rgb


def expand_to_square(img, background_color): #converts an image to sqaure
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
