# BQ-024 AI Email & Message Assistant

A Python console application that uses the Groq API to generate emails and messages from user-provided details.

## Features

- Professional Email
- Student Message
- Leave Application
- Formal Request
- Professional, Polite, and Friendly tones
- Input validation
- Generate again, create another message, or exit
- API errors are shown in a helpful way

## Requirements

- Python 3.10 or newer
- Internet connection
- Groq API key
- A currently supported Groq model ID

## Setup on Windows (VS Code)

1. Extract the ZIP file.
2. Open the extracted `BQ024_AI_Email_Message_Assistant` folder in VS Code.
3. Open **Terminal > New Terminal**.
4. Check that Python is installed:

   ```powershell
   python --version
   ```

5. Create a virtual environment:

   ```powershell
   python -m venv venv
   ```

6. Activate it in PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, you can use Command Prompt instead:

   ```cmd
   venv\\Scripts\\activate.bat
   ```

   Or, in PowerShell, allow activation only for the current terminal session:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\venv\Scripts\Activate.ps1
   ```

7. Install the required packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

8. Create your private settings file:
   - Make a copy of `.env.example`.
   - Rename the copy to `.env`.
   - Open `.env` and enter your Groq API key and a currently supported Groq model ID.

   Example format:

   ```env
   GROQ_API_KEY=put_your_key_here
   GROQ_MODEL=put_a_supported_model_id_here
   ```

   Keep your real API key private. Do not share `.env` or upload it to GitHub.

9. Run the application:

   ```powershell
   python main.py
   ```

## If Python is not recognized

Install Python from https://www.python.org/downloads/windows/ and select **Add python.exe to PATH** during installation. Close and reopen VS Code, then run:

```powershell
python --version
```

If `python` is not recognized, try `python3 --version`. Use the command that works in place of `python` in the setup steps.

## Project files

- `main.py` - console menu and application flow
- `prompts.py` - message categories, tones, and AI prompt
- `groq_service.py` - Groq API connection
- `requirements.txt` - required Python packages
- `.env.example` - example environment settings
- `.gitignore` - excludes secrets and temporary files

## Troubleshooting

- **Missing API key:** Make sure the file is named `.env` (not `.env.txt`) and contains `GROQ_API_KEY`.
- **Missing model:** Add a currently supported model ID to `GROQ_MODEL` in `.env`.
- **Package not found:** Activate the virtual environment and run `python -m pip install -r requirements.txt`.
- **API error:** Check your internet connection, API key, model ID, and Groq account limits.

## Safety

Never put your real API key in source code, screenshots, public messages, or GitHub. The `.env` file is ignored by Git.
