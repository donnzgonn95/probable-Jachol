# Trading AI Analyzer

**Sprache / Language:** 🇬🇧 [English](README.md) · 🇩🇪 **Deutsch** · 🇵🇱 [Polski](README.pl.md)

Ein Python-basierter Prototyp zur Marktanalyse. Das Projekt verbindet technische Indikatoren, Unterstützungs- und Widerstandsniveaus, Volumenanalyse, Anomalieerkennung und interaktive Visualisierungen.

## Mein Einstieg ins Programmieren

Dieses Repository markiert einen wichtigen Schritt auf meinem Weg in die Softwareentwicklung: mein erstes funktionierendes Codeprojekt.

Die erste Version entstand in **Google Colab**. Dabei nutzte ich meinen Zugang zu **Beta-Test-Tools von Google Labs** und einen KI-gestützten Entwicklungsprozess. Ich begann mit einer Idee, experimentierte mit dem Code, testete die Ergebnisse und arbeitete daran, die einzelnen Module zu verstehen und miteinander zu verbinden.

Das Projekt half mir, den Weg von Rohdaten über Analyse und Verarbeitung bis hin zu einer visuellen Darstellung kennenzulernen. Gleichzeitig entwickelte ich mein Interesse an Python, Datenanalyse, Automatisierung und dem verantwortungsvollen Einsatz von KI als Entwicklungswerkzeug weiter.

Es handelt sich um ein frühes Lern- und Prototyping-Projekt. Ich behaupte nicht, jede Codezeile manuell geschrieben zu haben oder dass die Anwendung produktionsreif ist.

## Funktionen

- Marktdaten mit `yfinance` abrufen
- Technische Indikatoren und Marktlevel untersuchen
- Unterstützungs- und Widerstandsniveaus mit DBSCAN clustern
- Volumenspitzen analysieren
- Auffällige Datenpunkte mit Isolation Forest erkennen
- Musterbasierte Signale erzeugen
- Interaktive Diagramme mit Plotly
- Benutzeroberfläche mit Streamlit

## Technologien

Python · Google Colab · Streamlit · pandas · NumPy · scikit-learn · Plotly · yfinance

## Lokal ausführen

Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

Anwendung starten:

```bash
streamlit run app.py
```

## Projektstatus

Experimentelles Lern- und Prototyping-Projekt. Analytische Signale sind keine Finanzberatung und kein Nachweis für eine profitable Handelsstrategie.
