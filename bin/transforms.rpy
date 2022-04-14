# ../files_list.rpy

## jump to other conf files
"conf.rpy"
"characters_base.rpy"
"functions.rpy"
"gui_.rpy"
"transforms.rpy"
"screens_.rpy"
"images_python.rpy"


## common files
"../characters.rpy"
"../images.rpy"

transform dropping:
    linear 1.5 yanchor -100
    pause 3.0

transform beating:
    zoom 1.2
    pause 0.2
    zoom 1.0
    pause 0.2
    repeat

transform title_beating:
    truecenter zoom 1.0
    pause 2.4
    block:
        linear 0.2 truecenter zoom 1.08
        pause 0.1
        linear 0.2 truecenter zoom 0.95
        pause 0.1
        repeat

transform bounce_left_right:
    linear 3.0 xalign 1.0
    linear 3.0 xalign 0.0
    repeat

transform left_right_zoom:
    anchor (.5, .5)

    parallel:
        zoom 0
        linear .5 zoom .75
        pause 2
        linear 1.0 zoom 4.0

    parallel:
        xpos 0.0 ypos .6
        linear 1.5 xpos 1.0
        linear 1.0 xpos .5 ypos .2

    pause .5
    repeat

transform shake:
   ease .05 yoffset 20
   ease .05 yoffset -20
   ease .03 yoffset 12
   ease .03 yoffset -12
   ease .01 yoffset 4
   ease .01 yoffset -4
   ease .01 yoffset 0
   repeat
transform creepy_transform:
    parallel:
        block:
            linear 0.1 xoffset -2 yoffset 2
            linear 0.1 xoffset 3 yoffset -3
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0
            repeat
    parallel:
        block:
            alpha .2
            linear 1.0 alpha .9
            linear 1.0 alpha .2
            repeat

transform blood_particle:
    yzoom 0 yanchor 0.2 subpixel True
    linear 10 xzoom 2 #Extends vertically

transform blood_particle2:
    subpixel True
    zoom 0.75
    alpha 0.75
    choice:
        linear 0.25 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.55 zoom 0

transform blur:
    ypos 0.5 blur 50
    alpha 1.0
    linear 1.5 ypos 0.0
    linear 0.3 blur 0

transform unblur:
    blur 50
    pause 1.0
    linear 1.0 blur 0

transform ani_alpha:
    alpha 1.0
    pause 0.2
    alpha 0.1
    pause 0.2
    repeat

define vpunch = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
define hpunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)
define m = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)

define dissolve = Dissolve(1.0)#, alpha=True)
define very_slow_dissolve = Dissolve(4.0)
define slow_dissolve = Dissolve(3.0)
define fast_dissolve = Dissolve(0.5)

define alpha_example = AlphaDissolve("alpha_control", delay=3.5)
define circleirisout = ImageDissolve("imdis", 1.0, 8)
define circleirisin = ImageDissolve("imdis", 1.0, 8 , reverse=True)
define teleport = ImageDissolve("imagedissolve teleport", 1.0, 0)

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
define slow_fade = Fade(0.2, 1.0, 0.8)
define very_slow_fade = Fade(0.6, 1.5, 0.8)

define true_left = Position(xpos=0.2)
define true_right= Position(xpos=0.8)

#TRANSFORMS WHICH ARE USED ONLY ONCE

transform kick_out:
    xpos 0.0 ypos 0.33
    easein 0.2 xalign 0.3
    pause 0.2
    easeout 0.4 rotate 70
    easein 0.2 rotate -90
    easeout 0.5 rotate 0 ypos 0.30
    ease 0.9 xalign 0.5

transform kicked_out:
    easeout 0.3 xpos 1.0 ypos -1.0 rotate 300

# koniec_przerwy

transform half_out:
    easein 1.2 xpos 1.5
    pause 1.0
    easein 1.2 xpos 1.2

transform question_konop:
    xpos 0.55 ypos -30
    rotate -50    
    zoom 0.8

transform creepy_kokichi:
    xanchor 0.05 zoom 1.10
    xpos -5
    subpixel True
    parallel:
        ease 2.0 xpos 5
        ease 1.0 xpos 0
        ease 1.0 xpos 5
        ease 2.0 xpos -5
        ease 1.0 xpos 0
        ease 1.0 xpos -5
        repeat

