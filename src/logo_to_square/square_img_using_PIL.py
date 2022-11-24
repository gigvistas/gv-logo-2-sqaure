from PIL import Image
from logo_to_square.img_processing_methods.transparent_ops import has_transparency,transparent_to_square
from logo_to_square.img_processing_methods.common_ops import resize_method
from logo_to_square.img_processing_methods.opaque_ops import get_bg_color,expand_to_square
from logo_to_square.img_processing_methods.getdominantcolor import ColorThief


def squareify(img_path,target_size, out_path,filename):
    target_size = target_size if target_size is not None else 200 
    img = Image.open(img_path)
    img=resize_method(img, target_size) #resize original image to 400 * lower dimension - maintaining aspect ratio
   
    if has_transparency(img):
        color_thief = ColorThief(img_path)
        
        # get the dominant color
        # param quality: quality settings 1 to 10 
        # 1 is the highest quality, the biggerthe number, 
        # the faster a color will be returned but the greater 
        # the likelihood that it will not be accuratex

        dominant_color = color_thief.get_color(quality=10)
        if dominant_color >(150,150,150):
            img=img.convert('RGBA')
            im_new = transparent_to_square(img,(0,0,0))
            im_new.save(out_path+'/'+filename+'_square.webp',quality=95)

        else:
            img=img.convert('RGBA')
            im_new =transparent_to_square(img,(255,255,255))
            im_new.save(out_path+'/'+filename+'_square.webp', quality=95)

    else:
        if img.mode != 'RGB':
            img=img.convert('RGB')
        bg_color = get_bg_color(img)
        im_new = expand_to_square(img, bg_color)
        newsize = (target_size, target_size)
        im_new = im_new.resize(newsize)
        im_new.save(out_path+'/'+filename+'_square.webp', quality=95)

def main(in_img_path, target_size, out_img_name,filename):
    print("Squarefiying logo ")
    squareify(in_img_path, target_size, out_img_name,filename)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    parser.add_argument('--in_path', metavar='path', required=True,
                        help='the path to input image')
    parser.add_argument('--target_size', metavar='path', required=True,
                        help='target size of output')
    parser.add_argument('--out_path', metavar='path', required=True,
                        help='output file name')
    parser.add_argument('--out_file_name', metavar='path', required=True,
                        help='output file name')                        
    args = parser.parse_args()
    main(in_img_path=args.in_path, target_size=args.target_size, out_img_name=args.out_path, filename=args.out_file_name)