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

screen blur_background:
    #add "blur"
    on "show" action Function(renpy.show_layer_at, choice_bg_transform_show, layer='master')
    on "hide" action Function(renpy.show_layer_at, choice_bg_transform_hide, layer='master')

screen choices_template(chapter, imagebuttons):
    use blur_background
    modal True
    style_prefix "choice"
    grid 2 2 at choice_transform:
        xalign 0.5
        yalign 0.5
        xspacing 100
        yspacing 50

        for (it, i) in enumerate(imagebuttons):
            $ mouse = "love" if i.startswith("blowek") else "active"
            imagebutton:
                activate_sound "music/sound effects/button_menu.mp3"
                hover "gui/choices/active_{}.png".format(i)
                mouse mouse
                idle "gui/choices/inactive_{}.png".format(i)
                action [Hide("choices_template", transition=ease),  Jump("{}.{}".format(chapter, i))]

screen chapters(n):
    for i in range(n):
        pass

screen z():
    if persistent.testing:
        use screen_buttons_template(0, 0, Jump("scenes2"))
    use screen_buttons_template(0.9, 0, ShowMenu("preferences"))

screen zz():
    mousearea:
        area (0.0, 0, 1.0, 0.2)
        hovered Show("z", transition=dissolve)
        unhovered Hide("z", transition=dissolve)

screen keymapscreen():    
       key "K_LEFT" action Jump("end")
       #key "K_RIGHT" action next_chapter()

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

screen subscribe_screen:
    #style_prefix "subbutton"
    use blur_background
    imagebutton auto "gui/button/subscribe/subscribe_%s.png":
        xpos 0.1 ypos 0.3
        mouse "active"
        activate_sound "music/sound effects/button.mp3"
        #unhovered If ((subscribed == False), true = [MouseMove(500, 300, 0.3)])
        unhovered MouseMove(500, 300, 0.3)
        #action [SetScreenVariable("subscribed", True), Jump("chapter1._3subscribe_like")]#, SelectedIf(False)]
        action [Show("subscribed_screen"), Hide("subscribe_screen"), Jump("chapter11._3subscribe_like")]#, SelectedIf(False)]
        #[Hide("subscribe_screen"), Show("subscribed_screen"), Jump("subscribe_like")]

screen subscribed_screen:
    use blur_background
    imagebutton auto "gui/button/subscribe/subscribed_%s.png":
        xpos 0.1 ypos 0.3

screen subscribed_like_screen:
    use blur_background
    modal True
    imagebutton auto "gui/button/subscribe/like_%s.png":
        xpos 0.8 ypos 0.3
        mouse "active"
        activate_sound "music/sound effects/button.mp3"
        action [Hide("subscribed_screen", transition=ease) , Hide("subscribed_like_screen", transition=ease), Jump("chapter11._4subscribe_thanks")]#Hide("subscribe", transition=dissolve), Jump("subscribe_thanks")]

transform text_fade_in(t, p=0):
    alpha 0
    pause p
    easeout t alpha 1

screen trofeum(t):
    zorder 1
    hbox:
        add "gui/button/trofeum.png"
        xpos 0.5 ypos 0.1
        text t xpos -320 ypos 0.5 style "trofeum"

screen new_item(name, description):
    zorder 1
    add "gui/button/new_item2.png"
    add "gui/items/{}.png".format(name)
    vbox:
        text name xpos 400 ypos 0.2 style "new_item_name"
        text description xpos 400 ypos 0.5 style "new_item_desc"


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
    use dropdown_menu(btnTexts=["foo", "bar", "baz"])
