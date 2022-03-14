## jump to other conf files
"gui_.rpy"
"characters_base.rpy"
"functions.rpy"
"screens_.rpy"
"music.rpy"

## common files
"../characters.rpy"
"../images.rpy"
"../screens.rpy"

## script
"../scripts/chapter1/1a_poczatek.rpy"

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
        "text" : gpj([GAME_PATH, "text.txt"]),
        "music" : gpj([GAME_PATH, "music"]),
        "mouse": gpj(["others/mouse"]),
    }
    PATHS["reactions"] = gpj(["images", "reactions"])
    PATHS["characters"] = lambda c, type="": gpj([PATHS["images"], "characters", c, type])
    PATHS["animations"] = lambda c, animation_name: gpj([PATHS["characters"](c, "animations"), animation_name])

    def font(font_name):
        return PATHS["fonts"]("{}.ttf".format(font_name))

    FONT_SIZE = 25
    FONT_SIZE_NAME = 50

    FONT_TEXT = font("ubuntu")
    FONT_NAME = font("lucky")

    AUTOMATIC_IMAGES = ["/"]
    AUTOMATIC_IMAGES_STRIP = [
        "images", "characters", "background", "scenes",
        "others", "ulubione", "transparenty", "transparenty2", 
        "reactions", "transitions", "title"]

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

init -8 python:

    if persistent.style is None:
        persistent.style = "main"
        persistent.style_class = MainStyle

    if persistent.cursor is None:
        print(persistent.cursor, "serop")
        persistent.cursor = "main"
    mouse = lambda x: "others/mouse/{}.png".format(x)

    def change_cursor(cursor):
        persistent.cursor = cursor
        config.mouse["default"] = config.mouse[cursor]

    config.mouse = {
            "default": [(mouse("main"), 1, 1)],
            "main": [(mouse("main"), 1, 1)],
            "green": [(mouse("green"), 1, 1)],
            "red": [(mouse("red"), 1, 1)],
            "loading": [(mouse("loading"), 1, 1)],
            "not": [(mouse("not"), 1, 1)],
            "love": [(mouse("love"), 1, 1)],
            "question": [(mouse("question"), 1, 1)],
    } 
    
    _dismiss_pause = False

define config.window_show_transition = dissolve
define config.layers = [ 'master', 'transient', 'topcia', 'screens', 'overlay']
#define config.say_menu_text_filter = alter_say_strings
