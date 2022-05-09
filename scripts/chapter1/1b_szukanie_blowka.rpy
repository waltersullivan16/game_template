# ../../files_list.rpy

############## Menu1 ######################
label chapter21:

label .menu1:
    scene lobby
    show screen choices_template("chapter21", ["blowek", "lexi", "grafika", "uciekaj"])
    pause

label .blowek:
    $ thinking(
        Konopski,'''
Tak, to dobry pomysł.
Jego obecność niewątpliwie podniosłaby moje morale.
Nie mógłbym przecież okryć się hańbą na oczach mistrza.
''')
    $change_scene()
    jump chapter22

label .lexi:
    jump .blowek

label .grafika:
    jump .blowek

label .uciekaj:
    jump .blowek

################### PIERWSZE SZUKANIE BLOWKA ##############

label chapter22:
    scene dark_courtroom
    show dark_blur
    $ play_music("ghost_sigh")
    pause 3.0

label ._1wstep:
    $ thinking(
        Konopski,'''
...
Co to ma kuźwa być?
Gdzie się podziała śmietanka towarzyska youtuba?
Gdzie kamery...? {w=1} Mateusz Kaniowski...? {w=1}Pełnoletnie fanki, mdlejące na mój widok...?
Czy cały wysiłek włożony w przygotowanie tych wszystkich wilczych punów pójdzie na marne?
Po co mam się niby wysilać, skoro i tak nie ma nikogo, kto mógłby potem zmontować kompilację \'Konopski best of\'?
...
Kogo my tu mamy?
Patrząc na te plebejskie twarze muśnięte odrobiną chamstwa, cała ta horda to wyznawcy Wardęgi.
''')
    $ thinking(Konopski, "Pardon, cała ta {size=+5}WATAHA®{/size}.")
    $ play_sound_effect("badum")
    pause 2.0
    $thinking(
        Konopski,'''
To nawet nie był żart.
W każdym razie, czy Wardęga serio nie mógłby urządzać zlotu swoich fanów w innym miejscu niż sala rozpraw...?
Na przykład w buszu?
I co ma ze sobą ta baba po lewej?
''')

label ._2o_junko_mowa:
    show junko1 with dissolve
    $renpy.pause(2)
    show junko2

    $thinking(
        Konopski,'''
O wilku mowa, złapała ze mną kontakt wzrokowy.
...
Czaicie? O WILKU. W sensie że{nw}
''')
    $ stop_music()
    show junko3 with vpunch

    $ thinking(Konopski, "{size=+20}{fast}Co do...?{/size}")

    show toko1 with dissolve
    show toko22

label ._3o_toko_mowa:
    $ thinking(Konopski, "Współczuję tej okularnicy całym sercem, ja na jej miejscu chyba bym{nw}")
    show toko3 with vpunch
    Konopski "{fast}{size=+50}Ja pierdolę co jest grane{/size}"


label ._4watahanska_wrogosc:
    $ thinking(Konopski,"Co to za stado poje{nw}")
    $ scene_courtroom1()

label ._5creepy_kokichi:
    $ play_sound_effect("kokichi")
    show blur with transition("maska", 3)
    show kokichi at creepy_kokichi with Dissolve(4.0)
    pause 2
    $ play_sound_effect("upadek")
    scene black with vpunch
    $ renpy.pause(2.0, hard=True)

############ MENU 2 ##########33

label chapter23:
    scene lobby with transition("eye", time=1.5, parts=16)

label ._1wstep:
    $ thinking(
        Konopski,'''
...
Nie wydaje mi się, żeby na sali był Blowek.
...
Zrobiło się tu strasznie duszno...''')

label ._2menu2:
    show screen choices_template("chapter23", ["blowek2", "lexi", "pocieszajka", "uciekaj"])
    pause

label .pocieszajka:
    jump .blowek2

label .blowek2:
    $ thinking(
        Konopski,'''
Poprawić czuprynkę?
Jak można poprawić czystą perfekcję?
Czemu w ogóle przeszło mi to przez myśl?
Poza tym, zorientowałbym się od razu, gdyby Blowek-sensei był na sali.
Zawsze i wszędzie dojrzałbym przystojne lico tego youtubowego Adonisa.
...{w=1}...{w=0.5}...
No dobra, sprawdzę. Tak dla pewności.
Może uda mi się to zrobić na tyle dyskretnie, że nikt nie zwróci na mnie uwagi.
...{w=1}
A nawet jeśli, to i tak nie ma się czym przejmować. Najgorsze i tak już mam za sobą.
''')

label .ostatnie_wahanie:
    scene black with transition("wet") 
    $stop_music()
    pause(1)
    $ change_style("straznik")
    $ thinking(BlankBlip, "Przynajmniej taką mam nadzieję...")
    $ change_scene(time=[0, 0], pause=1)

############# SZUKANIE BLOWKA 2 ##################

label chapter24:
    scene normal with Dissolve(3)

label .poczatek_szukania2:
    $ thinking(
        Konopski,'''
Jakoś tu spokojniej i mniej niepokojąco.
Może to zasługa światła.
A może to ja odrobinę się już wyluzowałem i zacząłem postrzegać rzeczy takimi, jakimi są naprawdę.
Może to nie było nawet stado Wardęgi.
Pardon, {size=+10}WATAHA®{/size} Wardęgi.
''')

    pause 1.5
    $ thinking(
        Konopski,'''
No i gdzie ba-dum-tssk?
Tym razem to miało pretendować do kategorii żart.
''')
    pause 1.0 
    $ thinking( Konopski, "Amatorzy.")

label .brak_badum:
    $ thinking(Konopski, "Mniejsza o to. Może to nie była nawet {size=+10}WATAHA®{/size}{nw}")
    $ play_sound_effect("badum")
    $ renpy.pause(2.0)

    $ thinking(
        Konopski,'''
Nie! {w=0.5} Tu tak totalnie {cps=10}NIE{/cps}!
Bardziej "NIE" niż za pierszym razem!
''')
    $ thinking(
        Konopski,"Czy wy w ogóle wiecie czym jest <ba-dum-tsk>?")
    pause(1)
    $play_sound_effect("badum")
    pause(3)
    $ thinking(Konopski, "...")
    $ thinking(
        Konopski,'''
Z kim ja pracuję...{w=1}
Dobra, jeszcze raz.
''')
    $ thinking(Konopski, "To nie byli ludzie z fandomu...{nw}")
    $ play_sound_effect("badum")
    pause 2

label chapter25:
    scene normal at blur
    show dark_blur with dissolve

label .gnojenie_pracowników:
    
    show konopski ej at right with moveinright
    Konopski "No już bez jaj co się tam dzieje?"
    show konopski ej angry angry_eyes with vpunch
    Konopski "No kuźwa, co za ciul wpuścił tu Chmielarka?" with vpunch
    Konopski "I od razu ostrzegam, niech mi tu żaden wesołek nawet nie próbuje wykręcić się wersją 'kurier przyniósł go w paczce'"
    Konopski "Bo to będzie żart śmieszny jak jego wypłata.{w=1}{nw}"
    $ play_sound_effect("badum")
    pause 3.0
    Konopski ej happy_eyes flower "Jest jakiś progres."
    pause 1
    Konopski ej -flower -happy_eyes "Że co proszę?"
    Konopski "Podczas rozmowy rekrutacyjnej zagrał na pianinie niczym prawdziwy wirtuoz?"
    Konopski ej angry angry_eyes "A co to ma kuźwa za znaczenie?{w=1}"
    Konopski "Jeszcze chwila i wszyscy wylecicie stąd na zbity ryj."
    pause 1
    Konopski ej -angry -angry_eyes "Nie mądralo, nie zdążysz ukryć się w szafie."
    Konopski "Przede wszystkim dlatego, że tu nie ma żadnej szafy."
    pause 1
    Konopski ej angry_eyes angry "{cps=10}NIE{/cps}, osobiście dopilnuję, żeby nie wpuszczać tu żadnego kuriera z szafą w paczce!"
    pause 1
    

label .koniec_przerwy:
    Konopski ej -angry_eyes -angry "Dobra, nie traćmy więcej czasu i zapomnijmy o sprawie."
    Konopski "Znajcie łaskę pana."
    Konopski ej angry_eyes "Ale niech mi to będzie ostatni raz, zrozumiano...?"
    pause 1
    show konopski -angry_eyes with ease
    Konopski "A teraz wracamy do pracy obiboki!"
    Konopski "Światła!{w=0.5} {size=+5}Kamera!"
    show konopski at half_out
    pause 3.0
    show question at question_konop
    Konopski "Świetnie, straciłem wątek. O czym to ja...?"
    Konopski "Ubliżanie ludziom? To było chyba coś w ten deseń..."
    pause 1
    hide question
    Konopski "Hmm? Co tam mamroczesz pod nosem randomowy statysto?"
    pause 1
    Konopski ej happy_eyes "Szukanie Blowka! No przecież!" 
    pause 1
    Konopski ej angry_eyes "Jak mogliście w takim momencie zabrać tyle mojego cennego czasu łachudry!"
    Konopski "Wasza wypłata nie będzie już nawet śmieszna!"
    Konopski "Waszej wypłaty po prostu nie będzie!"
    show konopski ej -angry_eyes
    pause 1
    Konopski ej angry_eyes "E, wy tam! Tylny rząd!"
    Konopski "Czy ja wam pozwoliłem przestać pracować?"
    Konopski "Wracać natychmiast na miejsca, wy lenie patentowane!"
    hide konopski with moveoutright
    hide blur with slow_dissolve

label chapter26:
    scene transparenty_courtroom 

label .co_tak_gwarno:
    
    $ play_music("crowd_talking", relative_volume=1.5)
 
    $ thinking(Konopski, '''
A co tu tak gwarno?
Szczerze mówiąc obawiałem się przez chwilę, że odrobinę za bardzo poniosły mnie nerwy i mój podniesiony głos przykuł czyjąś uwagę.
Ale na szczęście te dzbany są zbyt zajęte sobą.
...
Nie żebym marudził, ale jest to dla mnie odrobinę dziwne.
...
No bo co niby może być bardziej absorbujące od interakcji ze mną...?
...{w=1}...{w=1}
No oczywiście!
''')
#TODO love sound effect
    $ play_sound_effect("magic")
    $ Konopski(text_style("blowek", "{size=+10}Blowek!{/size}"))
    $ thinking(Konopski, '''
Tam może być Blowek!
Wszystko składa się w jedną całość!{w=1}
''')

label .zwiady:
    $ thinking(Konopski, '''
Dobra, szkoda czasu, idę na zwiady.
Wkroczyłem właśnie na wrogie terytorium, więc od teraz muszę zachować szczególną ostrożność.
''')
    $ mute_blip()
$ thinking(Konopski, '''
Bez wątpienia kluczową rolę odegrają wszystkie umiejętności zdobyte podczas gry w Thiefa.{w=1}
Głupio wam teraz, snoby, twierdzący że gry to tylko głupia rozrywka dla dzieci?
Szach-mat frajerzy.
...
No ale bierzmy się do roboty.
Wchodzę do jaskini lwa.
''', style="whisper")

label .jaskinia_wilka:
    $ thinking(Konopski, "Albo raczej...")
    $ thinking(Konopski, "Wchodzę do jaskini WILKA.")
    pause 1
    Konopski "{size=+5}EKHEM{/size}"
    Konopski "Powiedziałem..."
    $ mute_blip(False)
    Konopski "Wchodzę do jaskni {size=+5}WILKA{/size}"
    $ play_sound_effect("badum")

label .dziki_tlum:
    $ change_style("main")
    
    $ stop_music()
    scene transparenty_courtroom
    pause 1.5
    Konopski "No teraz było ja{w=0.1}{nw}"
    show transparenty_courtroom_red# with flashbulb_fast
    #scene transparenty_courtroom_eyes# with flashbulb_fast
    $ play_sound_effect("danger")
    #scene transparenty_courtroom_eyes
    pause 2.0
    #play_sound_effect("upadek")
    show black with vpunch
    pause 2.0
     #   renpy.transition(transition("eye", time=1.5, parts=16))
label .co_sie_dzieje:
    scene transparenty_courtroom2 at sh_blur with transition("eye", time=1.5, parts=16)
    pause 1.0
    $ styled_monologue("crooked", Konopski, '''
Co tu sie wydarzylo...?
...
Gdzie ja...{w=1}
Jak... {w=1} 
Moja glowa...
''')
    scene black with transition("eye", time=2.0, reverse=True)
    pause 1.0
    $change_style("black")
    "" "{size=+10}WDECH{w=1} WYDECH {w=1}{nw}"
    "" " {size=+20}WDECH {w=1} WYDECH{/size}"
    pause 1.
    $ change_style("main")
    Konopski "Ok."
    Konopski "Już mi trochę lepiej.{w=1} Chyba.{w=1}"
    Konopski "W każdym razie font wrócił do normy, więc jest progres."
    pause 1

label chapter27:

label .bibi:

    scene transparenty_courtroom_red0 with transition("eye", time=1.5, parts=16)
    pause .5
    $ play_sound_effect("danger")
    scene transparenty_courtroom_red
    pause 1
    scene black with transition("eye", time=.1, reverse=True)
label .a:
    $change_style("black")
    "" "{cps=55}{size=+20}COFAM MOJE SŁOWA JEST GORZEJ DUŻO GORZEJ JA PIERDOLĘ MOJE ŻYCIE TO BIAŁYSTOK{w=1}{/cps}{/size}"#{nw}"
    pause
    $ play_sound_effect("bibi1", group="junko_bibi")
    pause 3 
    $change_style("main")
    Konopski "Eeeeeee...{w=2}{nw}"
    Konopski "Ale że co?"
    show transparenty_courtroom with transition("eye", time=1., parts=16)
    pause 1.0
    $ junko_bibi("bibi2")
    Konopski "Słucham? Mogłabyś powtórzyć dziwna dziewczynko z misiem?"
    $ junko_bibi("bibi2")
    Konopski "Mam podejść i zobaczyć co...?"
    $ junko_bibi("bibi3", pause=1)
    Konopski "..."
    scene transparenty_courtroom5
    pause .5
    $ play_sound_effect("transparenty")
    pause 2
    Konopski "TRANSPARENTY?"
    $ junko_bibi("bibi4", pause=1)
    Konopski "Przygotowaliście transparenty, żeby zagrzewać nas do boju, tak?"
    $ junko_bibi("bibi_tak", pause=1)


#    Konopski '''
#...
#
#Yyyyyy{w=1} Hej...
#
#Jak to {w=1} miło was widzieć.
#
#Przepraszam za moją chwilową niedyspozycję, takie tam problemy z {w=.5}yyy {w=0.5} no tego,,,{w=0.5} Wiecie o co chodzi?
#
#...
#
#Widzę w waszych oczach pełne zrozumienie, więc chyba nie ma sensu ciągnąć tematu.
#
#Słuchajcie, ajnie się z wami rozmawia i w ogóle, zostałbym dłużej, ale obowiązki wzywają, więc no...{w=1} tego... {w=1}wiecie o co chodzi.
#
#Narauuu
#'''
label .junko_transparent:
    Konopski "Jakie to miłe i... eee... kreatywne."
    $ thinking(Konopski, '''
Chyba zbyt pochopnie ich oceniłem...
Co prawda mają chamskie mordy, ale w gruncie rzeczy są całkiem w porządku.
''')
    Konopski "Mogłabyś odwrócić swój transparent w moją stronę, żebym mógł...{nw}"

label .transparenty_main:
    $ image_punch("zniszcz_sztubaka")
    pause 2.0
    Konopski "Albo wiesz co, zmieniłem zdanie, możesz już zabrać swój{nw}"
    $image_punch("zad")
    pause 1.0
    $ thinking(
        Konopski,'''
Prostackie grubiaństwo. Niczego innego się po nich nie spodziewałem.
Jaki pan, taki kram.
Kto z Wardęga przystaje{nw}
''')
    $image_punch("sor")
    pause 2.0
    $ thinking(
        Konopski,'''
    ...
    Muszę przyznać, że ta eskalująca agresja wywołuje we mnie lekką nutkę niepokoju...
    ''')
label .dis_na_motloch:
    scene black with transition("farba", time=1.5)
    $stop_music()
    show konopski main with moveinbottom
    $ character_monologue(Konopski, '''
Ech, te dzisiejsze fandomy.
{cps=10}ZA MOICH CZASÓW{/cps} wszyscy żyli ze sobą w zgodzie i harmonii. A teraz...? Szkoda gadać.
Tym dzikusom nie pomoże już najbardziej prestiżowy kurs walki z patusiarstwem.{w=1}
Mam oczywiście na myśli Projekt Lady.
No ale nieważne. Nie wiem czemu aż tak spinam dupę.
Co mnie obchodzi zepsucie moralne jakiejś leśnej hołoty?
W gruncie rzeczy są oni przecież nieszkodli {nw}
''')
    hide window

label .transparenty_video:
    
    $play_video("transparenty")
    $ change_scene()

### MENU 3 + PRÓBA UCIECZKI


label chapter28:
    scene lobby with slow_dissolve

label .menu3_ucieczka:
    $ thinking(Konopski, '''
...
Haha{w=0.5} {size=-5}hahaha{/size}{w=0.8}{size=-10} ha
Co za banda pociesznych zgrywusów...
Aż mi się łezka w oku zakręciła...{w=1}
A Blowka jak nie było tak nie ma...
{cps=10}...{/cps}
Taaaa...
Skoro sensei uznał, że nie jest to na tyle istotne wydarzenie, żeby zawracać sobie nim głowę...
...to czy nie byłoby to z mojej strony wysoce niestosowne, gdybym sam się na nim pojawił?
Może to zostać odebrane jako próba podważenia słuszności jego decyzji.
''')
    show screen choices_template("chapter25", ["uciekaj", "uciekaj", "uciekaj", "uciekaj"])
    pause

label .proba:

    $ thinking(
        Konopski,'''
Chwila. Stop.
Nie mogę tak po prostu stąd wyjść...
{cps=8}...{/cps}{w=2}
Gdzie mój płaszcz?
...
Dobra, walić to, spadam jak jest.
Narauuu{nw}''')
    jump dziewczeta
