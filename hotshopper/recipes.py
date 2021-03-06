import tkinter as tk

from hotshopper.ingredients import *


class Recipe:
    name = ""
    weeks = []
    ingredients = []
    selected = False

    def set_selected(self, selected: tk.BooleanVar, week: int):
        if selected.get():
            self.selected = True
            self.weeks.append(week)
            print(self.name + " is selected for week " + str(week))
        else:
            self.selected = False
            print(self.name + " is deselected from week " + str(week))
            self.weeks.remove(week)


class PotatoSoup(Recipe):
    name = "Kartoffelsuppe (S.77)"
    ingredients = [Carrot(kilogram, 0.5),
                   Onion(piece, 1),
                   StarchyPotato(gram, 750),
                   HamCubes(gram, 125),
                   Leek(piece, 1),
                   CremeFraiche(gram, 100),
                   CardamomMilled(piece, 1),
                   ]


class ParsleyRootCurry(Recipe):
    name = "Petersilienwurzelcurry (S.89, Sep - Mai)"
    ingredients = [LowStarchPotatoe(gram, 750),
                   ChiliPepper(piece, 1),
                   Carrot(gram, 250),
                   Onion(piece, 5),
                   Ginger(piece, 1),
                   Garlic(piece, 2),
                   ParsleyRoot(gram, 600),
                   Leek(piece, 1),
                   CoconutMilk(piece, 1),
                   Lime(piece, 1),
                   ]


class SwedeStew(Recipe):
    name = "Steckrübeneintopf (S.80, Okt - Jan)"
    ingredients = [Onion(piece, 1),
                   Swede(gram, 500),
                   StarchyPotato(gram, 400),
                   Leek(piece, 1),
                   Cream(piece, 1),
                   SoySauce(piece, 1)
                   ]


class SalsaNoodles(Recipe):
    name = "Salsanudeln mit Tomatensalat (S.90)"
    ingredients = [SpaghettiNoodles(gram, 400),
                   Lemon(piece, 1),
                   ParsleyFrozen(piece, 1),
                   DillFrozen(piece, 1),
                   AgaveSyrup(piece, 1),
                   HazelnutMilled(piece, 1),
                   Onion(piece, 1),
                   Tomato(piece, 4),
                   BasilFrozen(piece, 1)
                   ]


class OrientalSproutPan(Recipe):
    name = "Orientalische Rosenkohlpfanne (S.92)"
    ingredients = [PrimarilyWaxyPotato(kilogram, 1),
                   Sprout(gram, 750),
                   Carrot(gram, 150),
                   Onion(piece, 1),
                   Ginger(piece, 1),
                   SoySauce(piece, 1),
                   FetaCheese(gram, 100)
                   ]


class OvenTomatoes(Recipe):
    name = "Ofentomaten (S.100)"
    ingredients = [Caraway(piece, 1),
                   PrimarilyWaxyPotato(gram, 1800),
                   CaneSugar(piece, 1),
                   Tomato(piece, 6)
                   ]


class Pichelsteiner(Recipe):
    name = "Pichelsteiner (S.116)"
    ingredients = [Carrot(gram, 400),
                   CeleryRoot(gram, 250),
                   LowStarchPotatoe(gram, 600),
                   Leek(piece, 2),
                   BeefCuts(gram, 300),
                   ]


class ChicoryWithHam(Recipe):
    name = "Chicorée mit Schinken (S.121, Okt-Apr)"
    ingredients = [Chicory(piece, 4),
                   Orange(piece, 2),
                   GoudaSlices(gram, 100),
                   HamSlices(piece, 8),
                   CreamCheese(piece, 1),
                   PrimarilyWaxyPotato(gram, 1000)
                   ]


class PepperSalad(Recipe):
    name = "Paprikasalat (S.63 EX)"
    ingredients = [Cabanossi(gram, 250),
                   PepperRed(piece, 6),
                   Zucchini(piece, 2),
                   Buckwheat(gram, 50),
                   ]


class CoconutSoup(Recipe):
    name = "Kokossuppe (S.76 EX)"
    ingredients = [Onion(piece, 1),
                   Ginger(piece, 1),
                   ChickenCuts(gram, 200),
                   SugarSnap(gram, 200),
                   MungbeanSproute(gram, 150),
                   GreenCurryPaste(piece, 1),
                   CoconutMilk(piece, 1),
                   GlassNoodles(gram, 100),
                   SoySauce(piece, 1)
                   ]


class NoodlePanWithPumpkinAndTomatos(Recipe):
    name = "Nudelpfanne mit Kürbis und Tomaten (S.82 EX, Sep-Dez)"
    ingredients = [Macaroni(gram, 400),
                   Onion(piece, 1),
                   HokkaidoPumpkin(gram, 600),
                   PepperYellow(piece, 2),
                   CherryTomato(gram, 200),
                   Pistachios(gram, 50)
                   ]


class LeekNoodles(Recipe):
    name = "Lauchnudeln (S.85 EX)"
    ingredients = [Leek(piece, 1),
                   Tagliatelle(gram, 300),
                   OnionRed(piece, 2),
                   Smetana(piece, 1),
                   Pistachios(gram, 40)
                   ]


class RicePan(Recipe):
    name = "Reispfanne (S.88 EX)"
    ingredients = [RiceBasmati(gram, 280),
                   ChiliPepper(piece, 2),
                   Ginger(piece, 2),
                   PepperRed(piece, 4),
                   MungbeanSproute(piece, 1),
                   SoySauce(piece, 1)
                   ]


class GnocchiWithTomatoSauce(Recipe):
    name = "Gnocchi mit Tomatensauce (S.94 EX)"
    ingredients = [Onion(piece, 1),
                   Garlic(piece, 2),
                   TomatoSauce(piece, 2),
                   Gnocchi(gram, 1000),
                   CherryTomato(gram, 200)
                   ]


class PaprikaCreamCauliflower(Recipe):
    name = "Paprika-Sahne-Blumenkohl (S.103 EX)"
    ingredients = [CauliflowerFrozen(gram, 1000),
                   Onion(piece, 2),
                   ParsleyFrozen(piece, 1),
                   MacadamiaNut(gram, 80),
                   Ajvar(gram, 100),
                   Smetana(piece, 1),
                   ToastbreadWholemeal(piece, 1)
                   ]


class AsparagusWithSpinachCheeseSauce(Recipe):
    name = "Spargel mit Spinat-Käse-Sauce (S.106 EX, April - Mai)"
    ingredients = [Asparagus(gram, 1000),
                   Onion(piece, 2),
                   SpinachCreamed(gram, 400),
                   Gorgonzola(gram, 150),
                   HazelnutFlakes(gram, 30)
                   ]


class ChickenFajitas(Recipe):
    name = "Hähnchen-Fajitas (S.117 EX)"
    ingredients = [ChiliPepper(piece, 2),
                   Lime(piece, 2),
                   Garlic(piece, 2),
                   ChickenCuts(gram, 250),
                   PepperGreen(piece, 3),
                   OnionRed(piece, 3),
                   Avocado(piece, 1),
                   Tortilla(piece, 8)
                   ]


class SproutBolognese(Recipe):
    name = "Rosenkohlbolognese (S.126 EX)"
    ingredients = [StarchyPotato(gram, 800),
                   Onion(piece, 2),
                   Carrot(gram, 200),
                   Sprout(gram, 600),
                   GroundMeat(gram, 400),
                   TomatoPaste(gram, 50),
                   ]


class HotDogs(Recipe):
    name = "Hot Dogs"
    ingredients = [Baguette(piece, 2),
                   Wiener(piece, 8),
                   Pickles(piece, 1),
                   Onion(piece, 4)
                   ]


class RicePudding(Recipe):
    name = "Milchreis"
    ingredients = [RicePudding(gram, 250),
                   Milk(gram, 1000),
                   VanillaSugar(piece, 1),
                   ]


class SausageSalad(Recipe):
    name = "Wurstsalat"
    ingredients = [SausageStripes(gram, 400),
                   Pickles(piece, 1),
                   Onion(piece, 2),
                   Baguette(piece, 1)
                   ]


class VeggieRice(Recipe):
    name = "Reis-Gemüse-Pfanne (klassisch)"
    ingredients = [RiceBasmati(piece, 2),
                   PepperRed(piece, 1),
                   CreamCheese(gram, 300),
                   TomatoPaste(gram, 150),
                   Onion(piece, 2),
                   Zucchini(piece, 1),
                   PeasAndCarrotsFrozen(gram, 200),
                   BroccoliFrozen(gram, 150)
                   ]


class ZucchiniTomatoPan(Recipe):
    name = "Tomaten-Zucchini-Pfanne"
    ingredients = [Onion(piece, 2),
                   Garlic(piece, 2),
                   Zucchini(piece, 3),
                   PepperRoasted(piece, 1),
                   TomatoPickled(piece, 2),
                   Baguette(piece, 1)
                   ]


class SaladAndMaultaschen(Recipe):
    name = "Salat mit Maultaschen"
    ingredients = [Lettuce(piece, 1),
                   Tomato(piece, 2),
                   PepperRed(piece, 1),
                   Cucumber(piece, 1),
                   Onion(piece, 5),
                   Ginger(piece, 1),
                   Maultaschen(piece, 2),
                   SaladSauce(piece, 1)
                   ]


class NoodlesWithPesto(Recipe):
    name = "Pestonudeln"
    ingredients = [PestoGenovese(piece, 1),
                   NoodlesSpiral(gram, 500),
                   Cream(piece, 1),
                   Smetana(piece, 1),
                   Champignon(gram, 250),
                   Leek(piece, 2)
                   ]


class ChiliMascarponeNoodles(Recipe):
    name = "Chili-Mascarpone-Nudeln"
    ingredients = [NoodlesSpiral(gram, 400),
                   Mascarpone(gram, 250),
                   HamCooked(piece, 1),
                   Cream(piece, 1)
                   ]


class SchupfnudelnWithVegetables(Recipe):
    name = "Gemüseschupfnudeln"
    ingredients = [Schupfnudeln(gram, 1000),
                   VegetablesFrozen(piece, 1)
                   ]


class SchupfnudelnWithSourcrout(Recipe):
    name = "Schupfnudeln mit Sauerkraut"
    ingredients = [Schupfnudeln(gram, 1000),
                   HamCubes(gram, 200),
                   Sourcrout(piece, 1)
                   ]


class GyrosPita(Recipe):
    name = "Gyros-Pita"
    ingredients = [PorkCuts(gram, 250),
                   Tomato(piece, 3),
                   Onion(piece, 2),
                   Tzatziki(piece, 1),
                   PitaBread(piece, 1)
                   ]


class FishSticks(Recipe):
    name = "Fischstäbchen mit Kartoffelpüree & Erbsen"
    ingredients = [Fishsticks(piece, 1),
                   PeasFrozen(piece, 1),
                   StarchyPotato(gram, 700),
                   Milk(gram, 100),
                   ]


class BakedPotato(Recipe):
    name = "Ofenkartoffeln"
    ingredients = [
        StarchyPotato(gram, 1500),
        SourCream(piece, 2),
        EightHerbsFrozen(piece, 0.5)
    ]


class PotatoePancakes(Recipe):
    name = "Kartoffelpuffer"
    ingredients = [
        PotatoePancankesFrozen(piece, 1),
        ApplePuree(piece, 1)
    ]


class SandwichMaker(Recipe):
    name = "Sandwich-Maker"
    ingredients = [
        ToastbreadSandwich(piece, 1),
        Tomato(piece, 3),
        Salami(piece, 2),
        GoudaSlices(gram, 250)
    ]


class Lasagne(Recipe):
    name = "Lasagne"
    ingredients = [
        MaggiFixLasagna(piece, 2),
        CremeFraiche(piece, 1),
        GroundMeat(gram, 250),
        GratinCheese(piece, 1)
    ]


class CroquettesWithVegetables(Recipe):
    name = "Kroketten mit Gemüse"
    ingredients = [
        CroquettesFrozen(piece, 1),
        PeasFrozen(piece, 1),
        CauliflowerWithCreamFrozen(piece, 1)
    ]


class PepperCreamSchnitzel(Recipe):
    name = "Paprikarahmschnitzel"
    ingredients = [
        MaggiFixPepperCreamSchnitzel(piece, 2),
        PepperRed(piece, 2),
        Cream(piece, 2),
        TurkeySchnitzel(piece, 2),
        FriesFrozen(piece, 1)
    ]


class Barbecue(Recipe):
    name = "Grillen"
    ingredients = [
        Lettuce(piece, 1),
        Tomato(piece, 2),
        PepperRed(piece, 1),
        Cucumber(piece, 1),
        Onion(piece, 2),
        SaladSauce(piece, 1),
        Champignon(piece, 6),
        Zucchini(piece, 1),
        BarbecueMeat(piece, 1)
    ]


class Tortellini(Recipe):
    name = "Tortellini"
    ingredients = [
        TortelliniDried(piece, 2),
        TomatoSauce(piece, 2),
        Onion(piece, 2),
        ParmesanCheese(piece, 1)
    ]


class Waffles(Recipe):
    name = "Waffeln"
    ingredients = [
        WheatFlour(gram, 300),
        BakingPowder(gram, 10),
        CaneSugar(gram, 75),
        Egg(piece, 2),
        Milk(gram, 500)
    ]


class ToastHawaii(Recipe):
    name = "Toast Hawaii"
    ingredients = [
        ToastbreadWheatSlice(piece, 10),
        SandwichCheese(piece, 10),
        PineapplesSlicesPickled(piece, 10),
        HamCooked(piece, 1)
    ]


class CheeseNoodles(Recipe):
    name = "Käsespätzle"
    ingredients = [
        SpaetzleNoodles(piece, 1),
        SpaetzleCheese(piece, 1),
        Onion(piece, 4)
    ]


class SpaghettiWithTomatosauce(Recipe):
    name = "Spaghetti (mit Tomatensauce)"
    ingredients = [
        SpaghettiNoodles(gram, 500),
        TomatoSauce(piece, 2),
        Onion(piece, 2),
        ParmesanCheese(piece, 1)
    ]


class SpaghettiAglioOlio(Recipe):
    name = "Spaghetti Aglio Olio"
    ingredients = [
        SpaghettiNoodles(gram, 400),
        Garlic(piece, 5),
        Lemon(piece, 1)
    ]


class PepperStew(Recipe):
    name = "Paprikapfanne"
    ingredients = [
        PepperRed(piece, 3),
        PepperYellow(piece, 3),
        Tomato(piece, 4),
        Onion(gram, 500)
    ]
