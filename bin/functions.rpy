# ../files_list.rpy

init -14 python:
    def gpj(*parts):
        return os.path.join(*parts)

    def font(font_name):
        return gpj("gui", "fonts", "{}.ttf".format(font_name))

init -9 python:
    def char_talking(character, event, **kwargs):
        if event == "show" and not persistent.stop_lipsync:
            character.talking = True
            print(character, get_blip(), persistent.talking_mode)
            play_sound_effect(get_blip(), channel="sound", loop="True")

        elif event in ["end", "slow_done"]:
            character.talking = False
            #renpy.music.stop(channel="sound")
            stop_sound_effect()
            #if persistent.blip_mute is None:
            if persistent.special_sound is not None and event == "end":
                play_sound_effect(persistent.special_sound)
                persistent.special_sound = None
            if not persistent.lock:
                persistent.talking_mode = "normal"

    def silence(time=1):
        renpy.hide("window")
        renpy.pause(time)

    def stop_lipsync(character, text):
        persistent.stop_lipsync = True
        character(text)
        persistent.stop_lipsync = False 
    
    def offscreen_talking(time=2):
        renpy.hide("window")
        play_sound_effect("off_scene")
        renpy.pause(time)
        

    def get_frame(character, animation_name, frame):
        return "{} {} {}".format(character, animation_name, frame)

    def animation_maker(name, animation_name, frames=2, pause=ANIMATION_PAUSE):
        animation_list = []
        for i in range(frames):
            animation_list.extend([get_frame(name, animation_name, i + 1), ANIMATION_PAUSE])
        return Animation(*animation_list)
    
    animation_reaction = lambda name: animation_maker(name, "reaction")
 
    def alter_say_strings(str_to_test, dot="1.0", comma="0.3"):
        alphabet = string.ascii_lowercase
        if not any([c in alphabet for c in str_to_test.lower()]):
            print(str_to_test, "adadas")
            return str_to_test
        str_map = {
            ". " : ". {{w={}}}".format(dot),
            ", " : ", {{w={}}}".format(comma),
        }
        for key in str_map:
            str_to_test = str_to_test.replace(key, str_map[key])
        return str_to_test
        
# scenes
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

