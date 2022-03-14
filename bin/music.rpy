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

    SOUNDTRACK = {
        "main": "main_menu",
        "intro": "beg",
        "lobby": "lobby",
        "scary": "wind",
        "dziewczyny1": "pearl",
        "dziewczyny2": "dziewczyny2",
        "gazeta": "gazeta",
        "straznik": "straznik",
        "title": "samurai",
        "chipdale": "chipdale",
    }
    def music(name):
        return gpj(["music", "{}.mp3".format(SOUNDTRACK[name])])

    def music_path(name):
        return gpj(["music", "{}.mp3".format(name)])
    
    # SOUND_EFFECTS = "blip", "badum", "punch"

    def sound(name):
        return music_path(SOUND_EFFECTS[name])

    config.main_menu_music = music("chipdale")

    def play_music(name, fadein=0.0, fadeout=0.1, loop=True):
        renpy.music.play(music(name), channel="music", fadein=fadein, fadeout=fadeout, loop=loop)

    def play_sound_effect(name, loop=False):
        renpy.music.play(music_path(name), channel="sound", loop=loop)

    def stop_music(channel="music", fadeout=1.0):
        renpy.music.stop(channel=channel, fadeout=fadeout)


    config.default_music_volume = 0.5
