import cv2
import argparse
import glob

def video2image(opt):
    video_paths = glob.glob(opt.video_dir+"/*.mp4") + glob.glob(opt.video_dir+"/*.mov")
    print(video_paths)
    for vp in video_paths:
        video_name = vp.split("/")[-1][:-4]
        vidcap = cv2.VideoCapture(vp)
        success,image = vidcap.read()
        count = 0
        new_path = opt.new_dir
        while success:
            cv2.imwrite(new_path+video_name+"_%04d.jpg" % count, image)     # save frame as JPEG file
            success,image = vidcap.read()
            # print('Read a new frame: ', success)
            count += 1

        print("finish! convert video to frame {name}".format(name=video_name))
    
    print("all convert finish!!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_dir', type=str, help='path to video directory')
    parser.add_argument('--new_dir', type=str, help='path for new directory')

    opt = parser.parse_args()

    video2image(opt)