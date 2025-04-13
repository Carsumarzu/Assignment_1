# Audio Compression and MIDI Synthesis Project

This project demonstrates a complete pipeline for processing audio using spectral analysis, compression techniques (MFCC with warping), quality comparison (PSNR), and MIDI music generation and synthesis.

## 📁 Project Structure

### `1_audio_spectrum/`
- `spectrum_code.m`: MATLAB code for computing and visualizing the audio spectrum.
- `spectrum_result.png`: Output image showing the result of the spectral analysis.

### `2_audio_compression/`
- `mfcc.py`: Python script that implements MFCC feature extraction with optional warping for audio compression.

### `3_compare_quality/`
- `PSNR_comparison.png`: Visual representation of PSNR comparison between different audio formats.
- `compare.py`: Script to calculate and compare PSNR (Peak Signal-to-Noise Ratio) between original and compressed audio.
- `mp3_convert.py`: Script to convert WAV files to MP3 format for quality comparison.

### `4_MIDI_music/`
- `MIDI.py`: Python script to generate MIDI music from the extracted features or manually defined patterns.
- `jazz_output.mid`: The generated MIDI file.
- `Jazz_Mix_Final.wav`: Final mixed WAV file of the MIDI music.
- `jazz_rendered.wav`: Synthesized audio rendered from the MIDI.

### `input/`
- `Group13.wav`: The original input audio file used throughout the project.

## 🧠 Key Features
- Spectral analysis using MATLAB.
- MFCC-based audio compression with optional warping techniques.
- Objective quality evaluation using PSNR metrics.
- MIDI generation and jazz music synthesis from processed audio data.

## 🛠 Requirements
- Python 3.x
- MATLAB (for `.m` files)
- Libraries: `numpy`, `scipy`, `pydub`, `matplotlib`, `mido`, `pygame` (for MIDI rendering)

## 🚀 How to Run
1. Start by analyzing the audio spectrum using MATLAB (`1_audio_spectrum/spectrum_code.m`).
2. Run `2_audio_compression/mfcc.py` to compress audio using MFCC.
3. Use scripts in `3_compare_quality/` to compare original and compressed files using PSNR.
4. Generate and render MIDI music using the scripts in `4_MIDI_music/`.

## 🎵 Output
- Compressed audio vs. original PSNR comparison.
- MIDI file and rendered jazz-style audio.

## 📄 License
This project is for academic purposes only.
