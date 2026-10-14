# Pass 1 — Claude Projects: verifierbar plattformskarta

**Datum:** 2026-10-14. **Status:** levererad källstudie; ingen runtimecertifiering.

**Uppdrag:** fastställa vad plattformen erbjuder och vilka gränser Apex V3 måste respektera. Detta spår granskar inte V2-repots filinnehåll, bedömer inte kvaliteten hos installerade skills och bygger inte V3.

## 1. Slutsats för beslutsfattaren

Den bäst underbyggda startpunkten är **Projects inbyggda koordinering och delade minne, med ett litet, tydligt motiverat Apex-lager**. Det är en kandidat att pröva, inte ett bevis för att all befintlig backend ska bort. Plattformen erbjuder redan koordinering, medan dess dokumentation visar viktiga skillnader mellan körmiljöer och konfigurationskällor. [S01, S02, S04]

Tre beslut bör därför tas före en stor ombyggnad:

1. Skilj **nativ funktion**, **egen text i den funktionen** och **egen exekverande mekanism**. Ett index som heter `MEMORY.md` räcker inte för att avgöra vilken kategori något tillhör.
2. Behandla V3 som **repo plus inställningar och externa anslutningar**, inte som en ZIP som ensam återställer allt.
3. Kräv en spårbar kedja från konfiguration till faktiskt resultat. En deklarerad hook, tillgänglig skill eller godkänd rapport är inte i sig bevis på korrekt utfört arbete.

Dessa är designrekommendationer från analysen, inte fynd om att V2:s kod innehåller ett visst fel.

### Viktig källbegränsning

Anthropics index länkar till `claude-projects`, men den detaljerade sidan gick inte att hämta med webbverktyget. Även Markdown-varianten misslyckades. Lanseringsartikeln kunde läsas i sökresultat från Anthropics egen domän. Angränsande officiella dokument har lästs i relevanta avsnitt. Därför är grundmodellen belagd, men exempelvis exakt koordinatoråtkomst, minnessynkronisering, låsning och inställningsarv fortfarande delvis öppna. [S01–S03]

Vi fyller inte dessa luckor med gamla AI-svar, tredjepartsspeglar eller antaganden om hur en agent borde fungera.

## 2. Vad som är belagt, observerat respektive föreslaget

**D — dokumenterat:** stöds av läst officiell dokumentation för angiven miljö. **H — historiskt:** officiellt beskrivet vid ett tidigare datum. **O — observerat:** synligt i användarens skärmbild, inte körtestat. **R — rapporterat:** förstahandsuppgift från en extern användare. **I — slutsats/förslag:** vår analys. **U — okänt:** saknar tillräckligt underlag.

Dokumentation är ett beskrivet produktbeteende, inte bevis för att varje körning i betan följer det. En skärmbild visar ett ögonblick, inte hur gårdagens sessioner kördes. En GitHub-issue är inte en bekräftelse från Anthropic bara för att den ligger i deras repository.

Se [evidensmatrisen](01-evidence.csv) för korta, avgränsade påståenden och [källregistret](01-sources.md) för åtkomst och läsomfattning.

## 3. Produktgränser som måste hållas isär

Anthropics lansering beskriver en projektkoordinator som fördelar arbete till nya eller befintliga trådar. Molntrådar arbetar på egna repositorykopior och branches; överlapp kan ändå ge mergekonflikter. Trådar delar projektminne och kan använda underagenter. Ett projektbibliotek samlar material och producerade artefakter. [S02]

Detta är inte samma sak som en lokal Claude Code-session, en underagent, Agent Teams eller en fristående rutin. Dokumentationen behandlar dessa som skilda funktioner. [S01, S10, S12]

| Yta | Hur den används i denna analys | Vad vi inte antar |
|---|---|---|
| Projects-koordinator | Plattformens projektövergripande samordning | Att Apex måste bygga en ny dispatcher |
| Projects-tråd | Arbetet som delegeras i projektet | Att hela huvudchattens historik automatiskt följer med |
| Underagent i en session | Avgränsad delegation inom arbetet | Att den har samma minne och inställningar som projektkoordinatorn |
| Agent Teams | Separat samarbetsfunktion | Att dess specifika regler gäller Projects |
| Fristående molnsession | Referens för dokumenterat molnbeteende | Att alla projektinställningar automatiskt ärvs |
| Remote Control | Gränssnitt till lokal exekvering | Att ett webbfönster betyder molnkörning |
| Routine | Sparat automatiskt uppdrag | Att den automatiskt deltar i samma projektminne |

**Konsekvens:** varje framtida rekommendation ska ange var den gäller. En lösning som fungerar i en lokal terminal kan vara olämplig i Projects molntrådar utan att lösningen eller skillen i sig är dålig.

## 4. Koordinatorn: samordning är inte allvetande

Att behålla plattformens koordinator stämmer med användarens mål: verksamhetsarbete ska inte kräva manuell trådadministration. Men det behövs en skillnad mellan **att kunna återhämta information**, **att få den automatiskt**, **att faktiskt läsa den** och **att kontrollera att slutsatsen håller**.

Den lästa primärinformationen fastställer inte exakt vilka verktyg koordinatorn alltid har för fullständiga trådhändelser. Ett tidigare påstående i vår diskussion om att koordinatorn bara kan se sammanfattningar var därför för kategoriskt. En aktuell användarrapport beskriver flera olika läsvägar med olika beteenden, men är inte ett verktygskontrakt för alla konton. [S02, G03]

**Rekommenderad princip:** en överlämning behöver peka på det användbara resultatet, dess underlag och det som återstår. Den ska inte återge varje arbetssteg. När något är viktigt eller motsägelsefullt ska koordinatorn kunna gå vidare till källan, i den mån tillgängliga verktyg medger det.

För en SEO-granskning kan det vara rapport, undersökta sidors identiteter och tydliga kunskapsluckor. För en kodändring kan det vara exakt commit och testutfall. För en film kan det vara den faktiska exporterade filen och en kontroll av längd, ljud och format. Dessa är föreslagna leveranskrav, inte en ny obligatorisk agenthierarki.

Vi ska inte kräva att Tim läser varje verktygsanrop från alla trådar. Det kan bli samma flaskhals i ny form. Däremot ska han inte förvandla en tråds självvärdering till ett starkare kvalitetslöfte.

## 4a. Ett arbetsflöde utan påhittad intern körordning

Följande är en konceptuell karta för granskningen, inte en återgiven dold systemprompt eller garanterad laddningsordning:

1. **Uppdrag och riktning.** Användaren ger en uppgift i projektet. Målet och tillgänglig projektkontext hjälper koordinatorn att avgränsa arbetet. [S02]
2. **Samordning.** Koordinatorn väljer arbete för nya eller befintliga trådar. Vilken historik och vilka instruktioner som faktiskt når mottagaren behöver kontrolleras separat.
3. **Körmiljö.** Trådens miljö avgör åtkomst till repo, beroenden, lokala verktyg och anslutningar. Samma synliga chattgränssnitt kan användas för olika exekveringsmiljöer. [S17]
4. **Arbete och återkoppling.** Modellen använder verktygsresultat för nästa beslut. Det ger oss en plats att skilja en lyckad läsning från en blockerad operation eller en slutsats utan tillräcklig grund. [S17]
5. **Resultat och fortsatt tillstånd.** Artefakten, verifieringsutfallet och öppna beroenden behöver nå rätt mottagare. Vad som ska återanvändas framöver hör inte automatiskt hemma i samma lager som hela körhistoriken.

Steg 2 och 5 är särskilt viktiga provpunkter. Vi antar varken att delat minne är en fullständig kopia av varje konversation eller att en lyckad filskrivning betyder att koordinatorn redan har läst resultatet. En tydlig systemkarta behöver visa var detta är observerat och var det ännu bara är förväntat.

## 5. Minne: den viktigaste korrigeringen

Skärmbilderna visar `MEMORY.md` under Projects **Auto memory**. Den lokala benämningen ”teamminne” bevisar därmed inte att en fristående minnesmotor har byggts. Det kan vara plattformens minne med verksamhetsspecifikt innehåll och egna kompletterande regler. **Ingen borttagning kan motiveras enbart med filnamnet.** [O01]

Den generella Claude Code-dokumentationen beskriver också ett `MEMORY.md`-index med ämnesfiler, men anger maskinlokal lagring för den mekanismen. Projects-lanseringen beskriver delning mellan projekttrådar. Dessa utsagor gäller olika ytor; det är fel att använda den ena för att förneka den andra. [S07, S02]

V2-granskningen behöver därför skilja på fyra möjliga saker:

- Nativ lagring och återhämtning som Projects tillhandahåller.
- Egna instruktioner om vad Claude ska spara där.
- Egna skript som läser, skriver, kontrollerar eller kopierar samma data.
- Eventuella parallella kopior i repo, lokala sessioner eller andra minnesmotorer.

Det avgörs genom sökvägar, läsare, skrivare och anropskedjor. En kontroll av döda länkar kan vara nyttig, men visar inte att sparade påståenden är sanna. Ett kort index kan fortfarande hänvisa till fel fakta. Ett långt index kan innehålla viktig information som ska flyttas, inte raderas.

**Öppet:** exakt Projects-gräns för indexladdning, hur konkurrerande uppdateringar hanteras, när en ny uppgift når andra pågående trådar och vad som överlever projektbyte. Den generella gränsen 200 rader/25 KB får inte föras över till Projects utan stöd. [S03, S07]

**Pass 1-beslut:** inga externa minnesverktyg väljs och inget minne döms ut. Pass 2 jämför alternativen mot verkliga luckor, inte mot antalet stjärnor på GitHub.

## 6. Instruktioner, inställningar och faktiskt laddat material

`CLAUDE.md` ger kontext och vägledning; den är inte en exekverad behörighetskontroll. Regler för JSON-inställningars företräde är inte samma sak som att två motsägelsefulla textinstruktioner säkert löses på önskat sätt. [S07, S15]

Den generella dokumentationen skiljer mellan startupmaterial och sådant som hämtas när det behövs. Skills laddar normalt beskrivningar först och innehåll när de används. Förinladdade skills hos underagenter är ett annat fall. [S08]

**Konsekvens för V3:** målet bör vara ett tydligt hem för varje informationstyp, inte bara färre tecken. Det går exempelvis att korta `CLAUDE.md` men återinjicera samma regler genom en hook och ett minnesindex. Då har man flyttat problemet, inte löst det.

| Information | Kandidat till ansvar, att pröva i pass 2 |
|---|---|
| Varaktigt verksamhetsmål | Project Goal, utan att tolka det som obegränsat mandat |
| Gemensamt arbetssätt | Project instructions med få tydliga principer |
| Hur repositoryt fungerar | `CLAUDE.md` och relevanta lokala regler |
| Uppgiftsspecifik metod | Befintlig skill, med sina hjälpfiler |
| Föränderligt beslut eller preferens | Rätt nativ minnesyta med källa och aktualitet |
| Aktuell arbetsprodukt och bevis | Rapport, fil, commit eller annat åtkomligt resultat |
| Tvingande gräns för en extern handling | Verifierad behörighet eller avgränsad kontroll nära handlingen |

Detta är en ansvarsskiss, inte en föreskriven filstruktur. Vi skriver inte nya permanenta instruktioner innan den jämförts med V2-granskningen.

## 7. Molnkonfiguration: ett repo och flera repos beter sig olika

I Anthropic-hostade molnsessioner laddas delade repoinställningar vid ett repo. Med flera repos laddas inte repots hooks, permission-regler eller `env` på samma sätt; dokumentationen anger att bara två pluginrelaterade nycklar läses och att de deklarerade pluginen ändå inte installeras där. Lokala användarinställningar följer inte med. [S04]

**Detta är ett högt prioriterat kompatibilitetsfynd, inte ett konstaterat V2-fel.** Skärmbilden visar ett valt standardrepo, men det fastställer inte vilka repos varje tidigare tråd hade anslutna. Att ha kopierat ett exempelrepo till en mapp är inte heller automatiskt samma sak som att lägga till det som sessionens projektrepo.

Här behöver den andra granskningschatten ställa en mycket konkret fråga: *Om en nödvändig kontroll ligger i `.claude/settings.json`, vilka sessionstyper kan då lämna den oladdad?*

Tre lösningar får jämföras senare: behåll en enkel en-repo-arbetsväg; använd en dokumenterat tillämplig miljö- eller serverkonfiguration; eller placera en kritisk gräns vid målsystemet. Ingen av dessa ska väljas utan behovs- och konsekvensbedömning.

En gren får inte få etiketten ”säker” enbart för att kontrollskript finns på disk. Samtidigt ska vi inte lägga till nya guard-skript för ett tillstånd som inte förekommer i arbetssättet.

## 8. Miljön är en del av leveransen

Molninställningar hanterar bland annat miljövariabler, nätverk, hemligheter och VM-provisionering separat från repot. Setup kan återanvändas från en filsystemssnapshot; körande processer ingår inte i en sådan snapshot. Setup och SessionStart har olika livscykler. [S05]

Det ger två olika kontrollfrågor: *finns verktyget installerat?* och *kör tjänsten i denna session?* En installationskontroll svarar inte på båda.

V3 bör därför kunna återställas med en liten driftbeskrivning: rätt repo/ref, nödvändiga miljöinställningar, aktiverade anslutningar och hur deras funktion kontrolleras. Beskrivningen ska inte innehålla faktiska hemligheter.

**Egen rekommendation:** återkommande startarbete bör vara idempotent och ha ett mätbart syfte. Att installera samma paket om och om igen eller skapa nya sammanfattningar vid varje start kan ge kostnad utan nytta. Men en nödvändig misslyckad installation får inte döljas som lyckad med en generell felundertryckning.

En observerad text i ett tomt formulär kan vara platshållartext. Skärmbildens setupfält räcker därför inte som belägg för att ett visst skript faktiskt är sparat. [O03]

## 9. Lokal körning, åtkomst och externa verktyg

Remote Control kör Claude på användarens dator; webben eller mobilen är gränssnitt till den processen. Datorns tillgänglighet är därför en del av den arbetsvägens tillförlitlighet. [S11]

Skärmbilderna visar en lokal åtkomstfunktion, men inte vilka uppgifter som verkligen kördes lokalt. Lanseringsartikelns äldre formulering att lokala trådar kommer senare får inte användas som ett aktuellt förbud. [O03, S02]

Molntrådarnas skills behöver nå rätt laddningskälla. Datorns personliga skillmapp läses inte automatiskt där; dokumenterade vägar är bland annat versionshanterade projektskills och kontosynkade skills. Det är inte ett skäl att riva ett fungerande bibliotek. [S08]

Projects-trådar har dessutom ett uttryckligt krav på Claude GitHub App för repos de klonar. Detta får inte blandas ihop med att ChatGPTs GitHub-anslutning kan skriva i researchrepot. Det är två olika integrationer. [S06]

**Föreslagen kontrollkedja:** tillgänglig → autentiserad → tillåten för uppgiften → faktiskt använd → resultat återläst. För en e-handelsintegration måste varje steg vara sant. ”Full network” är inte ett generellt godkännande att ändra kunddata eller publicera. Nätverk, anslutningsbehörighet och handlingskontroll är skilda frågor. [S05, S14]

## 10. Effort, kontext och usage

Skärmbilderna visar separata inställningar för koordinator och trådar. De säger inget säkert om historiska, effektiva inställningar eller om vilken faktor som orsakat ett dåligt resultat. [O02]

Den generella modelldokumentationen beskriver effort som styrning av adaptivt resonemang och visar att explicita val, inställningar och gränser påverkar utfallet. Det följer inte att högsta nivån alltid ger bäst arbete per resurs. [S09]

**Testhypotes, inte diagnos:** mer effort för koordinatorn kan hjälpa om svag uppdragsformulering eller bedömning är flaskhalsen. Mer effort i tråden kan hjälpa om själva analysen är flaskhalsen. Inget av detta hjälper säkert när ett underlag aldrig laddas eller ett verktyg blockeras.

Prompt-cache återanvänder tidigare bearbetade prefix. Den är inte projektets långtidsminne. Sammanräknade cacheläsningar över många anrop är inte storleken på ett enda aktivt kontextfönster. [S13]

**Konsekvens:** bedöm kvalitet, omarbete, relevanta fynd, körningar och resursmått tillsammans. Råa tokenantal från en sammanställning räcker inte för att beräkna bortkastad abonnemangskvot eller en exakt kostnad. Särskilt måste saknade sessioner och olika mätperioder hanteras innan jämförelser.

Vi gör ingen ändring i V2:s modellval under denna research. Ett jämförbart experiment beskrivs i verifieringsbilagan.

## 11. Automation: start, återupptagning och färdig är olika tillstånd

Hook-dokumentationen skiljer bland annat på SessionStart, verktygshändelser och Stop. Ett Stop gäller att Claude avslutar ett svar, inte automatiskt att en verksamhetsuppgift har uppnått sitt mål. [S16]

Därför behöver en eventuell kontroll svara på den riktiga frågan. Att kräva ordet ”Täckning” kan kontrollera rapportformatet; det bevisar inte att varje källa lästes. Att tillåta en viss formulering är inte samma sak som att verifiera en export eller en uppdatering. Detta är logisk analys av kontrolltypen, inte ett påstående om exakt hur V2 implementerat den.

Officiella routines erbjuder schemalagda och händelsestyrda uppdrag i egna konfigurationer. De kör utan vanliga godkännandefrågor under passet; resurser och anslutningar måste därför avgränsas vid upplägget. Dokumentationen vi läst fastställer inte arv av ett visst Projects-minne. [S12]

**För V3:** skilj rutin som tar fram ett utkast från rutin som publicerar eller ändrar något externt. Fortsättning efter kvotåterställning, omstart av koordinatorn och start av en ny rutin får inte beskrivas som samma mekanism. Skärmbilden visar kontroller för några av dessa, men deras fulla återstartssemantik behöver körprov. [O02]

## 12. Externa incidenter: tre relevanta prövningar, inte tre bevisade rotorsaker

| Rapport | Vad den tillför | Vad den inte bevisar |
|---|---|---|
| G01, issue 96775 | Förstahandsrapport om godkänt arbete som blockerats, inklusive överlämning via koordinator. De två kommentarerna är från samma rapportör. | Att alla godkännanden i nuvarande Projects misslyckas eller att Apex har samma fel. |
| G02, issue 99688 | Reproduktionsbeskrivning om datorbindning, nätverksfel och OAuth. En annan användare bekräftar bara delen om trusted devices och lokal start. | Att hela rapportens förklaring är oberoende bekräftad eller att säkerhetsinställningar bör stängas av. |
| G03, issue 102074 | Rapport om olika beteenden för olika läsverktyg och Debug access. | Att åtkomst över kontogränser finns; rapportören säger uttryckligen att detta inte observerats. |

Alla tre var öppna vid kontrollen. Ingen läst kommentar gav en maintainerbekräftelse på hela den beskrivna mekanismen. Vi har inte reproducerat dem. [G01–G03]

**Analys:** V2-granskningen behöver ha plattformsfel och åtkomstproblem som alternativa förklaringar. Det är lika fel att skylla allt på `.md`-filerna som att skylla allt på Anthropic. Reddit söktes, men inget tillräckligt relevant, direkt underlag användes i denna leverans. Vi fyller inte ut med allmänna intryck av vad ”communityt tycker”.

## 13. Vad V3 kan utgå från — och vad som fortfarande ska avgöras

**Robusta utgångspunkter:** använd den inbyggda koordinatorn; håll driftinställningar synliga; behåll fungerande specialistmaterial; kontrollera rätt körmiljö; bedöm minnesmekanismer efter verkliga läs- och skrivvägar; bedöm resultat med åtkomliga belägg.

**Inte beslutade:** slutlig `CLAUDE.md`, hur många minnesfiler som behövs, externa minnesmotorer, exakta effort-standarder, vilka V2-hooks som tas bort eller hur rutiner kopplas till projektet. Att ange dessa nu skulle vara att bygga före granskningen.

| Alternativ | Argument att pröva | Vad som kan fälla alternativet |
|---|---|---|
| Nativ grund med nästan inga egna mekanismer | Minst egen drift och duplicering | Nödvändig kontinuitet eller säker gräns kan inte uppnås |
| Minimal hybrid | Små tillägg där mätbar lucka finns | Tilläggen duplicerar beteende eller kräver mer underhåll än de sparar |
| Ny egen orkestrering/minnesmotor | Möjlig kontroll över särskilda behov | Extra tjänster och felvägar utan visad förbättring; faktisk Projects-kompatibilitet saknas |

**Preliminärt val:** pröva första alternativet som referens och det andra som kandidat. Det tredje kräver konkret belägg för ett behov som de andra inte klarar. Detta följer uppdragets önskan om en enklare, mer kapabel grund — inte ett antagande att allt nativt fungerar felfritt.

## 13a. Felsökningsmodell för ytligt arbete

Ett kort svar är inte ensamt bevis för en ytlig undersökning. Omvänt kan en lång rapport innehålla lite faktiskt underlag. Därför föreslås följande differentiering innan backenden skrivs om:

| Möjlig felväg | Vilket belägg skiljer den från alternativen? | Felaktig snabbåtgärd att undvika |
|---|---|---|
| Underlaget nådde aldrig rätt tråd | Tillgängliga filer, laddningskälla och faktisk läsning | Att bara kräva längre svar |
| Verktyget eller behörigheten stoppade arbetet | Konkret nekande eller fel från rätt lager | Att skriva om minnet utan koppling till felet |
| Uppdraget förlorade ett krav vid överlämning | Ursprungligt krav jämfört med mottagarens uppdrag och leverans | Att öka antalet granskare utan bättre underlag |
| Analysen blev svag trots rätt åtkomst | Relevanta missade problem i ett kontrollerat arbetsprov | Att förklara allt med usage eller en standardetikett |
| Bra undersökning sammanfattades missvisande | Skillnaden mellan artefaktens belägg och slutrapportens påståenden | Att behandla rapportformat som kvalitetskontroll |

Detta är en hypotesmodell, inte fem konstaterade V2-fel. Låg kvarvarande usage väljs inte som huvudförklaring: användaren har beskrivit samma problem även tidigare. Orsak behöver fortfarande beläggas för varje situation.

För pass 2 blir det mest värdefulla därför inte en universell uppmaning om att ”tänka djupare”, utan att minska de identifierade hindren mellan uppdrag, relevant kontext, verktyg och verifierad leverans.

## 14. Vad som nu kan överlämnas

Den separata V2-granskningen kan använda denna rapport för att kontrollera effektiva konfigurationskällor, minnesidentitet, miljöberoenden och alternativa felmekanismer. Den ska fortfarande styrka varje eget fynd med V2-filer eller körspår.

Pass 2 kan nu jämföra informationsarkitektur och automationsalternativ utan att blanda ihop produkterna. Byggchatten får senare pröva våra rekommendationer tillsammans med båda granskningsrapporterna. **Ingen omröstning mellan tre AI-svar ersätter ett källbelägg eller ett reproducerbart prov.**

De kvarvarande frågorna är namngivna och testbara i [verifiering och överlämning](01-validation-and-handoff.md). Att de är öppna hindrar inte att denna källstudie levereras, men de hindrar oss från att kalla en ännu obebyggd V3 verifierad.
