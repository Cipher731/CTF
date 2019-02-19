import pickle
import os


def md5(s: str):
    import hashlib
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()


dic: dict = pickle.load(open(os.path.dirname(os.path.abspath(__file__)) + '/md5_captcha', 'rb'))


def captcha(s: str):
    ret = dic.get(s)
    if ret is None:
        i = 10000000
        while md5(str(i))[0:6] != s:
            i += 1
        ret = i
    return ret
