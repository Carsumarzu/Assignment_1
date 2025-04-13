import subprocess

def convert_wav_to_mp3(input_wav, output_mp3, bitrate="128k"):
    """
    Chuyển đổi file WAV sang MP3 với bitrate chỉ định.
    
    Args:
        input_wav (str): Đường dẫn file WAV đầu vào.
        output_mp3 (str): Đường dẫn file MP3 đầu ra.
        bitrate (str): Bitrate của file MP3 (mặc định: 128k).
    
    Returns:
        None
    """
    try:
        subprocess.run(["ffmpeg", "-y", "-i", input_wav, "-b:a", bitrate, output_mp3], 
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Đã chuyển đổi {input_wav} ➝ {output_mp3} thành công!")
    except Exception as e:
        print(f"❌ Lỗi khi chuyển đổi: {e}")

# Ví dụ sử dụng
input_wav = "Group13.wav"    # File WAV đầu vào
output_mp3 = "output.mp3"  # File MP3 đầu ra
convert_wav_to_mp3(input_wav, output_mp3)
