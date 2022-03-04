## jump to other conf files
"gui_.rpy"
"characters_base.rpy"
"functions.rpy"
"screens_.rpy"

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
        "text" : gpj([GAME_PATH, "text.txt"]),
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
    AUTOMATIC_IMAGES_STRIP = ["images", "characters", "background", "others", "ulubione", "transparenty", "transparenty2"]

    ANIMATION_PAUSE = 0.2

    TEXTBOX_NAMES = {
        "main": "phoenixdb.png",
        "multiple": "empty.png",
        "creepy": "creepy_textbox.png",
        "intro": "empty.png",
        "www": "empty.png",
        "empty": "empty.png",
    }

    def music(name):
        return gpj(["music", "soundtrack", "{}.mp3".format(name)])

    def sound_effect(name):
        return gpj(["music", "sound effects", "{}.mp3".format(name)])

    BLIP_SOUND = sound_effect("blip")
    BADUM_SOUND = sound_effect("badum")

init -8 python:

    if persistent.style is None:
        persistent.style = "main"
        persistent.style_class = MainStyle
    persistent.blip = BLIP_SOUND
    if persistent.mouse is None:
        persistent.mouse = "default"

define config.say_menu_text_filter = alter_say_strings

init 1 python:
    def change_cursor():
        setattr(config, "mouse", {"default": [("others/myszka_{}.png".format(persistent.mouse), 1, 1)]})
    change_cursor()
