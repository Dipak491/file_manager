import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from datetime import datetime
import csv

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("800x600")

        # File extension categories
        self.extension_filters = {
            "All Files": ["*.*"],
            "Music": [".mp3", ".wav", ".flac"],
            "Video": [".mp4", ".mkv", ".avi"],
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Archives": [".zip", ".rar", ".7z"],
            "Documents": [".pdf", ".docx", ".txt"]
        }

        self.current_directory = ""
        self.setup_ui()

    def setup_ui(self):
        # Top frame for controls
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=5, pady=5)

        # Browse button
        ttk.Button(control_frame, text="Browse Folder", command=self.browse_folder).pack(side=tk.LEFT)

        # Filter dropdown
        self.filter_var = tk.StringVar(value="All Files")
        filter_dropdown = ttk.Combobox(control_frame, textvariable=self.filter_var, 
                                     values=list(self.extension_filters.keys()), state="readonly")
        filter_dropdown.pack(side=tk.LEFT, padx=5)

        # Apply filter button
        ttk.Button(control_frame, text="Apply Filter", command=self.apply_filter).pack(side=tk.LEFT)

        # Export button
        ttk.Button(control_frame, text="Export List", command=self.export_list).pack(side=tk.RIGHT)

        # Current path label
        self.path_label = ttk.Label(self.root, text="No folder selected", wraplength=780)
        self.path_label.pack(fill=tk.X, padx=5)

        # Create treeview for file listing
        columns = ("Name", "Size", "Modified Date")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        
        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200)

        # Add scrollbars
        y_scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        x_scrollbar = ttk.Scrollbar(self.root, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)

        # Pack scrollbars and treeview
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Bind double-click event
        self.tree.bind("<Double-1>", self.open_file)

    def browse_folder(self):
        directory = filedialog.askdirectory()
        if directory:
            self.current_directory = directory
            self.path_label.config(text=directory)
            self.apply_filter()

    def get_file_size(self, file_path):
        size_bytes = os.path.getsize(file_path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.2f} TB"

    def apply_filter(self):
        if not self.current_directory:
            messagebox.showwarning("Warning", "Please select a folder first!")
            return

        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        selected_filter = self.filter_var.get()
        extensions = self.extension_filters[selected_filter]

        try:
            files = os.listdir(self.current_directory)
            for file in files:
                file_path = os.path.join(self.current_directory, file)
                if os.path.isfile(file_path):
                    # Check if file matches the selected filter
                    if selected_filter == "All Files" or any(file.lower().endswith(ext.lower()) for ext in extensions):
                        # Get file details
                        size = self.get_file_size(file_path)
                        modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                        
                        # Insert into treeview
                        self.tree.insert("", tk.END, values=(file, size, modified))
        except Exception as e:
            messagebox.showerror("Error", f"Error accessing folder: {str(e)}")

    def open_file(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        file_name = self.tree.item(selected_item[0])["values"][0]
        file_path = os.path.join(self.current_directory, file_name)

        try:
            os.startfile(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Error opening file: {str(e)}")

    def export_list(self):
        if not self.tree.get_children():
            messagebox.showwarning("Warning", "No files to export!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")]
        )

        if file_path:
            try:
                with open(file_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    # Write headers
                    headers = [self.tree.heading(col)["text"] for col in self.tree["columns"]]
                    writer.writerow(headers)
                    # Write data
                    for item in self.tree.get_children():
                        writer.writerow(self.tree.item(item)["values"])
                messagebox.showinfo("Success", "File list exported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error exporting file: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()