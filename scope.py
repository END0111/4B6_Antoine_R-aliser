# ce programme est un exemple de programme python qui utilise des fonctions et des variables globales
import time
i = 0
ma_variable_argument = "ma_variable_argument"
ma_variable_globale = "ma_variable_globale"
def ma_variable_locale():
    ma_variable_locale = "ma_variable_locale"
    print(ma_variable_locale)
def my_argument(ma_variable_argument):
    print(ma_variable_argument)
for i in range(3):
    time.sleep(1)
    ma_variable_locale()
    my_argument(ma_variable_argument)
    print(ma_variable_globale)
    i += 1

    
    
    