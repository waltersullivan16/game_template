"../files_list.txt"

init -8 python:
### CHARACTERS
    spose = "main"

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
            self._talking_animation = None

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
        def styles(self):

            if self._styles is None:
                    z = [p for p in os.listdir(PATH_CHARACTERS)]
                    print(z)
                    paths = list(filter(lambda x: x.split('/')[-1].startswith("animation"), [gpj(self.character_path, p)  for p in os.listdir(self.character_path)]))
                    self._styles = []
                    for anim_path in paths:
                        self._styles += [d for d in os.listdir(anim_path)]
            print("styles {}".format(self._styles))
            return self._styles
                
        def __str__(self):
            return self.name


        def body_path(self, body_part):
            return gpj(selfcharacter_path(self.name, self.group), body_part, self.body_image_name(body_part))

        def character_image(self):
            img_name = lambda part, i="": "{}_{}_[{}_{}]{}.png".format(self.name, part, self.name, part, i)
            img_path = lambda part, i="": gpj(self.character_path, part, img_name(part, i))
            
            def talking_animation():
                if self._talking_animation is None:
                    self._talking_animation = Animation(*[
                        img_path("head"), 0.2, img_path("head", 2), 0.2
                    ])
                return self._talking_animation

            return LiveComposite(
                (782, 705),
                (0, 0), ConditionSwitch(
                    "{}Class.talking".format(self.name.capitalize()), talking_animation(),
                    "True", img_path("head")), 
                (0, 0), img_path("suit"))
