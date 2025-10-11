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

class CheckboxDialog(ctk.CTkToplevel):
    def __init__(
        self,
        master,
        title="Select Options",
        description="Select your options:",
        options=None,
        checked_states=None,
        width=300,
        height=400,
    ):
        super().__init__(master)
        self.title(title)
        self.resizable(False, False)
        self.geometry(f"{width}x{height}")
        self.grab_set()   # lock focus
        self.focus()
        self.protocol("WM_DELETE_WINDOW", self.on_cancel)

        self.result = None
        self.check_vars = []

        # Default fallbacks
        if options is None:
            options = [f"Option {i+1}" for i in range(10)]
        if checked_states is None or len(checked_states) != len(options):
            checked_states = [False] * len(options)

        # Outer Frame
        outer_frame = ctk.CTkFrame(self)
        outer_frame.pack(padx=10, pady=10, fill="both", expand=True)

        ctk.CTkLabel(
            outer_frame,
            text=description,
            font=("Arial", 13, "bold")
        ).pack(pady=(5,8))

        # Scrollable checkboxes for smaller window
        scroll_frame = ctk.CTkScrollableFrame(outer_frame)
        scroll_frame.pack(fill="both", expand=True, pady=(0,8))

        # Method 1: Patches can be applied any time, each patch also have
        # Checks to determine whether patch have to be processed or not
        for state, opt in zip(checked_states, options):
            var = ctk.BooleanVar(value=state)
            chk = ctk.CTkCheckBox(scroll_frame, text=opt, variable=var)
            chk.pack(anchor="w", pady=2, padx=5)
            self.check_vars.append(var)
        
        # Method 2: Check for Applied patch; then lock in the option
        # This implementation make use of writing data into .sav file
        # for i, (state, opt) in enumerate(zip(checked_states, options)):
        #     var = ctk.BooleanVar(value=state)
        # 
        #     def on_toggle(index=i, var=var):
        #         # Prevent changing from True → False
        #         if checked_states[index] and not var.get():
        #             var.set(True)
        # 
        #     chk = ctk.CTkCheckBox(scroll_frame, text=opt, variable=var, command=on_toggle)
        #     chk.pack(anchor="w", pady=2, padx=5)
        #     self.check_vars.append(var)


        # Buttons
        btn_frame = ctk.CTkFrame(outer_frame, fg_color="transparent")
        btn_frame.pack(pady=5)

        ok_btn = ctk.CTkButton(btn_frame, text="OK", width=80, command=self.on_ok)
        cancel_btn = ctk.CTkButton(btn_frame, text="Cancel", width=80, fg_color="gray", command=self.on_cancel)

        ok_btn.pack(side="left", padx=8)
        cancel_btn.pack(side="right", padx=8)

        # Keyboard Bindings
        self.bind("<Return>", lambda e: self.on_ok())
        self.bind("<Escape>", lambda e: self.on_cancel())

        self.wait_window()  # Block until window is closed/destroyed

    # Retval == bool states for each checkboxes
    def on_ok(self):
        self.result = [var.get() for var in self.check_vars]
        self.destroy()

    # Retval == None
    def on_cancel(self):
        self.result = None
        self.destroy()

# Functions
def bool_list_to_int(bool_list: list) -> int:
    # Convert list of bools to int. Index 0 LSB
    result = 0
    for i, bit in enumerate(bool_list):
        if bit:
            result |= (1 << i)
    return result


def int_to_bool_list(value: int, length=None) -> list:
    # Convert int to list of bools. Index 0 is LSB
    # If length given, list will be padded/truncated
    bool_list = []
    while value > 0:
        bool_list.append(bool(value & 1))
        value >>= 1

    if length is not None:
        # Pad or truncate to match desired length
        bool_list = (bool_list + [False] * length)[:length]
    return bool_list