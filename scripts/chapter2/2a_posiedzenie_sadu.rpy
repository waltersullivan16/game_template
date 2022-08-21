label chapter2:
    $persistent.thinking = False
    $ change_style("main")
    scene courtroom_full
    $ play_sound_effect("crowd_long")
    #jump sad
    #jump wardega1
    #jump wardega-przemowienie
    #jump gimper

label poczatek_sadu:
    pause 1.0
    scene gavel
    $ play_sound_effect("gavel")
    pause 1.0
    $ play_music("trial")
    $ judge_scene()
    Lexio """
        Otwieram posiedzenie sądu najwyższego.

        Będzie rozpoznana sprawa obecnego tu młodocianego recydywisty Konopskiego.

        Czy mogę poprosić prokuratora oraz jego adiutanta o potwierdzenie gotowości do rozpoczęcia rozprawy?
    """

    $ pros_scene()
    Wardega "Jesteśmy w pełni gotowi wysoki sądzie."

    $ judge_scene()
    Lexio "Czy mógłbym prosić obronę o potwierdzenie gotowości do rozpoczęcia rozprawy?"

label kon:
    $ defense_scene("wtf")
    $ thinking(Konopski, "...")
    Konopski "Co to ma kuźwa być?"
    pause 1
    Konopski "Nie, no ale serio pytam. CO TO MA BYĆ?"
    Konopski "Renesans ery pranków?"
    Konopski "I w co ja jestem kuźwa ubrany?!"
    pause 1
    $ change_pose("konopski", "wkurw")
    Konopski "Kto i kiedy mnie w to ubrał?!"

    $ pros_scene("pogarda")
    pause 1
    Wardega "A oto i nasza diwa, jak zawsze w świetnej formie!"
    Wardega "Ledwo wyszła na scenę, a już zaczęła gwiazdorzyć!"

    $ defense_scene("kropla")
    $ thinking(Konopski, "A oto i nasz Wardęga.")
    $ thinking(Konopski, "Ledwo się odezwał, a już{w=1} mam ochotę strzelić sobie w łeb...")

    $ pros_scene()
    Wardega "Każdy na jej miejscu, kto ma w sobie choć odrobinę przyzwoitości, podziękowałby za tak szykowne wdzianko."
    $ change_pose("wardega", "egzaltacja2")
    Wardega "Ja na przykład jestem niezwykle wdzięczny za przyodzianie mnie w ten gustowny garniturek."

    $ defense_scene()
    $ thinking(Konopski, "No i tu muszę ci przyznać rację.")
    $ thinking(Konopski, "Ja też jestem niezwykle wdzięczny {w=1} za przyodzianie cię w ten gustowny garniturek.")
    $ change_pose("konopski", "beka")
    $ thinking(Konopski, "Ten widok w pewien sposób rekompensuje mi poniesione dziś straty moralne.")

    $ pros_scene()
    Wardega "No tak, jak ja mogłem wcześniej o tym nie pomyśleć! Przecież to takie oczywiste dlaczego czujesz się teraz tak niekomfortowo!"
    pause 1
    $ change_pose("wardega", "pogarda")
    Wardega "To twój pierwszy raz w nieobszczanych ciuchach, co, Konopski?{w=1}{nw}"

# OBJECTION!!!!
    $ stop_music()
    $ objection("konopski", "objection")
    $ change_pose("lexio", "wkurw")
    $ wtf_moments()
    $ defense_scene("objection")
    pause 1
    $ change_pose("konopski", "zawstydzenie")
    $ play_sound_effect("zawstydzenie", group="reactions")
    pause 2

    $ judge_scene("wkurw")
    $ play_sound_effect("wkurw", group="reactions")
    pause 2
    $ change_pose("lexio", "politowanie")
    Lexio "Co to do kurwy nędzy było?"

    $ defense_scene()
    Konopski "Eeee... ja chciałem wyrazić oburzenie i tak jakoś mi się wymsknęło..."

    $ judge_scene("wkurw")
    Lexio "Panie Konopski, takie rzeczy to się mogą panu wymsknąć na podwórku, to jest sala rozpraw, a nie jakaś obora, na litość boską!"

    $ defense_scene()
    Konopski "No to może zacznijmy od tego, żeby ten koleś w żabocie przestał być wobec mnie tak wulgarny. To jest sala rozpraw, a nie jakaś zatęchła leśna dziura, na litość boską!"

# zbliżenie na twarze revawardęgi/ lexia -> pause

    $ judge_scene()
    pause 1
    $ change_pose("lexio", "politowanie")
    Lexio "Co to jest żabot?{w=1}{nw}"

    $ defense_scene("kropla")
    $ play_sound_effect("kropla", group="reactions")
    Konopski "Kurwa serio?"

    # objection
    $ pros_scene("wkurw")
    Wardega "Panuj nad sobą, młody człowieku!"
    Wardega "Taki mały grzdylek, a tak brzydko mówi."

    $ judge_scene()
    Lexio "Karygodne."
    Lexio "Od razu widać, że recydywista."

    $ defense_scene()
    Konopski "Dobra, niech wam będzie, jestem nikczemnikiem o fagacim sercu{w=1}"

    #$judge_scene()
    #Lexio "No już spokojnie, nie bądź dla siebie taki surowy."

    #$ defense_scene()
    #Konopski "Tak czy siak, chciałbym zdementować te oszczerstwa"

    $ objection("revo", "excuseme", objection_sound=True)
    $ wtf_moments(scenes_list=[pros_scene, defense_scene, judge_scene, copros_scene])
    pause 1
    $change_pose("revo", "main")
    Revo "Państwo wybaczą, że w tak impertynencki sposób przerywam tę żarliwą debatę, ale chciałbym wtrącić swój komentarz, czy mogę?"
    
    $ judge_scene()
    #$ judge_scene("zdziwienie")
    Lexio "Pan adiutant! Prawie zupełnie o panu zapomniałem!"
    Lexio "Myślę, że{nw}"

    $ pros_scene("duma")
    Wardega "Śmiało, mój synu."

    $ defense_scene()
    $ thinking(Konopski, "...")
    pause 1
    $ change_pose("konopski", "kropla")
    $ thinking(Konopski, "Halo, centrala? Gdzie się kuźwa podziała moja opcja 'banuj'?")

    $ copros_scene()
    Revo "Dziękuję za pozytywne rozpatrzenie mojego postulatu o zabranie głosu."
    Revo "Przechodząc do rzeczy..."
    $ change_pose("revo", "kartka")
    $ play_music("revo_theme")
    Revo "Wedle mojego rozumienia treści zawartych w aktach, nie istnieje żadna korelacja pomiędzy trwającą obecnie dyskusją a przedmiotem sprawy per se."
    Revo "W związku z tym, chciałbym zasugerować odroczenie w czasie prowadzonej przez panów debaty, na rzecz skupienia się w pełni na postępowaniu procesowym."
    pause 1
    $change_pose("revo", "main")
    Revo "Oczywiście jest to tylko moja subiektywna opinia, niemająca na celu nikogo urazić. W żadnym razie proszę nie odbierać jej jako osobistego afrontu."
    
    $ pros_scene()
    $ stop_music()
    $ play_sound_effect("wkurw", group="reactions")
    pause 1
    $ change_pose("wardega", "wkurw")
    Wardega "Słyszysz Konopski? Dość już tych twoich dyrdymałów!"

    $ judge_scene()
    $ play_sound_effect("wkurw", group="reactions")
    pause 1
    $ change_pose("lexio", "wkurw")
    Lexio "Właśnie! Skończ z tym konopowaniem i pozwól z łaski swojej sfinalizować formalności!"

    $ defense_scene()
    pause 1
    $ change_pose("konopski", "thinking")
    $ thinking(Konopski, "Czy definicją słowa 'konopowanie' jest 'bycie Konopskim'?")   
    $ change_pose("konopski", "kropla")
    $ thinking(Konopski, " Bo jeśli tak, to może być to dla mnie problematyczne...")

    $ judge_scene()
    Lexio "Czy mógłbym prosić obronę o potwierdzenie gotowości do rozpoczęcia rozprawy?"

    $ defense_scene("wprost_zamkniete")
    pause 1

    $ judge_scene()
    Lexio "PANIE KONOPSKI"

    $ defense_scene("wprost_otwarte")
    Konopski "Co? Że niby ja?"
    pause 1
    $ change_pose("konopski", "main")
    Konopski "To do mnie było?"
    pause 1
    Konopski "A ja przypadkiem jeszcze przed chwilą nie byłem oskarżonym?"
    
    $ judge_scene("pretensja")
    Lexio "Czy mam przez to rozumieć, że nie chcesz być obrońcą?"

    $ defense_scene()
    Konopski "Tego nie powiedziałem..."

    $ judge_scene("pretensja")
    Lexio "To zgłaszasz tę gotowość czy nie?"

    $ defense_scene("thinking")
    Konopski "Eeee... "
    $ change_pose("konopski", "main")
    Konopski "No niech już będzie..."

    $ judge_scene()
    Lexio "Tak czy nie?"
    
    $ defense_scene()
    Konopski "Tak."

    $ judge_scene("radosc")
    Lexio "Świetnie!"
    $ change_pose("lexio", "main")
    Lexio "No i formalności już za nami!"
    
    $ pros_scene("smirk")
    Wardega "Dobra decyzja Konopski. Twój klient na pewno jest ci bardzo wdzięczny."

    $ judge_scene("radosc")
    Lexio "Otóż to! Żaden obrońca z urzędu nie chciał podjąć się tej sprawy."
    $ change_pose("lexio", "politowanie")
    Lexio "Jeden z nich, szczególnie lubujący się w beznadziejnych przypadkach, skomentował to słowami 'Jest różnica pomiędzy podjęciem wyzwania, a dobrowolnym pójściem na ścięcie'."

    $ defense_scene()
    Konopski "Brzmi... eksytująco."
    Konopski "Kim jest w takim razie mój... Och."
    $ change_pose("konopski", "kropla")
    Konopski "Ooooch. {w=1}No tak.{w=1}"
    $ thinking(Konopski, "Jak ja mogłem dać się wciągnąć w tę sztucznie podkręconą narrację...")

    $ pros_scene()
    Wardega "Mam wrażenie, że oskarżony i obrońca właśnie się ze sobą zapoznali."

    $ judge_scene()
    Lexio "Na to wygląda. Doskonale."
    Lexio "Możemy zatem wreszcie przejść do konkret{nw}"

# hold it!
    $ pros_scene()
    Wardega "Zanim zaczniemy, chciałbym jeszcze skierować kilka słów do strony broniącej. Czy mogę?"

    $ judge_scene()
    Lexio "..."
    $ change_pose("lexio", "politowanie")
    Lexio "Czy będzie to miało jakiś związek z listem carycy Katarzyny?"

    $ pros_scene("obrzydzenie")
    Wardega "Broń boże słowiański!"

    $ judge_scene()
    Lexio "W takim razie proszę mówić."
    jump mowa_wardegi

label mowa_wardegi:

    $ pros_scene()
    Wardega """
        Dziękuję wysoki sądzie. 

        Drodzy państwo, jestem w pełni świadom, iż część organizacyjna trwa już skandalicznie długo i wielu z państwa może czuć narastającą flustrację.

        Żywię jednak nadzieję, że będziecie na tyle wyrozumiali, że raczycie wybaczyć mi jeszcze jeden krótki segment wstępny.
    """
    
    $ defense_scene("wkurw")
    $ thinking(Konopski, "Ja z kolei żywię nadzieję, że zostaniesz wygwizdany.")
    $ pros_scene("politowanie")
    Wardega "Chciałbym bowiem skierować kilka słów do strony broniącej."
    $ change_pose("wardega", "rezygnacja")
    Wardega "Wiem że moja sława wyprzedza mnie, ale i tak chciałbym oficjalnie się przedstawić."

    $ defense_scene("wkurw")
    $ thinking(Konopski, "Co do... {w=1} Ja pitolę, kogoś tu już chyba do reszty posrało...")
    $ change_pose("konopski", "kropla")
    $ thinking(Konopski, "Ale już serio bez jaj, jeżeli będę musiał po raz kolejny przebrnąć przez ulubione powiedzenia Wardęgi, to się jak nic zapierdolę...")

    $ pros_scene("egzaltacja")
    $ play_music("wardega_intro")

    Wardega "Nazywam się Sylwester Sylwek Wardęga."
    Wardega "Dla jednych Zbawca, dla innych Kat, dla wszystkich Bożyszcze."

    $ defense_scene("kropla")
    $ thinking(Konopski, "Dla{w=1}czego on to mówi...")
    
    $ pros_scene("egzaltacja2")
    Wardega "Dla Watahy Samiec Alfa. {w=1}Dla Reva Ojciec. {w=1}Dla Fame MMA Wodzirej. {w=1}Dla Boxdela Obiekt Westchnień."
    $ defense_scene("kropla")
    $ thinking(Konopski, "Dla świata Wesz Społeczna.")

    $ pros_scene("serious")
    Wardega "Dla ciebie Konopski, Śmiertelne Zagrożenie"

    $ defense_scene()
    $ thinking(Konopski, "Śmiertelne zagrożenie?")

    $ pros_scene("serious")
    Wardega "Skrywające się w najmroczniejszych zakątkach lasu, Pradawne Zło."

    $ defense_scene("kropla")
    $ thinking(Konopski, "Pradawne zło...?")
    
    $ pros_scene("serious")
    Wardega "Stojący za twoimi plecami Slender Man."
label slender_lol:
    $defense_scene()
    pause 1
    $ change_pose("konopski", "beka")
    $ play_sound_effect("idea1", group="reactions")
    pause 1
    $ config.default_music_volume = 0.1
    $ thinking(Konopski, "... {w=1}kuźwa, co?")
    $ thinking(Konopski, "SLENDER MAN...?!")
    pause 1
    $ thinking(Konopski, "Ale w sensie, że...{w=1} ten wysoki, chudy koleś?{w=1} O nim mówimy?")
    $ thinking(Konopski, "O tym WYJĄTKOWO WYSOKIM i PRZERAŹLIWIE CHUDYM kolesiu?")
    pause 1
    $ thinking(Konopski, "Czyli o tego właśnie SLENDER mana nam chodzi? Tak dla jasności pytań, żeby nie było niedomówień.")
    pause 1
    $ change_pose("konopski", "thinking")
    $ thinking(Konopski, "Jakby ci to...")
    $ thinking(Konopski, "No bo wiesz, nie chcę zabrzmieć jak ten typ dzieciaka, który za punkt honoru obrał sobie zrujnowanie dziecięcych fantazji kolegom z podwórka.")
    $ thinking(Konopski, "Tak nawiasem mówiąc, mam wrażenie, graniczące z pewnością, że to ty należałeś do tego znienawidzonego grona nadgorliwców, uświadamiających naiwnej gawiedzi, że mikołaj nie isnieje.")
    $ thinking(Konopski, "Jebana sześćdziesiona.")
    $ thinking(Konopski, "Ale już mniejsza o to. Wróćmy do twoich marzeń byciu wysokim, chudym, przerażającym {w=1}SLENDER MANEM.")

label slender_story:
    $ thinking(Konopski, "Tak z czysto praktycznego punktu widzenia. Wyobraźmy sobie taki scenariusz.")
    $ thinking(Konopski, "Miejsce akcji: ciemny las.")
    $ thinking(Konopski, "Czas akcji: ciemna noc.")
    $ thinking(Konopski, "Ale nie aż tak ciemna.")
    $ thinking(Konopski, "Mówiąc krótko jest ciemno jak w dupie u murzyna.")
    $ change_pose("konopski", "kropla")
    pause 1
    $ thinking(Konopski, "Kuźwa, jakie szczęście że to tylko monolog wewnętrzny, bo w przeciwnym wypadku z miejsca trafiłbym do pierdla.")
    pause 1
    $ thinking(Konopski, "Albo, co gorsza, mogliby mnie zbanować.")

    $ thinking(Konopski, "No już mniejsza z tym. Głosówek z tego nie będzie, więc git.") 
    $ thinking(Konopski, "Wracając do tematu...")
    
    $ thinking(Konopski, "Załóżmy czysto teoretycznie, że jestem pizdeczką i boję się ciemności, {w=1}{fast} Podkreślam, CZYSTO TEORETYCZNIE, tylko baby są w takich sytuacjach obsrane, mężczyźni, w sposób męski, z męskim spokojem zachowują zimną, bogatą w męskość krew.")
    pause 1
    $ thinking(Konopski, "No to idę w tej ciemnicy, idę, idę, cisza totalna, aż tu nagle{w=1}")
    $ thinking(Konopski, "TRZASK")
    $ thinking(Konopski, "Odwracam się powoli, czując męski niepokój (czyli tak w zasadzie na luzaku).")
    pause 1
    $ thinking(Konopski, "Odwracam się bardzo powoli, żeby było klimatycznie.")
    pause 1
    $ thinking(Konopski, "Odwróciłem się.")
    $ thinking(Konopski, "PRZERAŻENIE")
    $ thinking(Konopski, "STRACH")
    $ thinking(Konopski, "TERROR")
    $ thinking(Konopski, "SERCE ZAMIERA W PIERSI{w=1} twojej, bo spodziewałeś się jakiejkolwiek reakcji.")
    $ thinking(Konopski, "A ja idę dalej. Jak gdyby nigdy nic.")
    $ thinking(Konopski, "No bo tak między nami mówiąc: nawet cię nie zauważyłem{w=1} ty jebany kurduplu.")
    pause 1
    $ thinking(Konopski, "Kurtyna.")
    pause 1
    $ thinking(Konopski, "Albo wiesz co, jak sobie teraz myślę, to chyba zbyt pochopnie oceniłem ten pomysł. Jest kilka osób, nadających się na twoje potencjalne ofiary.")
    $ thinking(Konopski, "Dajmy na to Mini Majk.") 
    
    #"KONOPSKI TY AROGANCKA AMEBO Z NIEDOWŁADEM MÓZGU"
    # w sumie spoko, muszę być jakąś wykoksaną amebą, chuj że z niedowładem, tak czy siak mam jakiś mózg

    $ pros_scene("wkurw")    
    $ stop_music()
    $ play_sound_effect("wkurw", group="reactions")
    Wardega "KONOPSKI TY AROGANCKI GNOJU! SŁUCHASZ TY W OGÓLE CO SIĘ DO CIEBIE MÓWI?"

    $defense_scene()
    Konopski "Eeee... no tak."
    pause 1
    $ change_pose("konopski", "high")
    Konopski "Tak słucham."

    $ pros_scene()
    pause 1
    $change_pose("wkurw")
    Wardega "Nie wciskaj mi tu kitu, ty farmazoniarzu, przecież widzę że odleciałeś myślami do jakiejś swojej konopolandii czy tam gdziekolwiek cię ponosi ten twój pusty łeb."

    $ judge_scene()
    Lexio "Do Konopiolandii!"

    $ defense_scene("kropla")
    $ thinking(Konopski, "Eeeee... wysoki sądzie? Taki luźny pomysł... możeby tak spróbować zachować jakieś pozory bezstronności, co ty na to? Dałoby radę?")
    
    $ pros_scene()
    Wardega "No i co cię tak nagle zamurowało Konopski? Rozumiesz jeszcze co się do ciebie mówi?"

    $ defense_scene()
    Konopski "No tak jakby nie zadałeś żadnego pytania, więc nie do końca wiem czego ode mnie oczekujesz? Mam też się przedstawić?"
    Konopski "Dla jednych Konopski, dla drugich Konopskyyy, dla Wardęgi{nw}"
   
    $ objection("wardega", "silence") 
    # todo
    # change_pose("konopski", "strach")
    # pause 1
    $ play_sound_effect("wkurw", group="reactions")
    $ pros_scene("objection")
    pause 1
    $ play_music("wardega_wkurw")
    pause 1
    $ change_pose("wardega", "wkurw")
    Wardega "Myślisz, że możesz sobie tak kpić ze mnie w żywe oczy? Taki jesteś dowcipny, ty niewychowana łazęgo? Taki z ciebie ironiczny mądrala? Taki obraz siebie ci się uroił w tym pustym łbie?"
    Wardega "To ja ci teraz powiem kim jesteś. Jesteś paskudnym, parszywym, aroganckim, skretyniałym, zdeprawowanym i szpetnym wybrykiem natury, który nie ma żadnego szacunku do autorytetów."

    $ defense_scene()#"pogarda")
    pause 1

    $ pros_scene()
    pause 1

    $ defense_scene()
    pause 1

    $ pros_scene()
    Wardega "Może jakiś komentarz? Przemyślenia?"
    
    $ defense_scene()
    Konopski "Nie, dziękuję, nie mam nic do dodania."

    $ objection("revo", "excuseme", objection_sound=True)
    $ copros_scene()
    Revo "Papo, z całym szacunkiem, uważam że pod wpływem emocji, zachowałeś się w sposób nieodpowiedni, przekraczając granice dobrego smaku."
    Revo "Oczywiście jest to tylko moja opinia, nie traktuj tego jako afront w swoją stronę."
 
    $ judge_scene()
    Lexio "Właśnie Wardęga, przegiąłeś pałę!"

    $ defense_scene("thinking")
    $ thinking(Konopski, "Muszę przyznać, że to dość... niespodziewany rozwój wydarzeń.")
    
    $ pros_scene()
    Wardega "No dajcie spokój panowie. DYSTANSIK."
    Wardega "Nie róbcie problemów tam gdzie ich nie ma, przecież tylko się tak droczymy."
    Wardega "On wie, że to tylko takie żarciki i nie ma mi tego za złe."
    Wardega "Co nie, Konopski? Sztama?"

    $ defense_scene()#"pogarda")
    Konopski "..."
    #rzut na chamskie mordy konopskiego, lexia revo
    $ pros_scene()
    Wardega "Widzicie? Uśmiechnął się lekko."

    $ judge_scene()
    Lexio "Przeproś."
label aa:
    $ pros_scene()
    Wardega "..."
    Wardega "Leksiu, jeśli mógłbym coś zasugerować... Nie gryzie się ręki, która cię karmi..."
    $ zoom_moment(WardegaClass, zoom=2.5, pos=(-0.4, -0.3), sound="pamietaj_o_tym_ze", time=2.3, talking=True)
    $ zoom_moment(LexioClass, zoom=3.5, pos=(-0.04, -0.1), time=3., talking=True)
    $ pros_scene()
    Wardega "A teraz bądź tak dobry i zastanów się kto jest twoim sojusznikiem."

    $ judge_scene()
    Lexio "Ok, to dajcie mi chwilę."

    $ defense_scene("kropla")
    $ thinking(Konopski, "To ja może spuszczę zasłonę milczenia na wątek zawiązywanych sojuszy i tylko rzucę taką refleksję, że ta ręka karmiąca Leksiia powinna trochę dać na wstrzymanie...")
    
    $ judge_scene()
    Lexio "Dobra, już."
    Lexio "Konopski, przeproś."
    $ objection("konopski", "objection")
    
    $defense_scene()
    Konopski "No teraz to cię chyba totalnie posrało, nie ma nawet takiej{nw}"

    $ judge_scene()
    Lexio "Ej, ej, ej. {w=1} Ej."
    Lexio "Konopski. {w=1} Ej."
    Lexio "Weź ty chłopcze przybastuj, bo wiesz, jak to mówią, nie gryzie się ręki która trzyma młotek."
    Lexio "Sędziowski młotek. Znaczy się, normalny pewnie też, ale mi chodziło o sędziowski. Bo jestem sędzią. Zrozumiałeś?"

    $ defense_scene()
    Konopski "Taaaak. Myślę że tak."
    $ thinking(Konopski, "Chyba że pytanie dotyczyło twojego bycia sędzią. Tego za chuj nie rozumiem.")

    $ judge_scene()
    Lexio "Zuch chłopak."
    Lexio "A teraz i się zastanów, co ci wolno, a czego nie, w razie gdybyś chciał zachować swoją wolność."
    Lexio "Prokuratorze! Psssst! Prokuratorze Wardęga! Dobrze mu powiedziałem?"

    $ pros_scene()
    Wardega "Wiadomo, Leksiu. Brzmiałeś jak zawodowy sędzia."

    $ judge_scene()
    Lexio "Hi hi :)"
    
    $ defense_scene()
    $ thinking(Konopski, "Dobrze powiedziane. BRZMIAŁ jak zawodowy sędzia.")

    $ pros_scene()
    Wardega "Dobra Konopski. Jako ten dojrzalszy i mądrzejszy pierwszy wyciągam dłoń i proponuję rozejm."

    $ defense_scene()
    Konopski "Sądzę, że nie{nw}"

    $ pros_scene()
    Wardega "Nikt cię nie pytał o zdanie."
    Wardega "W każdym razie, wydaje mi się, że wiem, gdzie leży źródło problemu, mianowicie dlaczego wykazujesz tak skandaliczny brak szacunku do mojej skromnej osoby."

    $ defense_scene()
    $ thinking(Konopski, "Czyżby...?")

    $ pros_scene()
    Wardega "Wynika to ze strachu. Jesteś przerażony wszelką interakcją ze mną, bo widzisz we mnie bardziej potwora, niż jednostkę ludzką."

    $ defense_scene()
    $ thinking(Konopski, "Taaaaa... Już to ustaliliśmy.{w=1} Slender mana.")

    $ pros_scene()
    Wardega "No i tak sobie pomyślałem, że może zmieniłbyś trochę perspektywę, gdybyś wiedział o mnie nieco więcej. Zdecydowałem więc, że opowiem ci historię swojego życia." 

    $ defense_scene()
    Konopski "Naprawdę nie ma takiej potrzeby..."

    $ pros_scene("egzaltacja")
    Wardega "Wychowały mnie wilki..."
    jump wardega_intro
