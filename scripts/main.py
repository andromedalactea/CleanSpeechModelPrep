import noisereduce as nr
import librosa
import soundfile as sf


class cleanAudioFile:
    def __init__(self, audio_path, output_audio_path):
        self.audio_path = audio_path # The path to the input audio file.
        self.output_audio_path = output_audio_path # The path where the cleaned audio file will be saved.
    
    def reduce_background_noise(self, noise_reduction_level=0.1):
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

    def main(self, noise_reduction_level=1):
        # Reduce background noise
        self.reduce_background_noise(noise_reduction_level)
        print(f'Cleaned audio file saved at {self.output_audio_path}')
# Example usage
if __name__ == "__main__":
    
    input_audio_path = 'test_audio_files/e002.wav'  # Replace with your audio file path
    output_audio_path = f'cleaned_audio.wav'  # Replace with your desired output path
    noise_reduction_level = 1   # Adjust this value between 0 (no reduction) and 1 (maximum reduction)

    audio_cleaner = cleanAudioFile(input_audio_path, output_audio_path)
    audio_cleaner.main(noise_reduction_level)