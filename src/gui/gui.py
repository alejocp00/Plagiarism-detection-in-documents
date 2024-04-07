
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from src.code.plagio_detector import detect_plagiarism

# Create a GUI window
window = tk.Tk()
window.title("Plagiarism Detection")

# Create a frame for the content
content_frame = tk.Frame(window)
content_frame.grid(column=0, row=0, padx=20, pady=20)

# Create labels for Text 1 and Text 2
text_area1_label = tk.Label(content_frame, text="Text 1:")
text_area1_label.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
text_area2_label = tk.Label(content_frame, text="Text 2:")
text_area2_label.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W)

# Create two text areas for input texts
text_area1 = scrolledtext.ScrolledText(content_frame, width=50, height=10)
text_area1.grid(column=0, row=1, padx=10, pady=5, sticky='w')
text_area2 = scrolledtext.ScrolledText(content_frame, width=50, height=10)
text_area2.grid(column=1, row=1, padx=10, pady=5, sticky='w')

# Create a button to trigger the plagiarism detection function
text1 =text_area1.get("1.0", tk.END)
text2 =text_area2.get("1.0", tk.END)
button = tk.Button(content_frame, text="Detect Plagiarism", command=detect_plagiarism(text1, text2))
button.grid(column=0, row=2, columnspan=2, pady=10)

# Create a label to display the similarity score
similarity_score_label = tk.Label(content_frame, text="", font=("Arial", 12))
similarity_score_label.grid(column=0, row=3, columnspan=2, pady=5)

window.mainloop()