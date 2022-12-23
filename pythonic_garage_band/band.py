class Band:
    def __init__(self, name, members):

        self.name = name
        self.members = members

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Band. name={self.name} and members={self.members}"

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    def to_list(self):
        pass

    def instruments(self, band):
        scraped = []
        for self.member in band:
            scraped.append(self.member.get_instrument)
        return scraped

    def individual_solos(self, band):
        self.play_solos()



class Musician:
    def __init__(self, name):
        self.instrument = None
        self.name = name
    
    def get_instrument(self):
        return self.instrument


class Guitarist(Musician):
    def __init__(self, name, instrument="guitar"):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name, instrument="bass"):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name, instrument="drums"):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def play_solo(self):
        return "rattle boom crash"

