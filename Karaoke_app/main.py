main.py
import tkinter as tk
from tkinter import filedialog
from music_manager import MusicManager

class KaraokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Karaokê")
        
        self.music_manager = MusicManager()

        self.load_button = tk.Button(root, text="Carregar Música", command=self.load_music)
        self.load_button.pack(pady=20)

        self.start_button = tk.Button(root, text="Iniciar Karaokê", command=self.start_karaoke)
        self.start_button.pack(pady=20)

        self.lyrics_label = tk.Label(root, text="", wraplength=300)
        self.lyrics_label.pack(pady=20)

    def load_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_path:
            self.music_manager.load_music(file_path)
            self.lyrics_label.config(text=self.music_manager.get_lyrics())

    def start_karaoke(self):
        self.music_manager.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = KaraokeApp(root)
    root.mainloop()