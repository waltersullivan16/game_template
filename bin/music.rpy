" ../files_list.rpy"
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
        "king": "king",
    }

    def music(name):
        return gpj("music", "soundtrack", "{}.mp3".format(SOUNDTRACK[name]))

    def sound(name):
        return gpj("music","sound effects", "{}.mp3".format(name))

    def video(name):
        return gpj("videos", "{}.webm".format(name))
    

    config.main_menu_music = music("chipdale")

    def play_music(name, fadein=0.0, fadeout=0.1, loop=True):
        renpy.music.play(music(name), channel="music", fadein=fadein, fadeout=fadeout, loop=loop)

    def play_sound_effect(name, channel="sfx1", loop=False, relative_volume=1.0):
        renpy.music.play(sound(name), channel=channel, loop=loop, relative_volume=relative_volume)#relative_volume)

    def stop_music(fadeout=1.0):
        renpy.music.stop(channel="music", fadeout=fadeout)

    def stop_sound_effect():
        renpy.music.stop(channel="sound")

    def play_video(name):
        renpy.movie_cutscene(video(name))

    config.default_music_volume = 0.5
