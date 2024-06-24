# PixelTap Auto Combatv2 Script

This project automates certain tasks within a game by detecting specific images on the screen and performing actions such as clicking and keyboard inputs. The script uses computer vision to locate elements and control the game through automation libraries.

## Features

- **Image Detection**: Detects various images on the screen using `pyautogui`.
- **Automated Clicking**: Automatically clicks on detected areas.
- **Keyboard Interaction**: Listens for specific keyboard inputs to control the script.
- **Logging**: Provides detailed logging for monitoring the script's activity.

## Installation

To get started with this project, you need to have Python installed. Then, you can install the required dependencies using pip and set up a virtual environment.

### Virtual Environment Setup

1. **Create a Virtual Environment**: 
    ```sh
    python -m venv venv
    ```

2. **Activate the Virtual Environment**:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. **Install Dependencies**:
    ```sh
    pip install opencv-python numpy pyautogui keyboard
    ```

4. **Deactivate the Virtual Environment** (when done):
    ```sh
    deactivate
    ```

## Usage

1. **Configure Image Paths and Parameters**: Update the image paths and other parameters in the script as needed.
2. **Set Up BlueStacks 5**: Ensure BlueStacks 5 is running with a resolution of 900x1600 and 240 DPI.
3. **Run the Script**: Execute the script using Python.

```sh
python combat2.py
```

3. **Control the script**
 - Press space to pause/resume the script.

 - Press esc to exit the script.

## Project Structure
```sh
.
├── images2
│   ├── fight.PNG
│   ├── random.PNG
│   ├── newgame.PNG
│   ├── starting.PNG
│   ├── share.PNG
│   ├── superkick.PNG
│   ├── sword.PNG
│   ├── shield.PNG
│   ├── end.PNG
│   ├── time1.PNG
│   ├── time2.PNG
├── combat2.py
├── README.md
└── venv
```

## How It Works

- **Screen Capture**: The script captures the screen to find specific elements.
- **Color Detection**: Detects a pink circle on the screen using HSV color space and contours.
- **Image Matching**: Matches predefined images on the screen to trigger clicks and other actions.

### Example Functions

- `capture_screen(region=None)`: Captures a screenshot of the specified region.
- `find_pink_circle(frame)`: Detects a pink circle in the provided frame.
- `click_pink_circle()`: Clicks on the detected pink circle.
- `find_and_click_image(image_path, confidence=0.8)`: Finds and clicks on the specified image if found on the screen.


## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact [Through Email](mailto:onurcangencbilkent@gmail.com).

Follow me on social media:
- Instagram: [@onurcan.gnc](https://www.instagram.com/onurcan.gnc/)
- Twitter: [@onurcangenc1999](https://x.com/onurcangenc1999)

---

Thank you for using this script ! 
Enjoy automating your game !







