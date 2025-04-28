
class RGB:
    def __init__(self, Red, Blue, Green):
        self.RGBVal1 = Red
        self.RGBVal2 = Blue
        self.RGBVal3 = Green

L1 = RGB(255, 0, 0)
L2 = RGB(0, 255, 0)
L3 = RGB(0, 0, 255)

RGBs = [L1, L2, L3]
for RGBs in RGBs:
    print(RGBs.RGBVal1)
    print(RGBs.RGBVal2)
    print(RGBs.RGBVal3)
#Lit 3 bouton et retourne message d erreur si..
def readButtons():
    return (True, False, True, "You lose")

(isBoutonPressed1, isBoutonPressed2, isBoutonPressed3, YouLose) = readButtons()
if YouLose == "OK":
    print("isBoutonPressed1")
    print("isBoutonPressed2")
    print("isBoutonPressed3")
else:
    print("There is an" + " L + SKILL_ISSUE")

nomEtAgePersonnes = [("Esteban", True, 19), ("Jerry", True, 13)]
for nom, alive, age in nomEtAgePersonnes:
    print(nom)
    print(alive)
    print(age)


RGB1 = {"RED": 255, "GREEN": 0, "BLUE": 0}
RGB2 = {"RED": 0, "GREEN": 255, "BLUE": 0}
RGB3 = {"RED": 0, "GREEN": 0, "BLUE": 255}
LEDset = [RGB1, RGB2, RGB3]
for LEDset in LEDset:
    print(LEDset["RED"])
    print(LEDset["BLUE"])
    print(LEDset["GREEN"])

