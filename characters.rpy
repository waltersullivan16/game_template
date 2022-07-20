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

    wardega_nvl = Character(None, kind=nvl)

###################### KONOPSKI ###########################
    
    KonopskiClass = CharacterBase("Konopski")
    Konopski = KonopskiClass.char
#define config.speaking_attribute = "talking"

    
layeredimage konopski:
    #image_format "images/characters/konopski/[persistent.version]/{image}.png"

    group body if_not "phoenix" auto variant "main":# prefix "body":
        attribute main default

    group body if_not "main" auto variant "phoenix":# prefix "body":
        attribute zawstydzenie default

    if KonopskiClass.talking:
        KonopskiClass.animations_switch

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
    
    RevoClass = CharacterBase("Revo", at_list=[Position(xpos=0.7)])
    Revo = RevoClass.char

layeredimage revo:
    group head auto:
        attribute main default
    if RevoClass.talking:
        RevoClass.animations_switch
    group suit auto:
        attribute normal default

###################### WARDEGA ###########################

init python:
    WardegaClass = CharacterBase("Wardega")#, at_list=[Position(xpos=0.7)])
    Wardega = WardegaClass.char

    WardegaClass.character_image()

layeredimage wardegea:
    group head auto:
        attribute serious default
    if WardegaClass.talking:
        WardegaClass.animations_switch

    group suit auto:
        attribute main default

default w_pose = "serious"
default wardega_head = "serious"
default wardega_suit = "main"
init python:
    renpy.image("mouth_w2", [
    "characters/wardega/mouth/wardega_mouth_[w_pose].png",
    "alpha 0.0",
    "pause 0.2",
    "alpha 1.0",
    "pause 0.2"])
image mouth_w:
    "characters/wardega/mouth/wardega_mouth_[w_pose].png"
    alpha 0.0
    pause 0.2
    alpha 1.0
    pause 0.2
    repeat
image wardega=WardegaClass.character_image()

image wardega2 = LiveComposite((782, 705),
    (0, 0), "characters/wardega/head/wardega_head_[w_pose].png",
    (0, 0), ConditionSwitch(
        "WardegaClass.talking", "mouth_w2",
        "True", Null()), 
    (0, 0), "characters/wardega/suit/wardega_suit_main.png"
)

###################### Lexio ###########################

init python:
    
    LexioClass = CharacterBase("Lexio", at_list=[Position(ypos=0.715)])
    Lexio = LexioClass.char

layeredimage lexio:
    group body:
        attribute main default

    if LexioClass.talking:
        LexioClass.animations_switch

###################### PEARL ###########################

init python:
    PearlClass = CharacterBase("pearl", group="dziewczyny", who_size=35) 
    Pearl = PearlClass.char
    Pearl.name = "nieletnia baba"

layeredimage pearl:
    group body auto:
        attribute main default
    if PearlClass.talking:
        PearlClass.animations_switch

### EMA ###
init python:
    EmaClass = CharacterBase("ema", group="dziewczyny", who_size=35)
    Ema = EmaClass.char
    #Ema.image = "ema"
    Ema.name = "dziwna baba"

layeredimage ema:
    group body auto:
        attribute main default
    if EmaClass.talking:
        EmaClass.animations_switch

### penny ###
init python:
    PennyClass = CharacterBase("penny", group="dziewczyny", who_size=35)
    Penny = PennyClass.char
    Penny.name = "brzydka baba"

layeredimage penny:
    group body auto:
        attribute main default
    if PennyClass.talking:
        PennyClass.animations_switch

init python:
    NajmanClass = CharacterBase("Najman", group="straznicy")
    Najman = NajmanClass.char
layeredimage najman:
    group body auto:
        attribute main default
    if NajmanClass.talking:
        NajmanClass.animations_switch

init python:
    LilMastiClass = CharacterBase("LilMasti", group="straznicy")
    LilMasti = LilMastiClass.char

layeredimage lilmasti: 
    #image_format "lilmasti/body/lilmasti {image}.png"

    group body if_not "bajka" auto variant "fighter":
        at Position(ypos=900)
        attribute main2 default

    group body if_not "fighter" auto variant "bajka":
        attribute normal default

    if LilMastiClass.talking:
        at Position(ypos=900)
        LilMastiClass.animations_switch

    group reaction:
        xpos 0.4
        zoom 0.3
        attribute normal default null
        attribute angry "reaction_angry"
        attribute angry2 "reaction_angry2"
'''
    group body if_not "bajka" auto variant "fighter":
        at Position(ypos=900)
        attribute main default
'''

init python:
    BoxdelClass = CharacterBase("Boxdel", group="reszta")
    Boxdel = BoxdelClass.char
    renpy.image("bb", animation_maker("boxdel", "main"))
    renpy.image("ds", BoxdelClass.animations_switch)

layeredimage boxdel:
    group body auto:
        attribute main default
    if BoxdelClass.talking:
        BoxdelClass.animations_switch


init python:
    UlfikClass = CharacterBase("Ulfik", group="reszta")
    Ulfik = UlfikClass.char
layeredimage ulfik:
    group body auto:
        attribute main default
    if UlfikClass.talking:
        UlfikClass.animations_switch
