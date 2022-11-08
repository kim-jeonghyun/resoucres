#!/bin/bash

# 코덱 설정 변경 및 확장자 변경으로 용량 최적화

OIFS="$IFS"
IFS=$'\n'

for f in $(find $1);
    do FILE=$(basename ${f})
    if [[ ( "$FILE" == *.mov ) || ( "$FILE" == *.MOV ) || ( "$FILE" == *.mkv ) || ( "$FILE" == *.avi ) || ( "$FILE" == *.AVI ) || ( "$FILE" == *.mp4 ) || ( "$FILE" == *.MP4 ) ]];
        then NAME=${FILE%.*}
             echo $NAME
             # -crf [quality] 비트레이트 대신 화질 기준으로 인코딩할 때 쓰는 옵션. libx264 코덱 기준 사용 가능 범위 0-51, 0은 무손실, 디폴트는 23
             ffmpeg -i "$f" -vcodec libx265 -crf 28 "$2$NAME.mp4";
    fi;
    done
IFS="$OIFS"

