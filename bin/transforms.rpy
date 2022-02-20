## jump to other conf files
"conf.rpy"
"characters_base.rpy"
"functions.rpy"
"gui_.rpy"
"transforms.rpy"


## common files
"../characters.rpy"
"../images.rpy"

## script
"../scripts/1_uwertura.rpy"
"../scripts/test.rpy"

transform dropping:
    linear 1.5 yanchor -100
    pause 3.0

transform beating:
    zoom 1.2
    pause 0.2
    zoom 1.0
    pause 0.2
    repeat

transform bounce2:
    linear 3.0 xalign 1.0
    linear 3.0 xalign 0.0
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

transform kick_out:
    xpos 0.0 ypos 0.33
    easein 0.2 xalign 0.3
    pause 0.2 
    easeout 0.4 rotate 70 
    easein 0.2 rotate -90 
    easeout 0.5 rotate 0 ypos 0.30
   
transform kicked_out:
    easeout 0.3 xpos 1.0 ypos -1.0 rotate 300

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
