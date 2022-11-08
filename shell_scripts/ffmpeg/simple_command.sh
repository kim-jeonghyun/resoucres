#!/bin/bash

# simple ffmpeg commands
# 참고 : https://ottverse.com/change-resolution-resize-scale-video-using-ffmpeg/

#change fps : 1초당 프레임 수를 줄여서 용량 줄이기 - 영상 길이는 keep
# needs three perameter $1 : input_path $2: out_path $3 : fps you specifies
# ffmpeg -i $1 -filter:v fps=$3 $2

# resize with specified width retaining the aspect ratio
# needs three perameter $1 : input_path $2: out_path $3 : relative rate
# 높이를 고정하고 싶다면 iw 대신 ih를 써서 -vf scale=-1:ih*$3 으로 쓰면 됨

ffmpeg -i $1 -vf scale=iw*$3:-1 $2
