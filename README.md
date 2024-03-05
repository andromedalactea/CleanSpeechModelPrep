# Audio Cleaning Utility

Welcome to the Audio Cleaning Utility repository! This tool is designed to help you enhance your audio files by reducing background noise and trimming silent segments

## Features
- **Background Noise Reduction**: Leverages the noisereduce and librosa libraries to effectively reduce unwanted static or background noise, making your audio clearer.
- **Silence Trimming**: Utilizes the pydub library to identify and trim sections of the audio that fall below a specified silence threshold, ensuring a more engaging and concise listening experience.

## Installation
To use this utility, you'll first need to install the required Python libraries. You can install all dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Usage
- **Prepare Your Audio Files**: Place the audio files you wish to clean in a designated folder.
- **Configuration**: Adjust the parameters in the main script to suit your audio cleaning needs, including noise reduction level, silence threshold, minimum silence length, and the amount of silence to keep for smooth transitions.
- **Run the Script**: Execute the main script with your audio file paths and desired settings.

```bash
# Example usage
if __name__ == "__main__":
    
    input_audio_path = 'test_audio_files/e005.wav'  # Replace with your audio file path
    output_audio_path = f'cleaned_audio_e005.wav'  # Replace with your desired output path

    # Parameters for clean audio file
    noise_reduction_level = 0.8   # Adjust this value between 0 (no reduction) and 1 (maximum reduction)
    silence_threshold = -60 # dB parameter to determine what is considered silence (absolute(lower value) = more silence detected)
    min_silence_len = 1000 # milliseconds of silence required to split the audio
    keep_silence = 150 # milliseconds of silence to leave at the beginning and end of each chunk, to have a smooth transition

    # Process the audio file
    audio_cleaner = cleanAudioFile(input_audio_path, output_audio_path)
    audio_cleaner.main(noise_reduction_level, silence_threshold, min_silence_len, keep_silence)
```

## Parameters
- **noise_reduction_level**: Range from 0 (no reduction) to 1 (maximum reduction). Adjust based on the level of noise in your audio.
- **silence_threshold**: dB level to identify silence. More negative values are more aggressive in detecting silence.
min_silence_len: Minimum length of silence (in milliseconds) that will be considered for trimming.
- **keep_silence**: Amount of silence (in milliseconds) to preserve at the start and end of trimmed segments for smoother transitions.

## Contributing
Contributions to improve the tool or extend its functionalities are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.