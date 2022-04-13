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
        "accent": FontInfo(color="blue"),
        "hover": FontInfo(color="blue"),
        "interface": FontInfo(name="haters", size=52),
    }

    def text_style(s, text):

        def add_style_to_text(text, style):
            return "{{={}}} {} {{/={}}}".format(style, text, style)
        text = alter_say_strings(text)

        return add_style_to_text(text, "{}_text_style".format(s))

    def character_monologue(character, text, fun=(lambda x: x)):
        for l in text.splitlines():
            if len(l) == 0:
                continue
            character(fun(l))

    def list_text(c, text):
        pass

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
    def just_text(x, y, xsize):
        persistent.hide_dialogue_windows = True
        style.say_dialogue.xpos = x
        style.say_dialogue.ypos = y 
        style.say_dialogue.ypos = xsize 
        style.rebuild()
