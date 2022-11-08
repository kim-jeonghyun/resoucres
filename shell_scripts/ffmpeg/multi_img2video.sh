#!/bin/bash


# 참고 : https://hamelot.io/visualization/using-ffmpeg-to-convert-a-set-of-images-into-a-video/
# 경로 1에 있는 image_%4d.jpg 이름의 이미지 파일들과 경로 2에 있는 오디오 파일을 합쳐 경로 3의 동영상 파일로 변환하여 내보내는 스크립트

ffmpeg -r 60 -f image2 -s 1920x1080 -i "$1"/image_%04d.jpg -i $2 -vcodec libx264 -crf 25 -acodec copy -shortest -vcodec libx264 -crf 25  -pix_fmt yuv420p $3