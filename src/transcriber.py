"""
WhisperX-Transkription
----------------------
Nutzt WhisperX, um eine Audiodatei zu transkribieren.
Fällt sauber zurück, wenn WhisperX/Torch nicht installiert sind.
"""

from pathlib import Path

def transcribe_audio(file_path: str, model_name: str = "base", device: str = "cpu",
                     batch_size: int = 16, compute_type: str = "int8") -> str:
    """
    Transkribiert die angegebene Audiodatei mit WhisperX.
    Args:
        file_path: Pfad zur Audio-Datei (wav/mp3/etc.)
        model_name: z.B. "base", "small", "medium"
        device: "cpu" oder "cuda"
        batch_size: Batchgröße für Inferenz
        compute_type: "int8" (CPU), "float16"/"int8" (GPU abhängig)
    Returns:
        Transkribierter Text (string) oder erklärende Fehlermeldung.
    """
    p = Path(file_path)
    if not p.exists():
        return f"[transcriber] Datei nicht gefunden: {file_path}"

    # Lazy-Import, damit das Modul auch ohne WhisperX importierbar bleibt
    try:
        import torch  # noqa: F401
        import whisperx
    except Exception as e:
        return (
            "[transcriber] WhisperX/Torch nicht verfügbar.\n"
            "Installiere Abhängigkeiten und ffmpeg:\n"
            "  pip install torch torchaudio whisperx\n"
            "  (ggf. passende Torch-Version für deine CUDA/CPU wählen)\n"
            f"Ursache: {e}"
        )

    try:
        # 1) Modell laden
        pipeline = whisperx.load_model(model_name, device, compute_type=compute_type)

        # 2) Audio laden
        audio = whisperx.load_audio(str(p))

        # 3) Transkription (erste Roh-Erkennung)
        result = pipeline.transcribe(audio, batch_size=batch_size)
        # result enthält u. a. "segments" und "text"

        # 4) (Optional) Alignment/Diarisierung – hier weggelassen, um Setup simpel zu halten
        # language = result.get("language", "de")
        # model_a, metadata = whisperx.load_align_model(language=language, device=device)
        # result = whisperx.align(result["segments"], model_a, metadata, audio, device)

        # 5) Text extrahieren
        if "text" in result and result["text"]:
            return result["text"].strip()

        # Fallback: Segmente zusammensetzen
        segments = result.get("segments", [])
        text = " ".join(seg.get("text", "") for seg in segments).strip()
        return text or "[transcriber] Kein Text erkannt."

    except Exception as e:
        return f"[transcriber] Fehler bei der Transkription: {e}"
