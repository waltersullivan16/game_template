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

style namebox_main:
    xalign 0.155
    yalign 0.3

style namebox_creepy:
    xalign 0.14
    yalign 0.24

style say_label_main:
    font font("ubuntu")
    properties gui.text_properties("name", accent=True)

style say_label_creepy:
    size 50
    font font("monster")
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
    background Frame(textbox_maker("creepy"), 1.0)
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

style say_dialogue_www:
    xpos 50 ypos 200
    #rest_indent 100
    xsize 900

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

style thoughts_text_style is text:
    size 25
    color COLORS["blue"]
    italic True
    font font("ubuntu")

style dark_thoughts_text_style is text:
    size 20
    color COLORS["dark_blue"]
    italic True
    font font("ubuntu")
    line_spacing 10

style intro_text_style is text:
    size 36
    color COLORS["white"]
    italic True

style creepy_text_style is text:
    size 25
    font font("monster")
    color COLORS["blood"]

style normal_text_style is text:
    font font("ubuntu")
    size 24

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

style window_info:
    ypos 400
    xpos 200
    xmaximum 800

style cite_text_style is text:
    font font("futura")
    color COLORS["black"]
    xpos 500
    italic True
    adjust_spacing 500
    first_indent 500
    rest_indent 500

define true_left = Position(xpos=0.2)
init -9 python:
    from collections import namedtuple, defaultdict

    COLORS = {
        "royal_blue": "#4169E1",
        "blue": "#00FFFF",
        "dark_blue": "#00008b",
        "blood": "#830303",
        "red": "#B22222",
        "black": "000000",
        "white": "#ffffff",
        "pink": "#ff69b4",
    }

    StyleInfo = namedtuple("StyleInfo",
        ["text_color", "text_font", "name_color", "name_font"])

    class FontStyle():
        def __init__(self, name, text_font="ubuntu", text_color="white", text_size=25, name_font="lucky", name_color="black", name_size=25):
            self.name = name
            self.text_font = font(text_font)
            self.text_color = COLORS[text_color]
            self.name_font = font(name_font)
            self.text_size = text_size
            self.name_color= COLORS[name_color]
            self.name_size = name_size
        def __eq__(self, other):
            if isinstance(other, FontStyle):
                return self.name == other.name
            return False

    MainStyle = FontStyle("main")
    IntroStyle = FontStyle("intro")
    CreepyStyle = FontStyle("creepy", text_color="red", name_font="monster", name_color="blood")
    WWWStyle = FontStyle("www")

    FONT_STYLES = defaultdict(lambda: StyleInfo("white", "ubuntu", "black", "lucky"))
    FONT_STYLES["main"] = StyleInfo("white", "ubuntu", "black", "lucky")
    FONT_STYLES["creepy"] = StyleInfo("red", "ubuntu", "blood", "monster")
    FONT_STYLES["www"] = StyleInfo("black", "ubuntu", "black", "lucky")
    FONT_STYLES["intro"] = StyleInfo("black", "ubuntu", "black", "lucky")

    
    def add_style_to_text(text, style):
        return "{{={}}} {} {{/={}}}".format(style, text, style)

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

    def font_text(font, text):
        return add_tags_to_text(text, [["font", font(font)]])

    thoughts_monologue = lambda c, t: character_monologue(c, t, lambda x: text_style("thoughts", x))
    intro_monologue = lambda c, t: character_monologue(c, t, lambda x: text_style("intro", x))

    def list_text(l):
        return "{w}\n".join(l)

### TEXT WITH TRANSFORM
    def creepy_maker(text):
        return At(text_style("creepy", text), creepy_transform)

### TEXTBOX
    def textbox_maker(textbox_name, alpha=0.85):
        return Transform(Image(gpj([PATHS["textbox"], TEXTBOX_NAMES[textbox_name]])), alpha=alpha)

    def change_style(s):
        persistent.style = s
        if s == "main":
            persistent.style_class = MainStyle
        elif s == "creepy":
            persistent.style_class = CreepyStyle
        elif s == "www":
            persistent.style_class = WWWStyle
        elif s == "intro":
            persistent.style_class = IntroStyle