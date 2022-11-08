import string
import random
import argparse

from pyparsing import punc8bit 
 

def create_password(args) :
    num = args.length
    punctuation = args.punctuation
    
    if punctuation is False:
        pw_candidate = string.ascii_letters + string.digits
    else:
        pw_candidate = string.ascii_letters + string.digits + string.punctuation 
    
    new_pw = ""
    for i in range(num):
        new_pw += random.choice(pw_candidate)
    
    print("\n생성된 랜덤 비밀번호", new_pw)


if __name__ == '__main__':
    # 인자값을 받을 수 있는 인스턴스 생성
    parser = argparse.ArgumentParser(description='Argparse Tutorial') 
    # 입력받을 인자값 설정 (default 값 설정가능)
    parser.add_argument('-l', '--length', type=int,   default=6,  help="password length")
    parser.add_argument('-p', '--punctuation', type=bool,   default=False,  help="whether punctuation is included")

    # args 에 위의 내용 저장
    args    = parser.parse_args()
    
    create_password(args)