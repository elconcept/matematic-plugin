# MateMatic — CHAT

Adaptacja 33 skilli z MateMatic Solutions dla ChatGPT.com w trybie CHAT. Format Agent Plugins 1.0, metadane Agent Skills i jawna polityka CHAT w każdym skillu.

Repozytorium publiczne nie oznacza publikacji pluginu w katalogu ChatGPT. Wtyczka ma tylko instrukcje i pliki pomocnicze: bez serwerów, połączeń, manifestów transportu i deklaracji aplikacji. Wymagania wykonania CLI/Python/Node/Playwright oraz dostęp do źródeł zewnętrznych są odrębne od instalacji skilli i należy je sprawdzać w każdej sesji.

## Źródła

Oryginalne skille: https://github.com/matematicsolutions/awesome-matematic-skills-pl
Pinned upstream commit: 5020ef19ff04ec8f358a3422ecc3bbd915422ab4
Źródła i licencje poszczególnych skilli znajdują się w katalogach skilli; wykaz w LICENSES.md. Zmiany względem upstream: usunięcie deklaracji bundla o połączeniach, dodanie nadrzędnej polityki CHAT, usunięcie nieobsługiwanych slash commands, metadane OpenAI.

## Instalacja

Przygotuj ZIP z katalogiem głównym zawierającym plugin.json i skills/, a następnie prześlij do Plugin Creator. Wgranie ZIP tworzy domyślnie prywatny plugin użytkownika. Do samej pracy ze skillami nie dodawaj żadnego serwera.

## Walidacja

Zobacz compatibility/REPORT.md. Test statyczny struktury: python3 scripts/validate_plugin.py . . Test dostępności w trybie CHAT wymaga osobnej kontroli po instalacji w ChatGPT.

## Wszystkie skille (33)

- adversarial-legal-review-pl
- akta-przeszukiwalne-pl
- atak-przeciwnika-pl
- chronologia-stanowiska-pl
- citation-grounding-pl
- deliverable-fidelity-pl
- doc-intel-contract-pl
- doc-intel-llm-tier-pl
- ekstraktor-cytatow-pl
- eu-sparql-search
- hierarchia-zrodel-pl
- humanizer-pl
- intake-sufficiency-pl
- kalkulatory-procesowe-pl
- legal-ai-audit-bundle
- legal-data-hunter-pl
- legal-request-router-pl
- markitdown
- marko-pl-content
- matematic-expert-panel
- memo-z-repertorium-pl
- ocena-outputu-pl
- opendataloader-pdf
- pierwsze-wrazenie-sedziego-pl
- redline-docx-pl
- saos-orzecznictwo
- struktura-wyroku-pl
- subsumpcja-pl
- terminy-procesowe-pl
- uodo-grounding-pl
- waliduj-podpis-pdf-pl
- webwright-legal-pl
- klauzule-kontraktowe-pl
