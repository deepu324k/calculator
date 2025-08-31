# Simple Visual Calculator

A basic calculator application with both a web interface and a Python Flask backend. This project demonstrates how to create a simple calculator using HTML, CSS, JavaScript, and Python.

## Project Structure

- `calculator.html` - The main web interface for the calculator
- `app.py` - Flask backend server that can handle calculations 
- `.vscode/` - VS Code configuration folder

## Features

- **Visual Calculator Interface**: Clean, modern design with number and operator buttons
- **Basic Math Operations**: Addition (+), subtraction (-), multiplication (×), division (÷)
- **Additional Functions**: 
  - All Clear (AC) to reset the calculator
  - Percentage (%) calculations
  - Decimal point support
- **Dark Mode Support**: Automatically adapts to your system's theme
- **Responsive Design**: Works on both desktop and mobile devices

## How to Use

### Option 1: Simple Web Calculator (HTML Only)
1. Simply open `calculator.html` in any web browser
2. Click the buttons to perform calculations
3. No additional setup required!

### Option 2: With Flask Backend (Advanced)
If you want to use the Python backend:

1. **Install Requirements**:
   ```
   pip install flask flask-cors
   ```

2. **Run the Backend**:
   ```
   python app.py
   ```

3. **Open the Calculator**:
   - Open `calculator.html` in your browser
   - The calculator will now use the Python backend for calculations

## File Explanations

### calculator.html
- Contains the complete calculator interface
- Uses Tailwind CSS for modern styling
- Has JavaScript code that handles button clicks and calculations
- Can work independently without the Python backend

### app.py
- A simple Flask web server
- Provides a `/calculate` endpoint that accepts math expressions
- Returns calculation results in JSON format
- Includes basic error handling for invalid calculations

## Technical Details

- **Frontend**: HTML5, CSS3 (Tailwind), Vanilla JavaScript
- **Backend**: Python Flask with CORS support
- **Styling**: Uses Tailwind CSS framework and Google Fonts (Inter)
- **Calculations**: Uses JavaScript's `eval()` function (frontend) and Python's `eval()` (backend)

## Notes for Students

- This is a beginner-friendly project that shows basic web development concepts
- The code includes helpful comments explaining what each part does
- The calculator handles common errors like division by zero
- The design follows modern web standards and responsive design principles

## Safety Note

This calculator uses `eval()` for simplicity, which is generally not recommended for production applications due to security concerns. For learning purposes, this is acceptable since the input comes only from the calculator buttons.

## Getting Started

1. Download or clone this project
2. Open `calculator.html` in your web browser
3. Start calculating!

For the Flask backend version, make sure you have Python installed and follow the Flask setup instructions above.
