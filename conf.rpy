init -10 python:
    import os
    import string
    from functools import partial
    from collections import namedtuple
    from itertools import chain

    ## PATHS ##
    title = "template"
    GAME_PATH = os.path.join('/home/akechi/lajno', title, 'game')
    IMAGES_PATH = os.path.join(GAME_PATH, "images")
    TEXTBOX_PATH = os.path.join("gui", "textbox")

    ## CHARACTERS ##

    get_character_path = lambda c, prefix='': os.path.join(IMAGES_PATH, "characters", c, prefix)
    get_character_animation_path = lambda c: os.path.join(IMAGES_PATH, "characters", c, "animations")

    ANIMATION_PAUSE = 0.2


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
    AUTOMATIC_IMAGES_STRIP = ["images", "images/characters"]

    ###### FUNCTIONS ######
    import glob

    def char_talking(character, event, **kwargs):
        if event == "show":
            character.talking = True
            renpy.music.play("music/blip.mp3", channel="sound", loop="True")
        elif event in ["end", "slow_done"]:
            character.talking = False
            renpy.music.stop(channel="sound")

    print(glob.glob(GAME_PATH),"fdfsf")

    def animation_maker(character, animation_name, animation_pause=ANIMATION_PAUSE):
        files = [os.path.splitext(f)[0].split(" ") for f in os.listdir(get_character_animation_path(character))]
        files = list(filter(lambda f: f[0] == character and f[1] == animation_name, files))
        return list(chain.from_iterable([[' '.join(f), animation_pause] for f in files]))

    def emotion_maker(character, emotion):
        arr = list(map(lambda x: int(x), renpy.get_image_bounds(character)))
        renpy.show(emotion, atl=Position(arr[0], arr[2]))

    def comic_text_maker(text, bubble):
        return LiveComposite(
            renpy.image_size(bubble),
            (0, 0), bubble,
            (0.0, 0.0), Text(text, style="bum"))#"top_text \"{}\"".format(text))

    def reactions(c):
        for r in os.listdir(os.path.join(IMAGES_PATH, 'reactions')):
            print("{}_{}_{}".format(c, 'reactions', r.split('.')[0]))
            #renpy.image("{}_{}_{}".format(c, 'reactions', r), os.path.join('reactions', r))

#        for dir_name in os.listdir(get_character_path(character)):
#            print(dir_name)
#            for img in os.listdir(dir_name):
#                print(img)
#                renpy.image('{}_{}_{}'.format(character, dir_name, img), Image(img))
#
    mouth_animation = lambda c: animation_maker(c, "mouth")

    ###### TRANSITIONS AND TRANFORMATIONS ######
#

