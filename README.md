# Eye Controlled Keyboard & Mouse

An innovative assistive technology application that allows users to control their computer using eye movements and blinks. This project combines computer vision, facial landmark detection, and voice recognition to create a hands-free computing experience.

## 🌟 Features

### Core Functionality
- **Eye Tracking**: Real-time iris tracking for precise cursor movement
- **Virtual Keyboard**: On-screen keyboard with QWERTY layout for text input
- **Blink Detection**: Multiple blink patterns for different actions
- **Mouse Control**: Full mouse functionality including clicking and dragging
- **Voice Commands**: Speech recognition for program control

### Input Methods
- **Single Blink**: Left mouse click or type selected key
- **Double Blink**: Right mouse click
- **Long Blink (0.5s+)**: Toggle mouse drag mode
- **Voice Commands**: "start" to begin, "exit"/"stop" to quit

### Keyboard Layout
```
1234567890
QWERTYUIOP
ASDFGHJKL
ZXCVBNM
.,?!
[SPACE] [BACK]
```

### Visual Feedback
- Real-time eye position indicator (red circle)
- Keyboard key highlighting when hovering
- Live text display showing typed content
- Smooth cursor movement with configurable smoothing

## 🎥 Demo Video

Watch the Eye Controlled Keyboard & Mouse in action:

[![Eye Keyboard Demo](https://drive.google.com/file/d/1n0TE9eLbCky5ErIZBrARGGVy3Zf01vBv/view?usp=sharing)](https://drive.google.com/file/d/1RZJjnm8A6VP5p8rg2Ee4vct_z8gGiEMX/view?usp=sharing)

*Click the image above to watch the demonstration video*

### What the Demo Shows:
- Real-time eye tracking and cursor movement
- Virtual keyboard interaction
- Blink detection for typing and clicking
- Voice command functionality
- Complete workflow from setup to text output

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Webcam (built-in or external)
- Microphone (for voice commands)

### Dependencies
Install the required packages:

```bash
pip install -r requirements.txt
```

### Required Libraries
- `opencv-python` - Computer vision and camera interface
- `mediapipe` - Facial landmark detection
- `pyautogui` - Mouse and keyboard automation
- `SpeechRecognition` - Voice command processing
- `pyaudio` - Audio input handling

## 📖 Usage

### Starting the Application
1. Run the main script:
   ```bash
   python eye_keyboard.py
   ```

2. A GUI window will appear with two buttons:
   - **Start Eye Keyboard**: Begins the eye tracking system
   - **Stop & Exit**: Safely closes the application

### Voice Commands
The application continuously listens for voice commands:
- Say **"start"** to begin eye tracking
- Say **"exit"** or **"stop"** to quit the program

### Eye Control Instructions
1. **Position your face** in front of the webcam
2. **Look at keys** on the virtual keyboard to highlight them
3. **Blink once** to type the highlighted key or click
4. **Blink twice quickly** for right-click
5. **Hold blink for 0.5+ seconds** to toggle drag mode

### Output
- Typed text is displayed in real-time on the camera feed
- Final text is automatically saved to `typed_output.txt` when exiting

## ⚙️ Configuration

### Adjustable Parameters
You can modify these variables in the code for customization:

```python
# Smoothing factor for cursor movement (0.1-0.5 recommended)
smooth_factor = 0.2

# Blink detection sensitivity
blink_interval = 0.5
long_blink_threshold = 0.5

# Face detection confidence
min_detection_confidence = 0.5
min_tracking_confidence = 0.5
```

## 🎯 Use Cases

### Accessibility
- **Motor Disabilities**: For users with limited hand/arm mobility
- **ALS/MND Patients**: Assistive communication device
- **Temporary Injuries**: Hands-free computing during recovery
- **Ergonomic Issues**: Reduce repetitive strain injuries

### Specialized Applications
- **Gaming**: Hands-free game control
- **Presentations**: Remote slide navigation
- **Art/Design**: Precise cursor control for digital art
- **Education**: Interactive learning tools

## ⚠️ Limitations

### Technical Limitations
- **Lighting Dependency**: Requires good lighting conditions
- **Face Angle**: Works best with face directly facing camera
- **Calibration**: May need adjustment for different users
- **Latency**: Slight delay in response (50-100ms typical)

### Hardware Requirements
- **Webcam Quality**: Higher resolution cameras provide better accuracy
- **Processing Power**: Requires moderate CPU for real-time processing
- **Internet Connection**: Voice recognition requires internet access

### Accuracy Constraints
- **Eye Tracking**: ±5-10 pixel accuracy depending on setup
- **Blink Detection**: May have false positives in bright environments
- **Voice Recognition**: Background noise can interfere with commands

### Known Issues
- **Multiple Faces**: Only tracks the first detected face
- **Glasses/Contacts**: May affect tracking accuracy
- **Screen Resolution**: Cursor mapping may need adjustment for high-DPI displays

## 🔧 Troubleshooting

### Common Problems

**Eye tracking not working:**
- Ensure good lighting on your face
- Check webcam permissions
- Verify face is centered in camera view

**Blink detection issues:**
- Adjust `long_blink_threshold` value
- Ensure eyes are fully visible
- Check for reflections on glasses

**Voice commands not responding:**
- Verify microphone permissions
- Check internet connection
- Speak clearly and wait for processing

**Cursor movement is jumpy:**
- Increase `smooth_factor` value
- Ensure stable camera position
- Check for camera shake or vibration

### Performance Optimization
- Close unnecessary applications
- Use a dedicated webcam (not built-in if possible)
- Ensure adequate lighting
- Position camera at eye level

## 🛡️ Privacy & Security

### Data Handling
- **No Data Storage**: No personal data is permanently stored
- **Local Processing**: Eye tracking happens locally on your device
- **Voice Recognition**: Uses Google's cloud service (requires internet)
- **Output Files**: Only saves typed text to local file

### Recommendations
- Use in private environments when possible
- Be aware of voice command processing through cloud services
- Regularly delete output files if they contain sensitive information

## 🔮 Future Enhancements

### Planned Features
- **Customizable Keyboard Layouts**: Support for different languages
- **Gesture Recognition**: Additional hand/head gestures
- **Machine Learning**: User-specific calibration and improvement
- **Multi-Monitor Support**: Enhanced screen mapping
- **Accessibility Modes**: High contrast, larger keys, audio feedback

### Potential Improvements
- **Wireless Camera Support**: Bluetooth/USB camera integration
- **Mobile App**: Smartphone camera as input device
- **Cloud Integration**: Text-to-speech and cloud storage
- **Gaming Modes**: Specialized controls for different games

## 📄 License

This project is open source. Please check the license file for specific terms and conditions.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes
- Feature enhancements
- Documentation improvements
- Accessibility improvements

## 📞 Support

For technical support or questions:
- Open an issue on the project repository
- Check the troubleshooting section above
- Review the code comments for implementation details

## 🙏 Acknowledgments

- **MediaPipe**: Google's machine learning framework for face detection
- **OpenCV**: Computer vision library for image processing
- **PyAutoGUI**: Cross-platform GUI automation
- **SpeechRecognition**: Python speech recognition library

---

**Note**: This application is designed as an assistive technology tool. For medical or professional use, please consult with appropriate healthcare or accessibility professionals.
