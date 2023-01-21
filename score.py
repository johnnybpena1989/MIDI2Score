import music21

def transcribe():
    filepath = file_entry.get()
    if not filepath:
        messagebox.showerror("Error", "Please select a file to transcribe")
        return
    if not os.path.isfile(filepath):
        messagebox.showerror("Error", "Invalid file path")
        return
    output_dir = output_entry.get()
    if not output_dir:
        messagebox.showerror("Error", "Please specify an output directory")
        return
    if not os.path.isdir(output_dir):
        messagebox.showerror("Error", "Invalid output directory")
        return
    from music21 import *
    s = converter.parse(filepath)
    for part in s.parts:
        fp = os.path.join(output_dir, f"{part.id}.pdf")
        part.show(fp=fp)
    messagebox.showinfo("Success", "File transcribed and exported successfully")
