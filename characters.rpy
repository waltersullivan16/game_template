"files_list.rpy"

init python:

    Unknown = Character(name = "???")
    Blank = Character(name = "")

    Straznik = Character(name = "STRAŻNIK")#, what_style="straznik_text")

    BlankBlipClass = CharacterBase(name="")#, blip="blip")
    BlankBlip = BlankBlipClass.char
    narrator = Character(None, kind=nvl)
    d1 = Character(None, kind=nvl, what_font=font("kalam"), window_left_margin=100, what_size=40, what_color=color("pink"))
    d2 = Character(None, kind=nvl, what_font=font("kalam"), what_size=40, what_color=color("light_pink"))
    d3 = Character(None, kind=nvl, what_font=font("kalam"), what_size=40, what_color=color("bright_pink"))

    nvl_wardega = Character(None, kind=nvl, what_slow_cps=20)

init python:
    poses = {
       "main": {"head": "main", "suit": "main"},
       "thinking": {"head": "wprost_otwarte", "suit": "thinking"},
       "kartka": {"head": "cocky", "suit": "kartka"},
       "objection": {"head": "objection", "suit": "objection"},
       "wtf": {"head": "wtf", "suit": "normal"},
       "kropla": {"head": "kropla", "suit": "kropla"},
       "zawstydzenie": {"head": "zawstydzenie", "suit": "zawstydzenie"},
       "wtf_moment": {"head": "wtf", "suit": "thinking"},
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
    pose_map = {
        "wtf_moment": {"head": "main"},
        "kartka": {"head": "main", "suit": "kartka"},
        "objection": {"head": "main", "suit": "objection"},
    }
    RevoClass = CharacterBase("Revo", at_list=[Position(xpos=0.7)], size=(748, 631), pose_map=pose_map)
    Revo = RevoClass.char
    
###################### WARDEGA ###########################

init python:

# HEADS
# duma, egzaltacja, egzaltacja2, main, obrzydzenie, politowanie, rezygnacja, smirk, smirk2, smutek,
# thinking, wkurw, 
# wtf: zaskoczone oczy skierowane na widownię
# wtf2: zaskoczone oczy skierowane na konopskiego

# SUITS
# main, rozlozone, palec, kartka
 
    pose_map = {
        "wkurw": {"head": "wkurw", "suit": "palec"},
        "pogarda": {"head": "smirk2", "suit": "rozlozone"},
        "smirk": {"head": "smirk", "suit": "rozlozone"},
        "kartka": {"head": "main", "suit": "kartka"},
        "serious": {"head": "main", "suit": "palec"},
        "wtf_moment": {"head": "wkurw"},
        "objection": {"head": "objection", "suit": "objection"}
    }

    WardegaClass = CharacterBase("Wardega", size=(1063, 720), pose_map=pose_map)#, at_list=[Position(xpos=0.7)])
    Wardega = WardegaClass.char

###################### Lexio ###########################

init python:
    
    pose_map = {
        "wkurw": {"head": "pretensja"},
        "wtf_moment": {"head": "politowanie"},
    }
    LexioClass = CharacterBase("Lexio", at_list=[Position(xpos=0.55, ypos=0.84)], pose_map=pose_map, size=(543, 503))
    Lexio = LexioClass.char
    Lexio.name = "Leksiu"
