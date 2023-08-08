class Fiets:
    def __init__(self, fiets_id):
        self.fiets_id = fiets_id


class Slot:
    def __init__(self, slot_id):
        self.fiets = None
        self.beschikbaar = True
        self.slot_id = slot_id

    def plaats_fiets(self, fiets):
        if self.beschikbaar:
            self.fiets = fiets
            self.beschikbaar = False
            print(f"Fiets {fiets.fiets_id} geplaatst in slot {self.slot_id}")

    def verwijder_fiets(self, fiets):
        if not self.beschikbaar:
            self.fiets = None
            self.beschikbaar = True
            print(f"Fiets {fiets.fiets_id} verwijderd uit slot {self.slot_id}")
            return fiets


class Station:
    def __init__(self, station_id, naam, capaciteit):
        self.station_id = station_id
        self.naam = naam
        self.sloten = []
        self.capaciteit = capaciteit

    def maak_sloten(self):
        for i in range(self.capaciteit):
            slot = Slot(f"S{i}")
            self.sloten.append(slot)

    def aantal_beschikbare_slots(self):
        return len([slot for slot in self.sloten if slot.beschikbaar])

    def aantal_beschikbare_fietsen(self):
        return len([slot for slot in self.sloten if not slot.beschikbaar])


fiets = Fiets("F1")
fiets2 = Fiets("F2")

Station1 = Station("S1", "Station1", 10)
Station1.maak_sloten()
Station1.sloten[0].plaats_fiets(fiets)
Station1.sloten[1].plaats_fiets(fiets2)

print(f"{Station1.naam} heeft {Station1.aantal_beschikbare_slots()} vrije plaatsen.")
print(f"{Station1.naam} heeft {Station1.aantal_beschikbare_fietsen()} aantal fietsen.")

Station1.sloten[0].verwijder_fiets(fiets)

print(f"{Station1.naam} heeft {Station1.aantal_beschikbare_slots()} vrije plaatsen.")
print(f"{Station1.naam} heeft {Station1.aantal_beschikbare_fietsen()} aantal fietsen.")
