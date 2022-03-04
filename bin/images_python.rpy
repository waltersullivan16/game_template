## jump to other conf files
"conf.rpy"
"characters_base.rpy"
"functions.rpy"
"gui_.rpy"
"transforms.rpy"

## common files
"../characters.rpy"
"../images.rpy"

## script
"../scripts/1_uwertura.rpy"
"../scripts/test.rpy"

transform co_to:
    xanchor 0.05 zoom 1.10
    xpos -5
    subpixel True
    parallel:
        ease 2.0 xpos 5
        ease 1.0 xpos 0
        ease 1.0 xpos 5
        ease 2.0 xpos -5
        ease 1.0 xpos 0
        ease 1.0 xpos -5
        repeat

transform blood_particle2:
    subpixel True
    zoom 0.75
    alpha 0.75
    choice:
        linear 0.25 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.55 zoom 0
transform blood_particle:
    yzoom 0 yanchor 0.2 subpixel True
    linear 10 xzoom 8 #Extends vertically
init -1 python:
    def _shake_function(trans, st, at, dt=.5, dist=64):
       #dt is duration timebase, dist is maximum shake distance in pixel
        if st <= dt:
            trans.xoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            trans.yoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            return 1.0/60
        else:
            return None


transform shake(t=.5, d=64):
    function renpy.curry(_shake_function)(dt=t, dist=d)
init python:
    def creepy_wardega():
        return LiveComposite(
            (1280, 720),
            (0, 50), Text("SYLWESTER", style="creepy"),
            (0, 500), Text("WARDEGA", style="creepy"))
transform wardega_pos:
    xpos 0 ypos 50

transform shake2:
    anchor (.5, .5)

    parallel:
        zoom 0
        linear .5 zoom .75
        pause 2
        linear 1.0 zoom 4.0

    parallel:
        xpos 0.0 ypos .6
        linear 1.5 xpos 1.0
        linear 1.0 xpos .5 ypos .2

    pause .5
    repeat
image crewar = At(creepy_wardega(),blood_particle)
init python:
    def fading_text(text, t, x, y, move_x, move_y, *args, **kwargs):
        ui.add(At(Text(text, *args, **kwargs), fade_move_with_pars(t, x, y, move_x, move_y)))

transform fade_move_with_pars(t, x, y, move_x, move_y):
    parallel:
        alpha 1.0
        linear t alpha 0
    parallel:
        pos (x, y)
        linear t pos (move_x, move_y)

transform dissolve_with_atl(time):
    alpha 0
    ease time alpha 1

image si = At(Text("dadas", style="creepy"), creepy_transform)
image si2 = At(Text("dad333as", style="creepy"), creepy_transform)
image crer:
    "si"
    pause 1.0
    "si2"
    xpos 0.5 ypos 0.

transform syl:
    alpha 0.0
    pause 1.0
    ease 0.1 alpha 1,0

transform syl2:
    alpha 0.0
    pause 3.0
    ease 0.1 alpha 1,0


### WARDEGA INTRO

image sylwester = At(creepy_maker("SYLWESTER"), dissolve_with_atl(3))
image wardega = At(creepy_maker("WARDEGA"), dissolve_with_atl(3))
image wardega_center = At("wardega", Position(ypos=0.6))

init python:
    def image_sound(image):
        renpy.show(image)
        renpy.play(os.path.join("music","wardega.mp3"))

    def image_dissolve(image, time=3):
        return At(image, dissolve_with_atl(time))

    def whisper():
        renpy.show("wardega_center")
        renpy.play("music/wardega.mp3")

    def show_at_position(image, x, y):
        return At(image, Position(xpos=x, ypos=y))

    def creepy_composition(name, positions):
        for (x,y) in positions:
            image_sound(show_at_position("wardega",x,y) , "wardega.mp3")

    def text_size(t, s):
        return add_tags_to_text(t, [["size", s]])

    def text_font(t, f):
        return add_tags_to_text(t, [["font", f]])

transform dissolve_with_sound(time):
    alpha 0
    ease time alpha 1

image sylwesterry = Composite(
    (1280, 720),
    (40, 450), At(creepy_maker("SYLWESTER"), dissolve_with_sound(4)),
    (100, 200), At(creepy_maker("SYLWESTER"), dissolve_with_sound(8)))

image junkoo:
    "junko1"
    pause 2.0
    "junko2"

image transparenty_prolog: 
    "maki1" with dissolve
    pause 1.0
    "maki2" with vpunch
    pause 0.5
    "ishimaru1" with dissolve
    pause 1.0
    "ishimaru2" with vpunch
    pause 0.5
    "gonta1" with dissolve
    pause 1.0
    "gonta2" with vpunch
    pause 0.5
    "tsumugi1" with dissolve
    pause 1.0
    "tsumugi2" with vpunch
    pause 0.5
    "kaito1" with dissolve
    pause 1.0
    "kaito2" with vpunch
    pause 0.5
    "mikan1" with dissolve
    pause 1.0
    "mikan2" with vpunch
    pause 0.5
    "kirumi1" with dissolve
    pause 1.0
    "kirumi2" with vpunch
    pause 0.5
    "dogen1" with dissolve
    pause 1.0
    "dogen2" with dissolve
    pause 1.0
    "koniec0" with vpunch
    pause 1.0
    "koniec1" with vpunch

image transparenty_omg:
    "zginie" with vpunch
    pause 1.5
    "wpierdol" with vpunch
    pause 1.5
    "debil" with vpunch
    pause 1.5
    "apetyt" with vpunch
    pause 1.5
    "bozia" with vpunch
    pause 1.5
    "kutas" with vpunch
    pause 1.5
    "kutas2" with vpunch
    pause 1.5
