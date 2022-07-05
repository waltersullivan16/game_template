# "../files_list.rpy"

init -12 python:

    COLORS = {
        "black": "000000",
        "white": "#ffffff",

        "blue": "#00FFFF",
        "dark_blue": "#00008b",
        "royal_blue": "#4169E1",

        "light_red": "#FA8072",
        "very_light_red": "#986868",
        "bright_red": "#D2042D",
        "red": "#B22222",
        "blood": "#830303",
        "tangerine": "#E78A61",

        "pink": "#ff69b4",
        
        "yellow": "#FFFF00",
        #"tet": "#f5a90e",
    }

    def text_style(s, text, **kwargs):
        persistent.blip = "thoughts" if s.startswith("thoughts") else "main"
        #print(persistent.blip)

        def add_style_to_text(text, style, **kwargs):

            for k, i in kwargs.items():
                b = "{{{}={}}}".format(k, i)# if len(x) == 2 else ""
                e = "{{/{}}}".format(k)
                text = "{} {} {}".format(b, text, e)

            return "{{={}}} {} {{/={}}}".format(style, text, style)

        text = alter_say_strings(text)

        if s.startswith("thoughts"):
            text = "({})".format(text)

        return add_style_to_text(text, "{}_text_style".format(s), **kwargs)

    def character_monologue(character, text, fun=(lambda x: x)):
        for l in text.splitlines():
            if len(l) == 0:
                continue
            if l.startswith("&&"):
                exec(l.split("|"))[1]
                continue
            character(fun(l))

    def list_text(text_arr, wait=1, nw=False):
        w = "{{w={}}}{}\n".format(wait, "{nw}" if nw else "")
        return w.join(text_arr)

    #styled_monologue = lambda s, c, t, **k: character_monologue(c, t, lambda x: text_style(s, x, **k))
    def styled_monologue(style, character, text, wait=1, nw=False, **kwargs):
        if type(text) == list:
            text = list_text(text, wait, nw)
        character_monologue(character, text, lambda x: text_style(style, x, **kwargs))

    def thinking(character, text, style=None, **kwargs):
        s = "thoughts_{}".format(persistent.style)
        styled_monologue(s, character, text, kwargs)

### TEXTBOX
    def textbox_maker(textbox_name, alpha=0.85):
        return Transform(Image(gpj("gui", "textbox", "{}_textbox.png".format(textbox_name))), alpha=alpha)

    def change_style(s):
        persistent.style = s
