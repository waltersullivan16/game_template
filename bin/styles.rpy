# STYLES: main, creepy, www, intro, quote, black, straznik

### DEFAULT

style say_window is default
style say_dialogue is default
style say_label is default

style namebox is default

style say_window_empty:
    background textbox_maker("empty")

style say_window_main:
    background Frame(textbox_maker("main"))
    yalign 1.0
    ysize 300
    xalign 0.0

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
    color color("black")

## CREEPY

style say_window_creepy is say_window_main

style say_window_creepy:
    background Frame(textbox_maker("creepy", 1))

style say_dialogue_creepy:
    xpos 90 ypos 0.5
    xsize 700
    line_spacing 7
    color color("tangerine")

style namebox_creepy:
    xalign 0.14
    yalign 0.24

style say_label_creepy:
    size 50
    font font("monster")
    color color("red")

### INTRO

style say_window_intro is say_window_empty

style say_dialogue_intro:
    xpos 350
    ypos 270
    xsize 800
    line_spacing 10

### WWW

style say_dialogue_www:
    xpos 50 ypos 200
    xsize 1500

### QUOTE

style say_dialogue_quote:
    xpos 50 ypos 200
    #rest_indent 100
    xsize 900


### BLACK
style say_dialogue_black:
    font font("indie")
    size 60
    slow_cps 20
    xalign 0.5 yalign 0.5
    xsize 1200
    line_spacing 10

### STRAZNIK

style say_dialogue_straznik:
    xalign 0.5 yalign 0.5
    xsize 1000
    line_spacing 10

style namebox_straznik:
    xalign 0.5 ypos 0.3

style say_label_straznik:
    size 80
    font font("ubuntu")

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
#    color color("blue")
#    italic True
#    font font("ubuntu")

style thoughts_main_text_style is text:
    size 25
    color color("blue")
    italic True
    font font("ubuntu")

style thoughts_creepy_text_style is text:
    size 25
    color color("light_red")
    italic True
    font font("ubuntu")

style dark_thoughts_text_style is text:
    size 22
    color color("dark_blue")
    italic True
    font font("ubuntu")
    line_spacing 10

style thoughts_whisper_text_style is text:
    size 18
    color color("light_red")

style intro_text_style is text:
    #xpos .6 ypos 0.6
    size 36
    color color("white")
    slow_cps 15 
    italic True

style creepy_text_style is text:
    size 55
    font font("monster")
    color color("blood")

style coda_text_style is text:
    font font("coda")
    color color("black")
    size 30

style archivo_text_style is text:
    font font("archivo")
    color color("black")
    size 35

style crooked_text_style is text:
    font font("crooked")
    color color("white")
    size 30

style www_text_style is text:
    font font("ubuntu")
    size 30
    color color("black")

style itis_text_style is text:
    font font("alba")
    size 60
    color color("pink")

style cite_text_style is text:
    font font("futura")
    color color("black")
    xpos 500
    size 25
    italic True
    adjust_spacing 500
    first_indent 500
    rest_indent 500

style quote_text_style is text:
    xmaximum 1000
    font font("pane")
    color color("white")
    size 40
    adjust_spacing 500
    slow_cps 20
    justify True

style quote_influ_text_style is text:
    font font("coda")
    color color("blood")
    slow_cps 10
    size 70

style author_text_style is text:
    font font("ubuntu")
    color color("white")
    size 30
    xpos 0.5 ypos 0.7
    slow_cps 25
    italic True

style chapter_text_style is text:
    font font("instruction")
    color color("white")
    size 60
    slow_cps 5

style straznik_text_style is text:
    font font("consult")
    size 50

style black_screen_text_style is text:
    font font("ubuntu")
    color color("white")
    size 60

style black_text_style is text:
    font font("ubuntu")
    color color("white")
    size 60

style jak_to_mowia_text_style is text:
    size 28
    bold True
    italic True

style strazmasterka_text_style is text:
    xpos 0
    size 100
    font font("breathe")
    color color("blood")
    bold True

style panic_text_style is text:
    font font("murder")
    color color("light_red")
    size 120

style blowek_text_style is text:
    size 45
    font font("love")
    color color("pink")

style dziewczyny_text_style is text:
    size 40
    font font("kalam")
    slow_cps 40

style wkurw_text_style is text:
    size 40
    font font("coda")
    color color("white")

style futura_text_style is text:
    size 30
    font("block")


style button:
    background "#006"
    insensitive_background "#444"
    hover_background "#00a"

style button_text:
    font font("sonic")
    selected_color color("yellow")

style trofeum:
    font font("ubuntu")
    color color("black")

style new_item:
    font font("coda")
    color color("white")
