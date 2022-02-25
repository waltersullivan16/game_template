## jump to other conf files
"gui_.rpy"
"characters_base.rpy"
"functions.rpy"

## common files
"../characters.rpy"
"../images.rpy"
"../screens.rpy"

## script
"../scripts/1_uwertura.rpy"

init -10 python:
# imports #
    import os
    import string
    from functools import partial
    from collections import namedtuple, defaultdict
    from itertools import chain

    TITLE = "template"
    #config.screen_width = 720
    #config.screen_height = 1280

    ## PATHS ##

    GAME_PATH = gpj(['/home/akechi/renpy/games', TITLE, 'game'])
    PATHS = {
        "images": gpj([GAME_PATH, "images"]),
        "textbox": gpj(["gui", "textbox"]),
        "fonts": lambda font: gpj(["gui", "fonts", font]),
        "text" : gpj([GAME_PATH, "text.txt"])
    }
    PATHS["reactions"] = gpj(["images", "reactions"])
    PATHS["characters"] = lambda c, type="": gpj([PATHS["images"], "characters", c, type])
    PATHS["animations"] = lambda c, animation_name: gpj([PATHS["characters"](c, "animations"), animation_name])

    ## FONTS ##
    FONTS_NAMES = ["cheri","ubuntu", "bubblegum", "superc", "fjalla", "exo", "lucky", "monster", "unique", "chomsky", "newspaper", "gothic", "deal"]
    FONTS = {font: PATHS["fonts"]("{}.ttf".format(font)) for font in FONTS_NAMES }

    FONT_SIZE = 25
    FONT_SIZE_NAME = 50

    FONT_TEXT = FONTS["ubuntu"]
    FONT_NAME = FONTS["lucky"]

    AUTOMATIC_IMAGES = ["/"]
    AUTOMATIC_IMAGES_STRIP = ["images", "images/characters", "background", "background/ulubione"]

    ANIMATION_PAUSE = 0.2

    TEXTBOX_NAMES = {
        "main": "phoenixdb.png",
        "multiple": "blank.png",
        "creepy": "creepy_textbox.png",
        "intro": "empty.png",
        "www": "empty.png",
        "empty": "empty.png",
    }

    if persistent.style is None:
        persistent.style = "main"

define config.say_menu_text_filter = alter_say_strings
