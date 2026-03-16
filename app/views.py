from django.shortcuts import render
import random


lenta = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

zaidimas_baigtas = False
laimetojas = None


def tikrinti_laimetoja():
    global laimetojas, zaidimas_baigtas

    
    for eilute in lenta:
        if eilute[0] == eilute[1] == eilute[2] != "":
            laimetojas = eilute[0]
            zaidimas_baigtas = True
            return

    
    for stulp in range(3):
        if lenta[0][stulp] == lenta[1][stulp] == lenta[2][stulp] != "":
            laimetojas = lenta[0][stulp]
            zaidimas_baigtas = True
            return

    
    if lenta[0][0] == lenta[1][1] == lenta[2][2] != "":
        laimetojas = lenta[0][0]
        zaidimas_baigtas = True
        return

    if lenta[0][2] == lenta[1][1] == lenta[2][0] != "":
        laimetojas = lenta[0][2]
        zaidimas_baigtas = True
        return

    
    if all(lang != "" for eil in lenta for lang in eil):
        laimetojas = "Lygiosios"
        zaidimas_baigtas = True


def kompiuterio_ejimas():
    tusci_lang = [(r, c) for r in range(3)
                  for c in range(3) if lenta[r][c] == ""]

    if tusci_lang:
        r, c = random.choice(tusci_lang)
        lenta[r][c] = "O"


def naujas_zaidimas():
    global lenta, zaidimas_baigtas, laimetojas
    lenta = [["", "", ""], ["", "", ""], ["", "", ""]]
    zaidimas_baigtas = False
    laimetojas = None


def zaidimo_langas(request):
    global zaidimas_baigtas, laimetojas

    
    if "naujas" in request.GET:
        naujas_zaidimas()

    
    if not zaidimas_baigtas:
        eil = request.GET.get("eil")
        stulp = request.GET.get("stulp")

        
        if eil is not None and stulp is not None:
            eil = int(eil)
            stulp = int(stulp)

            if lenta[eil][stulp] == "":
                lenta[eil][stulp] = "X"
                tikrinti_laimetoja()

                
                if not zaidimas_baigtas:
                    kompiuterio_ejimas()
                    tikrinti_laimetoja()

    return render(request, "zaidimas.html", {
        "lenta": lenta,
        "laimetojas": laimetojas,
        "zaidimas_baigtas": zaidimas_baigtas
    })
