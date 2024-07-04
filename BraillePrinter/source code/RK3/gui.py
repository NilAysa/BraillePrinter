import tkinter as tk
import threading

class BraillePrinterGUI:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(BraillePrinterGUI, cls).__new__(cls)
            return cls._instance
    
    def __init__(self, f):
        if hasattr(self, "_initialized") and self._initialized:
            return
        self._initialized = True
        
        
        self.root = tk.Tk()
        self.root.title("Braille Printer")
        
        self.f = f
        
        self.textBox = tk.Text(self.root, height = 20, width = 60)
        self.textBox.pack(pady = 10)
        
        self.printButton = tk.Button(self.root, text = "Print", command = self.onButtonClick)
        self.printButton.pack(pady = 10)

        self.printState = tk.Label(self.root, text = "Send text to Braille Printer")
        self.printState.pack(pady = 10)
        
        self.root.mainloop()
        
        
    def onButtonClick(self):
        self.printState.config(text = "Text sent to Braille Printer")
        self.printButton.config(state = tk.DISABLED)
        self.textBox.config(state = tk.DISABLED)
        threading.Thread(target = self.run).start()
        
        
    def run(self):
        self.printState.config(text = "Printing...")
        text = self.textBox.get('1.0', tk.END).strip()
        self.f(text)
        
        self.textBox.config(state = tk.NORMAL)
        self.textBox.delete("1.0", tk.END)
        self.printState.config(text = "Send text to Braille Printer")
        self.printButton.config(state = tk.NORMAL)
        