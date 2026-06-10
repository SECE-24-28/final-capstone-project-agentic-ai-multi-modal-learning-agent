import whisper

class VoiceProcessor:
    def __init__(self):
        print("Loading Whisper...")
        self.model = whisper.load_model("base")
        print("Whisper ready!")

    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        return {
            "text": result["text"],
            "language": result["language"]
        }