# "../files_list.rpy"

init -12 python:

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

    def text_style(s, text):
        persistent.blip = "blip_thinking" if s.startswith("thoughts") else "blip"
        print(persistent.blip)

        def add_style_to_text(text, style):
            return "{{={}}} {} {{/={}}}".format(style, text, style)
        text = alter_say_strings(text)
        return add_style_to_text(text, "{}_text_style".format(s))

    def character_monologue(character, text, fun=(lambda x: x)):
        for l in text.splitlines():
            if len(l) == 0:
                continue
            character(fun(l))

    def list_text(text_arr):
        print(list_text)
        return "{w=1}\n".join(text_arr)

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
