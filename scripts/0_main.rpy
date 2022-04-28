# "../bin/screens_.rpy"
# "../bin/gui_.rpy"
# "../bin/conf.rpy"
# "../bin/characters_base.rpy"

# ../files_list.rpy

# "chapter1/1a_poczatek.rpy"
# "chapter1/1b_dziewczyny.rpy"

label start:
    $ stop_music()
    #$ _dismiss_pause = True
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
        "currrent check":
            jump transparenty
            #$ load()
        "intro":
            jump intro_menu
        "szukanie blowka":
            jump szukanie_blowka_menu

        "dziewczyny":
            jump dziewczyny_menu
        "strażnik":
            jump straznik_menu

label intro_menu:
    menu:
        "początek":
            jump quote_screen
        "monolog":
            jump konop_monolog1
        "winny":
            jump winny
        "monolog2":
            jump winny
        "subskrybuj":
            jump subscribe

label szukanie_blowka_menu:
    menu:
        "co robic1":
            jump menu1_blowek
        "szukanie blowka part1":
            jump check_blowek1a
        "co robic2":
            jump menu2_blowek2
        "blowek2 poczatek":
            jump check_blowek2a
        "wkurw konopskiego":
            jump check_blowek2b
        "koniec przerwy":
            jump koniec_przerwy
        "rozważania na temat szukania blowka":
            jump lesne_tradycje
        "lesne menu":
            jump lesne_menu_var
        "transparenty":
            jump danger_transparenty

label dziewczyny_menu:
    menu:
        "bloody":
            jump bloody_text
        "kopniak":
            jump kopniak
        "legenda":
            jump legenda
        "gazeta0":
            jump gazeta0
        "gazeta1":
            jump gazeta1
        "gazeta2":
            jump gazeta2
        "powiedzenia":
            jump powiedzenia
        "koniec_powiedzen":
            jump koniec_powiedzen

label straznik_menu:
    menu:
        "namiejsce":
            jump namiejsce
        "lilmasti_intro":
            jump lilmasti_intro
        "lilmasti_konop":
            jump masti_konop

#label chapter1_t:
# quite_screen    
