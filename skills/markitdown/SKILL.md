---
name: markitdown
description: Konwersja dowolnego dokumentu (PDF, Word, Excel, PowerPoint, HTML, EPUB, audio, obrazy, YouTube) na Markdown dla LLM. Użyj gdy użytkownik mówi "konwertuj PDF", "przerób Word na markdown", "zamień PPT na MD", "markdown z Excela", "wyciągnij tekst z PDF", albo daje plik Office/PDF do analizy. Microsoft MarkItDown (pip) + MCP server.
license: MIT
allowed-tools: [Bash, Read, Write]
data-residency: local
requires-human-approval: false
pii-egress: none
---

## Adaptacja do ChatGPT (produkt CHAT, nadrzędna wobec instrukcji zależnych od środowiska)
- To jest skill instrukcyjny, nie połączenie sieciowe ani uruchomiony program. Wtyczka nie dostarcza serwerów, aplikacji, integracji, terminala, wykonawcy skryptów ani dodatkowych uprawnień.
- Wykorzystuj wyłącznie narzędzia faktycznie dostępne w bieżącej rozmowie. Polecenia CLI, slash commands, nazwy niepodłączonych konektorów i workflow Claude Code w dalszej części opisują upstream, nie funkcje dostępne automatycznie w ChatGPT.
- Jeżeli wymagane narzędzie nie jest dostępne, zastosuj metodę na rzeczywiście dostępnych plikach i danych albo precyzyjnie zgłoś ograniczenie. Nie symuluj przeszukania źródeł, walidacji kryptograficznej, uruchomienia skryptu ani utworzenia pliku.
- Dla twierdzeń prawnych sprawdzaj tekst przepisu lub orzeczenia w dostępnym źródle pierwotnym, wraz z datą i właściwym stanem prawnym. Nie wymyślaj sygnatur, cytatów ani wyników zewnętrznych baz.
- Źródłowa metodyka pozostaje obowiązująca w zakresie zgodnym z tą sesją. Wszelkie instrukcje sugerujące, że transport lub zewnętrzne narzędzie jest dołączone do tego pluginu, są nieaktualne w tej wersji.

---

# MarkItDown - konwerter dokumentów do Markdown (PL)

Lightweight utility Microsoftu - zachowuje strukturę (nagłówki, listy, tabele, linki), nie wygląd. Pod LLM, nie pod human.

## Instalacja (zrobione 2026-04-21)

```bash
python -m pip install --user markitdown markitdown-mcp
```

Wymaga Python 3.10+ (testowane na 3.14). CLI: `python -m markitdown`.

## Wspierane formaty

- **PDF** (preferuj dla krótkich, standardowych PDF; dla złożonych/tabel - OpenDataLoader PDF)
- **Office**: Word (.docx), Excel (.xlsx), PowerPoint (.pptx)
- **HTML, EPUB, CSV, JSON, XML**
- **Obrazy** (EXIF + OCR jeśli zainstalowane `[all]`)
- **Audio** (EXIF + transkrypcja jeśli włączone)
- **ZIP** (iteruje zawartość)
- **YouTube URL** (napisy)

## Użycie

### CLI (single file)
```bash
python -m markitdown input.pdf > output.md
python -m markitdown input.pptx -o output.md
```

### Batch (Obsidian Vault)
```bash
for f in "$USERPROFILE/Documents/Obsidian Vault/Konwerter"/*.pdf; do
  python -m markitdown "$f" > "${f%.pdf}.md"
done
```

### Python API
```python
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert("plik.docx")
print(result.text_content)
```

## Kiedy użyć MarkItDown vs OpenDataLoader PDF

| Sytuacja | Narzędzie |
|---|---|
| Word/Excel/PPT | **MarkItDown** |
| Prosty PDF, tekst liniowy | **MarkItDown** (szybsze) |
| Złożony PDF z tabelami, reading order, papers naukowe | **OpenDataLoader PDF** (jakość) |
| Audio/transkrypcja | Whisper (mamy `whisper-asr-pipeline`) |
| Web page | Defuddle (mamy `defuddle` od Kepano) |

## Integracja z vault

Output docelowo → `Konwerter/` (folder w vault dla source-pdf → MD). Frontmatter: `type: source-pdf, tags: [pdf, zrodlo]`. Zobacz `vault-rules.json` → `clippings.classification_rules.pdf_source`.

## Gotcha

- `markitdown[all]` na Python 3.14/3.15 failuje (onnxruntime, youtube-transcript-api konflikt) - użyj zainstalowanego `markitdown` bez extras
- Dla OCR obrazów / pełnego YouTube - Docker albo starszy Python (3.11/3.12)
- Nie używaj dla high-fidelity conversion dla human reading - tylko pod LLM
