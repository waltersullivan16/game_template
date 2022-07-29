init python:
    def change_scene(t=["wet", "wet"], time=[2, 2], pause=2, s="main", skip_loading=False, clean_only=False):
        renpy.transition(transition(t[0], time[0]))#t_time))
        renpy.show("black")
        stop_music()
        renpy.pause(pause)
        if not skip_loading:
            loading()
        change_style(s)
        renpy.transition(transition(t[1], time[1]))

    def show_scene(background, characters, overlay=[]):
        renpy.scene()
        renpy.show(background)
        print(characters)
        for c in characters:
            renpy.show("{}".format(c.image), at_list=c.at_list)
        for o in overlay:
            renpy.show(o)

    def judge_scene(): {show_scene("judge", [LexioClass], ["lawkaj"])}
    def pros_scene(**kwargs):
        change_pose("wardega", **kwargs)
        show_scene(
            "prosecution",
            [WardegaClass],
            ["lawkap"]
    )
    def copros_scene(**kwargs):
        change_pose("revo", **kwargs)
        show_scene(
        "coprosecution",
        [RevoClass]
    )
    def defense_scene(**kwargs):
        change_pose("konopski", **kwargs)
        show_scene(
            "defense", 
            #[(KonopskiClass, kpose)],
            [KonopskiClass],
            ["lawkad"]
        )
    def witness_scene(): {show_scene("witness", [Gimper])}
