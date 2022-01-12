import cv2
from detectByCamera import detectByCamera
from detectByPathVideo import detectByPathVideo
from detectByPathImage import detectByPathImage


def humanDetector(args):
    image_path = args["image"]
    video_path = args["video"]
    if str(args["camera"]) == "true":
        camera = True
    else:
        camera = False
    writer = None
    if args["output"] is not None and image_path is None:
        writer = cv2.VideoWriter(
            args["output"], cv2.VideoWriter_fourcc(*"MJPG"), 10, (600, 600)
        )
    if camera:
        print("[INFO] Opening Web Cam.")
        detectByCamera(writer)
    elif video_path is not None:
        print("[INFO] Opening Video from path.")
        detectByPathVideo(video_path, writer)
    elif image_path is not None:
        print("[INFO] Opening Image from path.")
        detectByPathImage(image_path, args["output"])
