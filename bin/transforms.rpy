init -10 python:
    def blurred(s, b=2.5):
        return Transform(im.Blur(s, b))

transform dropping:
    linear 1.5 yanchor -100
    pause 3.0

transform beating:
    zoom 1.2
    pause 0.2
    zoom 1.0
    pause 0.2
    repeat

transform blur(x=50):
    blur x

transform choice_bg_transform_show:
    blur 20.0

transform choice_bg_transform_hide:
    blur 0.0

transform choice_transform:
    alpha 0.0
    easein 1.0 alpha 1.0

transform character_zoom(z=2, x=0, y=0):
    xpos x ypos y
    zoom z

define vpunch = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
define hpunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)
define m = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)

define dissolve = Dissolve(1.0)#, alpha=True)
define very_slow_dissolve = Dissolve(4.0)
define slow_dissolve = Dissolve(3.0)
define fast_dissolve = Dissolve(0.5)

define alpha_example = AlphaDissolve("alpha_control", delay=3.5)
define circleirisout = ImageDissolve("imdis", 1.0, 8)
define circleirisin = ImageDissolve("imdis", 1.0, 8 , reverse=True)
define teleport = ImageDissolve("imagedissolve teleport", 1.0, 0)

define flashbulb = Fade(0.4, 0.5, 2.2, color='#fff')
define flashbulb_fast = Fade(0.1, 0.2, 0.1, color=color("white"))
define slow_fade = Fade(0.2, 1.0, 0.8)
define very_slow_fade = Fade(0.6, 1.5, 0.8)

define true_left = Position(xpos=0.2)
define true_right= Position(xpos=0.8)
