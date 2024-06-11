import cv2 as cv
import glob
import pickle
import os
from pathlib import Path

calibration_result_folder = "calibration_result"

cameraMatrix = pickle.load(open(calibration_result_folder + "/cameraMatrix.pkl", "rb" ))
dist = pickle.load(open(calibration_result_folder + "/dist.pkl", "rb"))

dist_folder = "test_dist_images"
if not os.path.exists(dist_folder):
    os.makedirs(dist_folder)

# Load test source images
images = glob.glob('./test_src_images/*.png')

for image in images:
    img = cv.imread(image)
    h, w = img.shape[:2]
    newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(cameraMatrix, dist, (w,h), 1, (w,h))

    # Undistort
    dst = cv.undistort(img, cameraMatrix, dist, None, newCameraMatrix)

    # crop the image
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    cv.imwrite(dist_folder + '/' + Path(image).stem + ".png", dst)
