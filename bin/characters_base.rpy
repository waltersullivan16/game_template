## jump to other conf files
"gui_.rpy"
"characters_base.rpy"
"functions.rpy"
"conf.rpy"

## common files
"../characters.rpy"
"../images.rpy"

## script
"../scripts/1_uwertura.rpy"

init -8 python:
### CHARACTERS
    CHARACTERS_NAMES = ["Konopski","Pearl", "Ema", "Penny"]#'Wardega', 'Konopski', 'Revo', 'Lexio', 'Gimper', 'Dziewczyna1', 'Dziewczyna2', 'Dziewczyna3']


## SPECIAL CHARACTERS

    class CharacterBase:
        def __init__(self, name, who_color='#000000', start=(100,100), mouth_pos=(100,59)):
            self.capital_name = name.upper()
            self.name = name.lower()
            self.mouth_pos = mouth_pos
            self.pos = start

            self.who_color = who_color
            self.show_args = [Transform(pos=start)]

            self.char = self.create_character()
            self.talking = False
            self.styles = []

        def create_character(self):
            return Character(
                name=self.capital_name,
                image=self.name,
                callback=partial(char_talking, self),
                who_color=self.who_color)

        def static_style(self, name):
            return Image("characters/konopski/animations/{}/{} {} 1.png".format(name, self.name, name))

        def fff(self, name):
            return self.static_style(name) if not self.talking else self.make_animation(name)

        def heads_switch(self):
            res = []
            for s in self.styles:
                res.extend(["{} {}".format(self.name, s), self.make_animation(s)])
            print(res)
            res.extend(["True", self.make_animation('main')])
            return ShowingSwitch(*res)

        @property
        def coordinates(self):
            position_array = renpy.get_image_bounds(self.image)
            print(position_array)
            return [position_array[0], position_array[2]]

        def make_animation(self, animation_name):
            return Animation(animation_maker(self.name, animation_name))

        def __str__(self):
            return self.name

    for character in CHARACTERS_NAMES:
        c_base = "{}Class = CharacterBase(\"{}\")".format(character, character)
        c_character = "{} = {}Class.char".format(character, character)
        c_anim = "a{} = lambda x: {}Class.make_animation(x)".format(character, character)
        print(anim, "fdfs")
        commands = [c_base, c_character, c_anim]
        for c in commands:
            exec(c)

    Unknown = Character(name = "???")
    Straznik = Character(name = "Groźny głos")
