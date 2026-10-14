# Pass 1 — Claude Projects: plattformskarta

Datum: 2026-10-14. Status: PÅGÅENDE RESEARCH, inte slutrapport.

## Uppdrag och gräns

Detta spår undersöker plattformen inför Apex V3. Det granskar inte Apex V2-repot och ändrar inga driftinställningar. V2-granskning och oberoende felanalys sker i separata spår. Privata transcripts, skärmbilder, kontouppgifter och lokala sökvägar publiceras inte här.

## Första belagda observationer

- Anthropics dokumentationsindex har en separat sida för Projects samt separata sidor för Agent Teams, subagents och molnsessioner. Dessa måste hållas isär vid källtillämpning. Källa: https://code.claude.com/docs/llms.txt
- Molnmiljöns dokumentation skiljer repositoryfiler från lokala användarinställningar och miljökonfiguration. Källa: https://code.claude.com/docs/en/cloud-environments — avsnittet What carries over from your setup.
- Dokumentationen om molnsessioner anger särskilt att Projects-trådar behöver Claude GitHub App på repositorier de klonar. Detta får inte ersättas av antagandet att valfri fungerande GitHub-anslutning räcker. Källa: https://code.claude.com/docs/en/claude-code-on-the-web — GitHub authentication options.

## Källbegränsning upptäckt i detta pass

Den officiella Projects-sidan är listad på https://code.claude.com/docs/en/claude-projects men direkt hämtning och Markdown-varianten har hittills misslyckats i webbverktyget. Detta bevisar inte att sidan saknas eller att funktionen inte finns. Detaljer som bara finns i speglar eller tidigare AI-svar får inte uppgraderas till verifierade plattformsfakta.

## Kvar i passet

Kontrollera officiella angränsande källor, avgränsa Projects-specifika luckor, undersök relevanta förstahandsrapporter, pröva slutsatserna och ersätt denna arbetsversion med rapport, källregister och verifieringspunkter. Inga prestandaförbättringar eller fungerande runtime-beteenden påstås utan körbevis.
