# "0_main.rpy"

# ../bin/gui_.rpy
# ../bin/conf.rpy
# ../characters.rpy
# ../screens.rpy

label dziewczeta:
    scene bg lobby
    $ change_style("main")

    Unknown "Och, tak się cieszę, że zdążyłyśmy! Bałyśmy się, że wszedł już pan na salę."
    show pearl embarassed with vpunch
    Pearl "A bardzo nam zależało, żeby podziękować panu za to wszystko co pan dla nas robi."
    show ema happy at right with vpunch
    Ema "Byłam bardzo zawiedziona, że afera cesarza narcyza przeszła zupełnie bez echa. Tak się cieszę, że tym razem udało się nagłośnić sprawę, może nareszcie coś się zmieni!"
    show penny gossip at true_left with vpunch
    Penny "Czy planuje pan dzisiaj poruszyć kwestię groomingu? Ten wątek jakoś zagubił się w całym tym ferworze walki, a przecież to naprawdę kluczowa sprawa."

    Konopski "..."
    $ thoughts_monologue(
        Konopski,
    "Niech to szlag.")
    show blur
    menu:
        "Uśmiechnij się czarująco i powiedz, że musisz iść do toalety":
            jump proba_ucieczki
        "Powiedz, że dasz im autograf, tylko muszą chwilę poczekać, bo zostawiłeś swój długopis w płaszczu":
            jump proba_ucieczki
        "To samo co powyżej, tylko zamień 'długopis' na 'pióro'. Brzmi bardziej dostojnie.":
            jump proba_ucieczki
        "Weź rozbieg, przeskocz nad najniższą i nie zatrzymuj się, aż nie dobiegniesz do domu. No chyba że gdzieś zauważysz swój wytworny płaszczyk.":
            jump proba_ucieczki

label proba_ucieczki:
    hide blur
    Konopski "Słuchajcie, jeśli chodzi o ten autograf, to dajcie mi chwilę..."
    Ema main "Proszę się nie wygłupiać, nie będziemy teraz zawracać panu głowy jakimiś błachostkami."
    Ema "Wiemy, że potrzebuje pan teraz jak najwięcej wsparcia."
    Penny main "Inni zaraz po usłyszeniu nazwiska prokuratora, uciekliby w popłochu."
    $ thoughts_monologue(
        Konopski, '''
Ja chciałbym uciec w popłochu, mimo że nawet nie usłyszałem...
...
Zaraz, zaraz.
Coś tu się nie zgadza.
Przecież to ja jestem prokuratorem.''')
    Konopski "O kim ty właściwie mówisz?"

    Pearl serious "Trwożę się wypowiedzieć to imię. Sama myśl wywołuje we mnie ciarki."
    Konopski "To może koleżanka?"
    jump dziewczeta_wardega

label dziewczeta_wardega:
    show ema at right
    show penny at true_left
    show pearl
    Ema determined "Dobrze zrobię to."
    Ema "Jest to prokurator.."
    pause 1.0
    show lobby at Glitch
    pause 1.0
    show ema at Glitch
    show pearl at Glitch
    show penny at Glitch
    jump bloody_text

label bloody_text:
    #show wardega_title at blood_particle#with Dissolve(2, alpha=True#)
    #$ renpy.movie_cutscene("cutscenes/strasznega.webm")
    #pause
    scene black
    # #$ fading_text("sniff", 1.0, 400, 300, 600, 600, color="#fff", size=24)
    # pause
    #play sound "music/wardega.mp3"
    #show text creepy_maker("WARDEGA") with Dissolve(2, alpha=True)
    # pause
    #hide text with Dissolve(3, alpha=True)
    #pause
    $ change_style("creepy")
    show konopski smirk at right with ease
    Konopski "Wy... zdajecie sobie sprawę z tego, że \"Wardęga\" to nie jest jego imię, prawda?"
    Konopski main "Co tu się właśnie wydarzyło?"
    Konopski "Co stało się z pierwszoosobowy styl narracji?"
    Konopski "Sympatycznym w swej prostocie okienkiem dialogowym?"
    Konopski "Bogatym w szczegóły drugim planem?"
label kopniak:
    show pearl determined at kick_out
    pause 0.9
    show konopski at kicked_out
    pause 0.2
    Pearl "Ale proszę nie wchodzić w kadr!"
    show ema determined at right with moveinbottom
    Ema "A poza tym, czy naprawdę myśli pan, że jest to odpowiedni moment na łamanie czwartej ściany?"
    Konopski "A mógłbym mieć jakiekolwiek wątpliwości dlatego bo...?"
    pause
    Ema thinking "Tak właściwie to nie wiem, ale jest w tym coś budzącego grozę..."
    jump legenda

label legenda:
    show penny main at true_left with moveinbottom
    show pearl
    show ema at right
    Penny "No wie pan, jak to mówią..."
    Penny cards "Nie należy wywoływać Wardęgi z lasu..."
    Konopski "Jakoś nie wydaje mi się, żeby ktokolwiek, kiedykolwiek to powiedział..."
    Ema determined "Legenda głosi, że jeśli podczas jakiejś dramy, wypowie się trzy razy WARDEGA, to w przeciągu
    dwóch godzin przejmie on nad tą dramą dowództwo, zmieniwszy wcześniej całą istotę problemu na coś zupełnie innego."
    Penny cards "Nie wolno jednak igrać z siłami ciemności."
    Penny "Użycie watahańskiej mocy dla własnych korzyści może przynieść poważne konsekwencje."
    Pearl "Jak to mówią: Wardęga nierychliwy, ale sprawiedliwy."
    Konopski "..."
    Konopski "Ci nieistniejący 'oni' mają zadziwiająco wiele do powiedzenia na temat Wardęgi..."
    Ema notes "A teraz, ku przestrodze, zobaczmy do czego prowadzić wymawianie imienia czarnoksiężnika swego na daremno."
    hide Ema
    hide Pearl
    hide Penny
    scene black
    Konopski "A teraz, ku przypomnieniu, podkreślmy fakt, że jego imię brzmi 'Sylwester', a nie 'Wardega'..."
    pause
    Konopski "Co, znowu cutscenka...? No błagam..."
    # vutscenka lol
    jump gazeta0

label gazeta0:

    $change_style("main")
    scene lobby with fade
    show pearl serious
    show ema confused at right
    show penny at true_left
    Konopski "..."
    Konopski "Słuchajcie, nie żebym się czepiał, ale czy nie wydaje wam się, że odrobinę przesadzacie z tym dramatyzmem?"
    Ema thinking "Ale to przecież nie jest naszego autorstwa."
    Penny gossip "To był filmik {b}KU PRZESTRODZE{/b}, umieszczony na oficjalnej stronie Wardęgi {a=a}www.zorro-z-lasu2.com{/a}. Prawie wszystko co do tej pory powiedziałyśmy pochodzi z tej strony."
    Konopski "To... wiele tłumaczy..."
    $ Konopski(text_style("thoughts", "Błagam, powiedzcie mi, że ta dwójka na końcu to część jakiejś zagadki..."))
    $ thoughts_monologue(
        Konopski, '''
To niemożliwe, że istnieje jeszcze jeden zorro-z-lasu, {w=1.0}prawda...?{w}
{size=+10}{cps=6}{b}PRAWDA?{/b}{/cps}{/size}''')
    Ema notes "Jest tu jeszcze sekcja {i}'Poznaj czarnoksiężnika'{/i}."
    Konopski "A czy moglibyśmy skończyć tę rozmowę po procesie? Ja naprawdę muszę jeszcze...{nw}"
    Ema "Ulubione filmy..."
    #$ Pearl(newspaper_text("{u}Ulubiony film{/u}{p}Nagranie z procesu O.J.Simsona."))
label gazeta1:
    #show pearl
    #show ema at left
    #show penny at right
    scene ulubione_filmy
    $change_style("www")
    #Konopski "dsadadad" (multiple=2)
    #Pearl "{size=+10}{font=gui/fonts/chomsky.ttf}{u}Ulubiony film{/u}{/font}{/size}{font=gui/fonts/unique.ttf}{p}Nagranie z procesu O.J.Simsona.{/font}"(multiple=2)
    $ fav_filmy1 = [
        text_style("coda", "1) Nagranie z procesu O.J.Simsona{w}"),
        text_style("www", "{p}{u}Komentarz{/u}:{size=+10}{cps=3} MAJSTERSZTYK.{/cps}{/size}{p}Opus magnum sądownictwa.{p}Pozycja {b}obowiązkowa{/b} dla fanów rezolutnej dysputy!!!{w}\n"),
        "\n\n\n",
        text_style("dark_thoughts", "{image=minikonopski} Fa...{w=1} fanów rezolutnej dysputy...?"),
    ]
    $Pearl("".join(fav_filmy1))
    $ fav_filmy2 = [
        text_style("coda", "2) Tańczący z wilkami"),
        text_style("coda", "3) Braterstwo wilków"),
        text_style("coda", "4) Wilkołak"),
        text_style("coda", "5) Anakonda"),
        #text_style("www", "{u}Komentarz{/u}: Czasami wychodzi ze mnie bestia ;P{w}\n"),
        "{u}Komentarz{/u}: Czasami wychodzi ze mnie bestia ;P{w}\n",
        text_style("dark_thoughts", "{image=minikonopski}..."),
        text_style("dark_thoughts", "{u}Komentarz{/u}:{w} Nie{p}{w} Po prostu {w}{b}{size=+10}NIE{/size}{/b}.")
    ]
    $Pearl("{w}\n".join(fav_filmy2))

    $ fav_filmy3 = [
        text_style("coda", "6) Cube"),
        text_style("coda", "7) Enigma"),
        text_style("coda", "8) Sudoku"),
        text_style("coda", "9) Krzyżówki panoramiczne"),
        text_style("dark_thoughts", "\n{image=minikonopski}"),
        text_style("dark_thoughts", "Czy my nadal jesteśmy w kategorii 'filmy'...?")
    ]
    $Pearl("{w}\n".join(fav_filmy3))
label gazeta2:
    hide pearl
    hide ema
    show bg ulubione_filmy with wiperight
    show pearl at true_left with moveinbottom
    $change_style("main")
    Pearl "To wszystko."
    $Konopski(text_style("thoughts", "Dzięki bogu..."))
    Konopski "Ok, to skoro już wiemy wszystko o czarnoksiężniku, to..."
    show bg ulubione with wiperight
    show ema at Position(ypos=800) with moveinbottom
    Ema main "{w=1}Ulubione powiedzenia"
    show bg ulubione_powiedzenia with wiperight
    Konopski "Dlaczego mi to robicie... Jestem po waszej stronie..."
    show pearl determined
    Ema determined "Musi pan myśleć strategicznie!"
    Ema "Dobre rozeznanie na froncie wroga może dać istotną przewagę!"
    $Konopski(text_style("thoughts", "No jasne, już nie mogę się doczekać momentu, w którym zmiotę wszystkie argumenty Wardęgi siłą jego ulubionych powiedzeń..."))
    hide pearl with moveinbottom
    hide ema with moveinbottom
label powiedzenia:
    show ulubione_powiedzenia
    hide ema
    hide pearl
    $ change_style("www")
    $ fav_powiedzenia = [
        text_style("coda", "1) Każdy kij ma dwa końce"),
        text_style("cite", "{space=50}powiedzenie ludowe"),
        text_style("coda", "2) Bo do dramy trzeba dwojga"),
        text_style("cite", "{space=50}powiedzenie ludowe"),
        text_style("coda", "3) Gdzie dwóch się bije, tam Wardęga korzysta,"),
        text_style("cite", "{space=50}autor anonimowy"),
        text_style("dark_thoughts", "\n{image=minikonopski}{size=+50}{cps=3}...{/size}{/cps} {w}{size=+30}co to kuźwa jest?{/size}"),
        text_style("cite", text_style("dark_thoughts", "powiedzenie ludowe")),
#        text_style("dark_thoughts", "Początkowo trochę zbił mnie z tropu ten odświeżający powiew normalności, ale widzę że koniec końców wszystkie drogi prowadzą do Wardęgi..."),
    ]
    $Ema(list_text(fav_powiedzenia))
    $fav_powiedzenia2 = [
        #text_style("coda", "4) Bez Wardęgi jak bez ręki."),
        #text_style("cite", "{space=50}Sylwester Wardęga"),
        #text_style("dark_thoughts", "{image=minikonopski} To... niepokojące na wielu płaszczyznach."),
        text_style("coda", "4) Kto z Wardęgą wojuje od Wardęgi ginie.."),
        text_style("cite", "{space=50}Zaradna Wersow i zdemoralizowany Konopski"),
        text_style("dark_thoughts", "\n{image=minikonopski}{size=+50}{cps=3}...{/size}{/cps} {w}{size=+30}co tu się wydarzyło...{/size}"),
        text_style("dark_thoughts", "Wardęga z youtuba, wszystkim lżej."),
        text_style("cite", text_style("dark_thoughts", "absolutnie wszyscy youtuberzy")),
        text_style("coda", "5) Z Wardęgą ci się upiecze.") +
        text_style("dark_thoughts","{w}Niech zgadnę, kto może być tego autorem...") +
        text_style("dark_thoughts", "Postawię na \'cnotliwego Lexia\'..."),
        text_style("cite", "{space=50}Cyceron"),
        text_style("dark_thoughts", "\n{image=minikonopski} {size=+50}{cps=3}.......{/size}{/cps}")
    ]
    $Ema(list_text(fav_powiedzenia2))

label koniec_powiedzen:
    scene black with fade 
    $change_style("main")
    pause 1.0
    $Konopski(text_style("thoughts", "Co jak co, ale jednego Wardędze nie można odmówić."))
    $Konopski(text_style("thoughts", "Zaskakująco dobrze się trzyma jak na swoje lata..."))
    pause
    scene lobby
    pause 1.0
    $Konopski(text_style("thoughts", "Co za ulga... Stęskniłem się za tym pomieszczeniem..."))
    $Konopski(text_style("thoughts", "..."))
    $Konopski(text_style("thoughts", "Nie, chwila, żadne 'stęskniłem się'."))
    $Konopski(text_style("thoughts", "Muszę. Stąd. W tym momencie..."))
    Pearl "...wyjść."
    show pearl main with moveinbottom
    show ema at right with moveinright
    show penny at true_left with moveinleft
    $Konopski(text_style("thoughts", "Czy mój plan natychmiastowej ewakuacji jest aż tak ewidentny...?"))
    menu:
        "Zaprzecz wszystkiemu":
                jump prawie_koniec
        "Zgrywaj biedactwo, przyłóż rękę do czoła i teatralnie zemdlej. Łkając z podłogi każ im znaleźć swój płaszcz.":
                jump prawie_koniec
        "Posądź o szpiegowanie dla Wardęgi i powiedz, że idziesz szukać kogoś z ochrony, bo miarka się już przebrała":
                jump prawie_koniec
        "Bądź twardzielem, zostaw baby i uciekaj":
                jump prawie_koniec
label prawie_koniec:
    Konopski "Słuchajcie, wy małe flądry, najpierw próbujecie zniszczyć mnie psychicznie poprzez zmuszenie do oglądania materiałów przygotowanych przez waszego guru, a teraz macie czelność insynuować, że mam zamiar stąd bezpardonowo uciec?"
    Pearl "Flądry...?"
    Ema "Guru...?"
    Penny "Uciec...?"
    Ema "My właśnie mówiłyśmy, że musimy wyjść, bo zaraz chyba będzie pan proszony na salę..."
    $ Konopski(text_style("thoughts", "..."))
    $ Konopski(text_style("thoughts", "A tegoroczna nagroda dla youtubera najgorzej traktującego swoje widzki wędruje dooooo..."))
    Konopski "A ja właśnie wam odpowiedziałem 'Bardzo miło mi było was poznać dziewczyny i naprawdę chętnie zostałbym z wami dłużej, ale wiecie, obowiązki wzywają'."
    Penny "I to dosłownie."
    Konopski "Słucham?"

label namiejsce:
    "" "PANIE KONOPSKI, PROSZĘ ZAJĄĆ SWOJE MIEJSCE!"
    Konopski "Nie, nie, nie, szybko, gdzie jest kurtka, walić kurtkę, wycho..."
    "" "PANIE KONOPSKI NA MIEJSCE"
    Konopski "Panie strażniku, przysięgam na wszystko, sala sądowa absolutnie moim miejscem nie jest!"
    "" "PANIE KONOPSKI CZY MAM UŻYĆ SIŁY?"
    Konopski "Czy naprawdę musicie w tak przemocowy sposób traktować prokuratora?"
    "" "Szanowny panie, cóż to za pomówienia, oczywiście że traktujemy prokuratora z należytym szacunkiem!"
    Konopski "No to czy mógłby pan..."
    "" "Ale do oskarżonych z całą pewnością tego szacunku nie mamy!"
    Konopski "Słucham? Zaszła jakaś pomyłka, ja przecież..."
    Pearl "Powodzenia, panie Konopski! Dziękujemy za... rezolutną dysputę!"
    Konopski "Błagam, powiedzcie że to jakiś prank..."
    Konopski "Dubiel, gdzie jesteś...   ?"
    jump end

label end:
    return
