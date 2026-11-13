# Audyt kompatybilności ChatGPT CHAT

Zbudowano 33 skille z metadanymi OpenAI policy.products: [CHAT]. Nie dodano manifestów ani konfiguracji serwera. To dowód zgodności strukturalnej, nie jeszcze test aktywacji w aktywnej sesji.

| Skill | Wzmianki o integracjach w metodyce | Wzmianki CLI/runtime |
|---|---:|---:|
| adversarial-legal-review-pl | 1 | 0 |
| akta-przeszukiwalne-pl | 0 | 6 |
| atak-przeciwnika-pl | 0 | 0 |
| chronologia-stanowiska-pl | 0 | 3 |
| citation-grounding-pl | 2 | 4 |
| deliverable-fidelity-pl | 0 | 2 |
| doc-intel-contract-pl | 0 | 21 |
| doc-intel-llm-tier-pl | 0 | 3 |
| ekstraktor-cytatow-pl | 0 | 0 |
| eu-sparql-search | 0 | 9 |
| hierarchia-zrodel-pl | 3 | 0 |
| humanizer-pl | 0 | 1 |
| intake-sufficiency-pl | 0 | 0 |
| kalkulatory-procesowe-pl | 2 | 0 |
| legal-ai-audit-bundle | 0 | 3 |
| legal-data-hunter-pl | 4 | 6 |
| legal-request-router-pl | 0 | 0 |
| markitdown | 1 | 10 |
| marko-pl-content | 0 | 1 |
| matematic-expert-panel | 0 | 0 |
| memo-z-repertorium-pl | 0 | 0 |
| ocena-outputu-pl | 0 | 0 |
| opendataloader-pdf | 0 | 10 |
| pierwsze-wrazenie-sedziego-pl | 0 | 0 |
| redline-docx-pl | 1 | 10 |
| saos-orzecznictwo | 2 | 7 |
| struktura-wyroku-pl | 0 | 0 |
| subsumpcja-pl | 0 | 0 |
| terminy-procesowe-pl | 4 | 0 |
| uodo-grounding-pl | 0 | 2 |
| waliduj-podpis-pdf-pl | 0 | 7 |
| webwright-legal-pl | 4 | 13 |
| klauzule-kontraktowe-pl | 0 | 0 |

Wzmianki nie oznaczają faktycznego transportu. Wszystkie zawarte instrukcje są objęte nadrzędną polityką CHAT, bez pozorowania niedostępnych narzędzi. Biblioteki zewnętrzne i skrypty mogą nie działać w zwykłej rozmowie.

Kryteria akceptacji: 33 unikalne SKILL.md; 33 agents/openai.yaml; prawidłowy manifest i opisy; oryginalne licencje; brak konfiguracji transportu; osobny test powdrożeniowy odczytu i jawnego uruchomienia skilli w ChatGPT.

Ograniczenia: nie gwarantuje automatycznej aktywacji ani dostępu do lokalnego dysku, OCR, podpisów PDF, przeglądarki czy baz prawnych. Instrukcje wymagające takich narzędzi należy realizować tylko przez rzeczywiście dostępne mechanizmy sesji.
