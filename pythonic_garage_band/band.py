class Band:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        pass

    def play_solos(self, member):
        pass

    def to_list(self):
        pass

class Musician:
    def __init__(self, name):
        self.name = name


class Guitarist(Musician):
    def __init__(self, name, instrument="guitar"):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):
    pass


class Drummer(Musician):
    def __init__(self, name, instrument="drums"):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
