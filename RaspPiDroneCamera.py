#Raspberry Pi Camera Code

from picamera import PiCamera
from time import sleep
import os
import random

camera = PiCamera()
path = '/media/pi/USB/test_directory/raspvideos'


def test_camera(duration=5):
    camera.start_preview(alpha=200)
    sleep(duration)
    camera.stop_preview()

def camera_module(path_folder,video_name='test',duration=5,opacity=200):
    """Main module for Raspberry Pi Camera

    path_folder = route for saving videos
    duration = time between each video (500> may not function properly)
    opacity = change how much of the video/pi screen viewable """
    
    camera.start_preview(alpha=opacity)
    camera.start_recording(path_folder + '/' + video_name + '.h264')
    sleep(duration)
    camera.stop_recording()
    camera.stop_preview()

    ret_path = path_folder + '/' + video_name + '.h264'
    return ret_path

def create_new_folder(path_folder,title='folder'):
    """ Checks if folder exists, if it does, add a digit, else make a new folder

    title = name of the folder (default: 'folder')
    
    return[0] = path of folder
    return[1] = name of folder made
    return[2] = number of folder made""" 
    
    number = 0
    while os.path.exists(path_folder + '/' + title + str(number)):
        number += 1
        
    os.makedirs(path_folder + '/' + title + str(number))
    folder_path = path_folder + '/' + title + str(number)
    folder_name = title + str(number)
    
    return folder_path,folder_name,number


def create_new_video_name(path_folder,video_name='video',folder_title='folder'):
    """ Makes name for videos in specified folder

    video_name = set name for videos
    folder_title = same as title
    
    """
    number = 0
    
    while os.path.exists(path_folder + '/' + video_name + str(number) + '.h264'):
        #print("IT WORKS")
        number += 1
    #print("Video assumed to be: " + path_folder + '/' + video_name + str(number) + '.h264')
    
    return number,video_name




def main(vid_path,duration,opacity):
    """Executes whole camera process to be used for the
    flight camera

    vid_path = path directory to where the videos will be stored
    """
    #print("Sending video as:" + vid_path)
    vid_data = create_new_video_name(vid_path)
    camera_module(vid_path,vid_data[1]+str(vid_data[0]),duration,opacity)
    
    
#print(os.listdir(path))

    
video_path = create_new_folder(path)[0]

while True:
                           
    main(video_path,20,200)

    

    
