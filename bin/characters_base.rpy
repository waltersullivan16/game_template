"../files_list.txt"


init -8 python:
### CHARACTERS

    PATH_CHARACTERS = gpj("images", "characters")

    class CharacterBase:
        def __init__(self, name, group="", version="", blip=None, at_list=[], size=None, image=None, **kwargs):
            self.capital_name = name.upper()
            self.name = name.lower()
            self.image = image or self.name
            self.group = group
            self.version = version
            self.thinking = False

            self.talking = False
            self.blip = blip
            self.at_list = at_list
            self.size = size

            self._animation_switch = None
            self._styles = None
            self._talking_animation = None

            self.kwargs = kwargs
            
            self.init_image()

        @property
        def char(self):
            return Character(
                name=self.capital_name,
                image=self.image,
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
            return gpj(PATH_CHARACTERS, self.group, self.name, self.version)

        @property
        def suit(self):
            return persistent.poses[self.name].get("suit", "main")

        @property
        def head(self):
            return persistent.poses[self.name].get("head", "main")

        @property
        def styles(self):

            if self._styles is None:
                    z = [p for p in os.listdir(PATH_CHARACTERS)]
                    #print(z)
                    paths = list(filter(lambda x: x.split('/')[-1].startswith("animation"), [gpj(self.character_path, p)  for p in os.listdir(self.character_path)]))
                    self._styles = []
                    for anim_path in paths:
                        self._styles += [d for d in os.listdir(anim_path)]
            #print("styles {}".format(self._styles))
            return self._styles
                
        def init_image(self):
            if self.size is not None:
                if self.name not in persistent.poses.keys():
                    persistent.poses[self.name] = {"suit": "main", "head": "main"}
                renpy.image(self.image, LiveCompositeImg(self.name, self.character_path, self.size).character_image)

        def __str__(self):
            return self.name


    class LiveCompositeImg:
        def __init__(self, name, path, size):
            self.name = name
            self.path = path
            self.size = size
            self._talking_animation = None
            self._character_image = None

        def component_path(self, body_part, pose=None): 
            return gpj(self.path, body_part, "[{}Class.{}].png".format(self.name.capitalize(), pose or body_part))

        @property
        def character_image(self):
            if self._character_image is None:

                self._character_image = LiveComposite(
                    self.size,
                    (0, 0), self.component_path("head"),
                    (0, 0), ConditionSwitch(
                        "{}Class.talking".format(self.name.capitalize()), self.talking_animation,
                        "True", "blank"),
                    (0, 0), self.component_path("suit"))

            return self._character_image

        @property
        def talking_animation(self):
            if self._talking_animation is None:
                self._talking_animation = Animation(*[
                    self.component_path("mouth", "head"), 0.2,  "blank", 0.2
                ])
            return self._talking_animation

    def change_pose(character, **kwargs):
        for k in kwargs:
            persistent.poses[character][k] = kwargs[k]
