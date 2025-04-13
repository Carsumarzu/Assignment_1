import librosa
import numpy as np

# HÀM TÍNH PSNR 
def calculate_psnr(original, compared):
    mse = np.mean((original - compared) ** 2)
    if mse == 0:
        return float('inf')
    max_val = 1.0  # Vì librosa load âm thanh với biên độ [-1, 1]
    psnr = 10 * np.log10(max_val**2 / mse)
    return psnr

# Load âm thanh gốc 
y_orig, sr_orig = librosa.load('Group13.wav', sr=None)

# Load âm thanh MFCC tái tạo 
y_mfcc, sr_mfcc = librosa.load('reconstructed.wav', sr=sr_orig)

# Load âm thanh MP3 nén 
y_mp3, sr_mp3 = librosa.load('output.mp3', sr=sr_orig)

# CẮT cho độ dài giống nhau 
min_len = min(len(y_orig), len(y_mfcc), len(y_mp3))
y_orig = y_orig[:min_len]
y_mfcc = y_mfcc[:min_len]
y_mp3 = y_mp3[:min_len]

# TÍNH PSNR 
psnr_mfcc = calculate_psnr(y_orig, y_mfcc)
psnr_mp3 = calculate_psnr(y_orig, y_mp3)

# In kết quả 
print(f"🔊 PSNR of MFCC-compressed audio: {psnr_mfcc:.2f} dB")
print(f"🔊 PSNR of MP3-compressed audio : {psnr_mp3:.2f} dB")