#!/bin/bash

# 2개의 video file에서 정해진 구간만 trim해서 concat하는 스크립트
# 참고 : https://stackoverflow.com/questions/48882568/how-to-cut-from-multiple-input-videos-and-concat-to-single-video-using-ffmpeg



ffmpeg -i video_sample.mp4 -i black_with_audio.mp4 -filter_complex \
"[0:v]scale=320:240,setsar=4/3,trim=start=00:end=02,setpts=PTS-STARTPTS[v0]; \
 [0:a]atrim=start=00:end=02,asetpts=PTS-STARTPTS[a0]; \
 [1:v]scale=320:240,setsar=4/3,trim=start=15:end=18,setpts=PTS-STARTPTS[v1]; \
 [1:a]atrim=start=15:end=18,asetpts=PTS-STARTPTS[a1]; \
 [v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]" \
 -vsync vfr -map "[v]" -map "[a]" concat_test.mp4