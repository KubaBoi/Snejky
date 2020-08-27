import cv2
import numpy as np
import glob
from PIL import Image, ImageDraw

class MakeVideo:
    def recordFrame(self, frame, frameNumber, finalFrameNumber, fps):
        frame = Image.fromarray(frame)
        frameName = str(frameNumber)
        for i in range(0, 5 - len(str(frameNumber))):
            frameName = "0" + frameName

        frame.save("Snejky\\Video\\frames\\frame." + str(frameName) + ".png")
        print("SAVING FRAME: Snejky\\Video\\frames\\frame." + str(frameName) + ".png")
        if (frameNumber >= finalFrameNumber):
            self.makeVideo(fps)
            return False
        return True

    def makeVideo(self, fps):
        print("Making video from Snejky/Video/frames")

        img_array = []

        for filename in glob.glob('Snejky/Video/frames/*.png'):
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            break

        out = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

        for filename in glob.glob('Snejky/Video/frames/*.png'):
            img = cv2.imread(filename)
            out.write(img)
            """height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
            

            for i in range(len(img_array)):
                out.write(img_array[i])"""
        out.release()

#mk = MakeVideo()
#mk.makeVideo()