url = input()
url = url.split('?')
get = url[1].split('&')
key = input()
for i in range(len(get)):
    if get[i].split('=')[0] == key:
        print(get[i].split('=')[1])
