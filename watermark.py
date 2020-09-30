#####################################################
# watermark.py is an automatic watermarking script that takes in user input for a logo file, a directory of images to watermark
# and a directory to save watermark. It adds the logo to every image file in the input directory, saving them the watermarked
# images to the output directory. User can also change watermark position, opacity, and size.
#
# Created by: Rene Nagy
#####################################################


import os
import sys
import atexit
import ntpath

import PIL
from PIL import Image

#These are the extentions the script looks for when finding all images within a folder. For less common image formats, append the extention here
EXTS = ('.jpg', '.png', '.jfif')

#Default values here can be changed and will update throughtout the rest of the script
posDefault = 'bottomright'
opacityDefault = 255
sizeModifierDefault = 0.15


# resizeLogo takes in an image and resizes it to a fraction of the width of another image. The size is specified by sizeModifier. 
# The aspect ratio is maintained, so when width changes height is adjusted accordingly to keep the same aspect ratio and avoid distortion

### Code Found at https://gist.github.com/tomvon/ae288482869b495201a0 ###
def resizeLogo (logo):
    
    newWidth = int(imageWidth * sizeModifier)
    
    if newWidth > logo.size[0]:
      scalePercent = (newWidth / float(logo.size[0]))
      newHeight = int((float(logo.size[1]) * float(scalePercent)))
      logo = logo.resize((newWidth, newHeight), PIL.Image.ANTIALIAS)
    
    else:
      logoWidth = logo.size[0]
      logoHeight = logo.size[1]
      
      logo.thumbnail((imageWidth * sizeModifier, float('inf')))
      
      
      
    return(logo)
  

# setLogoOpacity changes all pixel's alpha values that are not already transparent to the that of the "opacity" variable (from default value or user input).     
def setLogoOpacity (logo):
    oldLogoPixels = logo.getdata()
    opacityLogoPixels = []
    
    if(lgo.lower().endswith('.jpg')):
        tempLogoPixels = []
        for pixel in oldLogoPixels:
            if (pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255):
                opacityLogoPixels.append((255, 255, 255, 0))
            else:
                opacityLogoPixels.append((pixel[0], pixel[1], pixel[2], opacity))
                
                
    else:    
      for pixel in oldLogoPixels:
          if pixel[3] == 0:
              opacityLogoPixels.append((255, 255, 255, 0))
          else:
              opacityLogoPixels.append((pixel[0], pixel[1], pixel[2], opacity))
        
    logo.putdata(opacityLogoPixels)
        
    return(logo)
    
    
# createLogoLayer takes the logo and pastes it on a new transparent image witht the same size as the image to be watermarked. 
# This is done in order to make the watermark and the image to be watermarked have the same size, so that the alpha composite function can be used.
# The location on which the logo is pasted depends on the "pos" variable (changed via user input or a default parameter)

### Adapted from code in watermark.py Github repo by theitrain ###
def createLogoLayer (logo, imageWidth, imageHeight):
    background = Image.new('RGBA', (imageWidth, imageHeight), (0,0,0,0))
        
    logoWidth = logo.size[0]
    logoHeight = logo.size[1]
    
    if pos == 'topleft':
        image.paste(logo, (0, 0), logo)
    elif pos == 'topright':
        image.paste(logo, (imageWidth - logoWidth, 0), logo)
    elif pos == 'bottomleft':
        image.paste(logo, (0, imageHeight - logoHeight), logo)
    elif pos == 'center':
        image.paste(logo, ((imageWidth - logoWidth)/2, (imageHeight - logoHeight)/2), logo)
    else:
        image.paste(logo, (imageWidth - logoWidth, imageHeight - logoHeight), logo)
    
    return(background)
    



# getListOfFiles takes in a directory and returns a list of all files in that directory and all subfolders in it
    
### code found at https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/ ###
def getListOfFiles(inputPath):
    listOfFiles = os.listdir(inputPath)
    allFiles = list()
    
    for entry in listOfFiles:
        fullPath = os.path.join(inputPath, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    
    return (allFiles)
    

############ Main Code Starts Here ############


atexit.register(raw_input, 'Press enter key to continue')


#If run without command line arguments, the script will take in user input
print('\nWelcome to the auto-watermark script!')
custom = raw_input('Press enter to continue with default settings. Type "custom" to change watermark location, opacity, and size: ')

    
if (custom.lower() == 'custom'):
    lgo = raw_input("\nEnter logo image file path: ")
    inputPath = raw_input("\nEnter file path of folder with images to watermark: ")
    watermarkSubfolders = raw_input('\nWould you like to watermark images in subfolders of the chosen folder?\nPress enter to watermark only images in the folder you entered. Type "yes" to watermark images in subfolders ')
    outputPath = raw_input("\nEnter file path of folder to save images \n(if this is chosen to be the same folder as the input folder, existing images will be overwritten!): ")
    
    
    pos = raw_input("\nSelect position to put watermark. Default position is " + str(posDefault) +  "\nEnter one of the following positions: topright, topleft, bottomright, bottomleft, center: ")  
        
    if (pos != 'topleft' and pos != 'topright' and pos != 'bottomleft' and pos != 'bottomright' and pos != 'center'):
        print('Invalid entry for position')
        sys.exit()
        
    opacity = int(raw_input("\nEnter integer between 0 and 255 to select opacity. The default value is " + str(opacityDefault) + ".\n0 is totally transparent, 255 is totally opaque: "))
        
    if(opacity > 255 or opacity < 0):
        print('Invalid value for opacity. Must be an integer from 0-255')
        sys.exit()
        
    sizeModifier = float(raw_input("\nEnter decimal between 0.0 and 1.0 to change size. The default value is " + str(sizeModifierDefault) + ".\n0.5 will create a watermark with half the width of the image it is applied to. 0.25 will create a watermark with one quarter the width of the image, and so on.\nEnter size modifer: "))
       
    if(sizeModifier > 1.0 or sizeModifier < 0):
        print('Invalid value for sizeModifer. Must be a float between 0.0 and 1.0')
        sys.exit()
            
else:
    lgo = raw_input("\nEnter logo image file path: ")
    inputPath = raw_input("\nEnter file path of folder with images to watermark: ")
    watermarkSubfolders = raw_input('\nWould you like to watermark images in subfolders of the chosen folder?\nPress enter to watermark only images in the folder you entered. Type "yes" to watermark images in subfolders ')
    outputPath = raw_input("\nEnter file path of folder to save images \n(if this is chosen to be the same folder as the input folder, existing images will be overwritten!): ")
    pos = posDefault
    opacity = opacityDefault
    sizeModifier = sizeModifierDefault
        



#Now that all user inputs are entered, the script finds all image files in the given input directory and watermarks them.
#Also watermarks images in all subfolders, if specified to do so.

if (watermarkSubfolders != 'yes'):
    for fileName in os.listdir(inputPath):
        if any([fileName.lower().endswith(ext) for ext in EXTS]) and fileName != lgo:
            image = Image.open(inputPath + '/' + fileName)
            image = image.convert('RGBA')
            imageWidth = image.size[0]
            imageHeight = image.size[1]
            
            logo = Image.open(lgo)
            logo = logo.convert('RGBA')
            
            logo = resizeLogo(logo)
            logo = setLogoOpacity(logo)
            logo_layer = createLogoLayer(logo, imageWidth, imageHeight)
            
            outputImage = Image.alpha_composite(image, logo_layer)
            
            if(fileName.lower().endswith('.jpg') or fileName.lower().endswith('.jfif')):
                outputImage = outputImage.convert('RGB')
            
            
            outputImage.save(outputPath + '/' + fileName) # If you want to add a prefix to saved images, simply add it here after the slash
            print('Added watermark to ' + inputPath + '/' + fileName)
            
else:
    allFiles = getListOfFiles(inputPath)
    for filePath in allFiles:
        if any([filePath.lower().endswith(ext) for ext in EXTS]) and filePath != lgo:
            
            head, tail = ntpath.split(filePath)
            fileName = tail or ntpath.basename(head)
            
            image = Image.open(filePath)
            
            image = image.convert('RGBA')
            imageWidth = image.size[0]
            imageHeight = image.size[1]
            
            logo = Image.open(lgo)
            logo = logo.convert('RGBA')
            
            logo = resizeLogo(logo)
            logo = setLogoOpacity(logo)
            logo_layer = createLogoLayer(logo, imageWidth, imageHeight)
            
            outputImage = Image.alpha_composite(image, logo_layer)
            
            if(fileName.lower().endswith('.jpg') or fileName.lower().endswith('.jfif')):
                outputImage = outputImage.convert('RGB')
            
            
            outputImage.save(outputPath + '/' + fileName) # If you want to add a prefix to saved images, simply add it here after the slash
            print('Added watermark to ' + filePath)
            

print('\nWatermarked photos saved to ' + outputPath)

