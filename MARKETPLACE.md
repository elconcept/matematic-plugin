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
      "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
      "category": "Education & Research"
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

### GitHub jako źródło dla ChatGPT CHAT

Istnieją dwie różne ścieżki instalacji z GitHub:

1. **Lokalne marketplace Codex/ChatGPT Desktop** (`codex plugin marketplace add`): instaluje skille do `~/.codex/plugins/cache/`, ale ten stan **nie jest dowodem** załadowania ich w nowej sesji ChatGPT CHAT na chatgpt.com. Można odświeżać źródło przez `codex plugin marketplace upgrade` w środowisku, w którym dostępna jest komenda. Samo wskazanie GitHub nie daje gwarancji automatycznej synchronizacji na każdej powierzchni.
2. **Import do workspace ChatGPT z GitHub** (dla uprawnionego administratora): w Admin Console → Plugins → Add → Import marketplace; źródło `https://github.com/elconcept/matematic-plugin`, Path puste, Branch `main`. Następnie sprawdzić raport importu, ustawienia instalacji i wywołać Sync now. Ta ścieżka obsługuje automatyczną **dzienną synchronizację** zmian GitHub.

Dla osobistego konta bez dostępu do Admin Console nie potwierdzono w dokumentacji równoważnej ścieżki osobistego GitHub-autosync do ChatGPT CHAT. Wtedy nie należy deklarować, że sama lokalna instalacja marketplace gwarantuje skille w webowym CHAT.

**Wyniki audytu 13.11.2026:** lokalny cache `matematic-plugin` ma 33 skille, a osobna, świeża sesja CHAT zgłosiła `0/33` po usunięciu statycznej instalacji ZIP. Ta starsza sesja nadal mogła widzieć zbuforowany rejestr `33/33`; nie traktować go jako potwierdzenia dostępności w nowych sesjach. Działająca `symetria-dowodowa-tknc` ma potwierdzoną instalację osobistą po stronie Plugin Creator (`created-by-me-remote`).

**Brak konieczności MCP:** wtyczka zawiera tylko skille. Nie dołączać `mcp.json` w celu naprawy rejestracji w CHAT.

Źródła: https://developers.openai.com/plugins/build/plugins oraz https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github

## Kompatybilność i ograniczenia

- Plugin jest **skills-only** i nie zawiera ani nie wymaga żadnego MCP.
- Wydanie `v0.1.0` powstało przed dodaniem marketplace manifestu; do importu marketplace użyj **gałęzi main**, a nie tego tagu.
- Nie przesądzaj dostępności wszystkich skilli w trybie CHAT na podstawie wyłącznie poprawnego importu. Wymagany jest osobny test po instalacji.
- Kod CLI, OCR, Playwright i operacje na plikach wymagają narzędzi dostępnych w konkretnej rozmowie, nawet gdy sam skill jest widoczny.

Źródło formatu: https://developers.openai.com/plugins/build/plugins
