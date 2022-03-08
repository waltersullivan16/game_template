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

init -9 python:
    def char_talking(character, event, **kwargs):
        if event == "show":
            character.talking = True
            #if persistent.blip_mute is None:
            renpy.music.play(music("blip"), channel="sound", loop="True")
        elif event in ["end", "slow_done"]:
            character.talking = False
            renpy.music.stop(channel="sound")
            if persistent.special_sound is not None and event == "end":
                renpy.music.play(persistent.special_sound, channel="sound")
                persistent.special_sound = None

# makers
    def count_files_dir(path):
        return len(os.listdir(path))

    def animation_list_maker(character, name, pause=ANIMATION_PAUSE):
        def get_frame(character, animation_name, frame):
            return "{} {} {}".format(character, animation_name, frame)
        animation_path = PATHS["animations"](character, name)
        #print("fdfssfsf", animation_path)
        amount = count_files_dir(animation_path)
        #print("animation list", amount)
        animation_list = []
        for i in range(amount):
            animation_list.extend([get_frame(character, name, i + 1), ANIMATION_PAUSE])
        return animation_list

    def animation_easy_maker(name, amount):
        animation_list = []
        for i in range(amount):
            animation_list.extend(["{} {}".format(name, i + 1), ANIMATION_PAUSE])
        #print(animation_list)
        return animation_list

    def animation_maker(character, animation_name, pause=ANIMATION_PAUSE):
        return Animation(*animation_list_maker(character, animation_name, pause))

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

    preferences.show_empty_window = False

    def alter_say_strings(str_to_test, dot="1.0", comma="0.3"):
        str_map = {
            ". " : ". {{w={}}}".format(dot),
            ", " : ", {{w={}}}".format(comma),
        }
        for key in str_map:
            str_to_test = str_to_test.replace(key, str_map[key])
        return str_to_test
    
    config.say_menu_text_filter = alter_say_strings
