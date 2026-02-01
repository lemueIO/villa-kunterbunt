# Changelog

Alle Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
und dieses Projekt hält sich an [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0-rc] - 2026-02-01

### 🚀 Highlights
- **Podcast Web Player**: Integration eines Web-Players für die Systemanalyse-Episode direkt im Header.
- **Systemanalytische Studie**: Meta-Analyse des Repositories als akademische Satire.
- **Druckvorbereitung**: Finale Anpassungen für den physischen Druck (Softcover & Hardcover) und Versandvorbereitung.

### Hinzugefügt
- **Podcast**:
    - `assets/Die Villa Kunterbunt - Analyse Podcast.mp3` hinzugefügt.
    - Web Player Implementierung via `podcast/index.html` und GitHub Pages.
    - Button im Header ("Web Player - Analyse Podcast").
- **Dokumente**:
    - `assets/Die Villa Kunterbunt - Systemanalytische Studie und Bewertung.pdf` – Die Meta-Ebene.
    - `assets/Die Villa Kunterbunt - Prolog.pdf` – Die Vorgeschichte.
- **Galerie & Visuals**:
    - Skript zur Thumbnail-Generierung (`assets/scripts/generate_thumbs.py`) für schnellere Ladezeiten.
    - Neue Illustrationen (u.a. `Die Villa Kunterbunt_040.PNG` - "Der finale Kurzschluss").
    - Open Graph Template für Social Media Vorschauen.
    - **Version Badge** (1.0-rc) oben rechts in der README.
- **Badges**:
    - Download Badge für "Systemanalytische Studie".
    - "Request Submission" Badge für Unternehmens-Teilnahme.

### Geändert
- **README.md**:
    - Komplettes Redesign der "Evaluation"-Sektion.
    - Zitate und Texte für "Kundenservice" und "Memoartiges Epos" geschärft.
    - Galerie-Layout optimiert und Button unter das Bild verschoben.
    - "Warum?" Sektion in eine `> [!NOTE]` Box umgewandelt für bessere Lesbarkeit.
- **Technik**:
    - Fix: Ungültige YAML Front Matter für GitHub Pages entfernt.
    - Fix: Badge-Links korrigiert und auf Raw-URLs umgestellt.

### Entfernt
- Veraltete Platzhalter-Bilder und duplizierte Download-Buttons.

## [0.1.0] - 2026-01-28

### Hinzugefügt
- **Initiales Release**: Start des "Villa Kunterbunt" Repositories als öffentliches Beschwerde-Protokoll.
- **Kern-Dokumente**:
    - `assets/Die Villa Kunterbunt - Korrespondez Epos - derlemue.pdf` (Das Hauptwerk).
    - `assets/E.ON-Report_ Datenübergabe.pdf` (Das Begleitschreiben an das QM).
- **Struktur**:
    - Grundlegende `README.md` mit Projektbeschreibung ("Das Korrespondenz Epos").
    - `LICENSE` (MIT).
    - Memes & Illustrationen Ordner initiiert.
