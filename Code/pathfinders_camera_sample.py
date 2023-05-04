#Camera Sample Script
#Sean's Camera Sample Script
#5/2/2023

#About:
#This script shows how to collect a single potograph using jetcam library
#Learning how to use python to control the jetracer

#import required libraries
import os, time 
from uuid import uuid1 #this library is used to generate unique file names
from jetcam.csi_camera import CSICamera #Use this to control the csi camera
from jetcam.utils import bgr8_to_jpeg

# Employing OOP
camera = CSICamera(width=224, height=224)
time.sleep(5)

#Collect an image and modify it  so that it may save as a .jpg file
#Note: When using the CSIcamera module, collected images are of type numpy.array 
image = camera.read()
image = bgr8_to_jpeg(image)

#Create a new unique filename to save the file in the new directory.
uuid = '%s' % (uuid1()) #creates a unique string of characters
directory = os.getcwd();
image_path = os.path.join(directory, 'sample_image_' + uuid + '.jpg')

#Saving the image to file
with open (image_path, 'wb') as f:
    f.write(image)

print('New File Created: \n')
print(image_path)


#Shutdown camera and release resources
camera.running = False