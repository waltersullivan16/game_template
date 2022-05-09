init python:
    def junko_bibi(name, pause=1.5):
        renpy.scene()
        renpy.show("transparenty_courtroom3")
        play_sound_effect(name, group="junko_bibi")
        renpy.pause(pause, hard=True)
        renpy.scene()
        renpy.show("transparenty_courtroom")
        renpy.pause(1)

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

    def change_scene(t=["wet", "wet"], time=[2, 2], pause=2, s="main", skip_loading=False, clean_only=False):
        renpy.transition(transition(t[0], time[0]))#t_time))
        renpy.show("black")
        stop_music()
        renpy.pause(pause)
        if not skip_loading:
            loading()
        change_style(s)
        renpy.transition(transition(t[1], time[1]))

    def falling(pause=1):
        play_sound_effect("upadek")
        renpy.transition("vpunch")
        renpy.show("black")

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

