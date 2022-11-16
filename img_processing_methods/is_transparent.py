# from PIL import Image
# im = Image.open("assets/tc4.png")
# print(im.mode)  # RGB
# print(im.info)
from PIL import Image

def has_transparency(im):
    if im.info.get("transparency", None) is not None:
        return True
    if im.mode == "P":
        transparent = im.info.get("transparency", -1)
        for _, index in im.getcolors():
            if index == transparent:
                return True
    elif im.mode == "RGBA":
        extrema = im.getextrema()
        if extrema[3][0] < 255:
            return True

    return False

