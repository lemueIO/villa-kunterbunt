<div align="center">

# 📜 Changelog
### Die Chronik des Wahnsinns

<p align="center">
  <img src="../website/global/images/open_graph.png" width="60%" alt="Cover Front" style="border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);">
</p>

[![Status](https://img.shields.io/badge/Status-Project_Active-success?style=for-the-badge)](#)
[![Phase L3](https://img.shields.io/badge/Phase_L3-Still_Missing-critical?style=for-the-badge)](#)

</div>

---
<br>

## 🗺️ Roadmap & Ausblick

| Zuständigkeit | Aufgabe | Status / Ziel |
| :--- | :--- | :--- |
| **derlemue** | **Stakeholder Management:** SPOC (Single Point of Contact) für E.ON / Bayernwerk. Koordination und Prüfung eingereichter Prozess-Dokumente. | *ongoing* |
| **Ph0x** | **SEO-Strategie:** Laufende Optimierung der Inhalte für maximale Auffindbarkeit in Suchmaschinen. | *ongoing* |
| **Cipher** | **Accessibility & Translation:** Erstellung der `README_DE2.md` (Leichte Sprache) und `README_EN.md` (1:1 Übersetzung). | *Q2/2026* |
| **Ph0x & Cipher** | **Internationalization:** Geplante Übersetzung aller Download-Materialien (PDFs, Reports) ins Englische. | *Planning* |
| **m3l** | **Education Edition:** Kommentierte Fassung des eBooks mit Erläuterungen für fachfremde Leser ohne elektrotechnische Vorkenntnisse. | *Q2/2026* |

<br>


## v.1.2.8 (The Dossier Release)
### "The Strategy of Protest"
*11. Februar 2026*

> **Status:** Veröffentlichung von Episode 05 ("Das Dossier") und Erweiterung des Meta-Podcast-Portals abgeschlossen.

#### 🎙️ Podcast & Audio
*   **Neue Episode (E05):** Veröffentlichung von "Die Strategie des radikalen Protests - Das Dossier".
    *   **Inhalt:** Analyse der "Intellectual Denial of Service" Strategie und des technischen Widerstands via GitHub.
    *   **Audio:** Vollständige Hifi-Metadaten-Integration und TLEN-Tagging (6:13).
    *   **Navigation:** Vernetzung mit E04 und Integration in den Meta-Index.
*   **UI/UX Refinement:** Überarbeitung der Button-Layouts und Abstände für ein konsistentes Premium-Erlebnis.
*   **Mobile Widget:** Optimierung der iPhone-Player-Anzeige durch synchronisierte Audiobook-Cover-Metadaten.

---
<br>

## v.1.2.7 (Audio Deployment & Metadata Consolidation)
### "The Sonic Waveform"
*11. Februar 2026*

> **Status:** Abschluss der massiven Audio-Aktualisierungswelle für alle Portale (`Main`, `Cowork`, `Meta`).

#### 🎙️ Audio-Deployment
*   **Massive Update Cycle:** Erfolgreicher Abschluss von 27 Verarbeitungsrunden zur Sicherstellung vollumfänglicher Metadaten-Abdeckung.
*   **Hifi Integration:** Synchronisation aller Audio-Assets mit dem neuesten Master-Stand, inklusive hochauflösender Cover-Art und Metadaten.
*   **Duration Accuracy:** Präzise Erfassung und Einbettung der `TLEN` (Total Length) Tags für alle Episoden zur Optimierung der Player-Synchronisation.
*   **Consistency Check:** Abschließende repository-weite Validierung der Dateisystem-Struktur und Audio-Integrität.

---
<br>

## v.1.2.6 (Hifi Meta & Duration Update)
### "The Resonance of Precision"
*11. Februar 2026*

> **Status:** High-Fidelity Metadaten-Einbettung und präzise Dauer-Tagging für alle Audio-Assets abgeschlossen.

#### 🎙️ Audio Veredelung
*   **Hifi Metadata Embedding:** Erneute Einbettung von hochauflösenden Metadaten (Titel, Interpret, Album, Cover) in alle MP3-Dateien (`main`, `cowork`, `meta`).
*   **Duration Tagging (TLEN):** Implementierung des `TLEN` ID3-Tags (Dauer in ms) zur Sicherstellung korrekter Zeitangaben in mobilen Playern und Widgets.
*   **Quality Assurance:** Einführung des `check_duration.py` Scripts zur automatisierten Verifizierung von Bitraten und Metadaten-Integrität.
*   **Workflow-Optimierung:** Zentralisierung der Audio-Prozexe in `core/scripts/embed_metadata.py` für konsistente Repository-weite Updates.

---
<br>

## v.1.2.5 (Podcast & Report Veredelung)
### "The Forensic Symphony"
*10. Februar 2026*

> **Status:** Integration des Meta-Podcast-Folge E03 und finale Design-Anpassung der Investigativ-Reports abgeschlossen.

#### 🎙️ Podcast & Audio
*   **Neue Episode (E03):** Veröffentlichung von "Die Analyse - E.ON Trustpilot Enthüllung".
    *   **Inhalt:** Forensische Aufarbeitung des Trustpilot-Ratings als Audio-Erlebnis.
    *   **Technik:** Implementierung neuer Player-Logik in `core/data/meta/podcast/` inklusive persistenter Playback-Events.
    *   **Branding:** Aktualisierung des "iPhone Widget Covers" (Front/Back Hover-Effekt) im Haupt-Index.

#### 🕵️ Investigativ-Report (Update)
*   **Layout-Refinement:** Umstrukturierung der Ressourcen-Sektion in `trustme/index.html`.
    *   **Header-Integration:** Ressourcen-Links direkt im Header für sofortigen Zugriff.
    *   **Daten-Transparenz:** Bereitstellung von farbcodierten Buttons für Rohdaten-Einsicht (DATEN-DUMP Positiv/Negativ).
    *   **UX-Optimierung:** 50% Verkleinerung der Buttons und Umstellung auf sachliche, knappe Beschreibungen für ein professionelles Report-Gefühl.

---
<br>

## v.1.2.4 (Investigative Update)
### "The Trustpilot Chronicles"
*10. Februar 2026*

> **Status:** Veröffentlichung der "Trustpilot-Akte" (Investigativ-Analysen) abgeschlossen.

#### 🕵️ Investigative Reports
*   **Trustpilot Analyse (E.ON):** Hinzufügung forensischer Analysen der Trustpilot-Bewertungen in `trustme/`.
    *   **Qualitative Analyse:** Untersuchung der Diskrepanz zwischen eingeladenen 5-Sterne-Bewertungen und organischen Beschwerden.
    *   **Botting-Detektion:** Visualisierung des "Einladungs-Bias" in der Kundenzufriedenheit.
    *   **Interaktive Reports:** Bereitstellung von zwei detaillierten investigativen Web-Ansichten.
    *   **History Cleanup:** Permanente Entfernung des `trustme/2/` Unterverzeichnisses aus der Git-Historie zur Bereinigung der Repository-Struktur.
    *   **Dokument-Links:** Direkte Verlinkung der Beweis-Dokumente im Footer inklusive fixer Dateinamen und "Open in New Tab" Funktionalität.
    *   **Datensatz-Selektion:** Forensischer Hinweis zur Methodik hinzugefügt – zur Gewährleistung der Analyse-Präzision wurden gezielt repräsentative Stichproben-Segmente anstatt des Gesamtdatensatzes herangezogen.

---
<br>

## v.1.2.3 (Workflow Stabilization & Audio Update)
### "The Guardian of Forks & Melodies"
*9. Februar 2026*

> **Status:** Automerge-Sicherheit für Forks und Audio-Veredelung abgeschlossen.

#### 🤖 Workflow & Automation
*   **Automerge Caller Revamp:** Vollständige Überarbeitung des Automerge-Workflows.
    *   **Repository Check:** Workflow auf `derlemue/villa-kunterbunt` beschränkt, um redundante Ausführungen auf Forks zu verhindern.
    *   **Permission Fix:** Umstellung auf `pull_request_target` und `pull_request_review`, um Schreibzugriffe (`GITHUB_TOKEN`) für PRs von Forks zu ermöglichen.
    *   **Validation:** Behebung von Syntax-Fehlern (`pull_request_review_target`) und ungültigen Inputs (`runs_on`).
    *   **Naming:** Umbenennung in "Automerge Caller" zur besseren Identifikation.

#### 🎵 Media & Content
*   **Audio Update:** Aktualisierung der Hintergrundmelodie (`villa_kunterbunt_background_melody.mp3`) in `website/global/audio/`.
*   **Repository Sync:** Manuelle Auflösung von Divergenzen und Synchronisation mit dem Remote-Stand (`git pull --rebase`).

---
<br>

## v.1.2.2 (Infrastructure Optimization & Metadata)
### "Dynamic Runners & Embedded Souls"
*7. Februar 2026*

> **Status:** Infrastruktur-Stabilisierung und MP3-Metadaten-Veredelung abgeschlossen.

#### 🚀 Infrastructure & CI/CD
*   **Dynamic Runner Selection:** Implementierung einer dynamischen Runner-Weiche im Deployment-Workflow.
    *   **Upstream (`derlemue`):** Nutzung von GitHub-hosted Runnern (`ubuntu-latest`) für maximale Verfügbarkeit.
    *   **Forks (`lemueIO`):** Automatische Nutzung von bis zu **8 Self-Hosted Docker-Runnern** zur Lastverteilung.
*   **Deployment Stabilization:** Einführung von `concurrency: cancel-in-progress`, um Warteschlangen-Staus (Deadlocks) im Deployment zu verhindern.
*   **Sync Optimization:** Erhöhung der Synchronisations-Frequenz von täglich auf **alle 15 Minuten**, um Commit-Lag zu minimieren.
*   **Cleanup:** Vollständige Entfernung von `.agent/` (ehemals `.ag/`) und temporären `.queue/` Verzeichnissen aus der Git-Historie.
*   **Centralized Utilities:** Konsolidierung aller Wartungs-Scripte in `core/scripts/`.

#### 🎵 Media & Metadata
*   **Audio Restoration:** Wiederherstellung der ungekürzten Audiobook-Fassungen (47MB+ statt 16MB) für Main und Cowork.
*   **ID3 Tagging:** Einbettung von Metadaten (Artist: "Villa Kunterbunt", Album-Art, Cover) direkt in alle Audiobook-MP3s mittels Mutagen/Python.
*   **Title Revert:** Entfernung der technischen Nummerierung ("E01/E06") zugunsten der reinen Buchtitel ("Das Hörbuch") für ein cleanes Branding.
*   **MediaSession API:** Dynamische Metadaten-Bereitschaft im Player für korrekte Anzeige in iPhone-Widgets und Sperrbildschirmen.
*   **OpenGraph Optimization:** Website-Thumbnail auf **555KB** (1280x640) bei voller Qualität optimiert.

#### 🎨 UI Harmonization
*   **Layout Polish:** Vereinheitlichung der Abstände (`margin-top`) für Volume-Slider und Button-Abstände (`15px`) über alle Portale hinweg.
*   **Root Index:** Korrektur des Audio-Fades und Standardisierung der Lautstärke-Vorgaben.

---
<br>

## v.1.2.1 (Podcast Navigation & Branding)
### "Epos, Kompendium & Anthologie"
*6. Februar 2026*

> **Status:** Harmonisierung der Navigation und Branding-Vereinheitlichung abgeschlossen.

#### 🎙️ Podcast-Harmonisierung
*   **Branding-Vereinheitlichung:** Umstellung aller Podcast-Serien auf die neuen, prägnanten Namen:
    *   Haupt-Podcast: **"Das Epos"**
    *   Meta-Podcast: **"Das Kompendium"**
    *   Cowork-Podcast: **"Die Anthologie"**
*   **Header-Design:** Vereinheitlichung aller H1-Überschriften auf **"Die Villa Kunterbunt"** über alle Index- und Folgeseiten hinweg, ergänzt durch die neuen Serien- und Folgentitel in den Untertiteln.
*   **Button-Design:** Umstellung aller Navigations-Buttons auf die neuen Seriennamen inklusive passender Emojis (`🏰`, `🎙️`, `🎧`).
*   **Interaktivität:** Fix der Cover-Flip-Funktionalität für alle Episoden im Haupt-Index (E01-E07).
*   **Zentrierung:** Perfekte Zentrierung der "Alle Episoden"-Buttons mittels Flexbox auf allen Einzelseiten.

#### 🔧 Bugfixes & Polish
*   **Audio-Links:** Reparatur der fehlerhaften Audio-Pfade auf den Einzelseiten von E01, E04 und E05 (Synchronisation mit den tatsächlichen mp3-Dateinamen).
*   **Footer-Bereinigung:** Entfernung der Text-Pfeile (`←`) aus den GitHub-Links im Footer für ein minimalistisches, icon-basiertes Design.
*   **CSS-Standardisierung:** Konsequente Nutzung der `.action-link` Klasse zur Eliminierung von redundanten Inline-Styles.

---

## v.1.2.0 (Asset Organization & Structure)
### "Clean Root Policy - Alles an seinem Platz"
*6. Februar 2026*

> **Status:** Vollständige Restrukturierung der Datenablage abgeschlossen.

#### 🗂️ Repository Structure
*   **Clean Root Policy:** Implementierung einer skalierbaren Ordnerstruktur mit klarer Trennung zwischen `main`, `cowork`, `meta` und `git`.
*   **Data Migration:** Alle Assets in `core/data/{main,cowork,meta}` mit einheitlicher Unterstruktur (`images/`, `documents/`, `podcast/`, `gallery/`, `audio/`, `illustrations/`).
*   **Naming Convention:** Konsequente Umbenennung aller Dateien zu snake_case (z.B. `die_villa_kunterbunt_ebook_cover_front.png`).

#### 🎨 Assets & Media
*   **Main Project:** Original eBook-Cover (front/back) und Audiobook-Cover in `core/data/main/images/`.
*   **Anthologie (Cowork):** Vollständiger Asset-Satz (13 Dateien) für das Anthologie-Projekt in `core/data/cowork/images/`.
*   **Kompendium (Meta):** Vollständiger Asset-Satz (13 Dateien) für das Kompendium-Projekt in `core/data/meta/images/`.
*   **Git Assets:** OpenGraph-Template verschoben nach `core/git/images/` für Repository-Metadaten.
*   **Favicon:** Neues Zirkuszelt-Favicon generiert und integriert.

#### 🎵 Website Enhancements
*   **Audio Widget:** Redesign als schwebendes Widget (rechts, unterhalb Header) mit Auto-Collapse nach 4 Sekunden.
*   **Mute Indicator:** Pulsing-Animation (rot) bei stummgeschaltetem Audio.
*   **Volume Control:** Slider für Lautstärkeregelung hinzugefügt.
*   **Mobile Optimization:** Responsive Anpassungen für Touch-Geräte.

#### 📝 Documentation
*   **README Update:** Wiederherstellung und Verbesserung des "Hinweis für Unternehmen"-Abschnitts mit Anker-ID und Upload-Leitfaden-Link.
*   **Path Updates:** Alle Referenzen auf verschobene Assets aktualisiert.

---

## v.1.1.0-RC (Release Candidate)
### "Druckfertige Ausgabe - Die Rakete ist in der Luft"
*2. Februar 2026*

<p align="center">
  <img src="./images/villa_kunterbunt_print.png" width="60%" alt="Print Version" style="border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);">
</p>

> **Status:** Versand an Hauptdarsteller seit 02.02. erfolgreich ausgelöst.
> **Update 03.02.:** Finaler Feinschliff der Dokumentation (Day 1 Patch).

#### 🚀 Features & Content
*   **Podcast Integration:** Vollständige Web-Player für alle 5 Episoden ("Satire", "Analyse", "Dossier", "DeepDive", "Zupftest") implementiert.
*   **Ebook Release:** Bereitstellung des Ebooks in den Formaten PDF und ePub.
*   **Dokumente:** Veröffentlichung des "Begleitschreiben Reports" und der "Systemanalytischen Studie".
*   **Upload-Guides:** Neue Guides in Englisch (`index_en.html`) und Einfacher Sprache (`index_de2.html`) erstellt.
*   **Galerie:** Interaktive Galerie für Memes und Illustrationen hinzugefügt.

#### 🎨 Design & UI
*   **Premium Badges:** Vollständiges Redesign der Status-Badges (Anthrazit/Orange) für konsistenten, professionellen Look.
*   **Layout:** Optimierung der README für satirischen "Premium-Dokumentations-Stil".
*   **Navigation:** Verbesserte Verlinkungen zwischen den Dokumenten und Playern.
*   **Webplayer Button-Harmonisierung:** Konsistente Textausrichtung und Styling über alle 5 Podcast-Webplayer:
    *   Linke Buttons (vorherige Episode): linksbündig
    *   Rechte Buttons (nächste Episode): rechtsbündig
    *   Übersichts-Links (Anfang/Ende): zentriert mit Highlight-Styling, einheitlicher Text "Alle Episoden"
    *   Fix für mobile Ansicht: Fehlende CSS-Klassen in Episode 2 und 3 ergänzt
*   **Sprachwahl-Design:** Umstellung auf Badge-Buttons (Flagge + Name).
*   **Site-Navigation:** Links von der Landing-Page (`/site`) führen nun direkt und im gleichen Tab zur Repository-README.
*   **Guide-Navigation:** "Zurück"-Links in den Upload-Guides springen nun per Anker direkt zum relevanten Abschnitt in der README (Deep-Links).
*   **Episode 6:** Neue Episode 6 "Die Studie" (Systemanalyse) hinzugefügt, inkl. Player und Navigation.
*   **Stability:** Implementierung manueller HTML-Anker in allen READMEs zur Sicherstellung robuster Deep-Links (Fix für Browser-Cache/GitHub-Rendering Issues).
*   **Mobile Support:** Implementierung von High-Resolution Flaggen (Base64 SVG) für perfekte Darstellung auf allen mobilen Geräten (iOS/Android) ohne Rendering-Fehler.
*   **Download Links:** Umstellung aller Dokumenten-Links auf absolute Pfade (GitHub Pages) zur Stabilisierung externer Referenzen.
*   **Header Design:** Optimierung des Layouts: Versions-Badges oben rechts, zentraler Website-Button (vergrößert 40px, Label "Jetzt erleben") über dem Titel mit finalem Spacing.

#### ✨ Final Polish (03.02.)
*   **Fork Badges:** Responsives 2x2 Grid-Layout für die Fork-Badges implementiert (inkl. Status-Anzeige).
*   **Screenshots:** Aktualisierung aller Screenshots in den Upload-Guides (Dateiauswahl, PR-Erstellung, Erfolg) für maximale Klarheit.
*   **Guides:** Vollständige Bebilderung der Upload-Prozesse in allen 3 Sprachversionen (`DE`, `DE-Einfach`, `EN`).

#### ⚙️ Infrastructure & Workflows
*   **Workflow Fixes:** Vollständige Implementierung von `sync-fork`, `deploy-pages` und `automerge` mit korrekten Berechtigungen.
*   **Automerge:** Aktiviert für Whitelist-User (derlemue, m3l1nda, osint-inc, Cipher-Pup).
*   **Self-Hosted CI/CD:** Optimierung für Self-Hosted Runner und Vermeidung von Deadlocks.
*   **Fixes:** Mermaid-Diagramm-Syntax in Upload-Guides gehärtet (Kompatibilitäts-Fix).
*   **Sync & Cleanup:** Finaler Sync und Bereinigung der Repository-Stände nach Auflösung von Divergenzen.



---

## v.1.0.0 (Initial Public Release)
### "Die Entdeckung der dritten Phase"
*Januar 2026*

*   Initiale Veröffentlichung der Korrespondenz.
*   Dokumentation des Phasenausfalls.
*   Erstellung der grundlegenden Repository-Struktur.

<div align="center">
  <i>"Fortschritt durch Stillstand."</i>
</div>
