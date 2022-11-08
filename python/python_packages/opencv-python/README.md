# opencv-python

Pre-built CPU-only OpenCV packages for Python

## documentation
[opencv-python](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

## installation

```
$ pip install --upgrade pip
$ pip install opencv-python
```

- Option 1 - Main modules package: pip install opencv-python
- Option 2 - Full package (contains both main modules and contrib/extra modules): pip install opencv-contrib-python (check contrib/extra modules listing from OpenCV documentation)


## tree
- video2image.py : 지정된 경로 내 비디오 파일을 jpg 이미지 파일로 변경하여 원래 파일명 폴더에 저장
- vidspeed_change.py : 지정된 경로 내 비디오 파일의 frame_per_second를 바꿔 영상의 재생 속도를 수정하여 저장
- vidframe_skip.py : 지정된 경로 내 비디오 파일의 frame을 n번째 마다 skip하여 용량 줄여 저장 

## note
- open-cv로 처리 과정을 거친 영상 파일은 소리 데이터를 상실합니다. 소리 데이터를 keep 하고자 하면 [ffmpeg](https://ffmpeg.org/) 를 활용해주세요.