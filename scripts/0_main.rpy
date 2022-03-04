# "../bin/screens_.rpy"
# "../bin/gui_.rpy"
# "../bin/conf.rpy"
# "../bin/characters_base.rpy"

# "1_uwertura.rpy"

label start:
    #scene lobby
    show screen z
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
        "abi":
            jump abi
        "abi2":
            jump blowek2
        "abi3":
            jump transparenty2
        "monolog1":
            jump konop_monolog1
        "monolog2":
            jump konop_monolog2
        "transparenty":
            jump transparenty
        "wybór1":
            jump wybor1
        "wybór1 - blowek":
            jump blowek
        "dziewczeta":
            jump dziewczeta
        "bloody_text":
            jump bloody_text
        "next":
            jump scenes2

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
