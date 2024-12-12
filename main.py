def read_import():
    infile = open("World Series.txt",'r')
    inport = []
    for i in infile:
        i = i.rstrip('\n')
        inport = inport + [i]
    print(inport)
    infile.close()
    return inport

def reader(file):
    win = []
    a = 0
    team = input("World Series winner: ")

    try:
        while file[a] != '':
            if file[a] == team:
                win = win+[file[a-1]]
            a += 1
    except:
        pass
    try:
        if win[0]:
            print(team)
            for i in win:
                print(i)
    except:
        print("Team", team, "not found.")

def main():
    the_list = read_import()
    reader(the_list)

main()