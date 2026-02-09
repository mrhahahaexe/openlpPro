# 🚀 OpenLP Pro: Next-Gen Church Presentation

**OpenLP Pro** is a high-performance, feature-rich fork of the open-source church presentation software. It is specifically engineered to eliminate downtime and maximize efficiency during live services.

## ✨ "Pro" Feature Deep Dive

### 📖 Bible Plugin: The "Fast" Tab
The **Fast Tab** is the crown jewel of OpenLP Pro. It replaces traditional clicking with a ultra-responsive command-line style search.
*   **Dynamic Auto-Search**: As you type, the results populate instantly. Typing `gen`, then a space, then `1` will progressively load Genesis and then Genesis 1.
*   **Shorthand Genius**: Supports rapid-fire shorthand. `jam 3 1` instantly resolves to James 3:1. No more colons required.
*   **Instant Projection**: Pressing **Enter** immediately projects the top result to the live screen, allowing you to follow a speaker's spontaneous scripture references in real-time.

### � Redesigned Bible Selection UI (Searchable Input)
The standard "Select" tab has been completely redesigned for speed.
*   **Searchable Book Field**: Instead of scrolling through 66 books in a dropdown, the Book field is now an **input field with auto-completion**. Simply type `Mat` and hit tab.
*   **SpinBox Logic**: Chapter and Verse selection use sleek numeric spinboxes instead of dropdowns, allowing for much faster adjustment via keyboard or mouse wheel.

### 🎵 Songs Plugin: Integrated Web Search
Never be caught without lyrics again.
*   **Live Web Fetching**: A dedicated "Web Search" tab connects directly to online lyric databases (via Genius API).
*   **Automatic Formatting**: Fetches, cleans, and formats lyrics into verses and choruses automatically, letting you project a new song in seconds without manual copy-pasting.

### 📱 Bridged AI Song Recognition (The Android Bridge)
This is an expert-level integration that uses an Android device as a hardware bridge to Google's world-class AI.
*   **Google AI Power**: The system triggers your Android phone to listen to live audio using the Google Assistant's "What's this song?" feature.
*   **OCR Title Scraping**: OpenLP Pro captures the phone's screen, uses high-accuracy OCR (Optical Character Recognition) to scrape the Song Title and Artist from the Assistant result, and automatically fetches the lyrics on your PC.
*   **Seamless Bridge**: Bridged via ADB (Android Debug Bridge) for zero-latency control.

---

## � Setup & Technical Configuration

### 💻 PC Setup
1.  **Dependencies**: Install Python 3.12 and run `pip install -e .`.
2.  **External Tools**: Install `Tesseract OCR` on your PC and add it to your System PATH (required for song recognition).
3.  **Environment**: Create a `.env` file in the root directory with your `ADB_PATH` and other configuration options.

### � Phone Setup (The Android Bridge)
To use the AI Song Recognition feature, your Android phone must be configured as follows:
1.  **Enable Developer Options**: Go to Settings > About Phone > Tap "Build Number" 7 times.
2.  **USB Debugging**: Enable "USB Debugging" in Developer Options and connect your phone to the PC via USB.
3.  **Preferred AI**: Ensure **Google Assistant** is set as your default "Digital Assistant App".
4.  **Input Method**: The phone's default keyboard must be set to a standard input method (e.g., Gboard) that supports Google Assistant triggering.
5.  **Always-on Display**: It is recommended to keep the screen from sleeping while in the booth.

### 🔨 Building & Distribution

#### 1. Compile UI Resources
OpenLP uses compiled resources for icons. Run this if you've changed any images:
```powershell
pyside6-rcc -g python -o openlp/core/resources.py resources/images/openlp-2.qrc
```

#### 2. Create Standalone Bundle (PyInstaller)
This creates a folder in `dist/OpenLP-Custom` containing the executable and all libraries.
```powershell
pyinstaller --noconfirm openlp_build.spec
```

#### 3. Create Windows Installer (Inno Setup)
To create the `OpenLP_Pro_Setup.exe` file for easy installation:
1.  Download and install **Inno Setup**.
2.  Open `openlp_installer.iss` in the Inno Setup Compiler.
3.  Press **Build > Compile** (F9).
4.  Find your installer in the `installer_output` folder.

#### 🚀 How to Publish Updates to GitHub
If you've made changes and want to save them to your repository:
```powershell
# 1. Stage all changes
git add .

# 2. Commit with a descriptive message
git commit -m "Fixed theme loading and generic icon issues"

# 3. Push to GitHub
git push origin master
```

---
*OpenLP Pro: Because every second counts in live worship.*
