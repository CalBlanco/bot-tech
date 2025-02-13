import tkinter as tk
import json
from tkinter import ttk

class TextAnnotator:
    def __init__(self, config_or_config_path):
        self.root = tk.Tk()
        self.root.title("Text Annotator")


        if isinstance(config_or_config_path, str):
        # Load config
            with open(config_or_config_path) as f:
                self.config = json.load(f)
        else:
            self.config = config_or_config_path

        # Main components
        self.text_display = tk.Text(self.root, height=10, width=60)
        self.text_display.pack(pady=10)
        
        # Label frame for each annotation type
        self.label_vars = {}
        for label_type, options in self.config['labels'].items():
            frame = ttk.LabelFrame(self.root, text=label_type)
            frame.pack(pady=5, padx=10, fill="x")
            
            # Create radio buttons for each option
            self.label_vars[label_type] = tk.StringVar()
            for option in options:
                ttk.Radiobutton(frame, text=option, 
                              variable=self.label_vars[label_type],
                              value=option).pack(side=tk.LEFT, padx=5)
        
        # Navigation buttons
        ttk.Button(self.root, text="Next", command=self.next_item).pack(pady=5)

    def next_item(self):
        # Save current annotations and load next item
        pass

    def run(self):
        self.root.mainloop()