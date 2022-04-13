### DEFAULT

style say_window is default
style namebox_main is default
style namebox_label is say_label_name
style say_label_main is default

style say_window:
    background Frame(textbox_maker("empty"))

style say_dialogue_main:
    xpos 150 ypos 0.5
    xsize 1000
    line_spacing 7

style namebox_main:
    xalign 0.155
    yalign 0.3

style say_label_main:
    size 50
    font font("lucky")
    color COLORS["black"]

style say_window_main:
    background Frame(textbox_maker("main"))
    yalign 1.0
    ysize 300
    xalign 0.0

## CREEPY

style say_window_creepy:
    background Frame(textbox_maker("creepy"), 1)
    yalign 1.0
    ysize 300
    xalign 0.0

style say_dialogue_creepy:
    xpos 90 ypos 0.5
    xsize 700
    line_spacing 7

style namebox_creepy:
    xalign 0.14
    yalign 0.24

style say_label_creepy:
    size 50
    font font("monster")
    color COLORS["red"]

### INTRO

style say_dialogue_intro:
    xpos 350
    ypos 270
    xsize 800
    line_spacing 10

### WWW
style say_dialogue_www:
    xpos 50 ypos 200
    #rest_indent 100
    xsize 900

### QUOTE

style say_dialogue_quote:
    xpos 50 ypos 200
    #rest_indent 100
    xsize 900


### BLACK
style say_dialogue_black:
    xpos 0.1 ypos 300
    xsize 2000

####################### MULTIPLE WINDOWS ####################################

style multiple2_say_window:
    xsize 1200
    ysize 720

style block1_multiple2_say_window:
    background textbox_maker("empty")

style block2_multiple2_namebox:
    xpos 10 ypos 10

style block_2_multiple2_say_label:
    font font("ubuntu")
    properties gui.text_properties("name", accent=True)

style block2_multiple2_say_window:
    background Frame(textbox_maker("main"))
    xalign 0.0
    yalign 1.0
    ysize 300

style block2_multiple2_say_dialogue:
    xpos 100 ypos 150

#style thoughts_text_style is text:
#    size 25
#    color COLORS["blue"]
#    italic True
#    font font("ubuntu")

style thoughts_main_text_style is text:
    size 25
    color COLORS["blue"]
    italic True
    font font("ubuntu")

style thoughts_creepy_text_style is text:
    size 25
    color COLORS["light_red"]
    italic True
    font font("ubuntu")

style dark_thoughts_text_style is text:
    size 20
    color COLORS["dark_blue"]
    italic True
    font font("ubuntu")
    line_spacing 10

style intro_text_style is text:
    #xpos .6 ypos 0.6
    size 36
    color COLORS["white"]
    slow_cps 15 
    italic True

style creepy_text_style is text:
    size 55
    font font("monster")
    color COLORS["blood"]

style coda_text_style is text:
    font font("coda")
    #underline True
    color COLORS["black"]
    size 30

style www_text_style is text:
    font font("ubuntu")
    size 30
    color COLORS["black"]

style itis_text_style is text:
    font font("alba")
    size 60
    color COLORS["pink"]

style cite_text_style is text:
    font font("futura")
    color COLORS["black"]
    xpos 500
    italic True
    adjust_spacing 500
    first_indent 500
    rest_indent 500

style quote_text_style is text:
    xmaximum 1000
    font font("pane")
    color COLORS["white"]
    size 40
    adjust_spacing 500
    slow_cps 20
    justify True

style quote_influ_text_style is text:
    font font("coda")
    color COLORS["blood"]
    slow_cps 10
    size 70

style author_text_style is text:
    font font("ubuntu")
    color COLORS["white"]
    size 30
    xpos 0.5 ypos 0.7
    slow_cps 25
    italic True

style chapter_text_style is text:
    font font("instruction")
    color COLORS["white"]
    size 60
    slow_cps 5

style straznik_text_style is text:
    font font("blackops")
    #font font("major")
    size 40

style black_screen_text_style is text:
    font font("ubuntu")
    color COLORS["white"]
    size 60

style jak_to_mowia_text_style is text:
    bold True
    italic True
    size 28
