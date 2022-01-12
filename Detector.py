import numpy as np
import cv2
from imutils.video import FPS


class Detector:
    def __init__(self, args):
        self._face_model = cv2.dnn.readNetFromCaffe(
            "models/res10_300x300_ssd_iter_140000.prototxt",
            caffeModel="models/res10_300x300_ssd_iter_140000.caffemodel",
        )
        self._args = args
        self._writer = None

    def run(self):
        image_path = self._args["image"]
        video_path = self._args["video"]
        if str(self._args["camera"]) == "true":
            camera = True
        else:
            camera = False

        if str(self._args["GPU"]) == "true":
            print("true")
            self._face_model.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            self._face_model.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        if self._args["output"] is not None and image_path is None:
            self._writer = cv2.VideoWriter(
                self._args["output"],
                cv2.VideoWriter_fourcc(*"MJPG"),
                10,
                (600, 600),
            )
        if camera:
            print("[INFO] Opening Web Cam.")
            self._processCamera()
        elif video_path is not None:
            print("[INFO] Opening Video from path.")
            self._processVideo(video_path)
        elif image_path is not None:
            print("[INFO] Opening Image from path.")
            self._processImage(image_path, self._args["output"])

    def _processImage(self, imgName, output_path):
        self._img = cv2.imread(imgName)
        (self._height, self._width) = self._img.shape[:2]

        self._processFrame()
        if output_path is not None:
            cv2.imwrite(output_path, self._img)

        cv2.imshow("Output", self._img)
        cv2.waitKey(0)

    def _processVideo(self, videoName):
        cap = cv2.VideoCapture(videoName)
        if cap.isOpened() == False:
            print("Error opening video...")
            return
        (sucess, self._img) = cap.read()
        (self._height, self._width) = self._img.shape[:2]

        fps = FPS().start()

        while sucess:
            self._processFrame()
            self._save()
            cv2.imshow("Output", self._img)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            fps.update()
            (sucess, self._img) = cap.read()

        fps.stop()
        print("Elapsed time: {:.2f}".format(fps.elapsed()))
        print("FPS: {:.2f}".format(fps.fps()))

        cap.release()
        cv2.destroyAllWindows()

    def _processCamera(self):
        video = cv2.VideoCapture(0)
        print("Detecting people...")
        self._width = 800
        self._height = 800

        fps = FPS().start()

        while True:
            check, self._img = video.read()
            self._processFrame()
            self._save()
            cv2.imshow("Output", self._img)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            fps.update()

        fps.stop()
        print("Elapsed time: {:.2f}".format(fps.elapsed()))
        print("FPS: {:.2f}".format(fps.fps()))

    def _processFrame(self):
        blob = cv2.dnn.blobFromImage(
            self._img,
            1.0,
            (300, 300),
            (104.0, 177.0, 123.0),
            swapRB=False,
            crop=False,
        )

        self._face_model.setInput(blob)
        prediction = self._face_model.forward()

        for i in range(0, prediction.shape[2]):
            if prediction[0, 0, i, 2] > 0.5:
                bbox = prediction[0, 0, i, 3:7] * np.array(
                    [self._width, self._height, self._width, self._height]
                )
                (xmin, ymin, xmax, ymax) = bbox.astype("int")
                cv2.rectangle(
                    self._img, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2
                )

    def _save(self):
        if self._writer is not None:
            self._writer.write(self._img)
