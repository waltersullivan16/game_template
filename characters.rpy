## jump to other conf files
"../files_list.txt"

### KONOPSKI ###
#image konopski = ConditionSwitch(
#    "KonopskiClass.talking == True", aKonopski("confused"),
#    "True", "konopski_body_confused")
init python:
    KonopskiClass.add_styles(["main", "smirk", "thinking", "ej", "ej_happy", "ej_angry"])

layeredimage konopski:
    group body auto:
        attribute main default

    if KonopskiClass.talking:
        KonopskiClass.animations_switch

    group reaction:
        xpos 201
        attribute normal default null
        attribute kropla "reaction_sweatdrop"
        attribute flower "flowers"
        attribute angry "reaction_angry"


### PEARL ###
init python:
    PearlClass.add_styles(["main", "serious", "embarassed", "sad", "crying", "determined", "pleased", "suprised"])

layeredimage pearl:
    group body auto:
        attribute main default
    if PearlClass.talking:
        PearlClass.animations_switch

### EMA ###
init python:
    EmaClass.add_styles(["main","confused", "determined", "happy", "notes", "sad", "shocked", "thinking"])

layeredimage ema:
    group body auto:
        attribute main default
    if EmaClass.talking:
        EmaClass.animations_switch

### penny ###
init python:
    PennyClass.add_styles(["main", "cards", "gossip"])

layeredimage penny:
    group body auto:
        attribute main default
    if PennyClass.talking:
        PennyClass.animations_switch

'''
    define WardegaC = Characterr("Wardega")
    define Wardega = WardegaC.char

    layeredimage wardega:
        group body auto:
            attribute main default

    define KonopskiC = Characterr("Konopski")
    define m = KonopskiC.mouth



    define RevoC = Characterr("Revo")
    define Revo = RevoC.char

    define GimperC = Characterr("Gimper")
    define Gimper = GimperC.char

    define LexioC = Characterr("Lexio")
    define Lexio = LexioC.char


    #    if WardegaC.talking:
    #        WardegaC.mouth at WardegaC.mouth_pos
    layeredimage revo:
        group body auto:
            attribute main default

    layeredimage gimper:
        group body auto:
            attribute main default

    layeredimage lexio:
        group body auto:
            attribute main default


    define Dziewczyna2C = Characterr("Dziewczyna2")
    define Dziewczyna2 = Dziewczyna2C.char

    layeredimage dziewczyna2:
        group body auto:
            attribute main default

    define Dziewczyna3C = Characterr("Dziewczyna3")
    define Dziewczyna3 = Dziewczyna3C.char

    layeredimage dziewczyna3:
        group body auto:
            attribute main default
'''
