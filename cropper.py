import os.path
from pathlib import Path
from PIL import Image

picture_extensions = ["jpg","jpeg","png","img","pdf"]

def main():
    picture_file = getPictureFile()
    width, height = getDimensions(picture_file)
    coordinates = getCropCoordinates(width, height)
    img = Image.open(picture_file)
    final_img = img.crop(tuple(coordinates))
    final_img.show()
    final_img.save("new_" + picture_file)

def getPictureFile():
    fileNameGotten = False
    while fileNameGotten == False:
        file_name = raw_input("What is the path of the file you would like to crop?\n")
        picture_file = Path(file_name)
        if picture_file.is_file():
            if file_name.split(".")[1].lower() in picture_extensions:
                return file_name
            else:
                print("%s is not a picture file, please try again." %file_name) #TOOD: loop over picture_extensions
        else:
            print("%s is not a file, please try again." %file_name)

def getDimensions(picture_file):
    with Image.open(picture_file) as img:
        return img.size

def getCropCoordinates(width, height):
    coordinates = [0] * 4
    coordinates[0] = getValidCoordinate(0, width-1, "X1")
    coordinates[1] = getValidCoordinate(0, height-1, "Y1")
    coordinates[2] = getValidCoordinate(coordinates[0]+1, width, "X2")
    coordinates[3] = getValidCoordinate(coordinates[1]+1, height, "Y2")
    return coordinates

def getValidCoordinate(min, max, cord):
    while True:
        coordinate = int(raw_input("Please enter in the %s coordinate from %d to %d\n" %(cord, min, max)))
        if coordinate < min or coordinate > max:
            print("The number entered is not between %d and %d\n" %min %max)
        else:
           return coordinate

if __name__ == '__main__':
    main()
