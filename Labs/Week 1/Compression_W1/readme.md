# 📦 Data Compression in Python

This script demonstrates different types of compression in Python using pre-built libraries:

* **Image compression** (using Pillow → JPEG lossy compression)
* **Audio compression** (using SoundFile → FLAC lossless compression)
* **Folder compression** (using `zipfile`)

---

## ⚙️ Installation

First, install the required dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install:

* **soundfile** → for audio compression (FLAC)
* **Pillow** → for image compression (JPEG)

> Note: `zipfile` and `os` are part of Python’s standard library, so no extra installation is needed.

---

## 🖼️ Image Compression (JPEG)

```python
def compress_PNG_image(input_path, output_path, quality):
    img = Image.open(input_path).convert("RGB")
    img.save(output_path, "JPEG", optimize=True, quality=quality)
```

* Converts the image to **JPEG** format.
* `quality` parameter controls compression (lower = smaller size but worse quality).
* Prints **original size, compressed size, and compression ratio**.

✅ Best for **photos and images** (lossy compression).

---

## 🎵 Audio Compression (FLAC)

```python
def compress_to_flac(input_audio, output_audio):
    data, samplerate = sf.read(input_audio)
    sf.write(output_audio, data, samplerate, format="FLAC")
```

* Reads an **uncompressed audio file** (like WAV).
* Saves it as **FLAC**, which is lossless but smaller.
* Prints original vs compressed size.

✅ Best for **music or audio recordings** where quality must be preserved.

---

## 📂 Folder Compression (ZIP)

```python
def compress_folder_to_zip(folder_path, output_zip):
    original_size = get_folder_size(folder_path)
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
```

* Walks through a folder and compresses **all files** into a `.zip`.
* Keeps folder structure.
* Prints **compression ratio**.

✅ Works for **any file type** (text, images, videos, etc.).

---

## 📂 Extracting a ZIP

```python
def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
```

* Extracts files from a ZIP archive into the target folder.

---

# 🔍 Example

Suppose your folder contains:

* `report.txt` → 2 MB → compresses to \~200 KB (text compresses well).
* `photo.jpg` → 3 MB → maybe compresses only to 2.9 MB (already compressed).
* `video.mp4` → 50 MB → stays almost the same (already compressed).

👉 **Total original size** = 55 MB
👉 **After ZIP** = \~53 MB (since video dominates).

✅ In short:

* **Yes, any file type can be zipped.**
* **Compression savings depend on the file type**:

  * Text shrinks a lot 📉
  * Media files (JPEG, MP4, MP3) barely shrink 📊