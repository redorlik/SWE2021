
def decode(list):
    return ''.join([x[0]*x[1] for x in list])

def encode(message):
    if message == '':
        return [('',0)]
    old = ''
    i = 1
    res = []
    for c in message:
        if c == old:
            i += 1
        else:
            if old:
                res.append((old,i))
                i = 1
            old = c
    res.append((old,i))
    return res

if __name__ == '__main__':
    import sys
    from time import sleep
    cmd_line = sys.argv
    print(cmd_line)
    if len(cmd_line)<3:
        print(f"Too few arguments ({cmd_line}): expected 3")
        exit(0)
    fil = cmd_line[-1]
    with open(fil,'r') as f:
        dat = f.read()
        if '-d' in cmd_line:
            print(decode(eval(dat)))
        if '-e' in cmd_line:
            print(encode(dat))
        if '-r' in cmd_line:
            # enkode and dekode
            print(decode(encode(dat)))
    sleep(1.5)
    exit(1)
