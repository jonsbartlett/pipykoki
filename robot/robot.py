from vision import *

class Robot:
    'A robot object which contains lists of the available parts'
    def __init__(self):
        self.cam = Vision()
        
    def see(self, (x,y) = (800,600), preview = False, preview_time = 1):
        return self.cam.vision_see((x,y), preview, preview_time)
    

    
