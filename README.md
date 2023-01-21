# MIDI2SCORE

MIDI2SCORE is a Python script that allows you to transcribe multi-track MIDI files into properly scored sheet music. The script uses the `music21` library to parse MIDI files and extract individual tracks, notes, and chords. Each track is then scored based on the detected instruments and displayed in sheet music format.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- `music21` library

You can install the `music21` library by running `pip install music21` in the command line.

### Installing

## 1. Clone the repository to your local machine using git or download the ZIP file
```sh
git clone https://github.com/<your-username>/MIDI2SCORE.git
```
## 2. Navigate to the repository directory
```sh
cd MIDI2SCORE
```
## 3. Run the script
```sh
python midi2score.py <midi_file_path>
```
This will load the specified MIDI file, extract the individual tracks, notes, and chords, score the notes based on the detected instruments and display the sheet music.

### Examples
Here are some examples of how to use the script:

```sh
python midi2score.py sample.mid
```
This will transcribe the notes of the MIDI file "sample.mid" and display the sheet music for each track

```sh
python midi2score.py sample1.mid sample2.mid
```
This will transcribe the notes of the MIDI files "sample1.mid" and "sample2.mid" and display the sheet music for each track

## Built With
* Python - Programming language
* music21 - Python library for computer-aided musical analysis

## Contributing
If you would like to contribute to the project, please fork the repository, make your changes and create a pull request.

Authors
Your name - Initial work
License
This project is licensed under the MIT License - see the LICENSE.md file for details

Acknowledgments
[music21
