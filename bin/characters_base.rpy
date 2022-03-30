## jump to other conf files
"gui_.rpy"
"characters_base.rpy"
"functions.rpy"
"conf.rpy"

## common files
"../characters.rpy"
"../images.rpy"
"../gui.rpy"

## script
"../scripts/1_uwertura.rpy"

init -8 python:
### CHARACTERS
    CHARACTERS_NAMES = ["Konopski","Pearl", "Ema", "Penny", "Najman", "LilMasti"]#'Wardega', 'Konopski', 'Revo', 'Lexio', 'Gimper', 'Dziewczyna1', 'Dziewczyna2', 'Dziewczyna3']


## SPECIAL CHARACTERS

    class CharacterBase:
        def __init__(self, name, who_color='#000000'):
            self.capital_name = name.upper()
            self.name = name.lower()

            #self.mouth_pos = mouth_pos
            #self.pos = start
            #self.who_color = who_color
            #self.show_args = [Transform(pos=start)]

            self.char = self.create_character()
            self.talking = False

            self.styles = []
            self.animations = {}
            self.animations_switch = ShowingSwitch()

        def create_character(self):
            return Character(
                name=self.capital_name,
                image=self.name,
                callback=partial(char_talking, self))
                #who_color=self.who_color)

        def generate_animation_switch(self):
            res = []
            for s in self.styles:
                #img_name = "{}_animation_{}".format(self.name, s)
                #renpy.image(img_name, animation_mouth(self.name, s))
                #elem=["{} {}".format(self.name, s), img_name]
                #res.extend(["{} {}".format(self.name, s), img_name])
                res.extend(["{} {}".format(self.name, s), animation_maker2(self.name, s)])
                #res += elem
                #print(elem, res)
                #print(img_name)
            return ShowingSwitch(*res)

        def add_styles(self, styles):
            self.styles = styles
            self.animations_switch = self.generate_animation_switch()

        def __str__(self):
            return self.name

    for character in CHARACTERS_NAMES:
        c_base = "{}Class = CharacterBase(\"{}\")".format(character, character)
        c_character = "{} = {}Class.char".format(character, character)
        #c_anim = "a{} = lambda x: {}Class.make_animation(x)".format(character, character)
        #print(anim, "fdfs")
        commands = [c_base, c_character]#, c_anim]
        for c in commands:
            exec(c)

    Unknown = Character(name = "???")
    Blank = Character(name = "blank")
    Straznik = Character(name = "STRAŻNIK", what_style="straznik_text")
