# Statki Minimax

[![python](https://img.shields.io/badge/Python-3.14-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![ruff](https://github.com/wnowicki/pytemp/workflows/Ruff/badge.svg)](https://github.com/wnowicki/pytemp/actions?query=branch%3Amain)
[![pytest](https://github.com/wnowicki/pytemp/workflows/Pytest/badge.svg)](https://github.com/wnowicki/pytemp/actions?query=branch%3Amain)
[![pylint](https://github.com/wnowicki/pytemp/workflows/Pylint/badge.svg)](https://github.com/wnowicki/pytemp/actions?query=branch%3Amain)
[![markdown](https://github.com/wnowicki/pytemp/workflows/Markdown%20Lint/badge.svg)](https://github.com/wnowicki/pytemp/actions?query=branch%3Amain)
[![License: GPLv3](https://img.shields.io/badge/License-MIT-blue.svg)](https://license.md/licenses/mit-license/)

Projekt przedstawia prostą implementację gry Statki z AI wykorzystującym uproszczoną wersję algorytmu Minimax.

AI:
- analizuje możliwe ruchy,
- wykorzystuje funkcję heurystyczną,
- preferuje pola obok wcześniejszych trafień.

## Uruchomienie

Klonowanie repozytorium:

```shell
git clone https://github.com/MaksymilianWolanski/BattleShips-MiniMax.git
```

Wejście do folderu:

```shell
cd ai-statki-minimax
```

Utworzenie środowiska:

```shell
uv venv
```

Aktywacja środowiska:

```shell
.venv\Scripts\activate
```

Uruchomienie gry:

```shell
uv run python -m app.main
```

## Test

```shell
uv run pytest
```

## Walidacja jakościowa

```shell
uv run ruff check .
```

## Security

If you discover any security-related issues, please use the issue tracker.

---
Copyright (c) 2026 Maksymilian Wolański