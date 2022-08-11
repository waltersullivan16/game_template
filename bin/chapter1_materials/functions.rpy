init -9 python:
    def animation_maker(name, animation_name, frames=2, pause=0.2):
        def get_frame(character, animation_name, frame):
            return "{} {} {}".format(character, animation_name, frame)

        animation_list = []
        for i in range(frames):
            animation_list.extend([get_frame(name, animation_name, i + 1), pause])
        #print(animation_list)
        return Animation(*animation_list)
    
    animation_reaction = lambda name: animation_maker(name, "reaction")
     
    def too_loud(max_volume=0.1):
        return check_music_volume(max_volume)

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

    def falling(pause=1):
        play_sound_effect("upadek")
        renpy.transition("vpunch")
        renpy.show("black")

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
