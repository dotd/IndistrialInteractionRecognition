from definitions_youtube_download import ROOT_DIR
from youtube_download.tools.FrameExtractor import FrameExtractor
from dot_utils.files.FileUtils import get_files_in_folder


def extract_frames(path=f"{ROOT_DIR}/movies/", frames_limit = 10, files_limit=1):
    # get the files
    files = get_files_in_folder(path, "mp4")
    frames_counter = 0
    files_counter = 0
    for file in files:
        frame_extractor = FrameExtractor(f"{file}")
        length = frame_extractor.get_video_duration()
        print(f"{file} len={length}")
        frame_extractor.get_n_images(every_x_frame=1000)
        frame_extractor.extract_frames(every_x_frame=1000, img_name='frame', dest_path=f"{ROOT_DIR}/frames/")


if __name__ == "__main__":
    extract_frames()