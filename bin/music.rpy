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
"../scripts/chapter1/1a_poczatek.rpy"

init -10 python:
    def music(name):
        return gpj(["music", "{}.mp3".format(name)])
    
    SOUND_EFFECTS = {
        "blip": "blip",
        "badum": "badum",
        "punch": "punch",
    }
    # SOUNDTRACK: [beg, main_menu, wind, pearl, lobby]

    config.main_menu_music = music("main_menu")

    def play_music(name, loop=True):
        renpy.music.play(music(name), channel="music", fadein=2.0, fadeout=1.0, loop=loop)

    def stop_music(channel="music", fadeout=1.0):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    def play_sound_effect(name, loop=False):
        renpy.music.play(music(name), channel="sound", loop=loop)

    config.default_music_volume = 0.5
    SOUNDTRACK = {
        "intro": "beg",
        "lobby": "lobby",
        "scary": "wind",
        "dziewczyny1": "pearl",
        "dziewczyny2": "dziewczyny2",
        "gazeta": "gazeta",
        "straznik": "straznik",
    }
