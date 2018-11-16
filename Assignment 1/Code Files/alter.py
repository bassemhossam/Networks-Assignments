import sys
def alter(str, index):
    if str[index-1] == '0':
        str = str[: index-1] + '1' + str[index:]
    elif str[index-1] == '1':
        str = str[: index - 1] + '0' + str[index:]

    return str


message = input()
key = input()
index = sys.argv[1]
print(alter(message, int(index)))
print(key)
