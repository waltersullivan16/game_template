## jump to other conf files
"conf.rpy"
"characters_base.rpy"
"functions.rpy"
"transforms.rpy"
"images_python.rpy"
"screens_.rpy"

## common files
"../characters.rpy"
"../images.rpy"
"../screens.rpy"
"../gui.rpy"

## script
"../scripts/0_main.rpy"
"../scripts/1_uwertura.rpy"


style window:
    background Frame(textbox_maker("main"))
    xalign 0.0
    yalign 1.0
    ysize 300

style namebox:
    xalign 0.155
    yalign 0.3

style namebox_creepy:
    xalign 0.14
    yalign 0.24

style say_label_main:
    font FONTS["ubuntu"]
    properties gui.text_properties("name", accent=True)

style say_label_creepy:
    size 50
    font FONTS["monster"]
    color COLORS["red"]

style say_window_main:
    background Frame(textbox_maker("main"))
    xalign 0.0
    yalign 1.0
    ysize 300

style say_dialogue_main:
    #properties gui.text_properties("dialogue")
    xpos 150
    ypos 0.5
    xsize 1000#gui.dialogue_width
    line_spacing 7

style say_dialogue_creepy:
    xpos 90
    ypos 0.5
    xsize 700#gui.dialogue_width
    line_spacing 7

style say_window_creepy:
    background Frame(textbox_maker("creepy"))
    xalign 0.0
    yalign 1.0
    ysize 300

style say_window_intro:
    background textbox_maker("intro")

style say_window_empty:
    background textbox_maker("empty")
style say_window_www:
    background textbox_maker("empty")

style say_dialogue_intro:
    xpos 350
    ypos 270
    xsize 800

#style say_dialogue_i:
#    xsize 900

style say_dialogue_www:
    xpos 50 ypos 200
    #rest_indent 100
    xsize 900

style multiple2_say_window:
    xsize 1200
    ysize 720

style block1_multiple2_say_window:
    background Frame(textbox_maker("main"))
    xalign 0.0
    yalign 1.0
    ysize 300

style block2_multiple2_say_window:
    background textbox_maker("multiple")
    xpos 200
    ypos 750

style block2_multiple2_say_dialogue:
    xpos 100 ypos 150

style thoughts_text_style is text:
    size 25
    color COLORS["blue"]
    italic True
    font FONTS["ubuntu"]

style dark_thoughts_text_style is text:
    size 30
    color COLORS["dark_blue"]
    italic True
    font FONTS["ubuntu"]

style intro_text_style is text:
    size 36
    color COLORS["white"]
    italic True

style creepy_text_style is text:
    size 25
    font FONTS["monster"]
    color COLORS["blood"]

style comics_text_style is text:
    size 50
    xanchor -1.5 yanchor 0.5

style normal_text_style is text:
    font FONTS["ubuntu"]
    size 24

style newspaper_text_style is text:
    font font("newspaper")
    color COLORS["black"]
    size 22

style chomsky_text_style is text:
    font FONTS["chomsky"]
    color COLORS["black"]
    size 40

style america_text_style is text:
    font font("america")
    underline True
    color COLORS["black"]
    size 50

style coda_text_style is text:
    font font("coda")
    #underline True
    color COLORS["black"]
    size 30

style www_text_style is text:
    font font("ubuntu")
    size 30
    color COLORS["black"]

style window_info:
    ypos 400
    xpos 200
    xmaximum 800

define true_left = Position(xpos=0.2)
init -1 python:

    COLORS = {
        "royal_blue": "#4169E1",
        "blue": "#00FFFF",
        "dark_blue": "#00008b",
        "blood": "#830303",
        "red": "#B22222",
        "black": "000000",
        "white": "#ffffff",
    }

    from collections import defaultdict
    COLORS_TEXT = defaultdict(lambda: "white")
    COLORS_TEXT["www"] = "black"
    COLORS_TEXT["creepy"] = "red"

    COLORS_LABELS= defaultdict(lambda: "black")
    COLORS_LABELS["creepy"] = "blood"

    def add_style_to_text(text, style):
        return "{{={}}} {} {{/={}}}".format(style, text, style)

    def thoughts_text(text):
        return add_style_to_text(text, "thoughts_text_style")

    def intro_text(text):
        return add_style_to_text(text, "intro_text_style")

    def text_style(s, text):
        return add_style_to_text(text, "{}_text_style".format(s))

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

    def character_monologue(character, text, fun=(lambda x: x)):
        for l in text.splitlines():
            if len(l) == 0:
                continue
            character(fun(l))

    def font_text(text, font):
        return add_tags_to_text(text, [["font", FONTS[font]]])

    thoughts_monologue = lambda c, t: character_monologue(c, t, thoughts_text)
    intro_monologue = lambda c, t: character_monologue(c, t, intro_text)

    def list_text(l):
        return "{w}\n".join(l)

### TRANSFORM FUNCTIONS
    def creepy_maker(text):
        return At(text_style("creepy", text), creepy_transform)

    def comic_maker(text, bubble):
        return LiveComposite(
            renpy.image_size(bubble),
            (0, 0), bubble,
            (0.0, 0.0), comics_text(text))

### TEXTBOX
    def textbox_maker(textbox_name, alpha=0.85):
        return Transform(Image(gpj([PATHS["textbox"], TEXTBOX_NAMES[textbox_name]])), alpha=alpha)

    def change_style(s):
        persistent.style = s
