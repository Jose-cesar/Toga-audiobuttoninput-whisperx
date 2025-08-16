import sounddevice as sd
import wave
from pathlib import Path


class Recorder:
    def __init__(self, filename="output.wav", samplerate=44100, channels=1):
        self.filename = Path(filename)
        self.samplerate = samplerate
        self.channels = channels
        self.recording = None

    def record(self, duration=5):
        """Nimmt für X Sekunden Audio auf."""
        print(f"[Recorder] Starte Aufnahme für {duration} Sekunden...")
        self.recording = sd.rec(
            int(duration * self.samplerate),
            samplerate=self.samplerate,
            channels=self.channels,
            dtype="int16"
        )
        sd.wait()  # Warten bis Aufnahme fertig ist
        print("[Recorder] Aufnahme beendet.")

        # Speichern als WAV
        with wave.open(str(self.filename), "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(self.samplerate)
            wf.writeframes(self.recording.tobytes())

        print(f"[Recorder] Datei gespeichert unter: {self.filename}")

    def set_output(self, filename):
        """Ändert den Ausgabepfad für die nächste Aufnahme."""
        self.filename = Path(filename)
