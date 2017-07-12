import sys


def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)
    #print lines
    # return lines

def main():
    pattern = sys.argv[1]
    search = grep(pattern)
    next(search)
    line = sys.stdin.readlines()
    # line = sys.stdin.read()
    for i in range(len(line)):
        search.send(line[i])


def help(string):
    help = string
    if (help == '-h'):
        print("Documentatin")
    else:
        raise  Exception

if __name__ == '__main__':
    main()
if __name__ == '__main__':
    help()
