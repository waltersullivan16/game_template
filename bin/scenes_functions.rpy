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

    def change_pose(c, p=None):
        if p is not None:
            c.change_pose(p)

    def show_scene(background, characters, overlay=[], t=None):
        renpy.scene()
        renpy.show(background)
        #print(characters)
        for c in characters:
            renpy.show("{}".format(c.image), at_list=c.at_list)
        for o in overlay:
            renpy.show(o)

    def judge_scene(pose=None, t=None):
        change_pose(LexioClass, pose)
        show_scene("judge", [LexioClass], ["lawkaj"], t=t)

    def pros_scene(pose="main", t=None):
        WardegaClass.change_pose(pose)
        show_scene(
            "prosecution",
            [WardegaClass],
            ["lawkap"],
            t=t
    )
    def copros_scene(pose="main", t=None):
        change_pose(RevoClass, pose)
        show_scene(
        "coprosecution",
        [RevoClass], t=t
    )
    def defense_scene(pose="main", t=None):
        KonopskiClass.change_pose(pose)
        show_scene(
            "defense", 
            #[(KonopskiClass, kpose)],
            [KonopskiClass],
            ["lawkad"], t=t
        )
    def witness_scene(): {show_scene("witness", [Gimper])}

    def objection(character, name):
        play_sound_effect("{}_{}".format(name, character.name,), group="objection")
        renpy.show("{}_bubble".format(name))
        renpy.pause(2)
        renpy.hide("{}_bubble".format(name))

    def wtf_moments(scenes_list=[judge_scene, pros_scene, copros_scene, defense_scene]):
        def wtf_moment(scene):
            renpy.transition(transition("imdis"))
            scene()
            play_sound_effect("bum")
            renpy.pause(1)

        for s in scenes_list:
            wtf_moment(s)
