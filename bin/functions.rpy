# ../files_list.rpy

init -14 python:
    def gpj(*parts):
        return os.path.join(*parts)

    def font(font_name):
        return gpj("gui", "fonts", "{}.ttf".format(font_name))

    def color(color):
        return COLORS[color]

    def get_dirs(path):
        return [d for d in os.listdir(path) if os.path.isdir(gpj(path, d))]

init -9 python:
    def char_talking(character, event, **kwargs):
        if event == "show":
            character.talking = True
            blip = character.blip or persistent.blip
            print(character, character.name, character.blip,blip)
            play_sound_effect(blip, channel="sound", loop="True")

        elif event in ["end", "slow_done"]:
            character.talking = False
            stop_sound_effect()

    def label_callback(name, abnormal):
        if not name.startswith('_'):
            persistent.prev = persistent.label
            persistent.label = name
            name_arr = name.split('.')
            persistent.base = name_arr[-len(name_arr)]

    def loading(transition="farba", time=0.5):#, transition2):
        renpy.show("bg black")
        def loading_change(pause1=1.0,pause2=0.3):
            change_cursor("loading")
            renpy.pause(pause1)
            change_cursor("main")
            renpy.pause(pause2)
        loading_change(1.0,0.3)
        loading_change(1, 0)
        renpy.transition(transition, time)

    def get_frame(character, animation_name, frame):
        return "{} {} {}".format(character, animation_name, frame)

    def animation_maker(name, animation_name, frames=2, pause=0.2):
        animation_list = []
        for i in range(frames):
            animation_list.extend([get_frame(name, animation_name, i + 1), pause])
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
        #wipe_path = gpj("gui","transitions", "wipes")
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

    def new_trofeum(t):
        renpy.show_screen("trofeum", t)
        play_sound_effect("trofeum")
        renpy.pause(3.0)
        renpy.hide_screen("trofeum")

    def conditional_wait(condition, text_arr, last_text, p=1):
        print(condition, condition())
        print(preferences.get_volume("music"))
        i = 0
        while condition():
            character, text = text_arr[i]
            character(text)
            renpy.pause(p)
            i = (i + 1) % len(text_arr)
        character, text = last_text
        character(text)

    def check_too_loud_music(max_volume=0.1):
        return preferences.get_volume("music") >= max_volume

    def music_volume_wait():
        text_arr = [
            (Konopski, "Nie słyszę własnych myśli."),
            (Konopski, "Jest tak głośno, że nie umiem nawet skupić się na byciu przerażonym."),
            (LilMasti, "{size=-15}Dociera coś do ciebie knypku?{/size}"),
            (Konopski, "W międzyczasie sprawdźcie, czy na pewno daliście suba z dzwoneczkiem."),
        ]
        last_text = Konopski, "No nareszcie."
        conditional_wait(check_too_loud_music, text_arr, last_text)

    def gibberish(n=1):
        play_sound_effect("gibberish{}".format(n))

#    def replacement_show(*args, **kwargs):
#        renpy.show(*args, **kwargs)
#        return 
#
#    def replacement_hide(*args, **kwargs):
#        renpy.transition(Dissolve(1))
#        renpy.hide(*args, **kwargs)
#        return 

    #config.show = replacement_show
    #config.hide = replacement_hide  

    def change_scene(t="wet", s="main"):
        renpy.transition(transition(t, 2))
        renpy.show("black")
        stop_music()
        renpy.pause(2)
        loading()
        change_style(s)
        renpy.transition(transition(t, 2))
