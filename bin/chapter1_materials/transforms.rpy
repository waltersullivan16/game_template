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


transform ani_alpha:
    alpha 1.0
    pause 0.2
    alpha 0.1
    pause 0.2
    repeat

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

transform scary_masti:
    zoom 2

transform beating_masti:
    truecenter zoom 2.0
    linear 0.2 truecenter zoom 2.28
    block:
        pause 0.1
        linear 0.2 truecenter zoom 1.28
        pause 0.1
        linear 0.2 truecenter zoom 1.05
        repeat 3
    linear 0.1 zoom 4.0
    pause 1.0
    linear 0.2 zoom 1
    pause 0.2
    block:
        linear 0.1 truecenter rotate -5
        pause 0.1
        linear 0.1 truecenter rotate 5
        pause 0.1
        repeat 5
    linear 0.1 ypos 2.0

transform masti_wpierdol:
    truecenter
    xpos 0.0 ypos 0.4
    linear 0.2 xanchor -0.5

    #on hide:
    #    easein 2.0 alpha 0.0
transform quick_zoom(z=2.0):
    truecenter zoom 0
    linear 0.1 zoom z

transform out_left:
    linear 3 xanchor 1500

transform sh_blur:
    truecenter zoom 1.3
    parallel:
        block:
            blur 50
        block:
            ease .7 xoffset 15 yoffset 15
            ease .7 xoffset 15 yoffset 0
            ease .7 xoffset -15 yoffset 0
            ease .7 xoffset -15 yoffset -15
            ease .7 xoffset 0 yoffset 15
            repeat

transform unblur2(x=50):
    blur x
    linear 1.0 blur 0

transform shake:
   ease .05 yoffset 20
   ease .05 yoffset -20
   ease .03 yoffset 12
   ease .03 yoffset -12
   ease .01 yoffset 4
   ease .01 yoffset -4
   ease .01 yoffset 0
   repeat
    