from pytube import YouTube
from dot_utils.files.FileUtils import load_string
# misc
import os
import shutil
import math
import datetime
# plots
import matplotlib.pyplot as plt

# image operation
import cv2
from definitions_youtube_download import ROOT_DIR


def download_movie(url_str, output_path):
    video = YouTube(url_str)
    video.streams.filter(file_extension="mp4").all()
    video.streams.get_by_itag(18).download(output_path=output_path)


def download_movies(list_files=f"{ROOT_DIR}/list_manufacturing_movies.txt",
                    output_path=f"{ROOT_DIR}/movies/",
                    limit_files=1):
    urls = load_string(list_files).split("\n")
    urls = list(filter(lambda x:len(x) > 10, urls))
    urls = urls[:limit_files]
    print(urls)

    for url_idx, url in enumerate(urls):
        download_movie(url, output_path)


if __name__ == "__main__":
    download_movies()

