def ignorecomm(f,s):
    if s[0]!='#':
        return s
    else:
        s=f.readline()
        return ignorecomm(f,s)
def Branch(s):
    if s=="Sigma:\n":
        sections.add("Sigma")
        Sigmaf(f,s)
    elif s=="Transitions:\n":
        sections.add("Transitions")
        Transitionsf(f,s)
    elif s=="States:\n":
        sections.add("States")
        Statesf(f,s)
    else:
        print("Aceasta informatie nu descrie un automat. Fisier invalid!")
        ok=0

def Sigmaf(f,s):
    s = f.readline()
    Sigma = []

    while s != "End\n":
        s = s.strip('\t\n')
        Sigma.append(s)
        s = f.readline()
    print(f"Alfabetul automatului este {Sigma}\n")


def Statesf(f,s):
    s = f.readline()
    States= []

    while s != "End\n":
        s = s.strip('\t\n')
        States.append(s)
        s = f.readline()
    print(f"Starile automatului sunt {States}\n")


def Transitionsf(f,s):
    s = f.readline()
    T = []
    while s != "End\n":
        s = s.strip('\t\n')
        T.append(s)
        s = f.readline()
    print(f"Tranzitiile automatului  sunt {T} \n")

sections=set()
ok=1
try:
    f=open("input.txt")
except:
    ok=0
    print("Fisierul nu exista!")
if ok:      #Sectiunea 1
    s=f.readline()
    s=ignorecomm(f,s)
    Branch(s)
    if ok:   # Sectiunea 2
        s = f.readline()
        s = ignorecomm(f, s)
        Branch(s)
        if ok:    #Sectiunea 3
            s = f.readline()
            s = ignorecomm(f, s)
            Branch(s)

print (sections)
