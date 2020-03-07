from pytube import YouTube
# misc
import os
import shutil
import math
import datetime
# plots
import matplotlib.pyplot as plt

# image operation
import cv2
from definitions_youtube_download import ROOT_DIR_ONE_UP


video = YouTube('https://www.youtube.com/watch?v=NqC_1GuY3dw')
video.streams.filter(file_extension = "mp4").all()
video.streams.get_by_itag(18).download()
