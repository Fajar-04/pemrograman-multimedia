import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio

audio = None
play_obj = None
file_path = ""

def load_music():
    global audio, file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3 *.wav")]
    )
    if file_path:
        audio = AudioSegment.from_file(file_path)
        label_status.config(text=f"Loaded: {file_path.split('/')[-1]}")

def play_music():
    global play_obj
    if audio:
        play_obj = _play_with_simpleaudio(audio)
        label_status.config(text="Music Playing...")

def stop_music():
    global play_obj
    if play_obj:
        play_obj.stop()
        label_status.config(text="Music Stopped")

root = tk.Tk()
root.title("Simple Music Player Fajar Apriliawan - 105841101122")
root.geometry("400x250")
root.resizable(False, False)


title_label = tk.Label(root, text="🎵 Simple Music Player", font=("Arial", 16))
title_label.pack(pady=10)

btn_load = tk.Button(root, text="Load Music", width=20, command=load_music)
btn_load.pack(pady=5)

btn_play = tk.Button(root, text="Play", width=20, command=play_music)
btn_play.pack(pady=5)


btn_stop = tk.Button(root, text="Stop", width=20, command=stop_music)
btn_stop.pack(pady=5)


label_status = tk.Label(root, text="No Music Loaded", fg="blue")
label_status.pack(pady=15)


root.mainloop()