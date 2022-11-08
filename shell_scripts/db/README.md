# database-related shell scripts

- db_remote2local.sh
1. 원래 로컬에 있던 데이터베이스를 백업하고,
2. 원격에 위치한 데이터베이스를 dump 받고,
3. dump받은 db를 로컬 데이터베이스로 복사한다.


how to use

원격 데이터베이스와 로컬 데이터베이스 설정값을 sh 파일 안에 입력하고, 스크립트 파일이 있는 디렉터리에서 아래와 같이 실행시킴

```
$ ./db_remote2local.sh
```
