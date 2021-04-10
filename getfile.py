import os,re,math
songtitles = []
reg = re.compile("\[(.*)\]")
song = [[], [], [], []]
hold = [[], [], [], []]
hit=False
for (dirpath, dirnames, filenames) in os.walk("./Songs"):
    songtitles.extend(dirnames)
    break

maps = [[] for x in songtitles]
for a in range(0, len(songtitles)):

    for (dirpath, dirnames, filenames) in os.walk("./Songs/" + songtitles[a]):
        for x in filenames:
            if x[-4:] == ".osu":
                maps[a].append(songtitles[a] + "/" + str(x))

        break
name=songtitles
name2=maps
for x in name:
    print(x, name.index(x))
chosen = int(input("select: "))
name = name[chosen]

for x in name2[chosen]:
    print(x, name2[chosen].index(x))

name2 = name2[chosen][int(input("select: "))]

file1 = open(
    "./Songs/" + name2,
    "r",
)
# file formatting
Lines = file1.readlines()
for line in Lines:

    if hit:
        line = line.split(",")[:-1] + [line.split(",")[5].split(":")[0]]
        line=[int(x) for x in line]
        
        if line[3] == 128:
            song[int(((line[0]/64)+1)/2)]

    else:
        if reg.findall(line) == ["HitObjects"]:
            hit = True
hold[0].append([999999999999999999, 999999999999999999])
hold[1].append([999999999999999999, 999999999999999999])
hold[2].append([999999999999999999, 999999999999999999])
hold[3].append([999999999999999999, 999999999999999999])
song[0].append(999999999999999999)
song[1].append(999999999999999999)
song[2].append(999999999999999999)
song[3].append(999999999999999999)
print(song,hold)
