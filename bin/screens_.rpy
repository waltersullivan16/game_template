"../files_list.rpy"

#### SCREENS ####

screen z():
    imagebutton:
        xpos 1000
        yalign 0.0
        #hover setattr(config, "mouse", {"default": [("others/myszka_error.png", 1, 1)]})
        idle "gui/button/kopi.png"
        action Jump("end")

    imagebutton:
        xalign 0.0
        yalign 0.0
        idle "gui/button/kopi.png"
        action Jump("uwertura_scenes")

screen choices_template(name, imagebuttons):
    #add "blur"
    for (it, i) in enumerate(imagebuttons):
        $ xpos_ = 100 if (it % 2) == 0 else 700
        $ ypos_ = 50 if it < 2 else 400 
        $ mouse = "love" if i.startswith("blowek") else "green"
        imagebutton:
            xpos xpos_
            ypos ypos_
            hover "gui/choices/active_{}.png".format(i)
            mouse mouse
            idle "gui/choices/inactive_{}.png".format(i)
            action [Hide(name, transition=dissolve),  Jump(i)]

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
        mouse "green"
        activate_sound "music/button.mp3"
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
        mouse "green"
        activate_sound "music/button.mp3"
        idle "images/others/like.png"
        action [Hide("blur"), Hide("subscribed_screen", transition=ease), Hide("subscribed_like_screen", transition=ease), Jump("subscribe_thanks")]#Hide("subscribe", transition=dissolve), Jump("subscribe_thanks")]
