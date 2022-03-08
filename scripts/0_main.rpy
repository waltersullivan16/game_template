# "../bin/screens_.rpy"
# "../bin/gui_.rpy"
# "../bin/conf.rpy"
# "../bin/characters_base.rpy"

# "chapter1/1a_poczatek.rpy"
# "chapter1/1b_dziewczyny.rpy"

label start:
    $ stop_music()
    #scene lobby
    show screen z with slow_fade
    #jump chapters
    jump uwertura_scenes
    #jump wybor
    #jump dziewczeta
    #jump dziewczeta_wardega
    #jump bloody_text
    #jump legenda
    #jump gazeta
    #jump namiejsce
    #jump sad_poczatek

label chapters:
    menu:
        "uwertura":
            jump uwertura_scenes
        "TEST":
            jump test

label uwertura_scenes:
    menu:
        "monolog1":
            jump konop_monolog1
        "monolog2":
            jump konop_monolog2
        "co robic1":
            jump menu1_blowek
        "szukanie blowka part1":
            jump check_blowek1a
        "co robic2":
            jump menu2_blowek2
        "t":
            jump check_blowek2f_anim
        "dziewczeta":
            jump dziewczeta
        "bloody":
            jump bloody_text

label scenes2:
    menu:
        "kopniak":
            jump kopniak
        "legenda":
            jump legenda
        "gazeta1":
            jump gazeta1
        "gazeta2":
            jump gazeta2
        "powiedzenia":
            jump powiedzenia
        "koniec_powiedzen":
            jump koniec_powiedzen
        "prev":
            jump uwertura_scenes
