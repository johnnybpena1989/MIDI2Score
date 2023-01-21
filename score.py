import music21

def transcribe_midi(file_path):
    # Load the MIDI file
    midi = music21.converter.parse(file_path)
    
    # Extract individual tracks
    tracks = music21.midi.translate.midiFileToStream(midi)
    for i, track in enumerate(tracks):
        # Extract notes and chords from track
        notes_chords = track.flat.notes
        # Score the notes based on detected instruments
        score = music21.stream.Score()
        score.insert(0, music21.instrument.fromString(track.getInstrument().midiProgram))
        score.append(notes_chords)
        # Print the sheet music
        score.show()

# Test the function with a sample MIDI file
transcribe_midi('sample.mid')