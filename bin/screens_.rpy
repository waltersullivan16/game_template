"../files_list.rpy"

#### SCREENS ####

screen z():
    zorder 2
    imagebutton:
        xpos 1000
        yalign 0.0
        #hover setattr(config, "mouse", {"default": [("others/myszka_error.png", 1, 1)]})
        idle "gui/button/kopi.png"
        mouse "active"
        action ToggleMute("music")

    imagebutton:
        xalign 0.0
        yalign 0.0
        idle "gui/button/kopi.png"
        mouse "active"
        action Jump("uwertura_scenes")
        #action Show("options")


screen options():
    add blur
    frame:
        has vbox
        bar value Preference("sound volume") released Play("sound", "music/sound effects/badum.mp3")
        bar value Preference("music volume")

screen button_overlay():
    mousearea:
        area (0, 0, 1.0, 100)
        hovered Show("options", transition=dissolve)
        unhovered Hide("options", transition=dissolve)

screen choices_template(name, imagebuttons):
    #add "blur"
    for (it, i) in enumerate(imagebuttons):
        $ xpos_ = 100 if (it % 2) == 0 else 700
        $ ypos_ = 50 if it < 2 else 400 
        $ mouse = "love" if i.startswith("blowek") else "active"
        imagebutton:
            xpos xpos_
            ypos ypos_
            activate_sound "music/sound effects/button_menu.mp3"
            hover "gui/choices/active_{}.png".format(i)
            mouse mouse
            idle "gui/choices/inactive_{}.png".format(i)
            action [Hide(name, transition=ease),  Jump(i)]

screen choices1_blowek():
    modal True
    use choices_template("choices1_blowek", ["blowek", "lexi", "grafika", "uciekaj"])

screen choices2_blowek_sequel():
    modal True
    use choices_template("choices2_blowek_sequel", ["blowek2", "lexi", "pocieszajka", "uciekaj"])

screen choices3_uciekaj():
    modal True
    use choices_template("choices3_uciekaj", ["uciekaj", "uciekaj", "uciekaj", "uciekaj"])

screen dragdrop_menu(items):
    
    frame:
        pos (0,0)
        side "c b r":
            area (100, 100, 600, 600) #(100, 100, 600, 400)

            viewport id "vp":
                draggable True

                vbox:
                    for i in items:
                        textbutton i.caption action i.action

            bar value XScrollValue("vp")
            vbar value YScrollValue("vp")

screen subscribe_screen():
    add "blur"
    imagebutton:
        xpos 0.1
        ypos 0.3
        hover "images/others/subscribe.png"
        unhovered [MouseMove(500, 300)]
        mouse "active"
        activate_sound "music/sound effects/button.mp3"
        idle "images/others/subscribe.png"
        action [Hide("subscribe_screen"), Jump("subscribe_like")]

screen subscribed_screen():
    add "blur"
    imagebutton:
        xpos 0.1
        ypos 0.3
        hover "images/others/subscribed.png"
        idle "images/others/subscribed.png"

screen subscribed_like_screen():
    add "blur"
    imagebutton:
        xpos 0.8
        ypos 0.3
        hover "images/others/like.png"
        unhovered [MouseMove(1050, 300)]
        mouse "active"
        activate_sound "music/sound effects/button.mp3"
        idle "images/others/like.png"
        action [Hide("blur"), Hide("subscribed_screen", transition=ease), Hide("subscribed_like_screen", transition=ease), Jump("subscribe_thanks")]#Hide("subscribe", transition=dissolve), Jump("subscribe_thanks")]

transform text_fade_in(t, p=0):
    alpha 0
    pause p
    easeout t alpha 1

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
