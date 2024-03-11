import os
import noisereduce as nr
import librosa
import soundfile as sf
from pydub import AudioSegment
from pydub.silence import split_on_silence

class cleanAudioFile:
    def __init__(self, audio_path, output_audio_path):
        self.audio_path = audio_path # The path to the input audio file.
        self.output_audio_path = output_audio_path # The path where the cleaned audio file will be saved.
    
    def reduce_background_noise(self, noise_reduction_level=0.7):
        """
        Reduces the background noise from an audio file and saves the cleaned audio.

        Parameters:
        - audio_path: The path to the input audio file.
        - output_path: The path where the cleaned audio file will be saved.
        """
        # Load audio file
        audio, rate = librosa.load(self.audio_path, sr=None)
        
        # Perform noise reduction
        reduced_noise_audio = nr.reduce_noise(y=audio, sr=rate, prop_decrease=noise_reduction_level)
        
        # Save the cleaned audio file
        sf.write(self.output_audio_path, reduced_noise_audio, rate)

    def trim_silence(self, silence_threshold=-40, min_silence_len=1000, keep_silence=100):
        """
        Trims silence from an audio file and saves the output.

        Parameters:
        - audio_path: Path to the input audio file.
        - output_path: Path where the trimmed audio file will be saved.
        - silence_threshold: The threshold for considering silence in dB. Default is -40 dB.
        - min_silence_len: The minimum length of silence to be considered for splitting, in milliseconds.
        - keep_silence: The amount of silence to leave at the beginning and end of each chunk, in milliseconds.
        """
        # Load the audio file
        audio = AudioSegment.from_file(self.output_audio_path)

        # Split audio on silence
        chunks = split_on_silence(
            audio,
            min_silence_len=min_silence_len,
            silence_thresh=silence_threshold,
            keep_silence=keep_silence
        )

        # Concatenate chunks
        trimmed_audio = AudioSegment.empty()
        for chunk in chunks:
            trimmed_audio += chunk

        # Save the trimmed audio
        trimmed_audio.export(self.output_audio_path, format="wav")

    def main(self, noise_reduction_level=1, silence_threshold=-40, min_silence_len=1000, keep_silence=100):
        # Reduce background noise
        self.reduce_background_noise(noise_reduction_level)

        # Trim silence
        self.trim_silence(silence_threshold, min_silence_len, keep_silence)

# Example usage
if __name__ == "__main__":
    
    input_audio_path = 'test_audio_files/e005.wav'  # Replace with your audio file path
    output_audio_path = f'output_files/cleaned_audio_e005.wav'  # Replace with your desired output path

    # Parameters for clean audio file
    noise_reduction_level = 0.8   # Adjust this value between 0 (no reduction) and 1 (maximum reduction)
    silence_threshold = -60 # dB parameter to determine what is considered silence (absolute(lower value) = more silence detected)
    min_silence_len = 1000 # milliseconds of silence required to split the audio
    keep_silence = 150 # milliseconds of silence to leave at the beginning and end of each chunk, to have a smooth transition

    # Process the audio file
    audio_cleaner = cleanAudioFile(input_audio_path, output_audio_path)
    audio_cleaner.main(noise_reduction_level, silence_threshold, min_silence_len, keep_silence)

    # Procedure for a folder
    
    # Itera sobre todos los archivos en el directorio de entrada
    for filename in os.listdir('test_audio_files'):
        try:
            if filename.endswith(".wav"):  # Ajusta esta condición para otros formatos de audio
                input_audio_path = os.path.join('test_audio_files', filename)
                output_audio_path = os.path.join('output_files', f"cleaned_{filename}".replace(".wav.wav", ".wav"))
                
                # Aplica la transformación al archivo de audio
                audio_cleaner = cleanAudioFile(input_audio_path, output_audio_path)
                audio_cleaner.main(noise_reduction_level, silence_threshold, min_silence_len, keep_silence)

                print(f"Archivo procesado y guardado en: {output_audio_path}")
        except: print(f"Error al procesar el archivo: {filename}")