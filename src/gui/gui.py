import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from src.code.plagio_detector import Plagiarism


class Gui:
    def __init__(self) -> None:

        # Create a GUI window
        self.window = tk.Tk()
        self.window.title("Plagiarism Detection")

        # Create a frame for the content
        self.content_frame = tk.Frame(self.window)
        self.content_frame.grid(column=0, row=0, padx=20, pady=20)

        # Create labels for Text 1 and Text 2
        self.text_area1_label = tk.Label(self.content_frame, text="Original text:")
        self.text_area1_label.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
        self.text_area2_label = tk.Label(
            self.content_frame, text="Possible plagiarism text:"
        )
        self.text_area2_label.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W)

        # Create two text areas for input texts
        self.text_area1 = scrolledtext.ScrolledText(
            self.content_frame, width=50, height=10
        )
        self.text_area1.grid(column=0, row=1, padx=10, pady=5, sticky="w")
        self.text_area2 = scrolledtext.ScrolledText(
            self.content_frame, width=50, height=10
        )
        self.text_area2.grid(column=1, row=1, padx=10, pady=5, sticky="w")

        # Create a button to trigger the plagiarism detection function
        self.detect_button = tk.Button(
            self.content_frame,
            text="Detect Plagiarism",
            command=self._detect_plagiarism,
        )
        self.detect_button.grid(column=0, row=2, columnspan=2, pady=10)

        # Create a label to display the similarity score
        self.similarity_score_label = tk.Label(
            self.content_frame, text="", font=("Arial", 12)
        )
        self.similarity_score_label.grid(column=0, row=3, columnspan=2, pady=5)

        # Create a button to show the most similar part of the texts
        self.show_similar_button = tk.Button(
            self.content_frame,
            text="Show most similar part",
            command=self._show_most_similar_part,
        )
        self.show_similar_button.grid(column=0, row=4, columnspan=2, pady=10)

    def _show_most_similar_part(self):
        """Show the most similar part of the two input texts."""
        text1 = self.text_area1.get("1.0", tk.END)
        text2 = self.text_area2.get("1.0", tk.END)

        similarity_percentage = self.plagiarism.most_similar_path()

        messagebox.showinfo(
            "Plagiarism Detection",
            f"The most similar text is: {similarity_percentage}",
        )

    def _detect_plagiarism(self):
        """Detect plagiarism between the two input texts."""
        self.plagiarism = Plagiarism()

        text1 = self.text_area1.get("1.0", tk.END)
        text2 = self.text_area2.get("1.0", tk.END)

        similarity_percentage = self.plagiarism.detect_plagiarism(text1, text2)

        self.similarity_score_label.config(text=f"Similarity: {similarity_percentage}%")

        messagebox.showinfo(
            "Plagiarism Detection",
            f"The similarity between the two texts is {similarity_percentage}%",
        )

    def run(self):
        # Run the GUI
        self.window.mainloop()
