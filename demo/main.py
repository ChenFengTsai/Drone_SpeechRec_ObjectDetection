from djitellopy import Tello
import sys
import os


from voice_detection import Voice_Detection
#from gesture_detection import Gesture_Detection
from yolov5.object_detection import Object_Tracking
import configparser



def main(drone, ip):
    # *voice detection to fly*
    vd = Voice_Detection(drone)
    vd.fly_drones_voice()
    print('voice detection done')
    
    # todo: gesture detection to trigger object detection
    #gd = Gesture_Detection(drone, ip)
    #gd.gesture_trigger()
    #print('done')
    
    # todo: object dection to find (bottle)
    ot = Object_Tracking(drone)
    ot.track_object()
    print('object tracking done')
    
    

if  __name__ == "__main__":
    config = configparser.ConfigParser()
    # Get the parent directory path
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    dir = os.path.join(parent_dir, '..','config.ini')
    config.read(dir)
    ip = config.get('wifi', 'ip')
    
    # initilize the drone
    drone = Tello(ip)
    drone.connect()
    drone.streamon()
    print(f"Battery life percentage: {drone.get_battery()}%")
    
    main(drone, ip)