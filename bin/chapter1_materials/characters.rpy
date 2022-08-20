#"files_list.rpy"
#
####################### PEARL ###########################
#
#init python:
#    PearlClass = CharacterBase("pearl", group="dziewczyny", who_size=35) 
#    Pearl = PearlClass.char
#    Pearl.name = "nieletnia baba"
#
#layeredimage pearl:
#    group body auto:
#        attribute main default
#    if PearlClass.talking:
#        PearlClass.animations_switch
#
#### EMA ###
#init python:
#    EmaClass = CharacterBase("ema", group="dziewczyny", who_size=35)
#    Ema = EmaClass.char
#    #Ema.image = "ema"
#    Ema.name = "dziwna baba"
#
#layeredimage ema:
#    group body auto:
#        attribute main default
#    if EmaClass.talking:
#        EmaClass.animations_switch
#
#### penny ###
#init python:
#    PennyClass = CharacterBase("penny", group="dziewczyny", who_size=35)
#    Penny = PennyClass.char
#    Penny.name = "brzydka baba"
#
#layeredimage penny:
#    group body auto:
#        attribute main default
#    if PennyClass.talking:
#        PennyClass.animations_switch
#
#init python:
#    NajmanClass = CharacterBase("Najman", group="straznicy")
#    Najman = NajmanClass.char
#layeredimage najman:
#    group body auto:
#        attribute main default
#    if NajmanClass.talking:
#        NajmanClass.animations_switch
#
#init python:
#    LilMastiClass = CharacterBase("LilMasti", group="straznicy")
#    LilMasti = LilMastiClass.char
#
#layeredimage lilmasti: 
#    #image_format "lilmasti/body/lilmasti {image}.png"
#
#    group body if_not "bajka" auto variant "fighter":
#        at Position(ypos=900)
#        attribute main2 default
#
#    group body if_not "fighter" auto variant "bajka":
#        attribute normal default
#
#    if LilMastiClass.talking:
#        at Position(ypos=900)
#        LilMastiClass.animations_switch
#
#    group reaction:
#        xpos 0.4
#        zoom 0.3
#        attribute normal default null
#        attribute angry "reaction_angry"
#        attribute angry2 "reaction_angry2"
#'''
#    group body if_not "bajka" auto variant "fighter":
#        at Position(ypos=900)
#        attribute main default
#'''
#
#init python:
#    BoxdelClass = CharacterBase("Boxdel", group="reszta")
#    Boxdel = BoxdelClass.char
#    renpy.image("bb", animation_maker("boxdel", "main"))
#    renpy.image("ds", BoxdelClass.animations_switch)
#
#layeredimage boxdel:
#    group body auto:
#        attribute main default
#    if BoxdelClass.talking:
#        BoxdelClass.animations_switch
#
#
#init python:
#    UlfikClass = CharacterBase("Ulfik", group="reszta")
#    Ulfik = UlfikClass.char
#layeredimage ulfik:
#    group body auto:
#        attribute main default
#    if UlfikClass.talking:
#        UlfikClass.animations_switch
