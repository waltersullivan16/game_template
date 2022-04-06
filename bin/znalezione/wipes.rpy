init python:
    wipe_path = lambda x: gpj("gui","transitions", "wipes", "{}.png".format(x))
    def make_trans(name, time=1.0, parts=8):
        return ImageDissolve(wipe_path(name), time, parts)

    transitions_list = ["cwipe", "ccwipe", "bites", "bowtie", "cmet", "cwside",
        "cwtop", "dots", "edges", "flips", "fur", "goslow", "letter", "maze", "radio",
        "snake", "snake2", "snakes", "sunshine", "glasswool", "wet", "mist", "mist2",
        "witraz", "shot", "puzz", "rain1", "rain2", "snow1", "curtains", "farba", "w35"]
    TRANSITIONS = {}
    for t in transitions_list:
        TRANSITIONS[t] = make_trans(t)
    transition_args = lambda n, t=1, p=8: make_trans(n, t, p)
    #TRANSITIONS["wet_time"] = lambda t: make_trans("wet", time=t)
    #TRANSITIONS["eye_time"] = lambda t, p: make_trans("eye", time=t, parts=p)
#ImageDissolve(wipe_path("eye"), 2.0, 64)
#    mist = make_trans("mist")
#    w36 = make_trans("mist2")
#
#
#    witraz = make_trans("witraz")
#
#    shot = make_trans("shot")
#    puzz = make_trans("puzz")
#    rain1 = make_trans("rain1")
#    rain2 = make_trans("rain2")
#    snow1 = make_trans("snow1")
#    curtains = make_trans("curtains")
#
init:
#    $ circlewipe = ImageDissolve("gui/transitions/wipes/circlewipe-cw.jpg", 1.0, 8)
#    $ ccirclewipe = ImageDissolve("transitions/wipes/circlewipe-ccw.jpg", 1.0, 8)
#    $ bites = ImageDissolve("transitions/wipes/bites.jpg", 5.0, 8)
#    $ bowtie = ImageDissolve("transitions/wipes/bowtie.png", 1.0, 8)
#    $ cmet = ImageDissolve("transitions/wipes/cmet.jpg", 1.0, 8)
#    $ cwside = ImageDissolve("transitions/wipes/cw-side.jpg", 1.0, 8)
#    $ cwtop = ImageDissolve("transitions/wipes/cw-top.jpg", 1.0, 8)
#    $ dots = ImageDissolve("transitions/wipes/dots.png", 1.0, 8)
#    $ edges = ImageDissolve("transitions/wipes/edges.png", 1.0, 8)
#    $ flips = ImageDissolve("transitions/wipes/flips.png", 1.0, 8)
#    $ fur = ImageDissolve("transitions/wipes/fur.jpg", 1.0, 8)
#    $ goslow = ImageDissolve("transitions/wipes/goslow.png", 5.0, 8)
#    $ letter = ImageDissolve("transitions/wipes/letter.png", 1.0, 8)
#    $ maze = ImageDissolve("transitions/wipes/maze.png", 1.0, 8)
#    $ radio = ImageDissolve("transitions/wipes/radio.jpg", 1.0, 8)
#    $ snake = ImageDissolve("transitions/wipes/snake.png", 1.0, 8)
#    $ snake2 = ImageDissolve("transitions/wipes/snake2.png", 1.0, 8)
#    $ snakes = ImageDissolve("transitions/wipes/snakes.png", 1.0, 8)
#    $ sunshine = ImageDissolve("transitions/wipes/sunshine.jpg", 1.0, 8)
#    $ glasswool = ImageDissolve("transitions/wipes/glasswool.jpg", 1.0, 8)
#    $ wet = ImageDissolve("transitions/wipes/wet.jpg", 1.0, 8)
#    $ wet_time = lambda t: ImageDissolve("transitions/wipes/wet.jpg", t, 8)
#    
#    $ shatter = ImageDissolve("transitions/wipes/shatter.png", 1.0, 8)
#

# unnamed
    $ w1 = ImageDissolve("transitions/wipes/1.jpg", 1.0, 8)
    $ w2 = ImageDissolve("transitions/wipes/2.png", 1.0, 8)
    $ w3 = ImageDissolve("transitions/wipes/3.jpg", 1.0, 8)
    $ w4 = ImageDissolve("transitions/wipes/4.jpg", 1.0, 8)
    $ w5 = ImageDissolve("transitions/wipes/5.jpg", 1.0, 8)
    $ w6 = ImageDissolve("transitions/wipes/6.jpg", 1.0, 8)
    $ w7 = ImageDissolve("transitions/wipes/7.png", 1.0, 8)
    $ w8 = ImageDissolve("transitions/wipes/8.jpg", 1.0, 8)
    $ w9 = ImageDissolve("transitions/wipes/9.jpg", 1.0, 8)
    $ w10 = ImageDissolve("transitions/wipes/10.jpg", 1.0, 8)
    $ w11 = ImageDissolve("transitions/wipes/11.jpg", 1.0, 8)
    $ w12 = ImageDissolve("transitions/wipes/12.jpg", 3.0, 8)
    $ w13 = ImageDissolve("transitions/wipes/13.jpg", 1.0, 8)
    $ w14 = ImageDissolve("transitions/wipes/14.png", 1.0, 8)
    $ w15 = ImageDissolve("transitions/wipes/15.png", 1.0, 8)
    $ w16 = ImageDissolve("transitions/wipes/16.png", 1.0, 8)
    $ w17 = ImageDissolve("transitions/wipes/17.png", 1.0, 8)
    $ w19 = ImageDissolve("transitions/wipes/19.jpg", 1.0, 8)
    $ w20 = ImageDissolve("transitions/wipes/20.jpg", 1.0, 8)
    $ w21 = ImageDissolve("transitions/wipes/21.jpg", 1.0, 8)
    $ w22 = ImageDissolve("transitions/wipes/22.png", 1.0, 8)
    $ w23 = ImageDissolve("transitions/wipes/23.png", 1.0, 8)
    $ w24 = ImageDissolve("transitions/wipes/24.png", 1.0, 8)
    $ w25 = ImageDissolve("transitions/wipes/25.png", 1.0, 8)
    $ w26 = ImageDissolve("transitions/wipes/26.png", 1.0, 8)
    $ w27 = ImageDissolve("transitions/wipes/27.png", 1.0, 8)
    $ w28 = ImageDissolve("transitions/wipes/28.png", 1.0, 8)

    $ w29 = ImageDissolve("transitions/wipes/29.png", 1.0, 8)
    $ w30 = ImageDissolve("transitions/wipes/30.png", 1.0, 8)
    $ w31 = ImageDissolve("transitions/wipes/31.png", 1.0, 8)
    $ w32 = ImageDissolve("transitions/wipes/32.png", 1.0, 8)
    $ w33 = ImageDissolve("transitions/wipes/33.png", 1.0, 8)

    $ w34 = ImageDissolve("transitions/wipes/34.png", 1.0, 8)
    $ w37 = ImageDissolve("transitions/wipes/37.png", 1.0, 8)

    $ pix1 = ImageDissolve("transitions/wipes/pix1.png", 2.0, 8)

    $ maska = ImageDissolve("transitions/wipes/maska.png", 3.0, 8)
