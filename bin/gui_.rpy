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

#style window:
    #background Frame(textbox_maker("main"))
    #xalign 0.0
    #yalign 1.0
    #ysize 300

#style namebox:
#    xalign 0.155
#    yalign 0.3

style namebox_main:
    xalign 0.155
    yalign 0.3

style namebox_creepy:
    xalign 0.14
    yalign 0.24

style say_label_main:
    #font font("monster")
    size 50
    font font("lucky")
    color COLORS["black"]
    #properties gui.text_properties("name", accent=True)

style say_label_creepy:
    size 50
    font font("monster")
    color COLORS["red"]

style say_window_main:
    background Frame(textbox_maker("main"))
    xalign 0.0
    yalign 1.0
    ysize 300


style say_dialogue_blank:
    #properties gui.text_properties("dialogue")
    #xpos 0
    #ypos 0.5
    #font font("ubuntu")
    xsize 50
    line_spacing 7

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

#style say_window_intro:
#    background textbox_maker("intro")
#style empty:
#    background textbox_maker("empty")

#style say_window_www:
 #   background textbox_maker("empty")

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
    xpos .6 ypos 0.6
    size 36
    color COLORS["white"]
    slow_cps 15 
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
    size 50

style black_screen_text_style is text:
    xpos 0
    ypos 0.5
    font font("ubuntu")


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
        def __init__(self, name="ubuntu", size=25, color="white"):
            self.name = font(name)
            self.size = size
            self.color = COLORS[color]

        def __eq__(self, other):
            if isinstance(other, FontInfo):
                return self.name == other.name

            return False


    BASE_TEXT_FONT = FontInfo()
    BASE_NAME_FONT = FontInfo(name="lucky", color="black", size=25)

    FONT_DICT = {
        "text": FontInfo(name="ubuntu"),
        "name": FontInfo(name="lucky", size=50, color="black"),
        "idle": FontInfo(color="white"),
        "accent": FontInfo(color="black"),
        "hover": FontInfo(color="blue"),
        "interface": FontInfo(name="haters", size=52),
    }
    #Other's Font

    def text_style(s, text):
        #if s.startswith("thoughts"):
        #    persistent.talking_mode = "thinking"

        def add_style_to_text(text, style):
            return "{{={}}} {} {{/={}}}".format(style, text, style)
        text = alter_say_strings(text)

        return add_style_to_text(text, "{}_text_style".format(s))

#    def music_text(t):
#        print("fdsfsdfs", t)
#        try:
#            name = t[2:]
#            if t[1] == "M":
#                play_music(name)
#            elif t[1] == "S":
#                play_sound_effect(name)
#        except:
#            Exception("wrong music format")
#        
#    def text_preprocessing(text):
#        print("dsadd", text)
#        if text.startswith("~"):
#            music_text(l)
#        
        
    def character_monologue(character, text, fun=(lambda x: x)):
        for l in text.splitlines():
            if len(l) == 0:
                continue
#            text_preprocessing(text)
           #print(l, fun)
            #persistent.lock = True
            character(fun(l))
            #persistent.lock = False

    styled_monologue = lambda s, c, t: character_monologue(c, t, lambda x: text_style(s, x))

    def thinking(character, text, style=None):
        persistent.blip = "blip_thinking"
        s = "thoughts_{}".format(persistent.style)
        styled_monologue(s, character, text)
        persistent.blip = "blip"
        

### TEXTBOX
    def textbox_maker(textbox_name, alpha=0.85):
        return Transform(Image(gpj("gui", "textbox", TEXTBOX_NAMES[textbox_name])), alpha=alpha)

    def change_style(s):
        persistent.style = s
        if s in ["www", "intro"]:
            persistent.hide_dialogue_windows
