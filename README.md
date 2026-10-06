# PDF Reader

**A Python application that converts PDF text to speech.**

## Project Structure
- `main.py` - Runs the program.

## Features
- Uses [VoiceRSS](https://www.voicerss.org/) API for the conversion.
- Saves the speech in a `.mp3` file.
- Uses `tkinter.filedialog` to let the user select the PDF file and then where to save the `.mp3` file.
- Shows messages during the operation to inform the user about the process.

## Limitations
- The application can only process PDFs whose extracted text fits within the [VoiceRSS](https://www.voicerss.org/) API's request limit. Longer PDFs may not be converted successfully.
- Scanned PDFs or PDFs containing primarily images may not produce usable text because the application relies on text extraction rather than OCR.

## Concepts Practiced
- Working with APIs.
- Using file dialogs to interact with the user.
- Handling API request errors.
- Informing the user about the process using print statements.

## Technologies
- Python 3.13
- tkinter
- pypdf
- requests
- `os` module

## Configuration
The application requires a VoiceRSS API key to run.
Get an API key by signing up at [VoiceRSS](https://www.voicerss.org/)
Then set the API_KEY as an environment variable:
```bash
# Windows (Powershell)
$env:API_KEY = "your-api-key"
```
```bash
# Windows (cmd)
set API_KEY=your-api-key
```
```bash
# macOS/Linux
export API_KEY="your-api-key"
```

### How to Run
Set the `API_KEY` environment variable (see [Configuration](#configuration)).
Then run the application:
```bash
python main.py
```
A `sample.pdf` is included to test with, and `sample_output.mp3` is an example of the output it produces.