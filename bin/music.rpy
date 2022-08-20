" ../files_list.rpy"

init -10 python:

    def music(name):
        return gpj("music", "soundtrack", f"{name}.mp3")

    def sound(name, group=""):
        return gpj("music","sound effects", group, f"{name}.mp3")

    def video(name, group=""):
        return gpj("videos", group, f"{name}.webm")

    def get_blip(b):
        #n = "blip_{}".format(b)
        #path = gpj("music", "sound effects", "{}.mp3".format(n))
        path = gpj("music", "sound effects", f"blip_{b}.mp3")
        #print(n, path)
        #return n if os.path.exists(gpj("music", "sound effects", "{}.mp3".format(n))) else "blip_main"
        return f"blip_{b}" if os.path.exists(gpj("music", "sound effects", f"blip_{b}.mp3")) else "blip_main"
        
    config.main_menu_music = music("chipdale")

    def play_music(name, fadein=0.0, fadeout=0.1, loop=True, relative_volume=0.5):
        renpy.music.play(music(name), channel="music", fadein=fadein, fadeout=fadeout, loop=loop, relative_volume=relative_volume)

    def play_sound_effect(name, channel="sfx1", loop=False, relative_volume=1.0, group="", fadein=0):
        renpy.music.play(sound(name, group), channel=channel, fadein=fadein, loop=loop, relative_volume=relative_volume)#relative_volume)

    def stop_music(fadeout=1.0):
        renpy.music.stop(channel="music", fadeout=fadeout)

    def stop_sound_effect(channel="sound"):
        renpy.music.stop(channel=channel)

    def play_video(name, stop_music=True, group=""):#, volume=1):
        #renpy.music.set_volume(5, channel='movie')
        renpy.movie_cutscene(video(name, group=group), stop_music=stop_music)

    def mute(channel="music", m=True):
        preferences.set_mute(channel, m)

    def mute_blip(m=True):
        mute("sfx", m)

    config.default_music_volume = 0.5
