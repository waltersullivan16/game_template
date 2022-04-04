## jump to other conf files
"conf.rpy"
"characters_base.rpy"
"functions.rpy"
"transforms.rpy"
"images_python.rpy"
"screens_.rpy"
"music.rpy"

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
    background Frame(textbox_maker("creepy"), 1)
    xalign 0.0
    yalign 1.0
    ysize 300

style say_window_intro:
    background textbox_maker("intro")

style say_window_empty:
    background textbox_maker("empty")

style say_window_www:
    background textbox_maker("empty")

style say_window_quote:
    background textbox_maker("black")

style say_dialogue_intro:
    xpos 350
    ypos 270
    xsize 800

style say_dialogue_www:
    xpos 50 ypos 200
    #rest_indent 100
    xsize 900

style say_dialogue_quote:
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

style straznik_text:
    xpos 100
    ypos 130
    xsize 1200

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
    font font("bahiana")
    size 80
init -12 python:
    from collections import namedtuple, defaultdict

    COLORS = {
        "royal_blue": "#4169E1",
        "blue": "#00FFFF",
        "dark_blue": "#00008b",
        "blood": "#830303",
        "red": "#B22222",
        "bright_red": "#D2042D",
        "light_red": "#FA8072",
        "black": "000000",
        "white": "#ffffff",
        "pink": "#ff69b4",
        "tet": "#f5a90e",
    }

    class FontInfo():
        def __init__(self, name="ubuntu", size=25, color="black"):
            self.name = font(name)
            self.size = size
            self.color = COLORS[color]
    
    FONT_DICT = {
        "text": FontInfo(name="ubuntu", color="white"),
        "name": FontInfo(name="lucky", size=50),
        "idle": FontInfo(color="white"),
        "accent": FontInfo(color="pink"),
        "hover": FontInfo(color="blue"),
        "interface": FontInfo(name="haters", color="white", size=52),
    }

   # StyleInfo = namedtuple("StyleInfo",
   #     ["text_color", "text_font", "name_color", "name_font"])
    
    class FontStyle():
        def __init__(self, name, text_font="ubuntu", text_color="white", text_size=25, name_font="lucky", name_color="black", name_size=25, hide_namebox = False):
            self.name = name
            self.text_font = font(text_font)
            self.text_color = COLORS[text_color]
            self.name_font = font(name_font)
            self.text_size = text_size
            self.name_color= COLORS[name_color]
            self.name_size = name_size
            
            self.hide_namebox = hide_namebox

        def __eq__(self, other):
            if isinstance(other, FontStyle):
                return self.name == other.name

            return False

    MainStyle = FontStyle("main")
    IntroStyle = FontStyle("intro", hide_namebox=True)
    CreepyStyle = FontStyle("creepy", text_color="red", name_font="monster", name_color="blood")
    WWWStyle = FontStyle("www", hide_namebox=True)

    def text_style(s, text):
        if s.startswith("thoughts"):
            persistent.talking_mode = "thinking"

        def add_style_to_text(text, style):
            return "{{={}}} {} {{/={}}}".format(style, text, style)

        return add_style_to_text(text, "{}_text_style".format(s))
    def music_text(t):
        try:
            name = t[2:]
            if t[1] == "M":
                play_music(name)
            elif t[1] == "S":
                play_sound_effect(name)
        except:
            Exception("wrong music format")
        
        
    def character_monologue(character, text, fun=(lambda x: x)):
        for l in text.splitlines():
            if len(l) == 0:
                continue
            elif l.startswith("~"):
                music_text(l)
                continue
            #print(l, fun)
            persistent.lock = True
            character(fun(l))
            persistent.lock = False

    styled_monologue = lambda s, c, t: character_monologue(c, t, lambda x: text_style(s, x))
    #thoughts_monologue = lambda c, t: character_monologue(c, t, lambda x: text_style("thoughts", x))
    intro_monologue = lambda c, t: character_monologue(c, t, lambda x: text_style("intro", x))

    def list_text(l):
        return "{w}\n".join(l)

    def thinking(character, text, style=None):
        persistent.talking_mode = "thinking"
        print("befoorer  ",persistent.talking_mode)
        s = "thoughts_{}".format(style) if style is not None else "thoughts"
        styled_monologue(s, character, text)
        print("after  ",persistent.talking_mode)
        #play_sound_effect("glitter")
        persistent.talking_mode = "normal"
        #persistent.talking_mode = "normal"
        

### TEXT WITH TRANSFORM
    def creepy_maker(text):
        return At(text_style("creepy", text), creepy_transform)

### TEXTBOX
    def textbox_maker(textbox_name, alpha=0.85):
        return Transform(Image(gpj("gui", "textbox", TEXTBOX_NAMES[textbox_name])), alpha=alpha)

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
