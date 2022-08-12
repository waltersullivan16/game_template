"files_list.rpy"

init -8 python:

    Unknown = Character(name = "???")
    Blank = Character(name = "")

    Straznik = Character(name = "STRAŻNIK")#, what_style="straznik_text")

    BlankBlipClass = CharacterBase(name="")#, blip="blip")
    BlankBlip = BlankBlipClass.char
    narrator = Character(None, kind=nvl)
    d1 = Character(None, kind=nvl, what_font=font("kalam"), window_left_margin=100, what_size=40, what_color=color("pink"))
    d2 = Character(None, kind=nvl, what_font=font("kalam"), what_size=40, what_color=color("light_pink"))
    d3 = Character(None, kind=nvl, what_font=font("kalam"), what_size=40, what_color=color("bright_pink"))

    wardega_nvl = Character(None, kind=nvl, what_slow_cps=20)

###################### KONOPSKI ###########################
default konopski_head = "main"
default konopski_suit = "objection"

init python:
    
    poses = {
       "main": {"head": "main", "suit": "main"},
       "thinking": {"head": "main", "suit": "thinking"},
       "kartka": {"head": "cocky", "suit": "kartka"},
       "objection": {"head": "cocky", "suit": "objection"},
       "zawstydzenie": {"head": "zalamanie", "suit": "zawstydzenie"},
       "kropla": {"head": "main", "suit": "kropla"},
    }

    KonopskiClass = CharacterBase("Konopski", image="konopski_phoenix", size=(800, 800), version="phoenix", at_list=[Position(ypos=1.2)], pose_map=poses)
    Konopski = KonopskiClass.char


#define config.speaking_attribute = "talking"

layeredimage konopski:
    #image_format "images/characters/konopski/[persistent.version]/{image}.png"

    group body auto:# prefix "body":
        attribute main default

    #if KonopskiClass.talking:
    #    KonopskiClass.animations_switch

    group anime auto:
        attribute normal default null

    group reaction:
        xpos 201
        attribute normal default null
        attribute kropla "reaction_sweatdrop"
        attribute angry "reaction_angry"
        attribute flower "flowers"
        attribute question "question" xpos 350 zoom 0.6

###################### revo ###########################

init python:
    RevoClass = CharacterBase("Revo", at_list=[Position(xpos=0.7)], size=(748, 631))
    Revo = RevoClass.char
    
###################### WARDEGA ###########################

init python:
 
    pose_map = {
        "main": {"head": "main", "suit": "main"},
        "egzaltacja": {"head": "egzaltacja", "suit": "main"},
        "egzaltacja2": {"head": "egzaltacja2", "suit": "main"},
        "palec": {"head": "smirk", "suit": "palec"},
        "pogarda": {"head": "main", "suit": "rozlozone"},
        "kartka": {"head": "main", "suit": "kartka"},
        "wkurw": {"head": "main", "suit": "wkurw"},
    }

    WardegaClass = CharacterBase("Wardega", size=(782, 705), pose_map=pose_map)#, at_list=[Position(xpos=0.7)])
    Wardega = WardegaClass.char

###################### Lexio ###########################

init python:
    
    pose_map = {
        "main": {"head": "main", "suit": "main"},
    }
    LexioClass = CharacterBase("Lexio", at_list=[Position(ypos=0.715)], pose_map=pose_map)
    Lexio = LexioClass.char

layeredimage lexio:
    group body:
        attribute main default

    if LexioClass.talking:
        LexioClass.animations_switch
