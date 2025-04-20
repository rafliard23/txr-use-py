import tkinter as tk
import customtkinter as ctk

class ToolTip:
    def __init__(self, widget, text, delay=500) -> None:
        self.widget = widget
        self.text = text
        self.delay = delay
        self.tip_window = None
        self.id = None
        self.widget.bind("<Enter>", self.schedule_tip)
        self.widget.bind("<Leave>", self.hide_tip)
        self.widget.bind("<ButtonPress>", self.hide_tip)

    def schedule_tip(self, event=None) -> None:
        # Schedule the tooltip to appear after delay
        self.unschedule()
        self.id = self.widget.after(self.delay, self.show_tip)

    def unschedule(self) -> None:
        # Cancel scheduled tooltip
        if self.id:
            self.widget.after_cancel(self.id)
            self.id = None

    def show_tip(self, event=None) -> None:
        # Display text in tooltip window
        if self.tip_window or not self.text:
            return
            
        # Get mouse position relative to screen
        x = self.widget.winfo_pointerx() + 10
        y = self.widget.winfo_pointery() + 10
        
        # Create tooltip window
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        
        # Use CustomTkinter styling
        frame = ctk.CTkFrame(tw, corner_radius=5)
        frame.pack()
        
        label = ctk.CTkLabel(
            frame, 
            text=self.text,
            bg_color='#ffffe0',
            text_color='black',
            justify="left",
            wraplength=400,
            padx=5,
            pady=5
        )
        label.pack()

    def hide_tip(self, event=None) -> None:
        # Hide the tooltip
        self.unschedule()
        if self.tip_window:
            self.tip_window.destroy()
        self.tip_window = None