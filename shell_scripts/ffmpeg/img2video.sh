#!/bin/bash

# image를 받아서 video로 만드는 스크립트
# 참고 : https://stackoverflow.com/questions/25891342/creating-a-video-from-a-single-image-for-a-specific-duration-in-ffmpeg

#with no audio
ffmpeg -loop 1 -i "$1" -c:v libx264 -t "$3" -pix_fmt yuv420p -vf scale=1920:1080 "$2"

