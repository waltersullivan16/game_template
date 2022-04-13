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

init -10 python:

    TITLE = "template"
    ## PATHS ##

    GAME_PATH = gpj('/home/akechi/renpy/games', TITLE, 'game')
    PATHS = {
        "images": gpj(GAME_PATH, "images"),
    }
    PATHS["characters"] = gpj(PATHS["images"], "characters")
    PATHS["animations"] = lambda c, animation_name: gpj(PATHS["characters"], c, "animations", animation_name)
    PATHS["reactions"] = gpj(PATHS["images"], "reactions")

    AUTOMATIC_IMAGES = ["/"]
    AUTOMATIC_IMAGES_STRIP = [
        "images", "characters", "background", "scenes",
        "others", "ulubione", "transparenty", "transparenty2", 
        "reactions", "transitions", "title", "dziewczyny", "straznicy"]

    ANIMATION_PAUSE = 0.2

    TEXTBOX_NAMES = {
        "main": "phoenixdb.png",
        "multiple": "empty.png",
        "creepy": "creepy_textbox.png",
        "intro": "empty.png",
        "www": "empty.png",
        "empty": "empty.png",
        "black": "black.png",
    }

init -11 python:
    print(persistent.style)

    if persistent.style is None:
        persistent.style = "main"
        persistent.style_class = MainStyle

    if persistent.cursor is None:
        persistent.cursor = "main"
    mouse = lambda x: "gui/mouse/{}.png".format(x)

    def change_cursor(cursor):
        persistent.cursor = cursor
        config.mouse["default"] = config.mouse[cursor]

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
    
    persistent.talking_mode = "normal"
    persistent.lock = False
    persistent.stop_lipsync = False
    #_dismiss_pause = False
    renpy.music.register_channel("sfx1", "sfx")

define config.window_show_transition = dissolve
define config.layers = [ 'master', 'transient', 'topcia', 'screens', 'overlay']
define config.say_menu_text_filter = alter_say_strings
default preferences.show_empty_window = False
default preferences.text_cps = 40
