import time

class frames:
    
    def dogFrameUpdater():
        Frames = len(dogFrames)
        dogFrames = ["Assets/Dog graphics/Dog1.gif",
                     "Assets/Dog graphics/Dog2.gif",
                     "Assets/Dog graphics/Dog3.gif",
                     "Assets/Dog graphics/Dog4.gif"]
            Frames = Frames + 1
            if (Frames == 5):
                Frames = 0
