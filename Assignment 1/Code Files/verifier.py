from fns import *


def decodeData(data, key):
    l_key = len(key)
    # Appends n-1 zeroes at end of data
    appended_data = data + '0' * (l_key - 1)
    return mod2div(appended_data, key)



data = input()
key = input()

remainder = decodeData(data,key)

if remainder.find('1') != -1:
    out = "message is incorrect"
else:
    out = "message is correct"
print(out)