#### SCREENS ####

screen z():
    imagebutton:
        xalign 0.0
        yalign 0.0
        idle "gui/button/end.png"
        action Jump("end")

#### TRANSFORMATIONS ####

transform dropping:
    linear 1.5 yanchor -100
    pause 3.0


transform beating:
    zoom 1.2
    pause 0.2
    zoom 1.0
    pause 0.2
    repeat


#### DIALOGUE BOX ###

TEXTBOX_NAME = "phoenixdb.png"

style window:
    background Frame(os.path.join(TEXTBOX_PATH, TEXTBOX_NAME))
    yalign 1.05
    ysize 300


style namebox:
    xalign 0.05
    yalign 0.16


style say_label:
    properties gui.text_properties("name", accent=True)


style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos 100
    yalign 0.6
    xsize gui.dialogue_width


style bum:
    font FONT_CHERI
    size 50
    xanchor 0.5 yanchor 0.5


