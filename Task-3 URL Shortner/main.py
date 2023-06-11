import tkinter as tk

import pyshorteners


def shorten_url():
    long_url = entry_url.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    entry_short_url.delete(0, tk.END)
    entry_short_url.insert(tk.END, short_url)


# Creating New window
window = tk.Tk()
window.title("URL Shortener - Python")

# Entry field
label_url = tk.Label(window, text="Enter the URL:-")
label_url.pack()

entry_url = tk.Entry(window, width=50)
entry_url.pack()

# Create Shorten button
button_shorten = tk.Button(window, text="Shorten URL", command=shorten_url)
button_shorten.pack()

# Short URL label and entry field
label_short_url = tk.Label(window, text="Shortened URL:-")
label_short_url.pack()

entry_short_url = tk.Entry(window, width=50)
entry_short_url.pack()

# Running GUI App
window.mainloop()
