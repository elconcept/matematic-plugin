---
name: subsumpcja-pl
description: "Buduje jawny sylogizm prawniczy (subsumcję) dla zagadnienia - rozkłada rozumowanie na przesłankę większą (norma + wykładnia), przesłankę mniejszą (istotne fakty), podciągnięcie faktów pod normę i wniosek, a potem wskazuje słabe ogniwa: ukryte założenia, sporne fakty."
---

## Adaptacja do ChatGPT (produkt CHAT, nadrzędna wobec instrukcji zależnych od środowiska)
- To jest skill instrukcyjny, nie połączenie sieciowe ani uruchomiony program. Wtyczka nie dostarcza serwerów, aplikacji, integracji, terminala, wykonawcy skryptów ani dodatkowych uprawnień.
- Wykorzystuj wyłącznie narzędzia faktycznie dostępne w bieżącej rozmowie. Polecenia CLI, slash commands, nazwy niepodłączonych konektorów i workflow Claude Code w dalszej części opisują upstream, nie funkcje dostępne automatycznie w ChatGPT.
- Jeżeli wymagane narzędzie nie jest dostępne, zastosuj metodę na rzeczywiście dostępnych plikach i danych albo precyzyjnie zgłoś ograniczenie. Nie symuluj przeszukania źródeł, walidacji kryptograficznej, uruchomienia skryptu ani utworzenia pliku.
- Dla twierdzeń prawnych sprawdzaj tekst przepisu lub orzeczenia w dostępnym źródle pierwotnym, wraz z datą i właściwym stanem prawnym. Nie wymyślaj sygnatur, cytatów ani wyników zewnętrznych baz.
- Źródłowa metodyka pozostaje obowiązująca w zakresie zgodnym z tą sesją. Wszelkie instrukcje sugerujące, że transport lub zewnętrzne narzędzie jest dołączone do tego pluginu, są nieaktualne w tej wersji.

---

# Subsumpcja PL - jawny sylogizm prawniczy

## Filozofia

**Błąd w opinii rzadko siedzi we wniosku - siedzi w przemilczanej przesłance.** Rozumowanie prawnicze
to sylogizm: norma (przesłanka większa), fakty (przesłanka mniejsza), podciągnięcie i wniosek. Gdy
któryś krok zostaje niewypowiedziany - „bo przecież oczywiste" - tam właśnie chowa się luka, którą
znajdzie druga strona albo sąd. Ten skill zmusza, by każdy krok wypowiedzieć i oznaczyć, co jest
pewne, a co sporne.

Skill **strukturyzuje** rozumowanie, nie rozstrzyga sprawy. Ocena i decyzja zostają prawnikowi.

## Workflow

1. **Przesłanka większa (norma + wykładnia)** - zidentyfikuj normę prawną (przepis), a potem jej
   wykładnię: jak rozumiane są przesłanki normy (językowo, systemowo, celowościowo). Powołaną normę
   przekaż do citation-grounding-pl do weryfikacji.
2. **Przesłanka mniejsza (fakty istotne)** - wypisz fakty, które mają znaczenie dla przesłanek normy.
   Oddziel fakty bezsporne od spornych i od ocen.
3. **Subsumcja (podciągnięcie)** - dla każdej przesłanki normy pokaż, który fakt ją spełnia (lub nie).
   To jest właściwa praca: dopasowanie faktu do znamienia normy.
4. **Wniosek** - skutek prawny wynikający z subsumcji.
5. **Test słabych ogniw** - oznacz: które przesłanki normy są sporne w wykładni, które fakty sporne
   dowodowo, jakie założenia przyjęto milcząco. To mapa dla adversarial-legal-review-pl.

## Format wyjścia

```
ZAGADNIENIE: <pytanie prawne>

PRZESŁANKA WIĘKSZA (norma): <przepis> - "<treść/znamiona>"
  Wykładnia: <jak rozumiane są znamiona; rozbieżności w doktrynie/orzecznictwie>

PRZESŁANKA MNIEJSZA (fakty istotne):
  - bezsporne: <...>
  - sporne (dowodowo): <...>

SUBSUMCJA (znamię -> fakt):
  - <znamię 1> : spełnione przez <fakt> | NIE spełnione | sporne
  - <znamię 2> : ...

WNIOSEK: <skutek prawny>

SŁABE OGNIWA (do adversarial-legal-review-pl):
  - wykładnia: <które znamię sporne i dlaczego>
  - fakty: <co wymaga dowodu>
  - założenia milczące: <...>
```

## Granice

- Sylogizm porządkuje rozumowanie - nie zastępuje wykładni ani ustaleń dowodowych. Trafność normy,
  wykładni i oceny faktów rozstrzyga prawnik.
- Skill nie waży argumentów za i przeciw (od tego jest adversarial-legal-review-pl) - układa je tak,
  by atak i weryfikacja miały na czym pracować.
- Subsumcja zakłada normę o znamionach. Dla klauzul generalnych i ważenia zasad sam sylogizm bywa
  niewystarczający - oznacz to jako rozumowanie ważące, nie subsumpcyjne.

## Atrybucja

Subsumcja (sylogizm prawniczy) to klasyczna metoda polskiej dogmatyki prawa. Pomysł jawnego
scaffoldu sylogizmu dla AI zainspirowany m.in. projektem **Fuzi.Mingcha** (irlab-sdu) - bez użycia
jego kodu ani modeli. Reguły, format i kotwice PL to oryginalne opracowanie MateMatic.
Interpretacja MateMatic, nie stanowisko NRA ani KRRP.
