% Read the audio signal from file
[data, fs] = audioread('Group13.wav');

% Get the length of the signal
N = length(data);

% Find the next power of 2 for zero-padding
NFFT = 2^nextpow2(N);

% Generate frequency axis for single-sided spectrum
f = fs/2 * linspace(0, 1, NFFT/2+1);

% Compute the magnitude of the FFT
X = abs(fft(data, NFFT));

% Plot the single-sided frequency spectrum
plot(f, X(1:NFFT/2+1));
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('Single-Sided Spectrum of the Recorded Audio Signal');



