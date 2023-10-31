data = str()
n = int(input())
for i in range(0, n):
    string = input()
    if data == "":
        data= string
    else:
        #print(data)
        d = str()
        if len(data) > len(string):
            for s in range(1, len(string)+1):
                d = string[0:s]
                if data.endswith(d):
                    data = data + string[s:]
                    break
            else:
                for x in range(len(string)-1, 0, -1):
                    d = string[x:]
                    if data.startswith(d):
                        data = string[0:x] + data
                        break
                else:
                    data += string
        else:
            for s in range(1, len(data)+1):
                d = data[0:s]
                if string.endswith(d):
                    data = string + data[s:]
                    break
            else:
                for x in range(len(data)-1, 0, -1):
                    d = data[x:]
                    if string.startswith(d):
                        data = data[0:x] + string
                        break
                else:
                    data += string

print(data)
