#!/bin/bash

# 코덱 설정 변경 및 확장자 변경으로 용량 최적화

OIFS="$IFS"
IFS=$'\n'

for f in $(find $1);
    do FILE=$(basename ${f})
    if [[ ( "$FILE" == *.mov ) || ( "$FILE" == *.MOV ) || ( "$FILE" == *.mkv ) || ( "$FILE" == *.avi ) || ( "$FILE" == *.AVI )]];
        then NAME=${FILE%.*}
             echo $NAME
             ffmpeg -i "$f" -vcodec libx265 -crf 28 "$2$NAME.mp4";
    fi;
    done

IFS="$OIFS"

