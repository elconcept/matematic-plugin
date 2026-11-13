# Marketplace w ChatGPT / Codex (bez MCP)

## Naprawa błędu „marketplace root does not contain a supported manifest”

Ten projekt udostępnia **jedną wtyczkę zawierającą 33 skille** w katalogu głównym repozytorium. Sam plik `plugin.json` określa wtyczkę, a nie marketplace.

W celu dodania repozytorium jako **marketplace** instalator musi znaleźć
`.agents/plugins/marketplace.json` w katalogu głównym checkoutu. Jest on już dołączony do repozytorium.

Plik `.agents/plugins/marketplace.json` zawiera wpis:
```json
{
  "name": "matematic-plugin",
  "interface": {"displayName": "MateMatic — CHAT"},
  "plugins": [
    {
      "name": "matematic-plugin",
      "source": {"source": "local", "path": "./"},
      "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
    }
  ]
}
```

`source.path: "./"` celowo wskazuje katalog główny repozytorium. To tam są istniejące `plugin.json`, `.codex-plugin/plugin.json` i `skills/`. Ścieżka względna jest interpretowana względem katalogu głównego marketplace, nie folderu `.agents/plugins/`.

## Import

W ChatGPT desktop / Codex wybierz **Add plugin marketplace** i podaj źródło
`elconcept/matematic-plugin` (repozytorium GitHub). Nie podawaj URL pliku `plugin.json` lub `marketplace.json`.

Jeśli narzędzie obsługuje terminal:
```sh
codex plugin marketplace add elconcept/matematic-plugin --ref main
codex plugin marketplace list
```

Po dodaniu marketplace zainstaluj widoczny w nim plugin **matematic-plugin** i sprawdź, czy w trybie **CHAT** można odczytać jego skille. W razie problemów z odświeżeniem instalacji uruchom ponownie aplikację desktopową.

## Kompatybilność i ograniczenia

- Plugin jest **skills-only** i nie zawiera ani nie wymaga żadnego MCP.
- Wydanie `v0.1.0` powstało przed dodaniem marketplace manifestu; do importu marketplace użyj **gałęzi main**, a nie tego tagu.
- Nie przesądzaj dostępności wszystkich skilli w trybie CHAT na podstawie wyłącznie poprawnego importu. Wymagany jest osobny test po instalacji.
- Kod CLI, OCR, Playwright i operacje na plikach wymagają narzędzi dostępnych w konkretnej rozmowie, nawet gdy sam skill jest widoczny.

Źródło formatu: https://developers.openai.com/plugins/build/plugins
