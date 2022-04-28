"../files_list.rpy"

################# TEMPLATES ################

screen screen_buttons_template(x, y, action):
    imagebutton:
        xalign x
        yalign y
        idle "gui/button/kopi2.png"
        hover "gui/button/kopi2_active.png"
        mouse "active"
        action action 

screen main_options_template(options):
    add "very_dark_blur"
    modal True
    vbox xalign .5 yalign .5:
        for (n, a) in options:
            textbutton n mouse "active" action a

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

screen z():
    use screen_buttons_template(0, 0, Jump("uwertura_scenes"))
    use screen_buttons_template(0.9, 0, ShowMenu("preferences"))


screen main_options():
    use main_options_template([
        ("main menu", Show("main_menu")),
        ("save", ShowMenu("save")),
        #("skip", (alternate Skip(fast=True, confirm=True))),
        #("auto", Preference("auto-forward", "toggle")),
        ("preferences", ShowMenu("preferences")),
        ("mute", ToggleMute("music")), 
        ("return", Hide("main_options"))
    ])
    

screen volume_options():
    modal True
    frame:
        has vbox
        bar value Preference("sound volume") released Play("sound", "music/sound effects/badum.mp3")
        bar value Preference("music volume")

screen button_overlay():
    mousearea:
        area (0, 0, 1.0, 100)
        hovered Show("volume_options", transition=dissolve)
        unhovered Hide("volume_options", transition=dissolve)


screen choices1_blowek():
    modal True
    use choices_template("choices1_blowek", ["blowek", "lexi", "grafika", "uciekaj"])

screen choices2_blowek_sequel():
    modal True
    use choices_template("choices2_blowek_sequel", ["blowek2", "lexi", "pocieszajka", "uciekaj"])

screen choices3_uciekaj():
    modal True
    use choices_template("choices3_uciekaj", ["uciekaj", "uciekaj", "uciekaj", "uciekaj"])

screen subscribe_screen():
    add "blur"
    imagebutton:
        xpos 0.1
        ypos 0.3
        hover "images/scenes/subscribe/subscribe.png"
        unhovered [MouseMove(500, 300, 0.3)]
        mouse "active"
        activate_sound "music/sound effects/button.mp3"
        idle "images/scenes/subscribe/subscribe.png"
        action [Hide("subscribe_screen"), Jump("subscribe_like")]

screen subscribed_screen():
    add "blur"
    imagebutton:
        xpos 0.1
        ypos 0.3
        hover "images/scenes/subscribe/subscribed.png"
        idle "images/scenes/subscribe/subscribed.png"

screen subscribed_like_screen():
    add "blur"
    imagebutton:
        xpos 0.8
        ypos 0.3
        hover "images/scenes/subscribe/like.png"
        unhovered [MouseMove(1050, 300, 0.3)]
        mouse "active"
        activate_sound "music/sound effects/button.mp3"
        idle "images/scenes/subscribe/like.png"
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

screen trofeum(t):
    zorder 1
    hbox:
        add "gui/button/trofeum.png"
        xpos 0.5 ypos 0.1
        text t xpos -350 ypos 0.4 style "trofeum"

screen new_item(name, description):
    zorder 1
    vbox xalign 0.5 yalign 0.1:
        add "gui/button/new_item.png"
        vbox:
            xpos 0.6 ypos 0.0
            text name xpos 0 ypos -230 style "new_item"
            text description xpos -100 ypos -100 style "new_item"

        vbox:
            xpos 0.1 ypos 0.1
            text "fsdfsd" xpos -350 ypos 0.2 style "new_item"
            text description xpos -500 ypos 0.5 style "new_item"


############ EXAMPLES ###########
screen dragdrop_example:
    draggroup:
        drag:
            drag_name "Ivdsady"
            child "gui/button/kopi.png"
            droppable False
            dragged False
            xpos 100 ypos 100
        drag:
            drag_name "Ivy"
            child "gui/button/kopi.png"
            droppable False
            dragged False
            xpos 150 ypos 100

### DROPDOWN MENU

screen dropdown_menu (selectedOption="", opt_xpos=300, opt_ypos=200, btnTexts=[""]):
    zorder 50
    $ s = 1
    textbutton selectedOption:
        xsize 200 ysize 50
        xpos opt_xpos  ypos opt_ypos
        action If ((s == 1), true = [ Show("dropdown_options", btnTexts=btnTexts, opt_xpos=opt_xpos, opt_ypos=opt_ypos), SetVariable(s, 0)], false = [Return])
       
screen dropdown_options (btnTexts, opt_xpos=0, opt_ypos=0):
    zorder 51
    modal True 
    $yIndent = 20
    $ySpacing = 40
    fixed:
        xpos opt_xpos        ypos opt_ypos+yIndent
        $listSize = len(btnTexts)
        for i in range(listSize):  
            $buttonOption = btnTexts[i]
            textbutton btnTexts[i]:
                xsize 200 ysize 50
                action [ Show("dropdown_menu", selectedOption=buttonOption, btnTexts=btnTexts, opt_xpos=opt_xpos, opt_ypos=opt_ypos), Hide("dropdown_options")] 
                #idle_background "gui/button/kopi2.png"
                #hover_background "gui/button/kopi2.png"
                ypos yIndent
            $yIndent += ySpacing

screen xx:
    use dropdown_menu(selectedOption="Foo", btnTexts=["foo", "bar", "baz"])
