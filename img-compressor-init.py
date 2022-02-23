import os
import sys
import PIL
from PIL import Image


def printLongLine():
    print("----------------------------------------------------------------")
    

def createTmpFolder():
    pass

def compressImage(file_name):
    #open image
    try:
        full_path = f"{working_dir}/{file_name}"
        if c_config['verbose']:
            print(f"Compressing image in {full_path}")
            
        im = Image.open(full_path)
        compressed_filename = c_config['prefix_str']+file_name;
        file_path = f"{destination_dir}/{compressed_filename}"
        im.save(file_path, optimize=c_config['optimize'], quality=c_config['quality'])

        return file_path

    except Exception as e:
        raise e
        return None

def getDimesions(im):
    if c_config['verbose']:
        print(f"This is the current width and height of the image: {dim}")

    return im.size

def init():
    
    if 'h' in sys.argv:
        print(
            'usage: ' + script_name + ' [options] source dest' 
        )
        sys.exit()

    flag_set = ['--name-option' ]
    options_set = {
        'compress': True,
    }

    if not os.path.isdir(working_dir):
        print("Source directory doesnot exist")
        sys.exit()

    if not os.path.isdir(destination_dir) :
        print("Destination directory doesnot exist")
        sys.exit()

    for root, dirs, files in os.walk(working_dir, topdown=False):
    
        print(f"root={root}")
        print(f"{files}")

        for name in files:
            name_ext = os.path.splitext(name)
            _extension = name_ext[1]
            _name = name_ext[0]
            _full_path = os.path.join(root, name)

            if _extension in allowed_exts:
                #compress image
                compressed_im = compressImage(name)

                if compressed_im :
                    compressed_imgs.append(compressed_im)

        print("C", compressed_imgs)


if __name__ == '__main__':

    printLongLine()
  
    allowed_exts = ['.png','.jpeg','.jpg','.gif']
    script_name = sys.argv[0]
    arglen = len(sys.argv)-1

    compressed_imgs=[]

    if arglen < 2:
        print("Parameters wasnt provided")
        sys.exit()

    #configutations
    c_config = {
        'prefix_str': "compressed_",
        'optimize': True,
        'quality': 30,
        'verbose': True
    }

    working_dir = sys.argv[1]
    destination_dir = sys.argv[2]

    init() # call main function

        


    
