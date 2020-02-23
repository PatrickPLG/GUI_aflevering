import time

class frames:
    def dogFrameUpdater():
        gameRunning = True
        dogFrames = ["Assets/Dog graphics/Dog1.gif",
                     "Assets/Dog graphics/Dog2.gif",
                     "Assets/Dog graphics/Dog3.gif",
                     "Assets/Dog graphics/Dog4.gif"]
        Frames = len(dogFrames)
        while gameRunning == True:
            Frames = Frames + 1
            time.sleep(1)
            if (Frames == 5):
                Frames = 0
