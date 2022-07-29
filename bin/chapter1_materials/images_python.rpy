init python:

    def show_with_args(x, transition=dissolve, at_list=[], pause_in=None, pause_out=None, sound=None, relative_volume=1):
        renpy.transition(transition)
        renpy.show(x, at_list=at_list)

        if pause_in:
            renpy.pause(pause_in)
        if sound:
            play_sound_effect(sound, relative_volume=relative_volume)
        if pause_out:
            renpy.pause(pause_out)

    image_punch = lambda x: show_with_args(x, transition=vpunch, sound="punch")
    image_trzask = lambda x: show_with_args(x, transition=vpunch, sound="trzask")

    def scene_courtroom1():
        def character_courtroom(character, first_transition=dissolve, second_transition=vpunch, pause_out1=0.5, pause_out2=0.2):

            show_with_args("{}1".format(character), first_transition, pause_out=pause_out1)
            show_with_args("{}2".format(character), second_transition, pause_out=pause_out2)

        order = ["maki", "ishimaru", "gonta", "tsumugi", "kaito", "mikan", "kirumi"]#, "dogen", "koniec"]
        for c in order:
            character_courtroom(c)
        character_courtroom("dogen", second_transition=ease, pause_out2=1)
        character_courtroom("koniec", pause_out1=1, first_transition=vpunch)
        show_with_args("koniec3", vpunch, pause_out=1)
