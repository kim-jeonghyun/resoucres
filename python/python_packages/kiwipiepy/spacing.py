from kiwipiepy import Kiwi
import numpy as np

kiwi = Kiwi()

def respacing(sent):
    """
    문자열을 넣었을 때 비어있으면 nan을 그렇지 않으면 kiwi의 띄어쓰기 교정 메서드를 적용한 문장을 반환한다.
    """
    if sent != sent:
        return np.nan
    else:
        return kiwi.space(sent)