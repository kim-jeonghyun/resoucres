import cv2
import os
import argparse
import math

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
def skip_fps(original_path, new_path, step):
    #새 dir 없으면 만들기
    get_path(new_path)

    # old dir 에서 영상 파일만 추리기
    video_paths = [f for f in os.listdir(original_path) if (f.split('.')[-1] in ['mov','mp4','MOV','MP4','AVI','avi']) and (f[0] != '.')]
    print(f"There are {len(video_paths)} videos.")
    
    for filename in video_paths:
        print(filename)
        # 원래 비디오와 파일 경로와 새롭게 생성후 저장될 비디오 파일 경로 지정
        old_vid = os.path.join(original_path, filename)
        new_vid = os.path.join(new_path, filename)

        video_capture = cv2.VideoCapture(old_vid)
        
        #원래 비디오의 frame수와 새롭게 skip하여 저장한 frame수 지정 
        fps = int(video_capture.get(cv2.CAP_PROP_FPS))
        old_frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        # new_frame_count = math.floor(old_frame_count*float(step))
        
        if not video_capture.isOpened():
            print("Video Capture cannot be opened.")
            return
        
        # 대상이 되는 비디오 파일을 열어서
        else:
            print(f"original f : {old_frame_count},  fps: {fps} skip in every {step}steps")
        video_codec = cv2.VideoWriter_fourcc(*'avc1')
        retval, video_frame = video_capture.read()
        if video_frame is not None:
            # 새 비디오 파일을 만든다.
             video_writer = cv2.VideoWriter(new_vid, video_codec, fps, (video_frame.shape[1], video_frame.shape[0]))
             frame_index = 0

             while video_capture.isOpened():
                 # 마지막 frame까지 도달하면 멈춤
                 if frame_index == old_frame_count:
                     break
                 # 프레임 이미지 읽어옴
                 retval, frame = video_capture.read()
                 if not retval:
                    break
                 elif frame_index in list(range(old_frame_count))[0:old_frame_count:int(step)]:
                    video_writer.write(frame)
                 else:
                    pass
                 frame_index += 1

        #     if video_writer.isOpened():
        #         video_writer.release()
        #     video_capture.release()
        #     print(f"speed-changed {filename} is now saved")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--original_path", help="directory where vid file exists")
    parser.add_argument("-n", "--new_path", help="directory where new vid is to be saved")
    parser.add_argument("-s", "--step", help="steps in which vid frame skips ")
    args = parser.parse_args()


    skip_fps(args.original_path, args.new_path, args.step)