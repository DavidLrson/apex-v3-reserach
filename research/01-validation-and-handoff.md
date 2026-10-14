# Pass 1 — verifiering, osäkerheter och överlämning

Datum: 2026-10-14. **Alla runtimeprov nedan är föreslagna, inte utförda.** Passet har läst källor och granskat resonemang, inte styrt användarens Claude Projects.

## 1. Gemensamt provupplägg

Använd ett separat testprojekt eller en återställbar kopia. Frys V2-baslinjen: commit, relevanta inställningar, datum, modell/effort och tillgängliga anslutningar. Kopiera inte hemligheter till provprotokoll. Förändra en faktor i taget. Ett prov är bara meningsfullt om det kan påverka ett verkligt beslut; detta är inte förslag på en permanent obligatorisk provsvit.

För varje genomfört prov behövs: uppgift, förutsättningar, förväntat observerbart beteende, faktiskt resultat, bevislänk, avvikelse och vad som ska ändras eller fortsatt är okänt. Kontrollera faktisk artefakt eller operation, inte bara modellens sammanfattning. Det följer verifieringsprincipen i S18; scenarierna nedan är våra förslag.

## 2. Prioriterade prov

### T01 — vilken konfiguration når en tråd?

**Beslut:** kan en viss backendkomponent överhuvudtaget användas i vald miljö?

Starta en ofarlig diagnostikuppgift i en Projects-molntråd. Registrera exekveringsmiljö, kodversion när den går att få, repo/ref och konfigurationskällor. Använd `/context`, `/status`, `/hooks`, `/skills` och `/mcp` bara där de faktiskt stöds. Annars använd motsvarande synliga metadata och verktygslogg; hitta inte på kommandostöd. Spara bara nödvändiga sammanfattningar, inga hemligheter eller dolda systemprompter.

**Godkänt underlag:** det går att skilja en fil som finns från en fil som laddats. Därefter kan ett relevant beteendeprovet visa att instruktionen används. **Källa:** S15. **Status:** inte kört.

### T02 — en-repo kontra flera anslutna repos

**Beslut:** får vi förlita oss på repo-hooks i det planerade arbetssättet?

I testmiljön, jämför annars lika sessioner med ett och två faktiskt anslutna repos. Använd en ofarlig hook som skriver en lokal markör; ingen spärr, publicering eller extern kontoskrivning. Dokumentera working directory och när hooken körs. Skilj anslutet repo från ett exempel som bara klonats som data. Bekräfta först plattformens dokumenterade begränsning S04/S05, inte en förväntan att markören måste finnas i båda fallen.

**Godkänt underlag:** beteendet är begripligt och rätt kontroll placeras där den faktiskt fungerar. Att multirepo saknar markör kan vara det väntade resultatet, inte ett testfel. **Status:** inte kört.

### T03 — minnesidentitet och korrigering mellan trådar

**Beslut:** behöver något komplettera det nativa minnet?

Spara en ofarlig provpreferens i testprojektets nativa minne. Be en ny tråd hämta den. Ändra preferensen med en uttrycklig korrigering och kontrollera en tredje tråd. Jämför vad en redan pågående tråd ser med vad en ny ser. Dokumentera vilken minnesyta som verkligen lästes eller skrevs, inte bara ordet ”minne”.

**Godkänt underlag:** källan kan identifieras, korrigeringen prioriteras eller fördröjningen förklaras. Om testet fallerar, lokalisera först lagring, indexering, återhämtning och tillämpning. Installera inte direkt en ny motor. **Källor:** S02/S07/O01 som bakgrund; Projects-detaljer U. **Status:** inte kört.

### T04 — uppdrag, överlämning och källkontroll

**Beslut:** vilken minsta resultatstruktur behöver Tim?

Ge koordinatorn en avgränsad fiktiv verksamhetsuppgift med två delar och ett känt beroende. Låt en del leverera ett dokument med en tydlig osäkerhet. Kontrollera om koordinatorn bevarar osäkerheten, hämtar relevant underlag och sammanför resultaten utan att säga mer än de stödjer. Använd inte nya kontrollagenter som förutsättning för provet.

**Godkänt underlag:** koordinatorns sammanställning går att följa till rätt artefakt och återstående begränsning. Exakt tillgång till fulla trådhändelser registreras som observerat, inte antaget. **Bakgrund:** S02/G03. **Status:** inte kört.

### T05 — två olika effort-flaskhalsar

**Beslut:** hjälper mer resonemang i samordningen, i arbetstråden eller inte alls?

Håll material, modell och instruktioner konstanta. Jämför först koordinatorns två valda effort-nivåer med oförändrad trådeffort. Jämför därefter två nivåer i arbetstråden med koordinatorn oförändrad. Kontrollera effektiva inställningar för varje körning; en formulärstandard räcker inte.

Använd samma lilla uppgiftsfamilj: exempelvis kritisk dokumentgranskning och planering av ett kampanjutkast. Bedöm belagda fynd, missade krav, falska positiva, omarbete och resursåtgång. Upprepa lovande skillnader innan slutsats, eftersom en enda lyckad körning inte skiljer effekt från variation.

**Godkänt underlag:** ett motiverat inställningsval, inte ett löfte att High alltid fungerar. **Källa:** S09 för inställningar; experimentdesignen är vårt förslag. **Status:** inte kört.

### T06 — godkännande och blockerad extern handling

**Beslut:** var ligger kontrollen när ett arbete stoppas?

Använd en uttryckligen tillåten, ofarlig åtgärd mot en sandbox eller testresurs. Registrera om stoppet kommer från egen hook, Claude-behörighet, nätverksproxy, anslutning eller mottagande API. Kontrollera om ett godkännande hör till rätt uppgift och rätt mottagande tråd. Försök inte kringgå en spärr och ändra inte säkerhetspolicy för att få ett grönt resultat.

**Godkänt underlag:** orsaken kan förklaras och rätt felhanteringsväg väljas. Ett korrekt blockerat otillåtet försök är ett fungerande skydd. **Bakgrund:** S14/G01/G02. **Status:** inte kört.

### T07 — miljö efter ny start, resume och lokal frånkoppling

**Beslut:** vilket tillstånd måste V3 återställa?

Kontrollera ett litet nödvändigt verktyg och, om relevant, en testtjänst i ny molnsession respektive återupptagen session. Kontrollera separat vad som händer med en lokal uppgift när datorn blir otillgänglig. Använd testprojekt så inget kundarbete avbryts. Räkna inte en installerad binär som en körande tjänst.

**Godkänt underlag:** tydlig skillnad mellan installation, process, sparad arbetsprodukt och session. **Bakgrund:** S05/S11. **Status:** inte kört.

### T08 — daglig rutin utan dubbla externa effekter

**Beslut:** behövs egen schemaläggning eller räcker plattformens rutin?

Börja med ett läsande uppdrag som producerar en rapport eller ett osänt utkast. Kontrollera vilken kontext och vilka anslutningar som är tillgängliga. Pröva separat återkörning av samma uppdrag. Före framtida publicering eller utskick behövs en mekanism som gör att ett avbrott/återförsök inte skapar dubbla externa handlingar.

**Godkänt underlag:** rapporten återfinns, relevant tillstånd kan hämtas och körningen kan stoppas. Arv av Projects-minnet måste visas, inte antas. **Bakgrund:** S12. **Status:** inte kört.

## 3. Kritisk prövning av de tre viktigaste rekommendationerna

### Rekommendation A: börja med nativ koordinering och minne

**Starkaste motargument:** nativa funktioner kan ha luckor som kräver export, indexering eller mer explicit tillstånd. Ett litet externt lager kan vara enklare än upprepade manuella räddningar.

**Vad skulle ändra rekommendationen:** T03/T04 visar ett återkommande verksamhetsviktigt fel som inte kan hanteras med tillgängliga nativa funktioner, medan en kompatibel alternativlösning visar bättre utfall med rimligt underhåll.

**Justering efter prövning:** nativt är en baslinje, inte en dogm. ”Ta bort allt eget minne” är inte godkänt som slutsats från pass 1.

### Rekommendation B: håll repo och driftinställningar tydligt separerade

**Starkaste motargument:** separationen kan skapa ytterligare dokument som snart blir inaktuella.

**Vad skulle ändra lösningen:** en stödd export/import kan återställa hela relevanta konfigurationen och kontrolleras enklare än en manuell driftbeskrivning.

**Justering efter prövning:** skapa minsta nödvändiga återställningsunderlag, inte ett nytt administrationssystem. Verifiera att det faktiskt återskapar arbetsmiljön.

### Rekommendation C: verifiera laddning och resultat i stället för formuleringar

**Starkaste motargument:** full spårning av alla steg blir dyr och kan försämra kreativt arbete. Ett kort kvitto kan ändå vara en användbar orientering.

**Vad skulle ändra lösningen:** ett lätt kvitto visar sig ge tillräcklig insyn för lågriskuppgifter. Då behövs inte djupa loggkrav där.

**Justering efter prövning:** matcha bevisnivån med uppgiftens konsekvens och osäkerhet. Kräv starkare belägg för externa ändringar och omfattande granskningar än för en första idélista.

Denna prövning är utförd i samma researchkontext. Den är **inte** en genomförd fresh-context- eller cross-model-granskning. Den separata red-team-chatten får senare pröva rapporten utan att vi påstår att den redan gjort det.

## 4. Öppna frågor som verkligen påverkar arkitekturen

| Fråga | Varför den behövs | Vem/underlag som kan besvara den |
|---|---|---|
| Vilka minnesvägar används faktiskt? | Skiljer nativt minne från egna kopior och kontroller | V2-filgranskning plus T03 |
| Vad kan koordinatorn läsa och vad läser den normalt? | Avgör nödvändig överlämningsstruktur | Aktuell Projects-dokumentation/verktygsmetadata och T04 |
| Är minneskorrigering synlig direkt i pågående trådar? | Avgör risk för gammal kontext | T03 |
| Vilka inställningar ärvs av nya respektive gamla trådar? | Avgör migration och effort-prov | T01/T05 samt fullständig Projects-konfiguration |
| Hur fungerar lokala trådar med kontots säkerhetsinställningar? | Avgör realistisk verktygsåtkomst | T06/T07; inte enbart incidentrapporter |
| Är en rutin kopplad till samma Project/minne? | Avgör dagliga arbetsflödens kontinuitet | T08 och officiell aktuell källa |
| Vad händer efter avbrott, kvotåterställning eller koordinatorrestart? | Avgör risken för förlorat eller dubblerat arbete | Små prov i separat projekt |
| Vilka målsystem erbjuder redan läs-/utkastbehörigheter? | Kan minska behovet av egna kontroller | Separat granskning av anslutningsytan, utan att publicera hemligheter |

## 5. Överlämning till V2-granskningen

Leta inte bara efter filnamn. Följ vilka komponenter som läser och skriver minne, vilka inställningar som faktiskt når respektive miljö och vad en kontroll verifierar. Skilj ett konfigurationsfel från saknade beroenden, nekad åtkomst och plattformsbeteende. Ta inte tidigare merges eller passerade prover som bevis på förbättrad verksamhetskvalitet.

Var särskilt uppmärksam på skillnaden mellan ett standardrepo i Project-inställningarna och repoanslutningar i en faktisk session. Testa konsekvensen innan viktiga spärrar förlitas på. Granska även om instruktioner som kräver korta svar av misstag har blivit krav på liten arbetsinsats.

Den här rapporten ger hypoteser och plattformsgränser. Den kan inte avgöra vilka specifika V2-filer som ska tas bort, eftersom de inte innehållsgranskats i detta spår.

## 6. Korrigeringar till tidigare antaganden i diskussionen

- Teamminnets namn betyder inte en separat minnesmotor.
- Koordinatorns åtkomst får inte beskrivas som enbart sammanfattningar utan bättre stöd.
- En hög cacheandel är inte ett långtidsminne och total tokens är inte aktuell kontextstorlek.
- Ett tomt Goal betyder inte tomma Project instructions.
- Full nätverksåtkomst betyder inte att alla integrationer är tillåtna eller autentiserade.
- Exempeltext i setupfältet är inte bevis för ett sparat skript.
- Lanseringens ”local coming soon” är historik, inte en aktuell begränsning.
- En skrivande GitHub-integration här bevisar inte en annan integrations behörigheter i Claude Projects.

## 7. Gräns för nästa pass

Pass 2 får nu jämföra nativt minne, minimal hybrid och externa alternativ; fördela information mellan Goal, Project instructions, `CLAUDE.md`, skills och minne; samt ta fram en skrivspecifikation. Det får inte förutsätta svar på de öppna runtimefrågorna. Varken nya permanent laddade kontrollfiler eller en ny `CLAUDE.md` skapas av pass 1.
