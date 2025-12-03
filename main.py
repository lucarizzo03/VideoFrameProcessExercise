
# input
frames = [
    {'timestamp': 0.0, 'width': 1920, 'height': 1080, 'brightness': 120},
    {'timestamp': 0.5, 'width': 1920, 'height': 1080, 'brightness': 45},   # too dark
    {'timestamp': 1.0, 'width': 1920, 'height': 1080, 'brightness': 125},
    {'timestamp': 1.5, 'width': 1920, 'height': 1080, 'brightness': 180},  # scene change
    {'timestamp': 2.0, 'width': 1920, 'height': 1080, 'brightness': 175},
]



def analyzeFrame(frames):
    
    # filter out frames < 50
    validFrames = []
    for f in frames:
        if f["brightness"] >= 50:
            validFrames.append(f)
              
    # edge case
    if len(validFrames) == 0:
        return "no valid frames"
            
    # identify scene changes (brightness diff > 40)
    sceneChanges = []
    for i in range(1, len(validFrames)):
        if abs(validFrames[i - 1]["brightness"] - validFrames[i]["brightness"] > 40):
            sceneChanges.append(validFrames[i]["timestamp"])
            
    return {
        "valid frame count": len(validFrames),
        "scene changes": sceneChanges
    }
        
        
        
if __name__ == "__main__":
    result = analyzeFrame(frames)
    print(result)
    