"../files_list.txt"

init -8 python:
### CHARACTERS
    CHARACTERS_NAMES = ["Pearl", "Ema", "Penny", "Najman", "LilMasti", "Unknown"]#'Wardega', 'Konopski', 'Revo', 'Lexio', 'Gimper', 'Dziewczyna1', 'Dziewczyna2', 'Dziewczyna3']


## SPECIAL CHARACTERS

    class CharacterBase:
        def __init__(self, name, styles=[], who_color='#000000'):
            self.capital_name = name.upper()
            self.name = name.lower()

            #self.mouth_pos = mouth_pos
            #self.pos = start
            #self.who_color = who_color
            #self.show_args = [Transform(pos=start)]

            self.char = self.create_character()
            self.talking = False

            self.styles = styles

        def create_character(self):
            return Character(
                name=self.capital_name,
                image=self.name,
                callback=partial(char_talking, self))
                #who_color=self.who_color)
        @property
        def animations_switch(self):
            res = []
            for s in self.styles:
                res.extend(["{} {}".format(self.name, s), animation_maker(self.name, s)])
            return ShowingSwitch(*res)

        def __str__(self):
            return self.name

    for character in CHARACTERS_NAMES:
        c_base = "{}Class = CharacterBase(\"{}\")".format(character, character)
        c_character = "{} = {}Class.char".format(character, character)
        commands = [c_base, c_character]#, c_anim]
        for c in commands:
            exec(c)

    Unknown = Character(name = "???")
    Blank = Character(name = "")
    Straznik = Character(name = "STRAŻNIK")#, what_style="straznik_text")

    Unknown.name ="???"
