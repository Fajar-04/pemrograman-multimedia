# Manipulasi Video dan Pembuatan GUI

# Manipulasi Video dengan MoviePy dan OpenCV

# Dasar-dasar MoviePy dan OpenCV

# Memuat dan Menyimpan File Video
from moviepy import VideoFileClip, concatenate_videoclips, vfx

# Memuat file video
video = VideoFileClip('video.mp4')

# Menyimpan file video
video.write_videofile('result.mp4')

# # Operasi Dasar

# # Pemotongan

# short_video = video.subclipped(0, 10)  
# short_video.write_videofile('short_result.mp4')

# # Penggabungan

# combined_video = concatenate_videoclips([video, short_video])
# combined_video.write_videofile('combined_result.mp4')

# # Penambahan Efek

# reversed_video = short_video.with_effects([vfx.TimeMirror()])
# reversed_video.write_videofile('reversed_result.mp4')


# # Pengaturan Kecepatan

# reversed_video = short_video.with_effects([vfx.TimeMirror()])
# reversed_video.write_videofile('reversed_result.mp4')

# Pembuatan GUI dengan Tkinter

# Membuat Jendela Aplikasi Dasar

import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Menampilkan Gambar
from PIL import Image, ImageTk

# Memuat gambar menggunakan Pillow
image = Image.open('gambar_mobil.jpg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# Menampilkan Audio
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3 *.wav *.flac *.ogg *.aac"), ("All Files", "*")]
    )
    if file_path:
        try:
            audio = AudioSegment.from_file(file_path)
        except Exception as exc:  
            tk.messagebox.showerror("Playback Error", f"Cannot load audio file:\n{exc}")
            return
        play(audio)

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()