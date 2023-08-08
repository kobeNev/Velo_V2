import json


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

    def verwijder_fiets(self, fiets):
        if not self.beschikbaar:
            self.fiets = None
            self.beschikbaar = True
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

    def __str__(self):
        return f"{self.naam} heeft {self.aantal_beschikbare_slots()} vrije plaatsen, en {self.aantal_beschikbare_fietsen()} fietsen beschikbaar."


class Gebruiker:
    def __init__(self, gebruiker_id, naam):
        self.gebruiker_id = gebruiker_id
        self.naam = naam
        self.max_capaciteit = 1
        self.fiets = []

    def Leen_fiets(self, fiets):
        if len(self.fiets) < self.max_capaciteit:
            self.fiets.append(fiets)
            fiets_slot = None
            for slot in Station1.sloten:
                if slot.fiets == fiets:
                    fiets_slot = slot
                    break
            if fiets_slot:
                fiets_slot.verwijder_fiets(fiets)
                print(
                    f"Fiets {fiets.fiets_id} geleend door {self.naam} uit slot {fiets_slot.slot_id}"
                )
            else:
                print(f"Fiets {fiets.fiets_id} kon niet worden geleend.")
        else:
            print(f"Gebruiker {self.naam} heeft al een fiets geleend.")

    def Retourneer_fiets(self, fiets):
        if fiets in self.fiets:
            self.fiets.remove(fiets)
            for slot in Station1.sloten:
                if slot.beschikbaar:
                    slot.plaats_fiets(fiets)
                    print(
                        f"Fiets {fiets.fiets_id} teruggebracht door {self.naam} in slot {slot.slot_id}"
                    )
                    break
            else:
                print(
                    f"Geen beschikbare sloten om de fiets {fiets.fiets_id} terug te brengen."
                )
        else:
            print(f"Gebruiker {self.naam} heeft deze fiets niet geleend.")


"""aanmaken atributen"""

fiets1 = Fiets("F1")
fiets2 = Fiets("F2")

Station1 = Station("S1", "Station1", 10)
Station1.maak_sloten()

Station1.sloten[0].plaats_fiets(fiets1)
Station1.sloten[1].plaats_fiets(fiets2)


def maak_gebruikers_van_json():
    with open("namenlijst.json", "r") as json_file:
        json_gegevens = json.load(json_file)

    gebruikers = []

    for index, item in enumerate(json_gegevens):
        naam = item["name"]
        gebruiker = Gebruiker(f"G{index}", naam)
        gebruikers.append(gebruiker)
    return gebruikers


"""testen van de functies"""

print(Station1)

gebruikers = maak_gebruikers_van_json()

gebruikers[0].Leen_fiets(fiets2)

print(Station1)

gebruikers[0].Leen_fiets(fiets1)

gebruikers[0].Retourneer_fiets(fiets2)

print(Station1)
