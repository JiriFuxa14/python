class Elf:
    pocet_elfu = 0

    def __init__(self, jmeno, vyrobek):
        self.jmeno = jmeno
        self.vyrobek = vyrobek
        Elf.pocet_elfu += 1
        print(f"Elf {self.jmeno} začal pracovat na {self.vyrobek}.")

    def __del__(self):
        Elf.pocet_elfu -= 1
        print(f"Elf {self.jmeno} dokončil práci a odešel od stolu.")

    def vyrobit_vyrobek(self):
        print(f"Elf {self.jmeno} vyrábí {self.vyrobek}.")

    @staticmethod
    def vypis_pocet_elfu():
        print(f"Aktuální počet elfů v dílně: {Elf.pocet_elfu}")


if __name__ == "__main__":
    elf1 = Elf("Jirka", "hračce")
    elf2 = Elf("Petr", "panence")
    elf3 = Elf("Anna", "vlaku")

    Elf.vypis_pocet_elfu()

    del elf1
    del elf2
    del elf3

    Elf.vypis_pocet_elfu()
