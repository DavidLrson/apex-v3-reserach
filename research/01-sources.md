# Pass 1 — källregister och läsomfattning

Kontrollerat 2026-10-14. Länkarna är primärkällor om inget annat anges. Webbläsarverktyget kan återge cachade dokument; kontrolltid är inte ett löfte om att leverantören uppdaterade sidan samma dag. Ingen komplett webbplats eller hela GitHub-issuebeståndet har lästs.

## Officiella källor

| ID | Källa | Lästa delar och tillämpning |
|---|---|---|
| S01 | [Dokumentationsindex](https://code.claude.com/docs/llms.txt) | Indexet inventerat. Projects, agents, moln, minne, rutiner och inställningar hålls isär. Indexet bevisar sidans listning, inte alla funktionsdetaljer. |
| S02 | [Projects redesigned](https://claude.com/resources/articles/projects-redesigned) | Officiell artikel daterad 2026-09-17. Brödtext återgiven i sökresultat läst: trådar, koordinator, delat minne, bibliotek, usage och modellval. Direkt öppning misslyckades. Historisk lansering, inte aktuell detaljspecifikation. |
| S03 | [Projects, detaljerad dokumentation](https://code.claude.com/docs/en/claude-projects) | **Inte läst:** direkt sida och `.md` gick inte att hämta. Listad i S01. Inga detaljclaims grundas enbart på denna länk. |
| S04 | [Settings files and precedence](https://code.claude.com/docs/en/settings) | Framför allt Settings in cloud sessions och relevanta företrädesundantag. En-repo kontra flera repos, lokala/managed-källor och konfigurationsyta. |
| S05 | [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments) | Miljöval, variabler, nätverk/hemligheter, GitHub-proxy, carryover-tabell, setup, snapshot-cache, återstart och hookbegränsningar. Inte varje domän i allowlistan analyserad. |
| S06 | [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web) | GitHub authentication options, cloud/Remote Control-skillnad, parallella sessioner, lokala bundles, uppföljning och teleport. Projects uttryckliga GitHub App-krav används. |
| S07 | [How Claude remembers your project](https://code.claude.com/docs/en/memory) | Instruktionsladdning, @-importer, villkorade regler, auto-memory-lagring och laddningsgränser. Generell Claude Code-dokumentation; inte facit för native Projects synkronisering. |
| S08 | [Extend Claude with skills](https://code.claude.com/docs/en/skills) | Laddningsplatser, moln/kontosynk, beskrivningar/innehåll, livscykel och underagentfall. Inte kvalitetsgranskning av användarens skills. |
| S09 | [Model configuration](https://code.claude.com/docs/en/model-config) | Effort, inställningsföreträde, modellberoende standarder och rollseparering mot observerad UI. Ingen benchmark av Apex. |
| S10 | [Agents overview](https://code.claude.com/docs/en/agents) | Skillnader mellan underagenter, teams och arbetsisolering. Den hämtade översikten är inte en fullständig Projects-specifikation. |
| S11 | [Remote Control](https://code.claude.com/docs/en/remote-control) | Lokal exekvering, lokala verktyg och datorns tillgänglighet. Produktens Projects-specifika koppling lämnas till avgränsade prov. |
| S12 | [Automate work with routines](https://code.claude.com/docs/en/routines) | Definition, triggers, miljö/anslutningar, obevakad körning och skillnad mot lokala schemalagda uppgifter. Inget belägg läst för automatiskt Projects-minnesarv. |
| S13 | [Prompt caching](https://code.claude.com/docs/en/prompt-caching) | Prefixåteranvändning, kontextlager, modell/effort och skillnaden mot persistenta minnen. Ingen abonnemangsprisberäkning gjord. |
| S14 | [Permission modes](https://code.claude.com/docs/en/permission-modes) | Auto-mode-klassificering, molnlägen, serverkontroll och gränser för repoinställningar. Inte en rekommendation att kringgå skydd. |
| S15 | [Debug your configuration](https://code.claude.com/docs/en/debug-your-config) | Diagnostik för laddad kontext, settings, hooks, MCP och skillnad mellan instruktion och tillämpad kontroll. Kommandona är inte körda i Projects här. |
| S16 | [Hooks reference](https://code.claude.com/docs/en/hooks) | Livscykel, locations, matchers och eventbetydelser. Referensen är mycket lång; inte alla hooktyper och exempel djupgranskade. |
| S17 | [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works) | Verktygsloop, miljöer, sessionskontinuitet och åtkomst. Generell förklaring, inte dold Projects-implementation. |
| S18 | [Best practices](https://code.claude.com/docs/en/best-practices) | Verifiering, utforskning före implementation och kontextkostnad. Råd är inte garantier om Apex. |

## Förstahandsrapporter på GitHub

Samtliga nedan hämtades via den anslutna GitHub-integrationen. Status vid hämtning: öppna. Ingen har reproducerats av oss. Rapportörernas slutsatser hålls isär från eventuella andras kommentarer.

| ID | Källa | Omfattning och begränsning |
|---|---|---|
| G01 | [Issue 96775](https://github.com/anthropics/claude-code/issues/96775) | Ärendet från 2026-09-24 och alla två kommentarer lästa. Kommentarerna är rapportörens egna. Berör godkännande och blockerad moln-/Projects-handling. Ingen maintainerbekräftelse läst. |
| G02 | [Issue 99688](https://github.com/anthropics/claude-code/issues/99688) | Ärendet från 2026-10-05 och dess enda kommentar lästa. En annan användare stöder endast problemet med trusted devices/lokal start, inte hela nätverksförklaringen. |
| G03 | [Issue 102074](https://github.com/anthropics/claude-code/issues/102074) | Ärendet från 2026-10-14 läst; inga kommentarer fanns. Gäller två projekt på samma konto. Ingen åtkomst över kontogräns observerades enligt rapportören. |

## Användarunderlag som inte publiceras

| ID | Underlag | Vad det får stödja |
|---|---|---|
| O01 | Skärmbilder av Memory | Att ett minnesindex och ämnesfiler visas i den nativa Auto memory-ytan; inte deras faktainnehåll eller lagringsimplementation. |
| O02 | General/Models/Usage | Visade inställningar, tomt Goal, rollseparerad effort och återupptagningskontroll. Inte historisk runtime, orsaker eller exakt kostnad. |
| O03 | Environment och miljödialog | Visad moln-/lokal uppdelning och inställningsytor. Inte fungerande autentisering eller faktisk setup-exekvering. |

Dessa observationer är minimerade. De privata bilderna är inte uppladdade i repot. Den fullständiga V2-implementationen granskas i ett annat spår och har inte använts som läst källkod i denna rapport.

## Sökning, negativa resultat och exkluderingar

Sökningen omfattade officiellt index, relevanta dokumentlänkar, lanseringsartikeln och GitHub-incidenter. GitHub-sökningen gav fler träffar än som lästes; träffantal redovisas inte som täckning. Gamla rapporter om terminal-team och allmänt auto-memory får inte räknas som verifierade nya Projects-fel.

Reddit söktes med bland annat `site:reddit.com/r/ClaudeCode "Projects" "coordinator"` och `"Projects beta" memory`. Resultaten var tomma, irrelevanta eller gav inte ett tillräckligt tydligt förstahandsunderlag. **Ingen Reddit-slutsats ingår.** Sekundära sammanfattningar och en dokumentationsspegel hittades, men användes inte som teknisk auktoritet.

Den officiella Projects-sidans misslyckade hämtning registreras som en åtkomstbegränsning, inte som bevis för att sidan eller funktionen saknas. Försök från den lokala körmiljön stoppades också av DNS-fel. Varken dessa fel eller äldre svar i chatten ersätts med uppdiktade detaljspecifikationer.

## Hur källor ska användas i nästa pass

Spara källans datum, avsnitt och vilken miljö den beskriver. En nytillkommen källa kan ändra en slutsats; dokumentera då vilken. Låt inte en lanseringsartikel avgöra en senare version och låt inte en generell CLI-guide avgöra ett Projects-specifikt minneskontrakt.
