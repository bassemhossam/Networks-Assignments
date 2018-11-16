from fns import *
def encodeData(data, key):

    l_key = len(key)

    # Appends n-1 zeroes at end of data
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)

    # Append remainder in the original data
    codeword = data + remainder
    return codeword

data = input()
key = input()
ans = encodeData(data,key)
print(ans)
print(key)

outputfile = open("transmitted_message.txt", "wb")
outputfile.write(bytes(ans, 'UTF-8'))
