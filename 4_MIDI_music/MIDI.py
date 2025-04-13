import pretty_midi
from pydub import AudioSegment
import subprocess
import os

# ======= 1. Load WAV để lấy độ dài ============

wav_file = "Group13.wav"
audio = AudioSegment.from_wav(wav_file)
duration_secs = len(audio) / 1000.0

# ======= 2. Tạo MIDI nhạc Jazz ============

midi = pretty_midi.PrettyMIDI()

# Piano hợp âm jazz
piano = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano

# Walking Bass
bass = pretty_midi.Instrument(program=33)  # Acoustic Bass

# Thiết lập thông số
tempo = 90
quarter_note = 60.0 / tempo
bars = int(duration_secs / (12 * quarter_note))  # 12-beat pattern loop

# Các hợp âm đơn giản cho Jazz Blues (C7 - F7 - G7)
chords = [['C4', 'E4', 'Bb4'],
          ['F4', 'A4', 'C5'],
          ['G4', 'B4', 'D5']]

# Walking bass pattern cho C-F-G
bass_notes = {
    'C': ['C2', 'E2', 'G2', 'A2'],
    'F': ['F2', 'A2', 'C3', 'D3'],
    'G': ['G2', 'B2', 'D3', 'E3']
}

# Loop theo 12-bar jazz blues
current_time = 0.0
for i in range(bars):
    for chord_idx in [0, 0, 1, 0, 2, 1, 0, 2, 1, 0, 2, 0]:  # jazz blues progression
        chord = chords[chord_idx]
        root = ['C', 'F', 'G'][chord_idx]
        # Thêm hợp âm piano
        for note in chord:
            piano.notes.append(
                pretty_midi.Note(
                    velocity=80,
                    pitch=pretty_midi.note_name_to_number(note),
                    start=current_time,
                    end=current_time + quarter_note * 2
                )
            )
        # Thêm walking bass
        for j, note in enumerate(bass_notes[root]):
            bass.notes.append(
                pretty_midi.Note(
                    velocity=90,
                    pitch=pretty_midi.note_name_to_number(note),
                    start=current_time + j * quarter_note,
                    end=current_time + (j + 0.9) * quarter_note
                )
            )
        current_time += 4 * quarter_note

# Gộp lại
midi.instruments.append(piano)
midi.instruments.append(bass)

# ======= 3. Xuất file MIDI ============

midi_path = "jazz_output.mid"
midi.write(midi_path)

# ======= 4. Chuyển MIDI -> WAV với FluidSynth ============

sf2_path = "FluidR3_GM.sf2"  # Đảm bảo bạn có file này trong thư mục hiện tại
midi_wav_path = "jazz_rendered.wav"

subprocess.run([
    "fluidsynth", "-ni", sf2_path, midi_path,
    "-F", midi_wav_path, "-r", "44100"
], check=True)

# ======= 5. Trộn WAV gốc với nhạc Jazz ============

jazz_audio = AudioSegment.from_wav(midi_wav_path)
mixed = audio.overlay(jazz_audio)

# ======= 6. Xuất kết quả ============

output_path = "Jazz_Mix_Final.wav"
mixed.export(output_path, format="wav")

print(f"✅ Done! Tệp đã lưu tại: {output_path}")
