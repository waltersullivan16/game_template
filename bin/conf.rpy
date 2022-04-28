## jump to other conf files
"gui_.rpy"
"characters_base.rpy"
"functions.rpy"
"screens_.rpy"
"music.rpy"
"images_python.rpy"

## common files
"../characters.rpy"
"../images.rpy"
"../screens.rpy"

## script
"../scripts/chapter1/1a_poczatek.rpy"
"../scripts/chapter1/1b_szukanie_blowka.rpy"

init -12 python:
    import os
    import string
    from functools import partial
    from collections import namedtuple, defaultdict
    from itertools import chain
    import random

init -10 python:

    TITLE = "template"
    ## PATHS ##

    GAME_PATH = gpj('/home/akechi/renpy/games', TITLE, 'game')


    TEXTBOX_NAMES = {
        "main": "phoenixdb.png",
        "creepy": "creepy_textbox.png",
        "empty": "empty.png",
        "black": "black.png",
    }

init -11 python:

    if persistent.style is None:
        persistent.style = "main"

    mouse = lambda x: gpj("gui", "mouse", "{}.png".format(x))

    config.mouse = {
            "default": [(mouse("main"), 1, 0)],
            "main": [(mouse("main"), 1, 0)],
            "active": [(mouse("active"), 1, 0)],
            "red": [(mouse("red"), 1, 0)],
            "loading": [(mouse("loading"), 1, 0)],
            "not": [(mouse("not"), 1, 0)],
            "love": [(mouse("love"), 1, 0)],
            "question": [(mouse("question"), 1, 0)],
    } 
    
    #_dismiss_pause = False

init -1 python:
    AUTOMATIC_IMAGES = ["/"]

    AUTOMATIC_IMAGES_STRIP = ["images"] + get_dirs("images")
    
    for x in ["scenes", "others"]:
        AUTOMATIC_IMAGES_STRIP += get_dirs(gpj("images", x))

    renpy.music.register_channel("sfx1", "sfx")
    renpy.music.register_channel("sfx2")#, "sfx")


define config.window_show_transition = dissolve
define config.layers = [ 'master', 'transient', 'topcia', 'screens', 'overlay']
define config.say_menu_text_filter = alter_say_strings
define config.menu_include_disabled = True
define config.label_callback = label_callback
#define config.menu_arguments_callback = True

default preferences.show_empty_window = False
default preferences.text_cps = 40
default menuset = set()
