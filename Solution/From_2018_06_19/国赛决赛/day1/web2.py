import pickle
import base64


# class Bomb:
#     def __init__(self, name):
#         self.name = name
#
#     def __getstate__(self):
#         return self.name
#
#     def __setstate__(self, state):
#         self.name = 1
#         print(f'Bang! From, {self.name}.')
#
#
# bomb = Bomb('Evan')
#
# pickled_bomb = pickle.dumps(bomb, protocol=0)
# unpickled_bomb = pickle.loads(pickled_bomb)


class Commodity:
    def __init__(self, name):
        self.name = name

    def __getstate__(self):
        return self.name

    def __setstate__(self, state):
        self.name = 1


c = Commodity('1')
# pp = pickle.dumps(c, 0)
pp = b"Y2NvcHlfcmVnCl9yZWNvbnN0cnVjdG9yCnAwCihjc3Nob3AubW9kZWxzCkNvbW1vZGl0eQpwMQpjX19idWlsdGluX18Kb2JqZWN0CnAyCk50cDMKUnA0CihkcDUKUydfc2FfaW5zdGFuY2Vfc3RhdGUnCnA2CmcwCihjc3FsYWxjaGVteS5vcm0uc3RhdGUKSW5zdGFuY2VTdGF0ZQpwNwpnMgpOdHA4ClJwOQooZHAxMApTJ2NsYXNzXycKcDExCmcxCnNTJ2xvYWRfb3B0aW9ucycKcDEyCmNfX2J1aWx0aW5fXwpzZXQKcDEzCigobHAxNAp0cDE1ClJwMTYKc1MnY29tbWl0dGVkX3N0YXRlJwpwMTcKKGRwMTgKc1MnaW5zdGFuY2UnCnAxOQpnNApzUydtYW5hZ2VyJwpwMjAKZzAKKGNzcWxhbGNoZW15Lm9ybS5pbnN0cnVtZW50YXRpb24KX1NlcmlhbGl6ZU1hbmFnZXIKcDIxCmcyCk50cDIyClJwMjMKKGRwMjQKUydjbGFzc18nCnAyNQpnMQpzYnNTJ2tleScKcDI2CihnMQooSTM2CnRwMjcKTnRwMjgKc1MnZXhwaXJlZF9hdHRyaWJ1dGVzJwpwMjkKZzEzCigobHAzMAp0cDMxClJwMzIKc1MnbG9hZF9wYXRoJwpwMzMKKGxwMzQKKGcxCk50cDM1CmFzYnNTJ25hbWUnCnAzNgpWTnFlREdGcldhWE9rSUNqQQpwMzcKc1MncHJpY2UnCnAzOApGMTg4LjAKc1MnYW1vdW50JwpwMzkKSTk5OTkKc1MnaWQnCnA0MApJMzYKc1MnZGVzYycKcDQxClZWREduWGFsRGRnbUFrVHRJdnNRV1lNdWxiRUtkUFVxY3dFcXJTcWJ3cFRwVEtoSXJJQUhTVGJSYlpqREdPTmhQenJnUU9rT2l1b05QRVp2Z2NqYVZIUXNKZWFRVnl3VUhlWXFICnA0MgpzYi4="
pp = base64.b64decode(pp)
print(pp.decode())
# pl = pickle.loads(pp)
# print(base64.b64encode(pp))

f = open('3', 'r')
f.write()
