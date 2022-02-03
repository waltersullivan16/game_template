init -10 python:
    import os
    import string
    from functools import partial
    from collections import namedtuple
    from itertools import chain

    ## PATHS ##
    title = "objection"
    GAME_PATH = os.path.join('/home/akechi/lajno', title, 'game')
    PATHS = {
        "images": os.path.join(GAME_PATH, "images"),
        "textbox": os.path.join("gui", "textbox"),
        "fonts": lambda font: os.path.join("gui", "fonts", font)
    }

    ## CHARACTERS ##

    get_character_path = lambda c, prefix='': os.path.join(PATHS["images"], "characters", c, prefix)
    get_character_animation_path = lambda c: os.path.join(PATHS["images"], "characters", c, "animations")

    ANIMATION_PAUSE = 0.2

    ## FONTS ##

    FONTS = {
        "cheri": PATHS["fonts"]("CHERI___.TTF"),
        "ubuntu": PATHS["fonts"]("ubuntu-regular.ttf"),
        "bubblegum": PATHS["fonts"]("bubblegum.ttf"),
        "superc": PATHS["fonts"]("superc.ttf"),
        "fjalla": PATHS["fonts"]("fjalla.ttf"),
        "exo": PATHS["fonts"]("exo.ttf"),
        "lucky": PATHS["fonts"]("lucky.ttf"),
    }

    FONT_SIZE = 25
    FONT_SIZE_NAME = 50

    FONT_TEXT = FONTS["ubuntu"]
    FONT_NAME = FONTS["lucky"]

    AUTOMATIC_IMAGES = ["/"]
    AUTOMATIC_IMAGES_STRIP = ["images", "images/characters", "images/characters/dziewczyny"]

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


    def comic_text_maker(text, bubble):
        return LiveComposite(
            renpy.image_size(bubble),
            (0, 0), bubble,
            (0.0, 0.0), Text(text, style="bum"))#"top_text \"{}\"".format(text))


    def reactions(c):
        for r in os.listdir(os.path.join(PATHS["images"], 'reactions')):
            print("{}_{}_{}".format(c, 'reactions', r.split('.')[0]))

    mouth_animation = lambda c: animation_maker(c, "mouth")


    def alter_say_strings(str_to_test, dot="0.5", comma="0.1"):
        str_map = {
            ". " : ". {{w={}}}".format(dot),
            ", " : ", {{w={}}}".format(comma),
        }
        for key in str_map:
            str_to_test = str_to_test.replace(key, str_map[key])
        return str_to_test


    def show_scene(background, characters):
        renpy.scene()
        renpy.show(background)
        for (c, t) in characters:
            renpy.show(c, at_list=t)

    def judge_scene(): {show_scene("judge", [(LexioC.name, LexioC.show_args)])}
    def pros_scene(): {show_scene(
        "prosecution",
        [("wardega", []), ("revo", [])]
    )}

    def defense_scene(): {show_scene("defense", [(KonopskiC.name, KonopskiC.show_args)])}
    def witness_scene(): {show_scene("witness", [(GimperC.name, GimperC.show_args)])}

    preferences.show_empty_window = False

define config.say_menu_text_filter = alter_say_strings
define TEXTBOX_NAME = "phoenixdb.png"

#### SCREENS ####

screen z():
    imagebutton:
        xalign 0.0
        yalign 0.0
        idle "gui/button/end.png"
        action Jump("end")

#### TRANSFORMATIONS ####

transform dropping:
    linear 1.5 yanchor -100
    pause 3.0


transform beating:
    zoom 1.2
    pause 0.2
    zoom 1.0
    pause 0.2
    repeat

transform bounce2:
    linear 3.0 xalign 1.0
    linear 3.0 xalign 0.0
    repeat


#### DIALOGUE BOX ###

style window:
    background Transform(Frame(os.path.join(PATHS["textbox"], TEXTBOX_NAME)), alpha=0.85)
    yalign 1.0
    ysize 300


style namebox:
    xalign 0.155
    yalign 0.3

style say_label:
    properties gui.text_properties("name", accent=True)


style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos 150
    ypos 0.5
    xsize 900#gui.dialogue_width
    line_spacing 7

style thoughts_dialogue:
    properties gui.text_properties("dialogue")
    xpos 150
    ypos 0.5
    xsize 900#gui.dialogue_width
    line_spacing 7

style bum:
    size 50
    xanchor -1.5 yanchor 0.5

style block2_multiple2_say_window:
    background Image(os.path.join("gui", "bubbled.png"))
    xpos 150
    ypos 0.5
    xsize 500
