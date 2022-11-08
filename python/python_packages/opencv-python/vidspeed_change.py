import cv2
import os
import argparse

"""
https://github.com/opencv/opencv-python
"""

def get_path(dir):
    """
    새로운 경로를 입력받았을 때 만약에 그 경로가 없다면 새로운 디렉토리를 만들어서 경로를 반환하는 함수
    """
    if not os.path.isdir(dir):
        os.mkdir(dir)
    return dir


# reduce video frame
def change_fps(original_path, save_path, rate):
    #새 dir 없으면 만들기
    get_path(save_path)

    # old dir 에서 영상 파일만 추리기
    video_paths = [f for f in os.listdir(original_path) if f.split('.')[-1] in ['mov','mp4','MOV','MP4','AVI','avi']]
    print(f"There are {len(video_paths)} videos.")
    
    for filename in video_paths:
        print(filename)
        old_vid = os.path.join(original_path, filename)
        new_vid = os.path.join(save_path, filename)

        video_capture = cv2.VideoCapture(old_vid)
        old_fps = int(video_capture.get(cv2.CAP_PROP_FPS))
        new_fps = round(old_fps*float(rate))
        frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        
        if not video_capture.isOpened():
            print("Video Capture cannot be opened.")
            return
        else:
            print(f"original fps : {old_fps}, new fps : {new_fps}, speed-changed rate : {rate}")
        video_codec = cv2.VideoWriter_fourcc(*'avc1')
        retval, video_frame = video_capture.read()
        if video_frame is not None:
            video_writer = cv2.VideoWriter(new_vid, video_codec, new_fps, (video_frame.shape[1], video_frame.shape[0]))
            frame_index = 0
            #print("frame_index is not None")

            while video_capture.isOpened():
                if frame_index == frame_count:
                    break
                retval, frame = video_capture.read()
                if not retval:
                    break
                video_writer.write(frame)
                frame_index += 1

            if video_writer.isOpened():
                video_writer.release()
            video_capture.release()
            print(f"speed-changed {filename} is now saved")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--original_path", help="directory where vid file exists")
    parser.add_argument("-s", "--save_path", help="directory where new vid is to be saved")
    #parser.add_argument("-f", "--filename", help="filename which files needs to be changed")
    parser.add_argument("-r", "--rate", help="rate by which fps of the vid changes")
    args = parser.parse_args()


    change_fps(args.original_path, args.save_path, args.rate)