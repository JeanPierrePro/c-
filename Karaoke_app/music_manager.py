# music_manager.py
from pydub import AudioSegment
import simpleaudio as sa

class MusicManager:
    def __init__(self):
        self.current_music = None
        self.lyrics = ""

    def load_music(self, file_path):
        self.current_music = AudioSegment.from_file(file_path)
        self.lyrics = self.extract_lyrics(file_path)  # Implementar a extração de letras

    def extract_lyrics(self, file_path):
        # Aqui você pode implementar a lógica para extrair letras de um arquivo
        # Por enquanto, vamos retornar uma letra de exemplo
        return "Aqui estão as letras da música."

    def play_music(self):
        if self.current_music:
            play_obj = sa.play_buffer(self.current_music.raw_data, num_channels=self.current_music.channels,
                                      bytes_per_sample=self.current_music.sample_width,
                                      sample_rate=self.current_music.frame_rate)
            play_obj.wait_done()  # Espera a música terminar

    def get_lyrics(self):
        return self.lyrics