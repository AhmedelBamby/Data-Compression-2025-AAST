from PIL import Image
import soundfile as sf
import zipfile
import os

def compress_PNG_image(input_path, output_path, quality):
    """
    Compress an image using JPEG format.

    Parameters
    ----------
    input_path : str
        Path to the input image (PNG, JPG, etc.).
    output_path : str
        Path where the compressed JPEG will be saved.
    quality : int, default=30
        JPEG quality (0–100). Lower = more compression, smaller size.
    """
    # Open and convert to RGB (JPEG doesn't support RGBA)
    img = Image.open(input_path).convert("RGB")

    # Save with specified compression quality
    img.save(output_path, "JPEG", optimize=True, quality=quality)

    compressed_size = os.path.getsize(output_path)
    original_size = os.path.getsize(input_path)
    
    ratio = (1 - compressed_size / original_size) * 100

    # Get sizes and ratio
    print(f"Original image size: {original_size / 1024:.2f} KB")
    print(f"Compressed image size: {compressed_size / 1024:.2f} KB")
    print(f"Compression Ratio: {ratio:.2f}%")


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


def get_folder_size(folder_path):
    """Return total size of all files in the folder (bytes)."""
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))
    return total_size


def compress_folder_to_zip(folder_path, output_zip):
    """Compress folder to ZIP and show compression ratio."""
    original_size = get_folder_size(folder_path)

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

    compressed_size = os.path.getsize(output_zip)
    ratio = (1 - compressed_size / original_size) * 100

    print(f"Original: {original_size/1024:.2f} KB")
    print(f"Compressed: {compressed_size/1024:.2f} KB")
    print(f"Compression Ratio: {ratio:.2f}%")


def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)


#compress_PNG_image("original_data/boat.png", "compressed_data/compressed_boat.jpeg", 10)

#compress_to_flac("original_data/file_example_WAV_1MG.wav", "compressed_data/audio_compressed.flac")

#compress folder with .jpeg images
'''compress_folder_to_zip("original_data/jpeg images", "compressed_data/compressed_jpeg_images.zip")
extract_zip("compressed_data/compressed_jpeg_images.zip", "extracted_data/extracted_jpeg_images")
print("jpeg images extracted successfully")'''

#compress folder with .txt files
compress_folder_to_zip("original_data/shakespeare_books", "compressed_data/compressed_shakespeare_books.zip")
extract_zip("compressed_data/compressed_shakespeare_books.zip", "extracted_data/extracted_shakespeare_books")
print("shakespeare books extracted successfully")
