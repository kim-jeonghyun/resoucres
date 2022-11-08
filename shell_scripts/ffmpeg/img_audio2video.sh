#!/bin/bash

# single image와 audio 파일을 받아서 audio 길이 만큼의 동영상 파일을 만드는 스크립트
# 참고 https://superuser.com/questions/1041816/combine-one-image-one-audio-file-to-make-one-video-using-ffmpeg

#with matching audio
ffmpeg -loop 1 -i "$1" -i "$2" -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest "$3"
