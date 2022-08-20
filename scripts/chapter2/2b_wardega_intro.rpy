label wardega_intro:
    scene wardega_intro
    $ persistent.nvl = "wardega"
    nvl clear
    #$ config.nvl_list_length = 2
    nvl_wardega """
    W księżycową ciemną noc, starą wilczycę ze snu wyrwało nieśmiałe kwilenie dzięcięcia.
    Nastawiła czujnie uszu i sierść srebrzystą zjeżyła, w obawie że zbliża się szubrawiec, który stadu zagrozić może.

    Szybko jednak strach naturę zmienił i miast o pobratymców swych, wilczyca trwożyć się zaczęła o nieznaną istotkę, której płacz na myśl przywodził skamlenie zagubionego wilczątka.

    Warto nadmienić, że ów poczciwa wadera niejedną latorośl na czułej piersi swej wychowała i matczyna miłość wypełniła ją do tego stopnia, że jakakolwiek krzywda wyrządzona najmłodszym, ból jej zadawała nie mniejszy, niżby broń okrutnych kłusowników uczynić to mogła.

"""
label konopski_wardega_intro1:
    $ defense_scene("kropla")
    $ thinking(Konopski, "Co do...")
    menu:
        "słuchaj dalej":
            jump wardega_intro2
        "OBJECTION!":
            jump wardega_intro_objection
        "odpłyń myślami":
            jump wardega_intro_skip

label wardega_intro2:
    scene wardega_intro
    $ persistent.nvl = "wardega"
    nvl clear
    wardega_nvl """

    Troskliwa matrona szybko odkryła, że dźwięk wydobywa się z wiklinowego koszyka, pozostawionego nad brzegiem pobliskiego ruczaju, tuż obok upiornie wyglądającego, spróchniałego dębu.

    Gdy podeszła bliżej, oczom jej ukazało się drżące z zimna ludzkie szczenię, okryte niedbale brudną, poszarpaną szmatką, tak cienką, że równie dobrze mogłoby wcale jej nie być.

    Tragiczny los małego nieszczęśnika wstrząsnął wilczycą na tyle, że aż uroniła pojedynczą łzę, która spłynąwszy po jej pysku, skapnęła wprost na twarzyczkę małego cierpiętnika.

    Chłopiec momentalnie podniósł w górę wzrok, a w niej serce zamarło, z obawy że jej widok do końca straumatyzuje biedną dziecinę, ale ku jej zdziwieniu, oczy malca, choć przekrwione zupełnie od łez, nie nosiły w sobie znamion strachu.

    A były to oczy elokwentne i ciekawskie, odrobinę zadziorne, ale jednocześnie zrezygnowane i umęczone, zupełnie jak gdyby należały do okrutnie doświadczonego przez los mędrca.

    Nagle stało się coś tak niespodziewanego, że aż po dziś dzień stara wilczyca nie jest pewna, czy aby nie były to tylko jej urojenia: mianowicie chłopiec, zachrypniętym, ledwo słyszalnym głosem, wyszeptał:

    \"Sylwester Wardęga\"
    """
label konopski_wardega_intro2:
    $ defense_scene("kropla")
    $ thinking(Konopski, "Może dajcie mi już po prostu dożywocie i skończcie te tortury...")
    menu:
        "Ledwo słyszalnym głosem wyszeptaj:{size=-10}'objection'{/size}":
            jump wardega_intro2
        "W opór słyszalnym głosem krzyknij: {size=+10} 'OBJECTION {/size}":
            jump wardega_intro_objection
        "Słuchaj dalej":
            jump wardega_intro3
        "Odpłyń myślami":
            jump wardega_intro_skip
# menu: słuchaj dalje/ odpłyń myślami
    #$ defense_scene()
    # lexio chra[anoe

label wardega_intro_objection:
    $ objection(Konopski, "objection")
    $ defense_scene()
    Konopski "To była naprawdę... {w=1} FASCYNUJĄCA historia i bez wątpienia wszyscy jesteśmy ciekawi co dalej, ale co ty na to, żeby przejść już do procesu, a potem już każdy, w domowym zaciszu, obejrzy sobie 'Księgę Dżungli'?"


label wardega_intro3:
    scene wardega_intro
    nvl clear
    wardega_nvl """
    Rezolutny chłopiec momentalnie oczarował wilcze stado. Hart ducha i niezwykła błyskotliwość malca były imponująca była do tego stopnia, iż nie bacząc na głęboko zakorzenioną odrazę do gatunku ludzkiego, zaczęli traktować go jak pełnoprawnego członka społeczności.

    Przybysz rósł jak na drożdzach i zanim się obejrzeli, ta, bądź co bądź, cudacznie wyglądająca istota, przeobraziła się przystojnego młodzieńca, o ciele tak muskularnym i nieskazitelnie pięknym, że wydawać by się mogło, że to wyrzeźbiony z marmuru grecki heros, a nie wychowany w spartańkich, leśnych warunkach śmiertelnik.

    Mijały lata, a idylliczne, wolne od trosk życie wilczej familii upływało na kontemplacji natury z domieszką leśnych figli.

    Zapewne taki stan rzeczy twałby się aż po dziś dzień, gdyby nie pewna kobieta, która z zawziętością podchodząco już pod gorliwość, szukała jak najbardziej ustronnego zakątka, który mógłby jej posłużyć za punkt treningowy.

    Nie był to bynajmniej kaprys z gatunku 'odklejenie rozwydrzonej influencerki z niedowładem umysłowym, którego źródłem jest przesadnie wyuzdane kręcenie dupskiem na onlyfansie'.
"""
    $ pros_scene()
    Wardega "Ach te parszywe, zakłamane lafiryndy, żerujące na nieświadomych zagrożeń facetach, którzy chcą sobie po prostu zwalić konia."
    # rzut na konopa/revo/ całą salę, wszyscy mają krople

    Wardega "Ekhem!"
    Wardega "Jak już mówiłem..."
    Wardega "..."
    Wardega "Jak już mówiłem... eeee..."

    $defense_scene()
    Konopski "Mówiłeś że to już koniec tej historii."

    $ pros_scene()
    Wardega "..."
    Wardega "Dobra, mam."
    Wardega "Jak już mówiłem w przeciwieństwie do tych wytapetowanych lachociągów, Monika dbało o zdrowie innych ludzi, bała się bowiem że jakiś przypadkowy przechodzień, ujrzawszy nieprawidłowo odchylony odcinek mostka w czasie wykonywania{nw}"
    #scene wardega_intro
    #Odkąd wspomniane już przelotnie, spróchniałe drzewo, przegrało nierówną walkę z czasem i ugiąwszy się pod własnym ciężarem zagrodziło niemal całkowicie wejście do wilczej kryjówki, członkowie zupełnie wyzbyli się strachu przed wizytą nieproszonych gości.
    # dźwięk parsknięcia
    pause 1    # dźwięk parsknięcia 

    Wardega "Ale ja byłem tym samym co zawsze, skromnym prostym, chłopakiem, stroniącym od przepychu do tego stopnia, że dostawszy zaproszenie na herbatkę do pałacu Buckingham odmówiłem.."
    menu:
        "wysłuchaj tej historii":
            jump wardega_krolowa
        "śpij dalej":
            jump wardega_intro_skip2
    
label wardega_intro_prankster:
    $ pros_scene()
    Wardega """
        Moja droga na szczyt była wyboista i pełna ślepych zaułków.

        Podli hejterzy nie szczędzili słów.

        PRANKSTER GANGSTER

        WŁOCHATY PRADZIADEK DUBIELA

        ZADZIORNY TARZAN
    
        Bywało nawet, że jakieś złośliwe indywidua nazywały mnie 'męskim odpowiednikiem Marty Linkiewicz'.
    
        Ma to w sobie zaskakująco dużo prawdy, różni nas jedynie fakt, że ja zamiast kręcenia dupą, kręciłem pranki.
    """
    
    $ defense_scene()
    $ thinking(Konopski, "No ja bym jeszcze dodał, że Marta Linkiewicz potrafi komuś spuścić wpierdol na fame mma.")
    $ thinking(Konopski, "A poza tym faktycznie, jak dwie krople wody...")

    # menu z uciekającym kursorem
    pause 1

label wardega_krolowa:
    $ pros_scene()
    Wardega """
        Tak, może i byłem rozpoznawalnym na całym świecie twórcą bestsellerowych filmików, które dzięki swym walorom humorystycznym były w stanie rozbawić nawet największego ponuraka. Może i wzbogaciłem się na tyle, że gdybym tylko chciał, kupiłbym puszczę kampinowską i wymienił łosie na wilki. Cóż jednak z tego, skoro w głębi serca, nadal byłem Sylwkiem. Tylko Sylwkiem.

        Tym samym co zawsze, skromnym prostym, chłopakiem, stroniącym od przepychu do tego stopnia, że dostawszy zaproszenie na herbatkę do pałacu Buckingham odmówiłem, nie chcąc jednak wyjść na bufona, zaproponowałem królowej spotkanie w mojej leśnechatce.

        Nie traktowałem oczywiście własnych słów na poważnie. Taki przeciętniak jak ja, goszczący pod swe strzechą królową? Przecież to niedorzeczność.

        Cóż to było za zaskoczenie, gdy następnego dnia odebrałem telefon od nieznanego numeru i wywiązała się rozmowa, która przebiegała mniej więcej tak:

        Halo? Sylwek? Sylwek Wardęga? Ten pocieszny prankster? Nawet nie masz pojęcia, jak bardzo ubawiły mnie twoje filmiki, ten pies pająk, wybitne dzieło, aż sama się zainspirowałam i hahaha no musisz to zobaczyć, te moje corgi wyglądają w pajęczych strojach FE NO ME NALNIE, jeszcze jak przebierają tymi swoimi krótkimi nóżkami, no boki zrywać.

        Na początku byłem sceptyczny, no bo wiecie, złote lata pranksterstwa, Dubiel na horyzoncie, syntezatory mowy... eee jakościowo jeden na dziesięć, ale funkcjonują, no i ta idealna polszczyzna, trochę podejrzane.

        No więc pytam nieśmiało 'Yyyy... Z kim mam przyjemność', po drugiej stronie śmiech, a po chwili 'Ech Sylwek, ty to jesteś numerant, ale do rzeczy, kiedy mógłbyś wygospodarować dla mnie trochę wolnego czasu'

        I koniec końców nie dowiedziałem się, czy kolejny wieczór spędzę z Dubielem czy królową Anglii, ale może tym lepiej, dreszczyk niepewności dodawał pikanterii tej całej przedziwnej sytuacji.

        Położyłem na stół ceratę, kupiłem maczugi keczupowe i wyjąłem z szafy swój najdostojnieszy druidzi płaszcz. Po chwili jednak schowałem go z powrotem, to nie miało być przecież oficjalne przyjęcie, tylko niezobowiązująca randka w ciemno. 

        Samego spotkania nie chce mi się już streszczać. Moim gościem okazała się być królowa, nawet spoko, ale jednak trochę nudno, najbardziej w pamięci utkwił mi moment, kiedy pijąc Sagę malinową ze szklanki coca-coli odchyliła mały palec, no bez jaj, myślałem że ją przez przypadek upuści, a to była świąteczna kolekcja limitowana, wiecie, taka z tymi białymi niedźwiedziami.

        No ale nieważne. Taka tam randomowa historyjka z życia. 
    """
    $ defense_scene()
    $ thinking(Konopski, "Co tu się odjebało...")

label wardega_intro_skip:
    scene black with dissolve
    pause 1
    $ play_video("blabla")
    Wardega "KONOPSKI"

label wardega_intro_bulwers:
    $ pros_scene("wkurw")
    Wardega "Nic nie dotarło do tego twojego pustego łba, co?"
    $ defense_scene()
    Konopski "Nieprawda, słuchałem pzez cały{nw}"
    $ pros_scene()
    Wardega "To nie było pytanie, ty niedorozwinięty troglodyto."
    $ defense_scene()
    Konopski "Eeee... niedorozwinięty troglodyto?"
    Konopski "Tak dla jasności, czy to forma droczenia się w ramach naszej, tak zwanej, 'sztamy', czy już{nw}" 
    $ pros_scene()
    Wardega "Jak nazywała się moja wilcza matrona?"

label pytanie_wilczyca:
    $ defense_scene()
    menu:
        "Czcigodna Pani Matka":
            jump zla_odpowiedz
        "Bagira":
            jump zla_odpowiedz
        "Rajstopowa Lexi":
            jump zla_odpowiedz
        "Aniela Bogusz":
            jump zla_odpowiedz

label zla_odpowiedz:
    $pros_scene()
    Wardega "Zła odpowiedź!"
    pause 0.5
    Wardega "Nigdy nie podałem jej imienia."
    $defense_scene()
    Konopski "No błagam, to było podchwytliwe, każdy by się na to złapał..."
    $pros_scene()
    Wardega "Czyżby? No to może sprawdziwym, co ty na to?"
    Wardega "Lexiu!"
    $ judge_scene("sleeping")
    pause 0.5
    $change_pose("lexio", "wkurw")
    Lexio "WINNY!"
    pause 0.5
    $ change_pose("lexio", "main")
    Lexio "Jakie było pytanie?"
    $ pros_scene()
    Wardega "Jak nazywała się moja wilcza matrona?"

    $ defense_scene()
    $ thinking(Konopski, "Każdy na MOIM MIEJSCU. ZANIM padła odpowiedź. Teraz to raczej oczywiste że wszyscy to wiedzą...")
    $ change_pose("konopski", "thinking")
    $ thinking(Konopski, "?")

    $ judge_scene()
    Lexio "Yyyyyyyy"

    $ defense_scene()
    pause 0.5
    $ change_pose("konopski", "smirk")
    $ thinking(Konopski, "No i co, ty sprytny kapuściany łbie?")
    $ thinking(Konopski, "Jak to jest tak samego siebie zaorać? Przyznasz w końcu, że{nw}")
    
    Wardega "No dokładnie tak Lexiu!"
    pause 0.5
    $ change_pose("konopski", "kropla")
    $ thinking(Konopski, "Chwila, co?")
    
    $ pros_scene()
    Wardega "Tak jak już mówiłem, nie ma odpowiedzi na to pytanie, więc milczenie jest jak najbardziej prawidłową odpowiedzią."

    $ objection("konopski", "objection")
    Konopski "No już bez jaj, cały czas pierdolisz od rzeczy, ale teraz to serio przeszedłeś sam siebie! Przestań w końcu rżnąć{nw}"
    
    $ objection("wardega", "silence")

label wardega_intro_koniec:
    

    $ pros_scene()
    Wardega """
    Nie na darmo jednak przyszło mi się zmierzyć z tyloma przeciwnościami losu.

    Cytując słowa Lil Masti:

    KREW POT I ŁZY MÓJ ZBUDOWAŁY TRON

    Niektórzy być może zastanawiają się, czemu w ogóle o tym wszystkim mówię?
"""

    $ defense_scene()
    $ thinking(Konopski, "Cytując słowa Gimpera...")
    $ thinking(Konopski, "BO JESTEŚ GŁUPI W CHUJ")

    $ pros_scene()
    Wardega "Bez wątpienia są to osobniki wydarte z człowieczeństwa, bez choćby cienia wrażliwości, a ich dusze łudząco przypominają mózg Moniki Kociołek."

    $ judge_scene()
    Lexio "Grubo!"

    $ defense_scene()
    $ thinking(Konopski, "Mocne słowa jak na taką bambaryłę...")
    $ thinking(Konopski, "Eeee... Nie powiedziałem tego na głos, prawda?")
    #$ thinking(Konopski, "Jeśli to się zaraz nie skończy, to chyba sam będę musiał po tym wszystkim poddać się lobotomii.")
    #$ thinking(Konopski, "Hmmm... No może jeszcze pod warunkiem, że wbijecie sto tysięcy łapek w górę...")

    $ pros_scene()
    Wardega "Takie pytanie byłoby przecież zupełnie nielogiczne: nie jestem w stanie wyyobrazić sobie sytuacji, nianadającej się na opowiedzenie tej historii."

    $ defense_scene()
    $ thinking(Konopski, "No to powinszować wyobraźni... Na poczekaniu mógłbym wymienić całe multum...")
    $ thinking(Konopski, "No to zaczynamy: proces sądowy...")

    $ pros_scene()
    Wardega "Oprócz niezaprzeczalnych walorów fabularnych"
    Wardega "Jak widzicie drodzy państwo, strona broniąca zrobiła mi tę uprzejmość i sama się wyjaśniła."
    Wardega "To grubiańskie zachowanie "
    

    # dźwięk zagrożenia
    Wardega "Masz jakiś problem, ty wyzbyty ogłady chłoptasiu?"
    $ defense_scene()
    Konopski "Tak się, składa, że więcej ni{nw}"

    $ pros_scene()
    Wardega "To było pytanie retoryczne, ty egocentryczny błaźnie."
    Wardega "Na pierwszy rzut oka widać, że nie masz absolutnie żadnego."

    $ defense_scene()
    Konopski "..."
    
    $ pros_scene()
    Wardega "..."

    $ defense_scene()
    $ thinking(Konopski, "Nie ma mowy, nie wciągniesz mnie w tej swoje gierki. Nie dam ci tej satysfakcji.")
    Konopski "Dobra, no to skoro przejrzałeś mnie już na wylot, to czy możemy wreszcie przejść do główne{nw}"

    $ pros_scene()
    Wardega "Na pewno intryguje cię, jak wyglądał mój proces dedukcji."

    $ defense_scene()
    Konopski "Szczerze mówiąc, mam to kompletnie w d{nw}"

    $ pros_scene()
    Wardega "Nie bedę cię dłużej trzymał w niepewności, aż szkoda patrzeć, jak ciekawość skręca cię od środka."

    $ defense_scene()
    $ thinking(Konopski, "Poprawka, to CIEBIE skręca od środka, potrzeba podzielenia się ze światem swoimi 'genialnymi' przemyśleniami.")
    
    $ pros_scene()
    Wardega "Słuchaj uważnie: całą prawdę o sobie masz jak wół wypisaną tym swoim bezczelnym, wiecznie zadowolonym z siebie ryju."

    $ defense_scene()
    $ thinking(Konopski, "...")

    $ pros_scene()
    Wardega "..."

    $ defense_scene()
    Konopski "Eeee... chwila... to już wszystko?"
    Konopski "To jest ta dogłębna psychoanaliza, którą tak bardzo chciałeś się podzielić ze światem?"

    $ pros_scene()
    Wardega "A czego się spodziewałeś?"
    Wardega "Na lekcjach biologii też byłeś wielce zaskoczony, że całą wiedzę na temat życia ameb, można zawrzeć w dwóch zdaniach?"

    $ defense_scene()
    Konopski "To nawet nie były dwa..."

    # załamanie
    $ thinking(Konopski, """
To... to nie ma sensu...
Nawet jeszcze nie zaczęła się rozprawa, a ja już czuję się tak zgnojony, że nie mam nawet siły myśleć, co będzie dalej...
To już nawet nie jest 'nierówna walka'. W nierównej walce miałbym mimo wszystko jakieś pole do manewru.
Tutaj jestem na z góry przegranej pozycji, bez żadnej możliwości obrony.
'Tortury psychiczne'. To jest najbardziej adekwatna nazwa tego, co tutaj się wyprawia.
Ciągnięcie tego dalej to masochizm...
No trudno. Czas się...
""")
# hold it! <takie rzuty na mordy srexia/wardęgi/konopskiegp
    
    $ copros_scene()
    Revo "W obliczu tego, do jakiego stopnia niezgodny z wytycznymi stał się przebieg tego procesu, zmuszony jestem wyjść z roli biernego obserwatora i skomentować zaistniałą sytuację."
    Revo "Papo, z całym szacunkiem, ale w moim odczuciu, myślenie emocjonalne wzięło nad tobą górę, w konsekwencji czego proces nabrał charakter tendencyjny, a kontynuowanie go w takiej formie byłoby nie tylko karygodnym naruszeniem praw obywatelskich, ale również ciosem zadanym idei sprawiedliwości per se."

    $ defense_scene()
    $ thinking(Konopski, "No świetnie, Revo, i to w wersji bano-odpornej.")
    $ thinking(Konopski, "Ja pitolę, serio musiał wybrać właśnie ten moment, żeby wypucować Wardędze...{w=1} Chwila, co?")
    $ thinking(Konopski, "Czy on właśnie powiedział to, co myślę, że powiedział?")
    $ thinking(Konopski, "O w dupę, przecież to musi być{nw}")

# rzut na zszokowanego wardęg
    $ judge_scene()
    Lexio "WOJNA DOMOWA!"

    $ defense_scene()
    $ thinking(Konopski, "Ja bym to raczej nazwał...")
    $ thinking(Konopski, "REVOlucją!")
    pause 1
    $ thinking(Konopski, "Kuźwa, jaka szkoda że to monolog wewnętrzny, tak dobry pun zmarnotrawiony...")

    $ copros_scene()
    Revo "Papo, wszystko w porządku?"

    $ pros_scene()
# nadal zszokowany wardęga
    Wardega "Gdyby ktoś inny wypowiedział te niesprawiedliwie krytyczne słowa, poczułbym się głęboko urażony."
    Wardega "Ale aż serce mi mięknie na widok twojego nieskażonego subiektywizmem lica i z pokorą wezmę sobie twoje uwagi do serca."

    $ copros_scene()
    Revo "Zawstydzasz mnie papo..."

# cała sala ooooo

    $ judge_scene()
    Lexio "Co? Już koniec?"
    Lexio "Tak szybko?"
    Lexio "A tak obiecująco się zapowia{nw}"

# całą sala świerszcze

    Lexio "Ekhem... znaczy się..."
    Lexio "Aż się zakrztusiłem ze wzruszenia."
    Lexio "No ale nieważne, grunt że konflikt międzypokoleniowy został zażegnany."
    Lexio "Mam rację?"

    "TAK"
    Lexio "Nie słyszę!"
    "TAK!"

    Lexio "Team X"
    "TO RODZINA"

    Lexio "Team X"
    "TO RODZINA"

    Lexio "WSZYSTKO DLA RODZINY"
    "W ŻYCIU TRZEBA DOBRZE ZJEŚĆ"
    #cała sala ooooooooo

    $ defense_scene()
    $ thinking(Konopski, "Czy ktoś mógłby mi z łaski swojej przypomnieć, co tu się właściwie dzieje?")

    $ judge_scene()
    Lexio "No i to jest publika która wie jak się bawić! Dziękuję wam kochani! Będę tu cały wieczór!"

    $ defense_scene()
    $ thinking(Konopski, "Podbijam pytanie...")

    $judge_scene()
    Lexio "Ach te wątki rodzinne... Nigdy nie potrafię opanować łez..."
    Lexio "Hufff, pufff... Aż się zmachałem.Ach te wątki rodzinne... Nigdy nie potrafię opanować łez..."
    Lexio "Czy ktoś z łaski swojej mógłby mi podać chusteczkę?"
        
    # rzut na salę i świerszcze

    $ pros_scene()
    Wardega "Konopski, na uszy ci się rzuciło od tej głupoty? Wysoki sąd prosi o chusteczkę."

    $ defense_scene()
    Konopski "Bardzo mi przykro, ale niestety nie mam chusteczki."

    $ pros_scene()
    Wardega "No tak, mój błąd."
    Wardega "Tobie pewnie w takich sytuacjach wystarczy."

    $ defense_scene()
    $ thinking(Konopski, "Może rękaw nie, ale twój żabot z pewnością dałby radę.")
    Wardega "Gdybyś spędził większość swojego życia w dżungli, wśród krwiożerczych drapieżników, mogących w każdej chwili rozszarpać cię na strzępy, bez okrycia wierzchniego, dostępu do czystej wody i akceptowalnej przez sanepid toalety, to dopiero zrozumiałbyś, czym są prawdziwe problemy."
    $judge_scene()
    Lexio "HA"


    $ defense_scene()
    Konopski "..."
    Konopski "Eeeee... Czekaj, bo chyba się pogubiłem..."
    Konopski "Popraw mnie, jeśli się mylę, ale{nw}"
    
    $ pros_scene()
    Wardega "Na pewno się mylisz."

    $ defense_scene()
    Konopski "..."
    
    $ pros_scene()
    Wardega "..."
    Wardega "Mógłbyś powtórzyć pytanie?"
    
    $ defense_scene()
    #"chcesz przez to powiedzieć, że miałeś jeszcze jeden epizod życia w lesie?"
    Konopski "\"Idyllicznego, wolnego od trosk życia, jakie wiodłeś wraz z oczarowaną twoją błyskotliwością, wilczą familią\"?"

    $ pros_scene()
    Wardega "..."
    Wardega "Konopski, ty niedorozwinięty troglodyto, czy nikt ci jeszcze nie uświadomił, że wielcy prorocy posługują się językiem metaforycznym?"
    Wardega "Czego was oni kurwa uczą w tych podstawówkach?"

    $ defense_scene()
    Konopski "..."
    $ thinking(Konopski, "Wielcy... prorocy?")

    $ pros_scene()
    Wardega "Założę się, że należysz do tej grupy osób, którzy traktują dosłownie fabułę starego testamentu."

    $ defense_scene()
    Konopski "A co ma piernik do{nw}"

    $ pros_scene()
    Wardega "Wiesz jak się mówi na takich ludzi jak ty?"

    $ defense_scene()
    Konopski "Oświeć mnie."

    $ pros_scene()
    Wardega "Debile."
    
    $judge_scene()
    Lexio "HA"

    #OBJECCTION
    $defense_scene()
    Konopski "Czy... eee... wysoki sąd mógłby chociać spróbować stwarzać pozory bezstronności?"
#silence
    $ pros_scene()
    Wardega "Wiesz Konopski, to niesamowite, że ciągle potrafisz mnie zadziwić."
    Wardega "Kiedy już jestem absolutnie pewien, że nie można niżej upaść, to ty, uśmiechając się jak najgorsza szumowina, zaczynasz pukać od spodu."

    $ defense_scene()
    Konopski "Eeee..."
    Konopski "Skąd możesz wiedzieć, jaki mam wyraz twarzy, skoro pukam od spodu?"

    $ pros_scene()
    Wardega "No zaraz mnie trzepnie, jak grochem o ścianę. To była metafora ty durniu."

    $ defense_scene()
    Konopski "To była ironia" # thinking: ty durniu.

    $ pros_scene()
    Wardega "Dość, tego, znowu gadamy o tobie parszywcu, podczas gdy powinniśmy zająć się Lexiem."
    Wardega "Spójrzcie na niego, tak bardzo zabolały go insynuacje jakoby w sposób nieprofesjonalny wykonywał swoją funkcję, że aż oczy skleiły mu się od łez!"

    $defense_scene()
    $thinking(Konopski, "Jakich łez? On po prostu ciągle trwa w stanie półdrzemki i walczy ze sobą, żeby całkowicie nie zasnąć, mimo że oczy same mu się zamkykają...")

    $pros_scene()
    Wardega "Jak się czujesz Lexiu? Bardzo dotknęły cię słowa tej kanalii? Potrzebujesz krótkiej przerwy?"

    $ judge_scene()
    Lexio "Eeee... no tak."
    Lexio "Co?"
    Lexio "To było do mnie?"

    $ defense_scene()
    $ thinking(Konopski, "No i co teraz kapuściany łbie? Gdzie się podziała twoja teoria rozpaczy i sklejonych od łez oczu?")
    $ thinking(Konopski, "Jakie to uczucie samego siebie zaorać?")

    $ pros_scene()
    Wardega "Szczerze mówiąc jestem w szoku."

    $ defense_scene()
    $ thinking(Konopski, "")
    $ thinking(Konopski, "Chyba zostanę przy 'Sylwester Wardęga', ty fanie 'rezolutnej dysputy'")

    $ pros_scene()
    Wardega "Zważywszy na dzisiejsze okoliczności, zdecydowałem się na formę oficjalną, ale zachowującą nutkę mistycyzmu."
    Wardega "W dniu dzisiejszym proszę zwracać się do mnie per"
    Wardega "'Panie Druidzie'."

    $ defense_scene()
    $ thinking(Konopski, "Ok, wszystko jedno, niech będzie Pan Druid, możemy już przejść dalej?")

    $ pros_scene()
    Wardega "Moje życiowe motto brzmi: każdy kij ma dwa końce."

    $ defense_scene()
    $ thinking(Konopski, "Gdzieś to już słyszałem...")

    $ pros_scene()
    Wardega "Ale to ja wiem za który z nich należy chwicić."

    $ defense_scene()
    Konopski "A to akurat nowość"

    $ pros_scene()
    Wardega "Więc czas żebym chwycił batutę i rozpoczął koncert sprawiedliwości."

    $ defense_scene()
    $ thinking(Konopski, "...")
    pause 1
    # thinking
    Konopski "Sam to wymyśliłeś?"

    $ pros_scene()
    Wardega "Nie zamierzam odpowiadać na pytania zadane tak bezczelnie spoufalającym się tonem."

    $ defense_scene()
    Konopski "Czy sam to pan wymyślił... Panie Druidzie?"

    $ pros_scene()
    Wardega "Pamiętałeś o capsie?"

    $ defense_scene()
    Konopski "Jakże bym śmiał zapomnieć."

    $ pros_scene()
    Wardega "Doskonale."
    pause 1.0
    # main
    Wardega "Mógłbyś powtórzyć pytanie?"

    $ defense_scene()
    Konopski "Czy pańskie motto Panie Druidzie zostało wymyślone w całości przez pana?"

    $ pros_scene()
    Wardega "Nie."
    Wardega "Ten fragment z batutą zapożyczyłam od jakiegoś kolesia z forum miłośników imagestocka."

    $ judge_scene()
    Lexio "Aaaaaa, już łapię."
    Lexio "W sensie że batuta to też kijek, tak? I ma dwa końce?"

    $ pros_scene()
    Wardega "Dokładnie tak Konopski. wiedziałem że będziesz miał problem z rozszyfrowaniem meandrów poezji."

    $ defense_scene()
    Konopski "Zdaje pan sobie sprawę, że nie ja zadałem to pytanie, prawda?"

    $ pros_scene() # irytacja?
    Wardega "..."
    Wardega "Dość już tego pajacowania Konopski, to nie czas i miejsce na czcze pogaduszki."

    $ defense_scene()
    Konopski "..."
    # zniecierpliwienie
    Konopski "Mea culpa, od teraz będę starał się powstrzymać od bezsensownych monologów..."
    jump wardega_przemowienie
