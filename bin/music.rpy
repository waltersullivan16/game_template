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

    def music(name):
        return gpj("music", "soundtrack", "{}.mp3".format(name))

    def sound(name, group=""):
        return gpj("music","sound effects", group, "{}.mp3".format(name))

    def video(name, group=""):
        return gpj("videos", group, "{}.webm".format(name))

    def get_blip(b):
        n = "blip_{}".format(b)
        path = gpj("music", "sound effects", "{}.mp3".format(n))
        #print(n, path)
        return n if os.path.exists(gpj("music", "sound effects", "{}.mp3".format(n))) else "blip_main"
        
    config.main_menu_music = music("chipdale")

    def play_music(name, fadein=0.0, fadeout=0.1, loop=True, relative_volume=0.5):
        renpy.music.play(music(name), channel="music", fadein=fadein, fadeout=fadeout, loop=loop, relative_volume=relative_volume)

    def play_sound_effect(name, channel="sfx1", loop=False, relative_volume=1.0, group=""):
        renpy.music.play(sound(name, group), channel=channel, loop=loop, relative_volume=relative_volume)#relative_volume)

    def stop_music(fadeout=1.0):
        renpy.music.stop(channel="music", fadeout=fadeout)

    def stop_sound_effect(channel="sound"):
        renpy.music.stop(channel=channel)

    def play_video(name, stop_music=True, group=""):
        renpy.movie_cutscene(video(name, group=group), stop_music=stop_music)

    def mute(channel="music", m=True):
        preferences.set_mute(channel, m)

    def mute_blip(m=True):
        mute("sfx", m)

    config.default_music_volume = 0.5
