label chapter2:
    $ change_style("main")
    scene courtroom_full
    #jump sad
    #jump wardega1
    #jump wardega-przemowienie
    #jump gimper

label poczatek_sadu:
    pause 1.0
    scene gavel
    $ play_sound_effect("gavel")
    #TODO: muzyka
    pause 1.0
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
    $ defense_scene(head="sykniecie")
    Konopski "..."
    Konopski "Co to ma kuźwa być?"
    pause 1
    Konopski "Nie, no ale serio pytam. CO TO MA BYĆ?"
    Konopski "Renesans ery pranków?"
    Konopski "I w co ja jestem kuźwa ubrany?!"
    Konopski "..."
    Konopski "Kto i kiedy mnie w to ubrał?!"

    $ pros_scene()
    Wardega "A oto i nasza diwa, jak zawsze w świetnej formie!"
    Wardega "Ledwo wyszła na scenę, a już zaczęła gwiazdorzyć"

    $ defense_scene()
    $ thinking(Konopski, "Nie daj się sprowokować. Nie daj się sprowokować. Nie daj się sprowokować.")

    $ pros_scene()
    Wardega "Każdy na jej miejscu miałby w sobie chociaż tyle przyzwoitości, żeby podziękować za przyodzianie w ten gustowny garniturek."
    Wardega "Ale najwidoczniej mamy przed sobą typ osoby, która otrzymawszy od babci dziergany na drutach sweter w renifery, robi aferę, że wolałaby wilki."

    $ defense_scene()
    $ thinking(Konopski, "Eeee... to był przykład z autopsji, tak?")

    $ pros_scene()
    Wardega "No tak, jak ja mogłem wcześniej o tym nie pomyśleć! Przecież to takie oczywiste dlaczego czujesz się teraz tak niekomfortowo!"
    Wardega "To twój pierwszy raz w nieobszczanych ciuchach, co, Konopski?"

# OBJECTION!!!!

    $ judge_scene()
    Lexio "Co to do kurwy nędzy było."

    $ defense_scene()
    Konopski "Eeee... ja chciałem wyrazić oburzenie i tak jakoś mi się wymsknęło..."

    $ judge_scene()
    Lexio "Panie Konopski, takie rzeczy to się mogą panu wymsknąć na podwórku, to jest sala rozpraw, a nie jakaś obora, na litość boską!"

    $ defense_scene()
    Konopski "No to może zacznijmy od tego, żeby ten koleś w żabocie przestał być wobec mnie tak wulgarny. To jest sala rozpraw, a nie jakaś zatęchła leśna nora, na litość boską!"

# zbliżenie na twarze revawardęgi/ lexia -> pause

    $ judge_scene()
    Lexio "Co to jest żabot?"

    $ defense_scene()
    Konopski "Kurwa serio?"

    # objection
    $ pros_scene()
    Wardega "Panuj nad sobą, młody człowieku!"
    Wardega "Taki mały grzdylek, a tak brzydko mówi."

    $ judge_scene()
    Lexio "Karygodne."
    Lexio "Od razu widać, że recydywista."

    $ defense_scene()
    Konopski "..."

    # excuse me!

    $ copros_scene()
    Revo "Za pozwoleniem, chciałbym zasugerować przesunięcie prowadzonej właśnie dysputy w czasie i przejście do głównego wątku rozprawy."

    $ pros_scene()
    Wardega "Słyszysz Konopski? Dość już tych twoich dyrdymałów!"

    $ judge_scene()
    Lexio "Właśnie! Skończ z tym konopowaniem i pozwól z łaski swojej sfinalizować formalności!"

    $ defense_scene()
    $ thinking(Konopski, "Czy definicją słowa 'konopowanie' jest 'bycie Konopskim'?")
    $ thinking(Konopski, "Bo jeśli tak, to może być to dla mnie problematyczne...")

    $ judge_scene()
    Lexio "Czy mógłbym prosić obronę o potwierdzenie gotowości do rozpoczęcia rozprawy?"

    $ defense_scene()
    Konopski "..."

    $ judge_scene()
    Lexio "PANIE KONOPSKI"

    $ defense_scene()
    Konopski "Co? Że niby ja?"
    pause 1
    Konopski "To do mnie było?"
    Konopski "A ja przypadkiem jeszcze przed chwilą nie byłem oskarżonym?"
    
    $ judge_scene()
    Lexio "Czy mam przez to rozumieć, że nie chcesz być obrońcą?"

    $ defense_scene()
    Konopski "Tego nie powiedziałem..."

    $ judge_scene()
    Lexio "To zgłaszasz tę gotowość czy nie?"

    $ defense_scene()
    Konopski "Eeee... No niech już będzie..."

    $ judge_scene()
    Lexio "Tak czy nie?"
    
    $ defense_scene()
    Konopski "Tak."

    $ judge_scene()
    Lexio "Świetnie!"
    Lexio "No i formalności już za nami!"
    
    $ pros_scene()
    Wardega "Dobra decyzja Konopski. Twój klient na pewno jest ci bardzo wdzięczny."

    $ judge_scene()
    Lexio "Otóż to! Żaden obrońca z urzędu nie chciał podjąć się tej sprawy."
    Lexio "Jeden z nich, szczególnie lubujący się w beznadziejnych przypadkach, skomentował to słowami 'Jest różnica pomiędzy podjęciem wyzwania, a dobrowolnym pójściem na ścięcie'."

    $ defense_scene()
    Konopski "Brzmi... eksytująco."
    Konopski "Kim jest w takim razie mój... Och."
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
    Lexio "Czy będzie to miało jakiś związek z listem carycy Katarzyny?"

    $ pros_scene()
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
    
    $ defense_scene()
    $ thinking(Konopski, "Ja z kolei żywię nadzieję, że zostaniesz wygwizdany.")

    $ pros_scene()
    Wardega """
        Chciałbym bowiem skierować kilka słów do strony broniącej.
        Wiem że moja sława wyprzedza mnie, ale i tak chciałbym oficjalnie się przedstawić.
    """

    $ defense_scene()
    $ thinking(Konopski, "Co do... {w=1} Ja pitolę, kogoś tu już chyba do reszty posrało...")
    $ thinking(Konopski, "Ale już serio bez jaj, jeżeli będę musiał po raz kolejny przebrnąć przez ulubione powiedzenia Wardęgi, to się jak nic zapierdolę...")

    $ pros_scene()
    Wardega "Nazywam się Sylwester Sylwek Wardęga."
    Wardega "Dla jednych Zbawca, dla innych Kat, dla wszystkich Bożyszcze."

    $ defense_scene()
    $ thinking(Konopski, "Dla mnie Stetryczały Goguś.")
    
    $ pros_scene()
    Wardega "Dla Watahy Samiec Alfa. {w=1}Dla Reva Ojciec. {w=1}Dla Fame MMA Wodzirej. {w=1}Dla Boxdela Obiekt Westchnień."
    
    $ defense_scene()
    $ thinking(Konopski, "Dla{w=1}czego on to mówi...")

    $ pros_scene()
    Wardega "Dla ciebie Konopski, Śmiertelne Zagrożenie, kryjące się w lesie Pradawne Zło, stojący za twoimi plecami Slender Man."

    $ defense_scene()
    $ thinking(Konopski, "...{w=1} kuźwa, prawie się zakrztusiłem... Slender man? Czy on nazwał siebie Slender manem?")
    $ thinking(Konopski, "Slender manem. Wardęga. LOL.")
    $ thinking(Konopski, "O nie, błagam, nie wytrzymam, lolololol, zaraz parsknę na całą salę, spokojnie, tylko spokojnie, wdech wydech.")
    $ thinking(Konopski, "Dobra, jest ok. Już jestem spokojny.")
    $ thinking(Konopski, "...")
    $ thinking(Konopski, "Chwila. Zastanówmy się.")
    $ thinking(Konopski, "Załóżmy, że mamy uniwersum, w którym Wardęga jest Slender manem.")
    $ thinking(Konopski, "Czy w takim razie tamtejszy Mini Majk to Micheal Jordan?")
    $ thinking(Konopski, "...")
    $ thinking(Konopski, "Dlaczego ja o tym pomyślałem, już do końca życia będzie prześladowała mnie wizja tych potwornych mutantów...")

    #"KONOPSKI TY AROGANCKA AMEBO Z NIEDOWŁADEM MÓZGU"
    # w sumie spoko, muszę być jakąś wykoksaną amebą, chuj że z niedowładem, tak czy siak mam jakiś mózg

    "KONOPSKI TY AROGANCKI GNOJU! SŁUCHASZ TY W OGÓLE CO SIĘ DO CIEBIE MÓWI?"

    Konopski "Eeee... no tak. Tak słucham."

    $ pros_scene()
    Wardega "Nie wciskaj mi tu kitu, ty farmazoniarzu, przecież widzę że odleciałeś myślami do jakiejś swojej konopolandii czy tam gdziekolwiek cię ponosi ten twój pusty łeb."

    $ judge_scene()
    Lexio "Do Konopiolandii!"

    $ defense_scene()
    $ thinking(Konopski, "Eeeee... wysoki sądzie? Taki luźny pomysł... możeby tak spróbować zachować jakieś pozory bezstronności, co ty na to? Dałoby radę?")
    
    $ pros_scene()
    Wardega "No i co cię tak nagle zamurowało Konopski? Rozumiesz jeszcze co się do ciebie mówi?"

    $ defense_scene()
    Konopski "No tak jakby nie zadałeś żadnego pytania, więc nie do końca wiem czego ode mnie oczekujesz? Mam też się przedstawić?"
    Konopski "Dla jednych Konopski, dla drugich Konopskyyy, dla Wardęgi{nw}"
    
    $ pros_scene()
    Wardega "Zamilcz!"
    Wardega "Myślisz, że możesz sobie tak kpić ze mnie w żywe oczy? Taki jesteś dowcipny, ty niewychowana łazęgo? Taki z ciebie ironiczny mądrala? Taki obraz siebie ci się uroił w tym pustym łbie?"
    Wardega "To ja ci teraz powiem kim jesteś. Jesteś paskudnym, parszywym, aroganckim, skretyniałym, zdeprawowanym i szpetnym wybrykiem natury, który nie ma żadnego szacunku do autorytetów."

    $ defense_scene()
    Konopski "..."

    $ pros_scene()
    Wardega "..."

    $ defense_scene()
    Konopski "..."

    $ pros_scene()
    Wardega "Może jakiś komentarz? Przemyślenia?"
    
    $ defense_scene()
    Konopski "Nie, dziękuję, nie mam nic do dodania."

    $ copros_scene()
    Revo "Papo, z cąłym szacunkiem, uważam że pod wpływem emocji, zachowałeś się w sposób nieodpowiedni, przekraczając granice dobrego smaku."
    Revo "Oczywiście jest to tylko moja opinia, nie traktuj tego jako afront w swoją stronę."
 
    $ judge_scene()
    Lexio "Właśnie Wardęga, przegiąłeś pałę!"

    $ defense_scene()
    $ thinking(Konopski, "Muszę przyznać, że to dość... niespodziewany rozwój wydarzeń.")
    
    $ pros_scene()
    Wardega "No dajcie spokój panowie. DYSTANSIK."
    Wardega "Nie róbcie problemów tam gdzie ich nie ma, przecież tylko się tak droczymy."
    Wardega "On wie, że to tylko takie żarciki i nie ma mi tego za złe."
    Wardega "Co nie, Konopski? Sztama?"

    $ defense_scene()
    Konopski "..."
    #rzut na chamskie mordy konopskiego, lexia revo
    $ pros_scene()
    Wardega "Widzicie? Uśmiechnął się lekko."

    $ judge_scene()
    Lexio "Przeproś."

    $ pros_scene()
    Wardega "..."
    Wardega "Lexiu, jeśli mógłbym coś zasugerować... Nie gryzie się ręki, która cię karmi..."
    Wardega "A teraz bądź tak dobry i zastanów się kto jest twoim sojusznikiem."

    $ judge_scene()
    Lexio "Ok, to dajcie mi chwilę."


    $ defense_scene()
    $ thinking(Konopski, "To ja może spuszczę zasłonę milczenia na wątek zawiązywanych sojuszy i tylko rzucę taką refleksję, że ta ręka karmiąca Lexia powinna trochę dać na wstrzymanie...")
    
    $ judge_scene()
    Lexio "Dobra, już."
    Lexio "Konopski, przeproś."
    
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
    Wardega "Wiadomo, Lexiu. Brzmiałeś jak zawodowy sędzia."

    $ judge_scene()
    Lexio "Hi hi :)"
    
    $ defense_scene()
    $ thinking(Konopski, "To jakieś wolne żarty...")

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

    $ pros_scene(head="egzaltacja")
    Wardega "Wychowały mnie wilki..."

label wardega_intro:
    scene wardega_intro
    nvl clear
    $ config.nvl_list_length = 2
    wardega_nvl """
    W księżycową ciemną noc, starą wilczycę ze snu wyrwało nieśmiałe kwilenie dzięcięcia.

    Nastawiła czujnie uszu i sierść srebrzystą zjeżyła, w obawie że zbliża się szubrawiec, który stadu zagrozić może.

    Szybko jednak strach naturę zmienił i miast o pobratymców swych, wilczyca trwożyć się zaczęła o nieznaną istotkę, której płacz na myśl przywodził skamlenie zagubionego wilczątka.

    Warto nadmienić, że ów poczciwa wadera niejedną latorośl na czułej piersi swej wychowała i matczyna miłość wypełniła ją do tego stopnia, że jakakolwiek krzywda wyrządzona najmłodszym, ból jej zadawała nie mniejszy, niżby broń okrutnych kłusowników uczynić to mogła.

"""
    $ defense_scene()
    $ thinking(Konopski, "Co do...")
"""

    Troskliwa matrona szybko odkryła, że dźwięk wydobywa się z wiklinowego koszyka, pozostawionego nad brzegiem pobliskiego ruczaju, tuż obok upiornie wyglądającego, spróchniałego dębu.

    Gdy podeszła bliżej, oczom jej ukazało się drżące z zimna ludzkie szczenię, okryte niedbale brudną, poszarpaną szmatką, tak cienką, że równie dobrze mogłoby wcale jej nie być.

    Tragiczny los małego nieszczęśnika wstrząsnął wilczycą na tyle, że aż uroniła pojedynczą łzę, która spłynąwszy po jej pysku, skapnęła wprost na twarzyczkę małego cierpiętnika.

    Chłopiec momentalnie podniósł w górę wzrok, a w niej serce zamarło, z obawy że jej widok do końca straumatyzuje biedną dziecinę, ale ku jej zdziwieniu, oczy malca, choć przekrwione zupełnie od łez, nie nosiły w sobie znamion strachu.

    A były to oczy elokwentne i ciekawskie, odrobinę zadziorne, ale jednocześnie zrezygnowane i umęczone, zupełnie jak gdyby należały do okrutnie doświadczonego przez los mędrca.

    Nagle stało się coś tak niespodziewanego, że aż po dziś dzień stara wilczyca nie jest pewna, czy aby nie były to tylko jej urojenia: mianowicie chłopiec, zachrypniętym, ledwo słyszalnym głosem, wyszeptał:

    \"Sylwester Wardęga\"
    """
# menu: słuchaj dalje/ odpłyń myślami
    #$ defense_scene()
    # lexio chra[anoe

label wardega_intro2:
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
    pause 1
    
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
    $ thinking(Konopski, "Oczywiście uwzględniłbym proces sądowy...")

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

label wardega_przemowienie:

    $ pros_scene()
    Wardega "Wspaniale, nareszcze możemy przejść do części, w której będziemy cię oficjalnie krytykować"

    $ defense_scene()
    Konopski "Rozumiem że wcześniej to były takie nieoficjalne zaczepki...?"

    $ judge_scene()
    Lexio "Nareszcie, dowal temu młokosowi!"

    $ defense_scene()
    Konopski "Czy możliwe jest jeszcze większe pogwałcenie zasady o niezawisłości sądów...?"

    $ pros_scene()
    Wardega "Zgromadziliśmy się tu dzisiaj, aby należycie ukarać obecnego tu oskarżonego, który tymczasowo nazywany będzie obrońcą."

    $ judge_scene()
    Lexio "A domyślnie nazywany będzie skazanym."

    $ defense_scene()
    Konopski "Nie było tematu..."

    $ pros_scene()
    Wardega """
        To pozbawiony jakiegokolwiek kompasu moralnego młodociany bandyta,
        który nawet w tym krytycznym dla siebie momencie nie potrafi opanować patologicznego braku szacunku wobec starszych.

        Życie innych ma dla niego tyle znaczenia co babki z piasku, które dla wlasnego widzimisie można zrównać z ziemią.

        Jeśli ten pączkujący jeszcze młodzian osiągnął tak zaawansowany stan deprawacji już teraz, to czego możemy się spodziewać, gdy drań osiągnie pełnoletność?
        """

    $ defense_scene()
    Konopski """
        Mam absolutną pewność, że gdybym zaoponował, to Wardęga zarzuciłby mnie jakimiś odpisami ze szpitali w Radomiu,
        które w połączeniu ze screenami postów na deviantarcie stanowiłyby bezsprzeczny dowód, że to on wie, ile tak naprawdę mam lat.

        Tylko czeka aż zabiorę głos, widzę jak podkręca sobie wąs ze złowrogim uśmiechem i trzyma rękę na jakieś teczce jakby to był rewolwer.

        Nie dam mu tej satysfakcji.
        """

    $ pros_scene()
    Wardega "Mówiłeś coś Konop?"

    $ defense_scene()
    Konopski "Nie."

    $ pros_scene()
    Wardega """
        Sami widzicie drodzy państwo, czy nie wydaje się wam naturalne, że będąc na jego miejscu, zabralibyście w tym momencie głos i z pokorą przyznali,
        że niezwykle trafnie oceniłem wasze krótkie ale występne życie, ale obiecujecie poprawę i prosicie o rozgrzeszenie?

        Jakim byłbym człowiek, gdybym nie uronił łzy słysząc łamiący się głos tego małego nicponia?

        Cóż jednak można zrobić, jeśli ten krnąbrny grzdyl nie widzi w swoim oku ani źdźbła, ani belki?

        Gdyby tego było mało, ten niemoralny partacz o przerośniętym ego, prowadzi kanał na youtubie. Chociaż, zważywszy na żenujący poziom zamieszczanych tam materiałów powienienem powiedzieć.

        RYNSZTOK NA YOUTUBIE
        """

    $ judge_scene()
    Lexio "Ołłłł snap!"

    $ defense_scene()
    Konopski "Ołłłłłł..."
    Konopski "Nie, nie wiem co dalej, nie mam absolutnie żadnego komentarza. Niech zostanie po prostu ołłłłłł."

    $ pros_scene()
    Wardega """
        Dobre z tym rynsztokiem, nie? Mnie bawi bardzo.
        Chciałbym być wreszcie rozpoznawalny nie jako ten-od psa-pajaka, tylko ten od rynsztoka... W sumie to też nie brzmi dobrze.
        """

    Konopski "Ale ty jesteś głównie rozponawalny jako ten od boobsmana."

    Wardega """
        Cóż to za czarna magia pozwala temu pędrakowwi czytac mi w myslach?"""
    Konopski " Zapomniałeś użyc niebieskiej czcionki"

    Wardega "Teraz też słychać?"

    Konopski "Teraz już nie."

    Wardega """
        Dobrze, mogę teraz dokończyć mój wewnętrzny monolog.
        Czy Revo też widzi we mnie 'tego od boobsmena'?

        Jakie słowa cisną mu się na usta, kiedy myśli o mnie?

        Brodaty przystojniaczek?

        Amant w sile wieku?
    """

    Lexio """
        Mistyczny dziadunio?

        Stary, ale wariat?
    """

    Konopski """
        Zrzędliwy lowelas?

        W tym samym czasie revo: jurny szeryf?
        Chwila, czemu ja w ogóle biorę w tym udział...?
        Revo: Plus przecież ja nazywam go w myślach po prostu wardega"""

    Wardega """
        Zabójczy kociak?
        Kuszący mędrzec?
    """
    Konopski "Czy PAN DRUID ma jeszcze jakieś zarzuty w moją stronę..?"

    Wardega "A co ty taki niecierpliwy jesteś Konopski, rozsadza cię młodzieńcza energia?"

    Konopski """A co ty taki powolny jesteś, Mistyczny dziaduniu?
    ...
    <takie mega parsknięcie>
    """

    Wardega "Bawią cię moje zarzuty Konop? Jesteś dumny ze swojego kryminalnego życia?"

    Lexio "Dobrze, Zabójczy kociaku, zniszcz swoją ofiarę!"

    Wardega """
        ...

        Chyba straciłem wątek.

    """

    Konopski "Ostatni był żart z moim rynsztokiem na youtubie."

#Popatrzcie państwo, na ten zuchwały uśmieszek obrońcy. Na pierwszy rzut oka, że jest równie zdeprawowany jak jego klient
    Wardega """

        Ach tak, jak mogłem zapomnieć!

        Wspomnianie już pożałowania godne materiały na hehe rynsztoku hehe oskarżonego, w połączeniu z wynaturzoną naturą, stanowi zagrożenie dla niewinnych obywateli.

        Nikogo nie powinno dziwić, że to nieposkromione łajdactwo doprowadziło w końcu do tragedii.

        Ten mały łachudra, wie, że słowa tną niejednokronie głębiej niż nóż. Warto zauważyć, że brak przemocy fizycznej jest spowodowany tylko mikrą aparycją tej ledwo wyglądającej zza stolika dzieciny
        """
    Konopski "Powiedziała osoba, która potrzebuje stołka, żeby móc wyglądać zza stolika..."

    Wardega """

        Zbrodniarz nie przebierał w ohydnych kłamstwach wymierzonych w kierunku poszkodowanego,
        korzystającego z życia lekkoducha, którego jedyny grzechem jest bezinteresowna chęć wniesienia w życie innych trochę światła.

        Czyn naprawdę chcemy winić tego sympatycznego mężczyzne za idealistyczne poglądy, przekonania o prawdziwej równości, nieznającej podziałów takich jak wiek czy pł...

        ...podziałów takich jak wiek?

        Czy to nie ironiczne, że zarzuty o kontakty z młodocianymi pochodzą od osoby młodocianej? Czy w takim razie ja też jestem w oczach tego kryminalisty postrzegany jako...

        Mając na względzie stan psychiczny ofiary nie mogę powiedzieć tego plugawego słowa. Nie jestem barbarzyńcą. Nie jestem...

        Konopem.

        Na koniec drodzy państwo, chciałbym pozwolić wypowiedzieć się poszkodowanemy. Oczywiście wystarczy krótki komentarz.
        """

    $ judge_scene()
    Lexio "Ten bestialski czyn zasługuje na dożywocie."

    $ defense_scene()
    Konopski "..."
    Konopski "Ołłłłłł."

    $ pros_scene()
    Wardega "Chciałbym teraz wezwać pierwszego świadka, Tomasza Gimpera Działowego."

    $ judge_scene()
    Lexio "Przyzwalam. Proszę o wprowadzenie go na salę."

    $ defense_scene()
    Konopski "..."
    Konopski "Co Gimper ma niby z tym wspólnego"

    $ pros_scene()
    Wardega "Jak oceniasz moją przemową mój synu? Czy zrobiłeś sobie notatki, aby móc potem się na niej wzorcować?"
    Revo "Bez wątpienia nie brakowało jej walorów stylistycznych papo, ale wielokrotne powoływanie się na wiek pozwanego było mało subtelnym, niepotrzebnym zabiegiem erystycznym."
    Wardega "Gdyby ktoś inny wypowiedział te niesprawiedliwie krytyczne słowa, poczułbym się głęboko urażony."
    Wardega "Ale aż serce mi mięknie na widok twojego nieskażonego subiektywizmem lica i z pokorą wezmę sobie twoje uwagi do serca."
    Revo "Wardęga-sensei..."

    scene courtroom
    Dziewczyna3 "Omg,omg widziałyście to? a słyszałyście fragment o rosnącym sercu na widok nieprzyzwoicie przystojnego lica?"
    Dziewczyna2 "Jezu, ogarnij się, to wcale nie było tak. Poza tym już ustaliłyśmy, że Wardęga/Revo to relacja ojciec-syn i shipowanie ich to właściwie kazirodztwo. To co robisz jest niesmaczne."
    Dziewczyna3 "Powiedziała fanka Konopski/Wardęga."
    Dziewczyna2 "Nie świruj, Konopski jest pełnoletni. Konopski/Wardęga to otp. Świat potrzebuje odrobiny angstu."
    Dziewczyna3 "Świat potrzebuje gejowskiej wersji Edypa."
    Dziewczyna1 "Ej, ej, ej, dziewczyny!"
    Dziewczyna1 "A co myślicie o Spysiński/Klaudeliza?"
    "....Ale ty masz chory łeb."
    jump gimper
