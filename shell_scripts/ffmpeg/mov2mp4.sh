#!/bin/bash

# 파일 포맷만 변경해 용량 줄이기
OIFS="$IFS"
IFS=$'\n'

for f in $(find $1);
    do FILE=$(basename ${f})
    if [[ ( "$FILE" == *.mov ) || ( "$FILE" == *.MOV ) || ( "$FILE" == *.mkv ) || ( "$FILE" == *.avi ) || ( "$FILE" == *.AVI )]];
        then NAME=${FILE%.*}
             echo $NAME
             ffmpeg -i "$f" "$2$NAME.mp4";
    fi;
    done

IFS="$OIFS"