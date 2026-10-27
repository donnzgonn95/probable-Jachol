# Trading AI Analyzer

**Język / Language:** 🇬🇧 [English](README.md) · 🇩🇪 [Deutsch](README.de.md) · 🇵🇱 **Polski**

Pythonowy prototyp do analizy rynków. Projekt łączy wskaźniki techniczne, poziomy wsparcia i oporu, analizę wolumenu, wykrywanie anomalii oraz interaktywne wizualizacje.

## Moje pierwsze kroki w programowaniu

To repozytorium dokumentuje ważny moment na mojej drodze do programowania — mój pierwszy działający projekt kodu.

Pierwszą wersję stworzyłem w **Google Colab**, korzystając z dostępu do **narzędzi beta-testowych Google Labs** i procesu rozwoju wspieranego przez AI. Zaczynałem od pomysłu, eksperymentowałem z kodem, testowałem wyniki i stopniowo poznawałem sposób działania poszczególnych modułów oraz ich współpracę.

Projekt pozwolił mi poznać praktyczny proces pracy z danymi: od pobierania i przetwarzania, przez analizę, po prezentację wyników. Rozwinął też moje zainteresowanie Pythonem, analizą danych, automatyzacją i odpowiedzialnym wykorzystaniem AI jako narzędzia wspierającego programowanie.

To wczesny projekt edukacyjny i prototyp. Nie twierdzę, że każdą linię kodu napisałem ręcznie ani że aplikacja jest gotowa do zastosowań produkcyjnych.

## Funkcje

- Pobieranie danych rynkowych przez `yfinance`
- Wskaźniki techniczne i poziomy rynkowe
- Grupowanie poziomów wsparcia i oporu z użyciem DBSCAN
- Analiza skoków wolumenu
- Wykrywanie anomalii metodą Isolation Forest
- Generowanie sygnałów na podstawie wzorców
- Interaktywne wykresy Plotly
- Interfejs Streamlit

## Technologie

Python · Google Colab · Streamlit · pandas · NumPy · scikit-learn · Plotly · yfinance

## Uruchomienie lokalne

Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

Uruchom aplikację:

```bash
streamlit run app.py
```

## Status projektu

Eksperymentalny projekt edukacyjny i prototyp. Wyniki analizy nie stanowią porady inwestycyjnej ani dowodu na skuteczność strategii tradingowej.
