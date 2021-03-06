def ignorecomm(f, s):
    if s[0] != '#' and s.strip() != "":
        return s
    else:
        s = f.readline()
        return ignorecomm(f, s)


def Branch(s, ok):
    if ok == 1:
        if s == "Sigma:\n":
            sections.add("Sigma")
            Sigmaf(f, s)
        elif s == "Transitions:\n":
            sections.add("Transitions")
            Transitionsf(f, s)
        elif s == "States:\n":
            sections.add("States")
            Statesf(f, s)
        else:
            print("Aceasta informatie nu descrie un automat. Sectiune invalida!")
            ok = 0
    else:
        print("\n")
        ok = 0
    return ok


def Sigmaf(f, s):
    s = f.readline()
    Sigma = []

    while s != "End\n" and s != "End":
        s = s.strip()
        Sigma.append(s)
        s = f.readline()
    print("Alfabetul automatului este", Sigma, "\n")


def Statesf(f, s):
    s = f.readline()
    States = []

    while s != "End\n" and s != "End":
        s = s.strip('\t\n')
        States.append(s)
        s = f.readline()
    print("Starile automatului sunt ", States, "\n")


def Transitionsf(f, s):
    s = f.readline()
    T = []
    while s != "End\n" and s != "End":
        s = s.strip('\t\n')
        T.append(s)
        s = f.readline()
    print("Tranzitiile automatului  sunt", T, " \n")


sections = set()
OK = 1
try:
    f = open("input.txt")
except:
    OK = 0
    print("Fisierul nu exista!")
if OK == 1:
    s = f.readline()
    s = ignorecomm(f, s)
    OK = Branch(s, OK)  # Sectiunea 1
    s = f.readline()
    s = ignorecomm(f, s)
    OK = Branch(s, OK)  # Sectiunea 2
    s = f.readline()
    s = ignorecomm(f, s)
    OK = Branch(s, OK)  # Sectiunea 3

if OK == 1:
    if sections != {"Transitions", "States", "Sigma"}:
        print("Missing states. INVALID INPUT")
print(sections)