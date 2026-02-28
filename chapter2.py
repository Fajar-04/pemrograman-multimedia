# Memuat dan Menyimpan Gambar

from PIL import Image

# Memuat gambar
image = Image.open('gambar_mobil.jpg')

# Menyimpan gambar
image.save('result.jpg')

# Cropping
cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')

# Resizing
resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')

# Filtering

from PIL import ImageFilter

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')

# Manipulasi Audio dengan Pydub

# Memuat dan Menyimpan File Audio
from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('audio.mp3')

# Menyimpan file audio
audio.export('result.mp3', format='mp3')

# Operasi Dasar
# Pemotongan

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')

# Penggabungan

combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')

# Konversi Format

audio.export('result.wav', format='wav')

# Pengaturan Volume

louder_audio = audio + 10 
louder_audio.export('louder_result.mp3', format='mp3')

