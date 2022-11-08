# Shell Script for ffmpeg



## tested environments

## tree

- mov2mp4.sh : mov, mkv 파일을 mp4로 변경, 용량 줄이기 [경로 1]의 모든 파일 중에서 확장자명이 .mov, .MOV, .mkv인 파일을 .mp4로 변경해 [경로 2]에 저장한다. 
- mov2mp4-optimize.sh : -vcodec libx265 -crf 28 를 통해 파일 포맷도 줄이고 품질도 조정해 용량 줄이기 (.mov 포맷에 비해 용량 80% 정도 감소)
- mp4-iptimized.sh : .mov, .mkv 외의 .mp4 확장자 영상도 -vcodec libx265 -crf 28 로 변환해 저장하는 스크립트

## how to use
```
./[쉘스크립트] [경로1] [경로2]
```

- img2video.sh : [경로 1]의 이미지 파일 1장을 동영상 파일로 변환해 [경로 2]에 저장한다. [int]초 길이로

## how to use
```
./img2video.sh [경로 1] [경로 2] [int]
```

- img_audio2video.sh : [경로 1]의 이미지 파일 1장과 [경로 2]의 오디오 파일을 조합하여 오디오 파일 길이 만큼의 동영상 파일로 변환해 [경로 3]으로 저장한다.

- video_concat.sh : 2개의 비디오 파일에서 정해진 구간만 trim해서 concat하는 스크립트

## how to use
```
./img_audio2video.sh [경로 1] [경로 2] [경로 3]
```

- multi_img2video.sh : [경로 1]에 있는 image_%4d.jpg 이름의 이미지 파일들과 [경로 2]에 있는 오디오 파일을 합쳐 [경로 3]의 동영상 파일로 변환하여 내보내는 스크립트

## how to use
```
./multi_img2video.sh [경로 1] [경로 2] [경로 3]
```

## note

- ffmpeg should be installed in your computer [download ffmpeg](https://ffmpeg.org/download.html)
for example, if you use macOC, you can download ffmpeg through homebrew.

```shell
$ brew install ffmpeg
```

- Don't forget to change the permission of the script file

```
chmod +x [파일명]
```