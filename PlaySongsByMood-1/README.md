# PlaySongsByMood

## Overview
PlaySongsByMood is a web application that captures images from the user's webcam, analyzes the emotions detected in those images, and plays corresponding music based on the detected emotions. The application utilizes Flask for the web server, OpenCV for image processing, DeepFace for emotion detection, and Pygame for sound playback.

## Project Structure
```
PlaySongsByMood
├── app.py                # Main entry point of the web application
├── function.py           # Functions for emotion analysis and sound playback
├── requirements.txt      # Project dependencies
├── static
│   └── js
│       └── camera.js     # JavaScript for camera functionality
├── templates
│   └── index.html        # HTML template for the web application
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd PlaySongsByMood
   ```

2. **Install Dependencies**
   Make sure you have Python installed. Then, create a virtual environment and install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Start the Flask server:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Usage
- Open the web application in your browser.
- Allow access to your webcam when prompted.
- Capture an image by pressing the spacebar.
- The application will analyze the emotion from the captured image and play the corresponding music.

## Dependencies
- Flask
- OpenCV
- DeepFace
- Pygame

## License
This project is licensed under the MIT License.