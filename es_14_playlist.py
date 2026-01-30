#Playlist
#Un dizionario associa nomi di playlist a liste di titoli di canzoni. Scrivere funzioni per:
#(a) contare le canzoni totali, (b) cercare in quale playlist si trova una canzone, (c) unire
#due playlist in una nuova.
def contaCanzoni(diz):
    cont = 0
    for chiave in diz:
        cont += len(diz[chiave])
    return cont
def trovaPlaylist(diz,canzone):
    for chiave in diz:
        for i in diz[chiave]:
            if i == canzone:
                return chiave
    return None
def unisciPlaylist(diz,nome,pl1,pl2):
    nuova = {}
    canzoni = []
    for chiave in diz:
        if chiave == pl1:
            for i in diz[chiave]:
                canzoni.append(i)
        if chiave == pl2:
            for k in diz[chiave]:
                canzoni.append(k)
    diz[nome] = canzoni
    return diz

def main():
    playlist = {
    "Rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
    "Pop": ["Thriller", "Like a Prayer", "Billie Jean"],
    "Relax": ["Hotel California", "Imagine", "Let It Be"]
    }
    tot = contaCanzoni(playlist)
    print(tot)
    playlistTro = trovaPlaylist(playlist,"Bohemian Rhapsody")
    print(playlistTro)
    playListNuova = unisciPlaylist(playlist,"Nuova","Rock","Pop")
    print(playListNuova)


if __name__=="__main__":
    main()