Audio Analysis and Compression Project
This project performs various audio signal processing tasks, including spectrum analysis, audio compression using MFCCs, and quality comparison using PSNR metrics.

📁 Project Structure
bash
Copy
Edit
main/
├── 1_audio_spectrum/
│   ├── spectrum_code.m            # MATLAB code for generating audio spectrum
│   └── spectrum_result.png        # Output image showing the audio spectrum
├── 2_audio_compression/
│   └── mfcc.py                    # Python script for compressing audio using MFCC
├── 3_compare_quality/
│   ├── PSNR_comparison.png        # Visualization of PSNR comparison
│   ├── compare.py                 # Script to compare audio quality metrics
│   └── mp3_convert.py             # Utility for converting audio to MP3
└── README.md                      # Project documentation
🔍 Features
1. Audio Spectrum Analysis
Implemented in MATLAB (spectrum_code.m)

Visualizes the frequency spectrum of an audio file

Output stored as spectrum_result.png

2. Audio Compression
Uses Mel-frequency cepstral coefficients (MFCC) to compress audio (mfcc.py)

Focuses on extracting meaningful audio features for potential compression

3. Quality Comparison
Compares the quality of original vs compressed audio using PSNR (compare.py)

Includes MP3 conversion utility (mp3_convert.py)

Generates a PSNR comparison chart (PSNR_comparison.png)

🛠️ Requirements
Python 3.x

Libraries: numpy, scipy, matplotlib, librosa, pydub

MATLAB (for spectrum analysis)

📦 Setup
Install the required Python libraries using:

bash
Copy
Edit
pip install numpy scipy matplotlib librosa pydub
Ensure that MATLAB is installed and added to your system path if running the .m file.

🚀 Usage
Run the scripts as follows:

Audio Spectrum Analysis: Open spectrum_code.m in MATLAB and run it.

Audio Compression:

bash
Copy
Edit
python 2_audio_compression/mfcc.py
Quality Comparison:

bash
Copy
Edit
python 3_compare_quality/compare.py
python 3_compare_quality/mp3_convert.py
📈 Output
spectrum_result.png: Visualization of the audio spectrum.

PSNR_comparison.png: PSNR comparison plot for audio quality analysis.
