transform pause(p):
    pause p

transform e:
    xoffset -1280 # assuming this is your horizontal resolution
    linear 0.5 xoffset 0

screen quote(t, influ, a, a_errata1, a_errata2):

    add "black"
    zorder -1
    $ curr_w = ""
    $ t2 = t.split(' ')
    $ p = 0
    text t xpos 0.1 ypos 0.2 style "quote_text_style" at pause(1.5)#text_fade_in(2.0, 1.5)#text_fade_in(4.0) with creepy_transform #creepy_transform#text_fade_in(1.0)
    text influ xpos 0.2 ypos 0.4 style "quote_influ_text_style" at text_fade_in(3.0, 5.5)#text_fade_in(4.0) with creepy_transform #creepy_transform#text_fade_in(1.0)
    text a xpos 0.3 ypos 0.6 style "author_text_style" at text_fade_in(2.0, 8.5)
    text a_errata1 xpos 0.3 ypos 0.6 style "author_text_style" at text_fade_in(2.0, 11.0)
    text a_errata2 xpos 0.3 ypos 0.6 style "author_text_style" at text_fade_in(2.0, 11.1)
