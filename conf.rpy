init -10 python:
    import os
    import string
    from functools import partial
    from collections import namedtuple
    from itertools import chain

    ## PATHS ##

    GAME_PATH = os.path.abspath(os.getcwd())
    IMAGES_PATH = os.path.join(GAME_PATH, "images")
    TEXTBOX_PATH = os.path.join("gui", "textbox")

    ## CHARACTERS ##

    get_character_path = lambda c, prefix='': os.path.join(IMAGES_PATH, c, prefix)
    get_character_animation_path = lambda c: os.path.join(IMAGES_PATH, c, "animations")

    ANIMATION_PAUSE = 0.2

    COMPOSITION = {}

    ## FONTS ##

    FONTS_PATH = os.path.join("gui", "fonts")
    get_font = lambda font: os.path.join(FONTS_PATH, font)

    FONT_CHERI = get_font("CHERI___.TTF")
    FONT_UBUNTU = get_font("Ubuntu-Regular.ttf")
    FONT_BUBBLEGUM = get_font("Bubblegum.ttf")

    FONT_SIZE = 25
    FONT_SIZE_NAME = 55

    FONT_TEXT = FONT_UBUNTU
    FONT_NAME = FONT_BUBBLEGUM

    AUTOMATIC_IMAGES = ["/"]
    AUTOMATIC_IMAGES_STRIP = ["images"]

    ###### FUNCTIONS ######


    def char_talking(character, event, **kwargs):
        if event == "show":
            character.talking = True
            renpy.music.play("music/blip.mp3", channel="sound", loop="True")
        elif event in ["end", "slow_done"]:
            character.talking = False
            renpy.music.stop(channel="sound")


    def animation_maker(character, animation_name, animation_pause=ANIMATION_PAUSE):
        files = [os.path.splitext(f)[0].split(" ") for f in os.listdir(get_character_animation_path(character))]
        files = list(filter(lambda f: f[0] == character and f[1] == animation_name, files))
        return list(chain.from_iterable([[' '.join(f), animation_pause] for f in files]))

    def emotion_maker(character, emotion):
        arr = list(map(lambda x: int(x), renpy.get_image_bounds(character)))
        renpy.show(emotion, atl=Position(arr[0], arr[2]))

    def comic_text_maker(text, bubble=BUBBLE):
        return LiveComposite(
            renpy.image_size(bubble),
            (0, 0), bubble,
            (0.0, 0.0), Text(text, style="bum"))#"top_text \"{}\"".format(text))

    #mouth_animation = lambda c: animation_maker(c, "mouth")

    ###### TRANSITIONS AND TRANFORMATIONS ######
#

