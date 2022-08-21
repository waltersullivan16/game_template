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

    def show_scene(background, characters, overlay=[], t=None):
        renpy.scene()
        renpy.show(background)
        #print(characters)
        for c in characters:
            renpy.show(c.image, at_list=c.at_list)
        for o in overlay:
            renpy.show(o)

    def judge_scene(pose="main", t=None):
        change_pose("lexio", pose)
        show_scene("judge", [LexioClass], ["lawkaj"], t=t)

    def pros_scene(pose="main", t=None):
        change_pose("wardega", pose)
        show_scene(
            "prosecution",
            [WardegaClass],
            ["lawkap"],
            t=t
    )
    def copros_scene(pose="main", t=None):
        change_pose("revo", pose)
        show_scene(
        "coprosecution",
        [RevoClass], t=t
    )
    def defense_scene(pose="main", t=None):
        change_pose("konopski", pose)
        show_scene(
            "defense", 
            #[(KonopskiClass, kpose)],
            [KonopskiClass],
            ["lawkad"], t=t
        )
    def witness_scene(): {show_scene("witness", [Gimper])}

    def objection(character, name, objection_sound=False):
        if objection_sound:
            play_sound_effect("objection_sound", channel="sfx2")
        play_sound_effect(f"{name}_{character}", group="objection")
        renpy.show(f'{name}_bubble')
        renpy.pause(2)
        renpy.hide(f"{name}_bubble")

    def wtf_moments(scenes_list=[judge_scene, pros_scene, copros_scene, defense_scene]):
        def wtf_moment(scene, pose="objection"):
            #renpy.transition(transition("imdis"))
            scene(pose)
            play_sound_effect("bum")
            renpy.pause(1)

        for s in scenes_list[:-1]:
            wtf_moment(s, "wtf_moment")
        wtf_moment(scenes_list[-1])

    def zoom_moment(character, pos=(0,0), zoom=2, text=None, sound=None, time=None, talking=False):
        renpy.scene()
        renpy.show("zoom_objection")
        #renpy.show(character.char, at_list=["zoom_character"])
        renpy.show(character.image, at_list=[character_zoom(z=zoom,x=pos[0], y=pos[1])])
        if talking:
            character.talking_cutscene = True
        if sound is not None:
            play_sound_effect(sound)
            play_sound_effect(sound)
        renpy.pause(time)
        character.talking_cutscene = False
