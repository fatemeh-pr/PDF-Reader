import os
import tkinter
import requests
import pypdf
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

API_URL = "https://api.voicerss.org/"
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise RuntimeError(
        "Environment variable API_KEY is not set.\n"
        "Get an api-key by signing up at 'https://www.voicerss.org'"
    )


def select_file():
    filepath = filedialog.askopenfilename(
        title="Select a Pdf File",
        filetypes=[("PDF File", "*.pdf")]
    )
    return filepath


def save_path():
    save_filepath = filedialog.asksaveasfilename(
        title="Choose the file destination.",
        filetypes=[("MP3", "*.mp3")],
        defaultextension=".mp3"
        )
    return save_filepath


def extract_text(reader):
    pages = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text is None:
            page_text = " "
        pages.append(" ".join(page_text.split()))
    text = " ".join(pages)
    return text


def get_audio(text):
    params = {"key": API_KEY,
            "src": text,
            "hl": "en-us",
            "v": "Amy",
            "r": 0,
            "c": "MP3",
            "f": "48khz_16bit_stereo"}
    try:
        response = requests.get(url=API_URL, params=params, timeout=30)
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None
    
    if response.status_code == 200:
        if response.text.startswith("ERROR"):
            print(response.text)
            return None
        else:
            return response.content
    else:
        print(response.status_code)
        print(response.reason)
        return None


def text_to_speech():
    print("Reading PDF...")
    filepath = select_file()
    if filepath:
        try:
            reader = pypdf.PdfReader(filepath)
        except pypdf.errors.PdfReadError:
            print("Please only choose a valid PDF file.")
            return
    else:
        print("Please choose a file.")
        return

    print("Extracting text...")
    text = extract_text(reader)
    if not text.strip():
        print("No readable text found in this PDF (it may be scanned/image-only)")
        return

    print("Generating speech...")
    content = get_audio(text)
    if content:
        print("Saving audio...")
        destination_path = save_path()
        if destination_path:
            with open(destination_path, mode="wb") as audio_file:
                audio_file.write(content)
                print("Done!")
        else:
            print("No path chosen. Audio saving failed.")
            return


if __name__ == "__main__":
    text_to_speech()
