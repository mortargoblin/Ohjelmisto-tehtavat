# pi-algorytmi

def main():
    print("Enter number of points")
    n = int(input("> "))
    print("Pi approximately equals:", calc_pi(n))

def calc_pi(points):
    from random import uniform
    from math import pi

    # tässä kohtaa arvotaan pisteiden sijainnit ja lasketaan osumat
    # 
    # voisin myös käyttää while looppia tässä, mutta mielestäni for loop
    # oli järkevämpi
    hit = 0
    for _ in range(points):
        x = uniform(-1,1)
        y = uniform(-1,1)
        if pow(x,2) + pow(y,2) < 1:
            hit += 1
        else:
            pass
    # palauta piin arvo osumien perusteella
    return 4 * hit / points

main()
