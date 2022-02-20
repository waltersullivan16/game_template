## jump to other conf files
"conf.rpy"
"characters_base.rpy"
"functions.rpy"
"transforms.rpy"
"images_python.rpy"

## common files
"../characters.rpy"
"../images.rpy"

## script
"../scripts/1_uwertura.rpy"
init python:

    COLORS = {
        "royal_blue": "#4169E1",
        "blood": "#830303"
    }

#### SCREENS ####

screen z():
    imagebutton:
        xalign 0.0
        yalign 0.0
        idle "gui/button/end.png"
        action Jump("end")

#### STYLE ####

define mode = "normal"
style window:
    background textbox_maker("main")
    yalign 1.0
    ysize 300

style namebox:
    xalign 0.155
    yalign 0.3

style say_label:
    properties gui.text_properties("name", accent=True)

style creepy_namebox_namelabel:
    size 50
    font FONTS["monster"]
    color COLORS["blood"]

style creepy_namebox_position:
    xpos 200
    ypos 100

style say_dialogue:
    #properties gui.text_properties("dialogue")
    xpos 190
    ypos 0.5
    xsize 900#gui.dialogue_width
    line_spacing 7

style thoughts_dialogue:
    properties gui.text_properties("dialogue")
    xpos 150
    ypos 0.5
    xsize 900
    line_spacing 7

style block2_multiple2_say_window:
    xpos 20
    ypos 0.4
    xsize 499

style thoughts_text_style is text:
    size 25
    color COLORS["royal_blue"]
    italic True
    font FONTS["ubuntu"]

style creepy_text_style is text:
    size 25
    font FONTS["monster"]
    color COLORS["blood"]

style comics_text_style is text:
    size 50
    xanchor -1.5 yanchor 0.5

style normal_text_style is text:
    font FONTS["ubuntu"]
    size 25

define true_left = Position(xpos=0.2)
init -1 python:

    def add_style_to_text(text, style):
        return "{{={}}} {} {{/={}}}".format(style, text, style)

    def thoughts_text(text):
        return add_style_to_text(text, "thoughts_text_style")

    def creepy_text(text):
        return Text(add_style_to_text(text, "creepy_text_style"))

    def comic_text(text):
        return Text(add_style_to_text(text, "comics_text_style"))

    def add_tags_to_text(text, style):
        # style format: list of arrays
        # first element of the array is a name of the style
        # second elements exists if style contains arguments (font size...)

        res = text
        for i in style:
            assert len(1) > 0
            opening = i[0] if (len(i) == 1) else "{}={}".format(i[0], i[1])
            ending = i[0]
            res = "{{{}}} {} {{/={}}}".format(opening, res, ending)
        print(text, res)

        return res

    def character_monologue(character, text, fun):
        for l in text.splitlines():
            if len(l) == 0:
                continue
            character(fun(l))

    thoughts_monologue = lambda c, t: character_monologue(c, t, thoughts_text)

    def tt():
        a = """ffff
            ffffff
            ffsfsdfs"""
        return add_tags_to_text(a, [["", "creepy_text_style"], ["i"]])

### TRANSFORM FUNCTIONS
    def creepy_maker(text):
        return At(creepy_text(text), creepy_transform)

    def comic_maker(text, bubble):
        return LiveComposite(
            renpy.image_size(bubble),
            (0, 0), bubble,
            (0.0, 0.0), comics_text(text))

### TEXTBOX
    def textbox_maker(textbox_name):
        return Transform(Frame(gpj([PATHS["textbox"], TEXTBOX_NAMES[textbox_name]])), alpha=0.85)

    def change_textbox(textbox_name="main"):
        style.window.background = textbox_maker(textbox_name)
        style.rebuild()

    def change_style_to_creepy():
        change_textbox("creepy")
        style.say_label = style.creepy_namebox_namelabel
        style.namebox = style.creepy_namebox_position
        style.rebuild()
