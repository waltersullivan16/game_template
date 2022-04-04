"../files_list.txt"

### KONOPSKI ###
#image konopski = ConditionSwitch(
#    "KonopskiClass.talking == True", aKonopski("confused"),
#    "True", "konopski_body_confused")
init -8 python:
    
    styles = ["main", "smirk", "thinking", "ej", "p2", "lol"]
    KonopskiClass = CharacterBase("Konopski", styles=styles)
    Konopski = KonopskiClass.char


layeredimage konopski:
    group body auto:
        attribute main default

    if KonopskiClass.talking:
        KonopskiClass.animations_switch

    group anime auto:
        attribute normal default null

    group reaction:
        xpos 201
        attribute normal default null
        attribute kropla "reaction_sweatdrop"
        attribute angry "reaction_angry"
        attribute danger "reaction_danger"
        attribute flower "flowers"
        attribute question "question" xpos 350 zoom 0.6

layeredimage konopski_phoenix:

    group head auto:
        attribute normal default null
    group suit auto:
        attribute normal default null
      

### PEARL ###
init python:
    styles = ["main", "serious", "embarassed", "sad", "crying", "determined", "pleased", "suprised"]
    PearlClass = CharacterBase("Pearl", styles)
    Pearl = PearlClass.char
#Nieletnia

layeredimage pearl:
    group body auto:
        attribute main default
    if PearlClass.talking:
        PearlClass.animations_switch

### EMA ###
init python:
    styles = ["main","confused", "determined", "happy", "notes", "sad", "shocked", "thinking"]
    EmaClass = CharacterBase("Ema", styles)
    Ema = EmaClass.char

layeredimage ema:
    group body auto:
        attribute main default
    if EmaClass.talking:
        EmaClass.animations_switch
### penny ###
init python:
    styles = ["main", "cards", "gossip"]
    PennyClass = CharacterBase("Penny", styles)
    Penny = PennyClass.char

layeredimage penny:
    group body auto:
        attribute main default
    if PennyClass.talking:
        PennyClass.animations_switch

init python:
    NajmanClass = CharacterBase("Najman", ["main"])
    Najman = NajmanClass.char
layeredimage najman:
    group body auto:
        attribute main default
    if NajmanClass.talking:
        NajmanClass.animations_switch

init python:
    LilMastiClass = CharacterBase("LilMasti", ["main"])
    LilMasti = LilMastiClass.char

layeredimage lilmasti: 
    group body auto:
        attribute main default
    if LilMastiClass.talking:
        LilMastiClass.animations_switch
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
