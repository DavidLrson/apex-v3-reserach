# Pass 1 — tillämpad metod

## Faktisk skillanvändning

Det tillhandahållna granskningsarkivet inventerades: 30 `SKILL.md`-filer. Vi aktiverar inte alla som samtidiga instruktioner. Följande metoder användes selektivt efter att deras relevanta instruktioner lästs:

| Skill | Konkret effekt på leveransen | Anpassning |
|---|---|---|
| `idea-refine` | Jämförelse mellan nativ grund, minimal hybrid och ny egen mekanism | Ingen ny intervju; målet var redan fastställt |
| `spec-driven-development` | Tydligt scope, leveranser och prov som kan avgöra beslut | Researchspecifikation, inte implementation |
| `workspace-surface-audit` | Skiljer dokumenterat, observerat, konfigurerat och verifierat | Ingen liveåtkomst till användarens Projects; ingen förhandsfavorisering av ECC |
| `agent-architecture-audit` | Informationsvägar, minnesidentitet och risk för falska verifieringar | Inte en full 12-lagers runtimeaudit; dold leverantörskod påstås inte vara läst |
| `automation-audit-ops` | Klassificering av konfiguration kontra fungerande hook/anslutning | V2-inventeringen sker i annat spår |
| `context-engineering` | Skiljer relevant underlag från alltid laddad text och opålitlig sammanfattning | Skillens procentsatser är heuristik, inte plattformsgränser |
| `context-budget` | Håller isär lagringsstorlek, laddad kontext och kumulativ usage | Ingen tokenberäkning från filstorlek används som faktisk runtimekostnad |
| `karpathy-guidelines` | Inga nya motorer eller backendregler utan konkret behov | Ändringar sker bara i researchrepot |
| `doubt-driven-development` | Tre centrala rekommendationer prövas mot motargument | Egen kritisk prövning; ingen fresh-context/cross-model-granskare körd |
| `verification-before-completion` | Källgränser och GitHub-publicering behöver faktiska kontroller | Publiceringskontroll är inte ett test av Apex V3 |

`claude-md` och `writing-for-agents` hör främst till pass 2 och senare skrivarbete. `santa-method` hör till den separata kritiska granskningen; ingen extra granskarpanel simulerades här. Befintliga e-handelsskills har inte kvalitetsgranskats eller modifierats.

## Källmetod

Utgå från officiellt index. Läs relevanta primäravsnitt. Ange produkt, körmiljö och datum. Använd förstahandsincidenter för att formulera möjliga felvägar, inte för att ersätta dokumentation. En utebliven hämtning är en lucka. En AI:s tidigare påstående är inte ett nytt källbelägg.

Källregister, evidensmatris och provunderlag är researchdokument. De ska inte bli ytterligare en uppsättning obligatoriska driftregler i Apex V3.

## Kontroll av leveransen

Före publicering kontrolleras UTF-8, filstruktur, interna länkar och att evidensmatrisens käll-ID:n finns i källregistret. Därefter skapas en GitHub-commit och dess branchreferens och filer återkontrolleras. Resultatet rapporteras i chatten efter utförda verktygsanrop, inte i förväg som ett godkänt V3-test.

Inga externa konton har ändrats utöver det uttryckligen auktoriserade researchrepositoryt. Inga runtimeprov, säkerhetsinställningsändringar eller privata rådata ingår i publiceringen.
