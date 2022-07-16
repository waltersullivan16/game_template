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
        conditional_wait(too_loud, text_arr, last_text, max_volume=0.1)

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

    def show_scene(background, characters, overlay=[]):
        renpy.scene()
        renpy.show(background)
        print(characters)
        for c, p in characters:
            renpy.show("{} {}".format(c.name, p), at_list=c.at_list)
        for o in overlay:
            renpy.show(o)

    def judge_scene(lpose="main"): {show_scene("judge", [(LexioClass, lpose)], ["lawkaj"])}
    def pros_scene(wpose="main"): {show_scene(
        "prosecution",
        [(WardegaClass, wpose)],
        ["lawkap"]
    )}
    def copros_scene(rpose="main"): {show_scene(
        "coprosecution",
        [(RevoClass, rpose)]
    )}
    def defense_scene(kpose="pmain"): {show_scene(
        "defense", 
        #[(KonopskiClass, kpose)],
        [(KonopskiClass, "phoenix politowanie")],
        ["lawkad"]
    )}
    def witness_scene(): {show_scene("witness", [Gimper])}

    def straznik(text):
        #renpy.transition(transition("shatter"))
        renpy.show("very_dark_blur")#, layer="overlay")
        change_style("straznik")
        #play_sound_effect("tiger")
        Straznik(text_style("straznik", text))
        change_style("main")
        #renpy.transition(transition("shot"))
        renpy.hide("very_dark_blur")
        renpy.pause(1.0)

    def dziewczyny(text):
        for t in text:
            Unknown(text_style("dziewczyny", "{} {{w=0.4}}{{nw}}".format(t)))
