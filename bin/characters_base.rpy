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
                return ['{} {} 1', animation_pause, '{} {} 2', animation_pause]
            for s in self.styles:
                renpy.image("{} {}".format(self.name, s), gpj(self.character_path, "body", "{}_body_{}.png".format(self.name, s)))
                renpy.image("{} {}_talking".format(self.name, s), animation_maker(self.name, s))

        @property
        def character_path(self):
            return gpj(PATH_CHARACTERS, self.group, self.name)

        @property
        def styles(self):

            if self._styles is None:
                anim_path = gpj(self.character_path, "animations")
                self._styles = [d for d in os.listdir(anim_path)] if os.path.exists(anim_path) else []
            return self._styles

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
                
        def __str__(self):
            return self.name
