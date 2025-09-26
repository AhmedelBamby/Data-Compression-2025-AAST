import soundfile as sf
import os

def compress_to_flac(input_audio, output_audio):
    """
    Compress a WAV (or other supported format) audio file into FLAC.

    Parameters
    ----------
    input_audio : str
        Path to the input audio file (e.g., WAV).
    output_audio : str
        Path to save the compressed FLAC file."""

    # Read audio file
    data, samplerate = sf.read(input_audio)

    # Write compressed FLAC
    sf.write(output_audio, data, samplerate, format="FLAC")

    compressed_size = os.path.getsize(output_audio)
    original_size = os.path.getsize(input_audio)
    
    ratio = (1 - compressed_size / original_size) * 100

    # Get sizes and ratio
    print(f"Original audio size: {original_size / 1024:.2f} KB")
    print(f"Compressed audio size: {compressed_size / 1024:.2f} KB")
    print(f"Compression Ratio: {ratio:.2f}%")


def decompress_from_flac(input_flac, output_audio):
    """
    Decompress a FLAC audio file to WAV (or other supported format).

    Parameters
    ----------
    input_flac : str
        Path to the input FLAC file.
    output_audio : str
        Path to save the decompressed audio file (e.g., WAV).
    """
    
    # Read FLAC file
    data, samplerate = sf.read(input_flac)
    
    # Write decompressed audio file
    sf.write(output_audio, data, samplerate, format="WAV")
    
    # Get sizes for comparison
    flac_size = os.path.getsize(input_flac)
    decompressed_size = os.path.getsize(output_audio)
    
    print(f"FLAC file size: {flac_size / 1024:.2f} KB")
    print(f"Decompressed audio size: {decompressed_size / 1024:.2f} KB")
    print(f"Decompression completed successfully!")
    print(f"File saved as: {output_audio}")



# Example usage:
# Create output directory if it doesn't exist
output_dir = "compressed_output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

compress_to_flac("file_example_WAV_1MG.wav", f"{output_dir}/file_example_WAV_compressed.flac")

# Test decompression
decompress_from_flac(f"{output_dir}/file_example_WAV_compressed.flac", f"{output_dir}/decompressed_audio.wav")