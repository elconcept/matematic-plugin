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

## Import lokalny (Desktop/Codex)

Ta metoda instaluje plugin w lokalnym cache Codex. Nie jest to tożsame z opublikowaniem jego skilli na koncie ChatGPT do użycia przez model w przeglądarce. 

W ChatGPT desktop / Codex wybierz **Add plugin marketplace** i podaj źródło
`elconcept/matematic-plugin` (repozytorium GitHub). Nie podawaj URL pliku `plugin.json` lub `marketplace.json`.

Jeśli narzędzie obsługuje terminal:
```sh
codex plugin marketplace add elconcept/matematic-plugin --ref main
codex plugin marketplace list
```

Po dodaniu marketplace zainstaluj widoczny w nim plugin **matematic-plugin** i sprawdź lokalne włączenie pluginu. Test skilli w CHAT jest oddzielnym kryterium; nie uznawaj go za zaliczony tylko na podstawie instalacji desktopowej.

## Potwierdzony problem: 33 skille w cache, zero w CHAT (13.11.2026)

W zweryfikowanej instalacji na macOS:
- `~/.codex/config.toml` deklaruje marketplace i `[plugins."matematic-plugin@matematic-plugin"] enabled = true`;
- cache `~/.codex/plugins/cache/matematic-plugin/matematic-plugin/0.1.0/` zawiera dokładnie 33 pliki `skills/*/SKILL.md` oraz 33 pliki `agents/openai.yaml` z `policy.products: [CHAT]`;
- w rejestrze skilli sesji ChatGPT CHAT skille z tej wtyczki **nie były obecne (0/33)**;
- w osobistym wykazie Plugin Creator nie było pluginu `matematic-plugin`.

To potwierdza instalację lokalną, lecz nie potwierdza udostępnienia przez konto ChatGPT. Nie wynika z tego konieczność dodawania `mcp.json` ani modyfikacji treści 33 skilli.

### Zalecana odrębna ścieżka dla chatgpt.com

1. Pobierz paczkę skills-only: [matematic-plugin-0.1.0.zip](https://github.com/elconcept/matematic-plugin/releases/download/v0.1.0/matematic-plugin-0.1.0.zip).
2. Prześlij archiwum do **Plugin Creator** w ChatGPT, aby utworzyć **osobisty plugin zapisany w koncie**. Samo lokalne polecenie `codex plugin marketplace add` nie zastępuje uploadu do konta.
3. Po potwierdzeniu utworzenia w Plugin Creator sprawdź obecność w katalogu `Personal`, a następnie utwórz nowe okno CHAT i sprawdź odczyt `SKILL.md` dla wszystkich 33 skilli.
4. Nie uznawaj zadania za zakończone, dopóki rejestr skilli faktycznie nie zawiera `matematic-plugin`. Jeżeli upload zostanie odrzucony, sprawdź diagnostykę komponentów i uprawnienia do funkcji na danym planie.

Publikacja ZIP i GitHub nie oznacza instalacji w koncie. Pakiet marketplace przeznaczony dla lokalnego Codex i pakiet uploadowany przez Plugin Creator to dwa różne mechanizmy dystrybucji. Żaden nie wymaga MCP dla wtyczki skills-only.

## Kompatybilność i ograniczenia

- Plugin jest **skills-only** i nie zawiera ani nie wymaga żadnego MCP.
- Wydanie `v0.1.0` powstało przed dodaniem marketplace manifestu; do importu marketplace użyj **gałęzi main**, a nie tego tagu.
- Nie przesądzaj dostępności wszystkich skilli w trybie CHAT na podstawie wyłącznie poprawnego importu. Wymagany jest osobny test po instalacji.
- Kod CLI, OCR, Playwright i operacje na plikach wymagają narzędzi dostępnych w konkretnej rozmowie, nawet gdy sam skill jest widoczny.

Źródło formatu: https://developers.openai.com/plugins/build/plugins
