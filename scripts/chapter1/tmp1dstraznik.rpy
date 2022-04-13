# "../../files_list.rpy"
# "1a_poczatek.rpy"

# ../bin/gui_.rpy
# ../bin/conf.rpy
# ../characters.rpy
# ../screens.rpy


label namiffejsce:
    $ Straznik(text_style("straznik", "PANIE KONOPSKI PROSZĘ ZAJĄĆ SWOJE MIEJSCE"))
    #$play_music("straznik")
    Konopski "Nie, nie, nie, szybko, gdzie jest kurtka, walić kurtkę, wycho...{nw}"
    $Straznik(text_style("straznik", "PANIE KONOPSKI, NA MIEJSCE, NATYCHMIAST"))
    Konopski "Panie strażniku, przysięgam na wszystko, sala sądowa absolutnie moim miejscem nie jest!"
    $Straznik(text_style("straznik", "PANIE KONOPSKI CZY MAM UŻYĆ SIŁY?"))
    Konopski "No nie wygłupiajmy się już, przecież nie jestem{nw}"
    $Straznik(text_style("straznik", "CZERWONY ALARM, CZERWONY ALARM!!"))
    $Straznik(text_style("straznik", "ODDZIAŁ BOJOWY MA SIĘ NATYCHMIAST STAWIĆ PRZED GŁÓWNĄ SALĄ ROZPRAW"))
    $Straznik(text_style("straznik", "MAMY TU PYSKATEGO DELIKWENTA ZE SKŁONNOŚCIAMI DO BUNTU"))
    $play_sound_effect("punch")
    show najman at true_left with vpunch
    pause 1
    $play_sound_effect("punch")
    show lil_masti at true_right with vpunch
    pause 1
    $play_sound_effect("punch")
    pause 1
    $play_sound_effect("punch")
    pause 1
    Konopski "Eee... czy my czekamy jeszcze na kogoś?"

    LilMasti "A co, spieszysz się gdzies z gnojku?"

    Konopski "...{w=1} Cofam pytanie."

    Najman "Ale po co tak ostro kobieto?"
    Najman "Widzę w tym młodym człowieku zamiłowanie do czekania."
    Najman "Pozna swój swego, nieprawdaż młody?"

    Konopski "Eeee... tak, nieprawdaż. W sensie prawdaż. W sensie ma pan całkowitą rację."
    Konopski "No to koniec. Już po mnie."
    Konopski "Mam nadzieję, że chociaż pochowają mnie w bluzie z filozofa."

    $Straznik(text_style("straznik", "CICHO TAM BYĆ, WY PTASIE MÓŻDZKI. SKUPCIE SIĘ NA GŁÓWNYM PROBLEMIE."))
    $Straznik(text_style("straznik", "GDZIE SIĘ ZNOWU SZWĘDA SZEREGOWY FERRARI?"))
    $Straznik(text_style("straznik", "MAM MU WYSŁAĆ SPECJALNE ZAPROSZENIE, ŻEBY ŁASKAWIE RUSZYŁ SWOJE WIELMOŻNE DUPSKO"))

    Konopski "To... to wszystko..."
    Konopski "Mi po prostu odbiła szajba."

    $Straznik(text_style("straznik", "CZY KTÓRYŚ Z TU ZGROMADZONYCH WIE COKOLWIEK NA TEN TEMAT?"))
    pause 1.0
    $Straznik(text_style("straznik", "Tak, szeregowy Najman?"))

    Najman "Panie poruczniku, mógłbym jeszcze zadać pytanie?"

    $Straznik(text_style("straznik", "W drodze wyjątku."))

    Najman "Czy mógłbym od tego momentu być zwolnionym z obowiązku mówienia?"
    #Najman "Wiem, że postacią epizodyczną, a co za tym idzie nikomu nie chciało się robić dla mnie lipsyncu."
    Najman "W wyniku jakiegoś przeoczenia nie dodano do mojej postaci lipsyncu."
    Najman "Czuję się z tym bardzo nieswojo, więc o ile to możliwe, chciałbym ograniczyć moje wypowiedzi do minimum."

    $Straznik(text_style("straznik", "Naturalnie Najman, stójcie tam sobie statycznie i udawajcie, że jesteście częścią drugiego planu."))

    Najman "Naprawdę?{w=0.5}{nw}"

    $Straznik(text_style("straznik", "{size=+10}NIE{/size}"))
    $Straznik(text_style("SZEREGOWY NAJMAN, WALNIJCIE SIĘ W TEN PUSTY ŁEB I NIE ZAWRACAJCIE MI WIĘCEJ GŁOWY JAKIMIŚ DYRDYMAŁAMI."))
    $Straznik(text_style("Jesteście postacią epizodyczną, nikomu nie chce się babrać z waszymi animacjami."))

    Najman "Bez obrazy poruczniku, ale wolę już być postacią epizodyczną niż głosem z offu"

    $Straznik(text_style("straznik", "..."))

    Najman "..."
    Najman "Przepraszam najmocniej, poniosło mnie."

    Konopski "A może to jest jakaś nowa formuła konferencji FAME MMA?"
    Konopski "Naprawdę fajnie im{nw}"
    Konopski "CZEMU JA SŁUCHAM TEJ DYSKUSJI ZAMIAST STĄD SPIERDALAĆ?"
    Konopski "..."
    Konopski "Dobra, pełne skupienie."
    Konopski "Jeden fałszywy ruch i już po mnie."
    Konopski "Całe szczęście, że posiadam cały wachlarz umiejętności, potrzebnych do bezszelestnego poruszania się."
    Konopski "No umówmy się: platynowe trofeum w Thiefie o czymś świadczy."
    Konopski "Do biegu.{w=0.5} Gotowi...{w=1} START!{w=1}"
    Konopski "Eeee...{w=1} W sumie to jak mam zacząć?"

    menu:
        "Wespnij się na najwyższy punkt w tym pokoju, stwórz mapę terytorium i na jej podstawie zdecyduj co dalej":
            jump skradanka
        "Przestaw poziom trudności na 'very easy' i przejdź obok nich >?":
            jump skradanka
        "Zastanów się, co na twoim miejscu zrobiłby Blowek":
            jump skradanka
        "Zaśpiewaj jak słowik 'barkę', a potem powiedz z wyrzutem, że największy polak by wybaczył":
            jump skradanka

    $Straznik(text_style("straznik", "Najman, za takie pyskówki, to wy zaraz dostaniecie bilet w jedną stronę na Jasną Górę, żebyście sobie tam poczekali aż ochłoniecie."))
    Najman "Z przyjemnością poruczniku."
    pause 1.0
    Najman "Ma pan na myśli czekanie na Ferrariego, tak?"
    $Straznik(text_style("straznik", "Nie.{w} Byłeś blisko, ale NIE."))
    Najman "Czyli o co{nw}"
    $Straznik(text_style("straznik", "Błagam, dajcie mu już ten lipsync."))
    $Straznik(text_style("straznik", "Nie wytrzymam ani sekundy dłużej."))
    $Straznik(text_style("straznik", "KONOPSKI, NA SCENĘ, JEST TU MIEJSCE NA TYLKO JEDEN GŁOS Z OFFU."))
    Konopski "W takim razie dlacz{nw}"
    $Straznik(text_style("straznik", "MÓWIŁEŚ COŚ?"))
    Konopski "..."

    #$Straznik(text_style("straznik", "Ale na twoje szczęście, mam w sobie jeszcze odrobinę człowieczeństwa, więc nie będzie żadnych reperkusji."))
    #$Straznik(text_style("straznik", ""))
    #Najman "Czyli się pan zgadza, tak?"
    #Lil_masti "Najman, z ciebie to jest jednak

    $Konopski(text_style("thoughts", "..."))
    $Konopski(text_style("thoughts", "Co tu się kuźwa dzieje..."))
    $Konopski(text_style("thoughts", ",,,"))
    $Konopski(text_style("thoughts", "No nieważne, to moja ostatnia szansa, której nie mogę zmarnować."))
    $Konopski(text_style("thoughts", "Korzystając z umiejętności nabytych podczas grania w Thiefa, wymknę się niepostrzeżenie jak prawdziwy{nw}"))
    Lil_masti "A gdzie ty się gnoju wybierasz?"

    #"" "Nie ma sensu go szukać poruczniku, szeregowy jest ciężko kontuzjowany, a co za tym idzie niezdolny do wyjścia z domu."
    Najman "A może jeszcze trochę poczekamy poruczniku?"
    $Straznik(text_style("straznik", "..."))
    #$Straznik(text_style("straznik", "Doskonały pomysł szeregowy. "))
    #$Straznik(text_style("straznik", "ACH TAK... A CÓZ TAKIEGO MU DOLEGA?"))
    #"" "Boli go mały palec u stopy."
    #$Straznik(text_style("straznik", "..."))
    #$Straznik(text_style("straznik", "JESTEM ZDEGUSTOWANY{w=1}"))
    #$Straznik(text_style("straznik", "NO ALE KONIEC TEMATU"))
    #$Straznik(text_style("straznik", "SPACYFIKOWAĆ MI TU TEGO NIEPOZORNIE WYGLĄDAJĄCEGO DELIKWENTA"))

    show blur
label do_domu:
    menu:
        "Do domu.":
            jump ucieczka_dom
        "DO DOMU!":
            jump ucieczka_dom
        "eeeee... do domu?":
            jump ucieczka_dom
        "A co cię to kuźwa obchodzi?":
            jump odwaga
    pause

label odwaga:
    "Nie masz wystarczającej ilości punktów samca alfy"
    jump do_domu

label ucieczka_dom:
    Lil_masti "To było pytanie retoryczne głupku."
    Lil_masti "O twoim losie decyduje teraz ja, generał Masti, zawsze gotowa, żeby spuścić ci wpierdol."
    Najman "HOHOHO spuścić HOHOHO"
    #<świerszcze>
    Najman "Tak dla jasności, ona wcale nie jest generałem, tak się tylko zgrywa."
    Lil_masti "..."
    Najman "Chciałaby wyjść przed szereg, ale jakoś to jej nie wychodzi."
    Lil_masti "Najman. Ostrzegam cię..."
    Najman "Zamiast kulturalnie poczekać, jak każdy szanujący się człowiek, to musi wciskać te swoje kłamstewka."
    Lil_masti "Szanujący się człowiek dostrzega różnicę pomiędzy 'kulturalnym czekaniem' a 'kuriozalnie długim czekaniem'."
    Najman "I do tego właśnie doprowadził ten cały feminizm. Gdzoe się podziały prawdziwe kobiety?"
    $Straznik(text_style("straznik", "Widzicie Najman, tak właśnie zachowuje się profesjonalista. "))

    Konopski "Dobrze, dobrze, już idę, po co te nerwy?"
    Konopski "Przecież tak się tylko z wami droczyłem, nie znacie się na żartach?"
    Konopski "dsaproszę, nie rób mi krzywdy..."

    Konopski "Swoją drogą, czy naprawdę musicie w tak przemocowy sposób traktować prokuratora?"
    $Straznik(text_style("straznik", "Szanowny panie, cóż to za pomówienia, oczywiście że traktujemy prokuratora z należytym szacunkiem!"))
    Konopski "Jakoś nie wydaje mi{nw}"
    $Straznik(text_style("straznik", "Ale do oskarżonych z całą pewnością tego szacunku nie mamy!"))
    Konopski "Ale że jak? Zaszła jakaś pomyłka, ja przecież{nw}"
    Pearl "Powodzenia, panie Konopski! Dziękujemy za... rezolutną dysputę!"
    Konopski "Błagam, powiedzcie że to jakiś prank..."
    $ stop_music()
    Konopski "Dubiel, gdzie jesteś...   ?"
    jump end

