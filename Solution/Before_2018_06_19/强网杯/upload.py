import requests
import string

s = string.ascii_letters + string.punctuation + string.digits

with open('payload.txt', 'w') as file:
    for a in s:
        for b in s:
            for c in s:
                for d in s:
                    for e in s:
                        for g in s:
                            file.writelines(a + b + c + d + e + g)
                        file.writelines(a + b + c + d + e)
                    file.writelines(a + b + c + d)
                file.writelines(a + b + c)
            file.writelines(a + b)
        file.writelines(a)
    file.close()
