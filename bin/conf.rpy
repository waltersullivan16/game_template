# list_files.rpy

init -12 python:
    import os
    import string
    from functools import partial
    from collections import namedtuple, defaultdict
    from itertools import chain
    import random

    TITLE = "template"
    GAME_PATH = gpj('/home/akechi/renpy/games', TITLE, 'game')
    #persistent.testing = True

init python:
    if persistent.count is None:
        persistent.count = 0
    else:
        persistent.count += 1
    print(persistent.count)

    if persistent.style is None:
        persistent.style = "main"
    if persistent.nvl is None:
        persistent.nvl = "main"
    if persistent.poses is None:
        persistent.poses = {}
    
    persistent.thinking = False

    mouse = lambda x: gpj("gui", "mouse", "{}.png".format(x))
    mouses_list = ["main", "active", "red", "loading", "not", "love", "question"]
    
    config.mouse = {n:[(mouse(n), 1, 0)] for n in mouses_list}
    config.mouse["default"] = [(mouse("main"), 1, 0)]
    
    _dismiss_pause = False

init -1 python:
    AUTOMATIC_IMAGES = ["/, _"]

    AUTOMATIC_IMAGES_STRIP = ["images"] + get_dirs("images")
    
    for x in ["scenes", "others", "background"]:
        AUTOMATIC_IMAGES_STRIP += get_dirs(gpj("images", x))
    renpy.music.register_channel("sfx1", "sfx")
    renpy.music.register_channel("sfx2")#n, "sfx")


define config.window_show_transition = dissolve
define config.layers = [ 'master', 'transient', 'topcia', 'screens', 'overlay']
define config.say_menu_text_filter = alter_say_strings
define config.menu_include_disabled = True
#define config.label_callback = label_callback
#define config.displayable_prefix["blur"] = blurred
#define config.menu_arguments_callback = True

default preferences.afm_time = 5
default preferences.afm_enable = True

default preferences.show_empty_window = False
default preferences.text_cps = 40
default menuset = set()
