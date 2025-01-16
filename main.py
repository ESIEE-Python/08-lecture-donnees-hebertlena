""" exo 8"""
#### Imports et définition des variables globales


FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        r = f.readlines()
        l= [i.strip("\n") for i in r]
        l= [i.split(";") for i in l]
        liste_int = [[int(x) for x in i] for i in l]
        return list(liste_int)


def get_list_k(data, k):
    """ retourn liste"""
    l = data
    return l[k]

def get_first(l):
    """ retourne premiere liste"""
    return l[0]

def get_last(l):
    """ retourne derniere liste"""
    return l[-1]

def get_max(l):
    """ retourne le max de la liste"""
    return max(l)

def get_min(l):
    """ retourne le min de la liste"""
    return min(l)

def get_sum(l):
    """ retourne la somme de la liste"""
    somme = 0
    for e in l :
        somme += e
    return somme


#### Fonction principale


def main():
    """ main"""
    r = read_data("listes.csv")
    print(r)
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
