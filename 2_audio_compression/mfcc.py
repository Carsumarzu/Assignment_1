import librosa
import numpy as np
import soundfile as sf
from sklearn.decomposition import PCA
import os

# BƯỚC 1: Load âm thanh gốc 
input_file = 'Group13.wav'  # Đổi tên file tùy ý
y, sr = librosa.load(input_file, sr=None)
print(f"Loaded audio: {input_file}, Duration: {len(y)/sr:.2f} seconds, Sampling Rate: {sr} Hz")

# BƯỚC 2: Trích xuất đặc trưng MFCC 
n_mfcc = 13
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
print("Original MFCC shape:", mfcc.shape)

# BƯỚC 3: Nén bằng PCA (giả lập Warping codec) 
n_components = 6  # Giữ lại 6 thành phần chính
pca = PCA(n_components=n_components)
mfcc_compressed = pca.fit_transform(mfcc.T)  # Transpose để đúng chiều dữ liệu
print("Compressed MFCC shape:", mfcc_compressed.shape)

# BƯỚC 4: Giải nén (Tái tạo MFCC) 
mfcc_restored = pca.inverse_transform(mfcc_compressed).T  # Transpose ngược lại
print("Restored MFCC shape:", mfcc_restored.shape)

# BƯỚC 5: Tái tạo tín hiệu âm thanh từ MFCC 
y_reconstructed = librosa.feature.inverse.mfcc_to_audio(mfcc_restored, sr=sr)

# BƯỚC 6: Lưu âm thanh đã tái tạo 
output_file = 'reconstructed.wav'
sf.write(output_file, y_reconstructed, sr)
print(f"Reconstructed audio saved as: {output_file}")

