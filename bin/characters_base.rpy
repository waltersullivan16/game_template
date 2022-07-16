"../files_list.txt"

init -8 python:
### CHARACTERS

    PATH_CHARACTERS = gpj("images", "characters")

    class CharacterBase:
        def __init__(self, name, group="", blip=None, at_list=[], default="main", **kwargs):
            self.capital_name = name.upper()
            self.name = name.lower()
            self.group = group

            self.talking = False
            self.blip = blip
            self.at_list = at_list
            self.default = default

            self._animation_switch = None
            self._styles = None
            self._styles2 = None

            self.kwargs = kwargs
            #self.init_images()

        @property
        def char(self):
            return Character(
                name=self.capital_name,
                image=self.name,
                callback=partial(char_talking, self), **self.kwargs)

        @property
        def animations_switch(self):
            if self._animation_switch is None:
                res = []
                for s in self.styles:
                    res.extend(["{} {}".format(self.name, s), animation_maker(self.name, s)])
                res.extend([self.name, animation_maker(self.name, "main")])
                self._animation_switch = ShowingSwitch(*res)
            return self._animation_switch

        @property
        def character_path(self):
            return gpj(PATH_CHARACTERS, self.group, self.name)

        @property
        def mouth_switch(self):
            if self._mouth_switch is None:
                res = []
                for s in self.styles:
                    res.extend(["{} {} talking".format(self.name,s ), At(s, "mouth_transform")])
                self._mouth_switch = ShowingSwitch(*res)
            return self._mouth_switch

        @property
        def styles(self):

            if self._styles is None:
                    z = [p for p in os.listdir(PATH_CHARACTERS)]
                    print(z)
                    paths = list(filter(lambda x: x.split('/')[-1].startswith("animation"), [gpj(self.character_path, p)  for p in os.listdir(self.character_path)]))
                    print("paths {}".format(paths))
                    self._styles = []
                    for anim_path in paths:
                        self._styles += [d for d in os.listdir(anim_path)]
            print("styles {}".format(self._styles))
            return self._styles
                
        def __str__(self):
            return self.name

        @property
        def animations_switch2(self):
            if self._animation_switch is None:
                res = []
                for s in self.styles:
                    res.extend(["{} {}".format(self.name, s), self.image_type(s)])
                res.extend([self.name, self.image_type("main")])
                self._animation_switch2 = ShowingSwitch(*res)
                print(res)
            return self._animation_switch2

        def init_images(self):
            def talking_animation(a, animation_pause=0.2):
                animation_format = lambda i: '{} {} {}'.format(self.name, a, i)
                return [animation_format('1'), animation_pause, animation_format('2'), animation_pause]

            for s in self.styles:
                #renpy.image("{} {}".format(self.name, s), gpj(self.character_path, "body", "{}_phoenix_head_{}.png".format(self.name, s)))
                renpy.image("{} {} talking".format(self.name, s), "mouth")
            renpy.image("konopski talking", "mouth")
            d = gpj(self.character_path, "mouth")

        def aa(self):
            print("dasdadasdas", renpy.get_attributes("konopski"))
            persistent.mouth = renpy.get_attributes(self.name)
            return "mouth"
            
        @property
        def styles2(self):
            def match_pattern(s):
                import re
                print(s)
                pattern = r'{}_body_(?P<arg>\w+)\.png'.format(self.name)
                print(pattern)
                match = re.match(pattern, s) 
                print(match)
                return match
            def get_arg_name(s):
                m = match_pattern(s)
                return m.group('arg') if m is not None else None

            if self._styles2 is None:
                anim_path = gpj(self.character_path, "body")
                self._styles2 = [get_arg_name(d) for d in os.listdir(anim_path)] if os.path.exists(anim_path) else []
            return self._styles2

        def image_name(self, atr):
            return "{} {}".format(self.name, atr)

        def anim_name(self, atr):
            return "{} {}_talking".format(self.name, atr)

        def image_type(self, atr):
            return self.anim_name(atr) if self.talking else self.image_name(atr)
