from Utas import *
from Busz import *

def main():
    Utas.utasGeneralas(Utas)
    busz = Busz("34", 50)
    Busz.jSonBeolvasasa(Busz, "160")
    Busz.jaratInitialize(busz, "160")
    Busz.buszKozlekedik(Busz)

if __name__ == "__main__":
    main()