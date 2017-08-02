from human import Person, PersonMixin, Woman, Man

Valya = Woman('Valentina', 'Brown', 1938)
Leon = Man('leon', 'Val', 1955)
Leon.proposed(Valya)
Leon.marriage(Valya)
Gornostay = Valya.family
# Valya.list_family.append(Valya.family)

Andrey = Man('Andrey', 'Malysh', 1968)
Marina = Woman('Marina', 'Malysh', 1968)
Andrey.proposed(Marina)
Andrey.marriage(Marina)
Malyshevy = Marina.family

Marina.root_family = Gornostay
Gornostay.children.append(Marina)
# Marina.list_family.append(Marina.family)

Tamara = Woman('Toma', 'Malysheva', 1995)
Tamara.family = Malyshevy
Tamara.root_family = Malyshevy
Malyshevy.add(Tamara)
Denis = Man('Denis', 'Tverd', 1992)
Denis.proposed(Tamara)
Denis.marriage(Tamara)
Denis.sex(Tamara)
Denis.sex(Tamara)
Denis.sex(Tamara)
Denis.sex(Tamara)
Sam = Woman('Sam', 'Snoy', 1955)
Drogo = Man('Drogo', 'Khal', 1992)
Leon.family.add_child(Sam)
Leon.family.add_child(Drogo)
Asha = Woman('Asha', 'n', 1995)
Drogo.proposed(Asha)
Drogo.marriage(Asha)
Drogo.sex(Asha)
Tamara.family.divorce()
Andrey = Man('Andrey', 'Mensh', 1990)
Andrey.proposed(Tamara)
Andrey.marriage(Tamara)
Andrey.sex(Tamara)
Deny = Woman('Deny', 'B', 1990)
Don = Man('Don', 'Grey', 1990)
Don.proposed(Deny)
Deny.marriage(Don)
