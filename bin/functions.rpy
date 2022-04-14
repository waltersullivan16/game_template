# ../files_list.rpy

init -14 python:
    def gpj(*parts):
        return os.path.join(*parts)

    def font(font_name):
        return gpj("gui", "fonts", "{}.ttf".format(font_name))

init -9 python:
    def char_talking(character, event, **kwargs):
        if event == "show":
            character.talking = True
            play_sound_effect(persistent.blip, channel="sound", loop="True")

        elif event in ["end", "slow_done"]:
            character.talking = False
            stop_sound_effect()

    def loading(transition="farba", time=0.5):#, transition2):
        renpy.show("bg black")
        def loading_change(pause1=1.0,pause2=0.3):
            change_cursor("loading")
            renpy.pause(pause1)
            change_cursor("main")
            renpy.pause(pause2)
        loading_change(1.0,0.3)
        loading_change(1, 0)

    def get_frame(character, animation_name, frame):
        return "{} {} {}".format(character, animation_name, frame)

    def animation_maker(name, animation_name, frames=2, pause=ANIMATION_PAUSE):
        animation_list = []
        for i in range(frames):
            animation_list.extend([get_frame(name, animation_name, i + 1), ANIMATION_PAUSE])
        return Animation(*animation_list)
    
    animation_reaction = lambda name: animation_maker(name, "reaction")
 
    def alter_say_strings(str_to_test, dot=0.3, comma=0.1, rest=0.2):
        str_map = {
            ". " : ". {{w={}}}".format(dot),
            ", " : ", {{w={}}}".format(comma),
            "! " : "! {{w={}}}".format(rest),
        }
        for key in str_map:
            str_to_test = str_to_test.replace(key, str_map[key])
        return str_to_test
        
    def change_cursor(cursor):
        globals()['default_mouse'] = cursor
        return

    def transition(name, time=1.0, parts=8, reverse=False):
        wipe_path = gpj("gui","transitions", "wipes")
        return ImageDissolve(gpj(wipe_path, "{}.png".format(name)), time, parts, reverse=reverse)
    
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

