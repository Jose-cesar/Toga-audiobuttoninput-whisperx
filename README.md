# Toga Audioinput + WhisperX

GUI-App mit **Toga**, die einen **Mikrofon-Button** bietet, Audio **lokal aufnimmt** und per **WhisperX** automatisch transkribiert. Der erkannte Text wird direkt in der Oberfläche angezeigt.

## ✨ Features
- Mikrofon-Button in der Toga-GUI
- Aufnahme lokal speichern (WAV/MP3)
- Automatische Transkription mit WhisperX (lokal)
- Ausgabe des Textes in ein Eingabefeld/Log
- Saubere Struktur (Recording/Transcription getrennt)

## 🧰 Tech-Stack
- Python, Toga
- WhisperX (lokal)
- (optional) miniaudio / sounddevice für Recording
- Git/GitHub, VS Code

## 📦 Installation
```bash
git clone https://github.com/<dein-user>/toga-audioinput-whisperx.git
cd toga-audioinput-whisperx
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

📸 Demo

So sieht die App aus:
<img width="474" height="1210" alt="image" src="https://github.com/user-attachments/assets/7a2a466f-3a4c-4323-af5c-1752c655f3b3" />

