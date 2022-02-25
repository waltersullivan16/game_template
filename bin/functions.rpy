## jump to other conf files
"bin/gui_.rpy"
"bin/conf.rpy"
"bin/characters_base.rpy"
"bin/transforms.rpy"

## common files
"../characters.rpy"
"../images.rpy"

## script
"../scripts/1_uwertura.rpy"
"../scripts/test.rpy"

init -11 python:
    def gpj(parts):
        return os.path.join(*parts)

init -9 python:
    def char_talking(character, event, **kwargs):
        if event == "show":
            character.talking = True
            renpy.music.play("music/blip.mp3", channel="sound", loop="True")
        elif event in ["end", "slow_done"]:
            character.talking = False
            renpy.music.stop(channel="sound")

    def get_frame(character, animation_name, frame):
        return "{} {} {}".format(character, animation_name, frame)

    def font(font_name):
        return PATHS["fonts"]("{}.ttf".format(font_name))

# makers
    def count_files_dir(path):
        return len(os.listdir(path))

    def animation_list_maker(character, name, pause=ANIMATION_PAUSE):
        animation_path = PATHS["animations"](character, name)
        print("fdfssfsf", animation_path)
        amount = count_files_dir(animation_path)
        print("animation list", amount)
        animation_list = []
        for i in range(amount):
            animation_list.extend([get_frame(character, name, i + 1), ANIMATION_PAUSE])
        return animation_list

    def animation_maker(character, animation_name, pause=ANIMATION_PAUSE):
        return Animation(*animation_list_maker(character, animation_name, pause))

    animation_mouth = lambda c: animation_maker(c, "mouth")

    def at_position(image, pos):
        return At(image, Position(xpos=pos[0], ypos=pos[1]))

    def emotion_maker(character, emotion):
        arr = list(map(lambda x: int(x), renpy.get_image_bounds(character)))
        renpy.show(emotion, atl=Position(arr[0], arr[2]))

    def reactions(c):
        for r in os.listdir(PATHS["reactions"]):
            print("{}_{}_{}".format(c, 'reactions', r.split('.')[0]))

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

    def alter_say_strings(str_to_test, dot="0.5", comma="0.1"):
        str_map = {
            ". " : ". {{w={}}}".format(dot),
            ", " : ", {{w={}}}".format(comma),
        }
        for key in str_map:
            str_to_test = str_to_test.replace(key, str_map[key])
        return str_to_test
