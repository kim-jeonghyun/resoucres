import os
from hashlib import blake2b  # sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s() 등 지원]
import argparse

def get_hash(text, target_len):
    """
    text와 target_len을 받으면, text size의 크기로 암호와된 텍스트를 반환하는 함수
    """
    salt = os.urandom(blake2b.SALT_SIZE)
    h1 = blake2b(salt=salt)
    h1.update(bytes(text, 'UTF-8'))
    return h1.hexdigest()[:target_len]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--text', type=str, help='path to video directory')
    parser.add_argument('-l', '--length', type=int, help='path for new directory')
    args = parser.parse_args()
    
    hashed_text = get_hash(args.text, args.length)
    print(hashed_text)
