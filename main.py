import argparse
from detector import detector


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video-file', help='path to input video file. Example: input/needle.mp4', type=str,
                        default="input/needle2.mp4")
    parser.add_argument('--flag', help='boolean flag to save plots', type=str, default=False)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    for key, value in vars(args).items():
        print(f"{key}:{value}")

    '''
    Coordinates of the bounding box for precise location of the Gauge, predicted by assumed Gauge Detector Model
    are entered manually for illustration purposes. 
    PLEASE ENTER PROPER VALUES OF COORDINATES, IF TESTING ON A NEW FILE
    
    sample values:
     stable-needle2.mp4:    cropX1=340, cropY1=380, cropX2=530, cropY2=570
     stable-needle.mp4:     cropX1=180, cropY1=350, cropX2=350, cropY2=550
     needle.mp4 :           cropX1=1, cropY1=100, cropX2=900, cropY2=1000
     needle2.mp4:           cropX1=1, cropY1=42, cropX2=1180, cropY2=1290
    '''
    # d = detector(args.video_file, args.flag, cropX1=1, cropY1=100, cropX2=900, cropY2=1000)  # needle
    # d = detector(args.video_file, args.flag, cropX1=180, cropY1=350, cropX2=350, cropY2=550)  # stable-needle
    # d = detector(args.video_file, args.flag, cropX1=340, cropY1=380, cropX2=530, cropY2=570)  # stable-needle2

    d = detector(args.video_file, args.flag, cropX1=1, cropY1=42, cropX2=1180, cropY2=1290)  # needle2
    d.detect()
