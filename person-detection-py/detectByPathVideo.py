import cv2
import imutils
from detect import detect


def detectByPathVideo(path, writer):
    video = cv2.VideoCapture(path)
    check, frame = video.read()
    if check == False:
        print(
            "Video Not Found. Please Enter a Valid Path (Full path of Video Should be Provided)."
        )
        return
    print("Detecting people...")
    while video.isOpened():
        # check is True if reading was successful
        check, frame = video.read()
        if check:
            frame = imutils.resize(frame, width=min(800, frame.shape[1]))
            frame = detect(frame)

            if writer is not None:
                writer.write(frame)

            key = cv2.waitKey(1)
            if key == ord("q"):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()
