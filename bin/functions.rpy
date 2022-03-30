## jump to other conf files
"gui_.rpy"
"conf.rpy"
"characters_base.rpy"
"transforms.rpy"
"images_python.rpy"
"screens_.rpy"

## common files
"../characters.rpy"
"../images.rpy"

## script
"../scripts/chapter1/1a_poczatek.rpy"
"../scripts/test.rpy"

init -11 python:
    def gpj(parts):
        return os.path.join(*parts)

    def font(font_name):
        return gpj(["gui", "fonts", "{}.ttf".format(font_name)])

init -9 python:
    def char_talking(character, event, **kwargs):
        if event == "show":
            character.talking = True
            play_sound_effect("blip", channel="sound", loop="True")

        elif event in ["end", "slow_done"]:
            character.talking = False
            #renpy.music.stop(channel="sound")
            stop_sound_effect()
            #if persistent.blip_mute is None:
            if persistent.special_sound is not None and event == "end":
                play_sound_effect(persistent.special_sound)
                persistent.special_sound = None
    def count_files_dir(path):
        return 2
        #return len(os.listdir(path))
    def get_frame(character, animation_name, frame):
        return "{} {} {}".format(character, animation_name, frame)

    def animation_maker(character, animation_name, pause=ANIMATION_PAUSE):

        animation_path = PATHS["animations"](character, animation_name)
        amount = count_files_dir(animation_path)
        animation_list = []
        for i in range(amount):
            animation_list.extend([get_frame(character, animation_name, i + 1), ANIMATION_PAUSE])
        return Animation(*animation_list)

    def animation_maker2(name, animation_name, frames=2, pause=ANIMATION_PAUSE):
        animation_list = []
        for i in range(frames):
            animation_list.extend([get_frame(name, animation_name, i + 1), ANIMATION_PAUSE])
        return Animation(*animation_list)

    def animation_mouth(character, animation_name, pause=ANIMATION_PAUSE):
        img_name = "{}_body_{}".format(character, animation_name)
        animation_list = [img_name, ANIMATION_PAUSE, img_name + "2", ANIMATION_PAUSE]
        return Animation(*animation_list)

    def animation_reaction(reaction, pause=ANIMATION_PAUSE):
        path = gpj([PATHS["reactions"], reaction])
        res = []
        for i in range(count_files_dir(path)):
            res.extend(["{} {}".format(reaction, i + 1), ANIMATION_PAUSE])
        print(res)
        return Animation(*res)
        
 
    def alter_say_strings(str_to_test, dot="1.0", comma="0.3"):
        if not(any(c not in '.,' for c in str_to_test)):
            dot = '0' 
            comma = '0'
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

