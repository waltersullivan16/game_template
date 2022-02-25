## jump to other conf files
"conf.rpy"
"characters_base.rpy"
"functions.rpy"
"transforms.rpy"
"images_python.rpy"
"gui_.rpy"

## common files
"../characters.rpy"
"../images.rpy"

## script
"../scripts/1_uwertura.rpy"

#### SCREENS ####

screen z():
    imagebutton:
        xpos 1000
        yalign 0.0
        idle "gui/button/end.png"
        action Jump("end")

    imagebutton:
        xalign 0.0
        yalign 0.0
        idle "gui/button/end.png"
        action Jump("uwertura_scenes")

screen choices1():
    imagebutton:
        xpos 100
        ypos 50
        hover "gui/choices/active_blowek.png"
        idle "gui/choices/inactive_blowek.png"
        action Jump("blowek")

    imagebutton:
        xpos 700
        ypos 50
        hover "gui/choices/active_lexi.png"
        idle "gui/choices/inactive_lexi.png"
        action Jump("end")

    imagebutton:
        xpos 100
        ypos 400
        hover "gui/choices/active_grafika.png"
        idle "gui/choices/inactive_grafika.png"
        action Jump("end")

    imagebutton:
        xpos 700
        ypos 400
        hover "gui/choices/active_uciekaj.png"
        idle "gui/choices/inactive_uciekaj.png"
        action Jump("end")

screen choices2():
    imagebutton:
        xpos 100
        ypos 50
        hover "gui/choices/active_blowek2.png"
        idle "gui/choices/inactive_blowek2.png"
        action Jump("blowek2")

    imagebutton:
        xpos 700
        ypos 50
        hover "gui/choices/active_lexi.png"
        idle "gui/choices/inactive_lexi.png"
        action Jump("end")

    imagebutton:
        xpos 100
        ypos 400
        hover "gui/choices/active_pocieszajka.png"
        idle "gui/choices/inactive_pocieszajka.png"
        action Jump("end")

    imagebutton:
        xpos 700
        ypos 400
        hover "gui/choices/active_uciekaj.png"
        idle "gui/choices/inactive_uciekaj.png"
        action Jump("end")

screen choices3():
    imagebutton:
        xpos 100
        ypos 50
        hover "gui/choices/active_uciekaj.png"
        idle "gui/choices/inactive_uciekaj.png"
        action Jump("uciekaj")

    imagebutton:
        xpos 700
        ypos 50
        hover "gui/choices/active_uciekaj.png"
        idle "gui/choices/inactive_uciekaj.png"
        action Jump("uciekaj")

    imagebutton:
        xpos 100
        ypos 400
        hover "gui/choices/active_uciekaj.png"
        idle "gui/choices/inactive_uciekaj.png"
        action Jump("uciekaj")

    imagebutton:
        xpos 700
        ypos 400
        hover "gui/choices/active_uciekaj.png"
        idle "gui/choices/inactive_uciekaj.png"
        action Jump("uciekaj")

screen intro():
    zorder 2
    window:
        ypos 0.0
        yalign 0.0
        background "gui/textbox/empty.png"
        xpos 200
        xsize 800
