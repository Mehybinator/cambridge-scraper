from tkinter import filedialog
from pydub import AudioSegment
from bs4 import BeautifulSoup
import customtkinter as ctk
from io import BytesIO
import threading
import requests
import settings
import sys
import os

scrape_urls = "https://dictionary.cambridge.org/dictionary/english/"
media_url = "https://dictionary.cambridge.org"
headers = {"User-Agent": settings.user_agent}
silence = AudioSegment.silent(duration=700)

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        if hasattr(sys, '_MEIPASS'):
            icon_path = os.path.join(sys._MEIPASS, "favicon.ico")
        else:
            icon_path = os.path.abspath("favicon.ico")

        self.iconbitmap(icon_path)
        self.title("Dictionary Voice Scraper")
        self.geometry("700x400")
        self.resizable(False, False)

        lbl1 = ctk.CTkLabel(self, font=("Tektur", 22), text="Welcome To Dictionary Voice Scraper")
        lbl2 = ctk.CTkLabel(self, font=("Tektur", 18), text="All You Have To Do Is Choose A Download Location And Your Words File!")
        lbl1.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
        lbl2.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

        self.lbl_dl_directory = ctk.CTkLabel(self, font=("Tektur", 13), bg_color="gray", text="Select A Download Directory!", padx=10)
        self.lbl_words_file = ctk.CTkLabel(self, font=("Tektur", 13), bg_color="gray", text="Select Your Source File!", padx=10)
        self.lbl_dl_directory.place(relx=0.1, rely=0.4, anchor=ctk.W)
        self.lbl_words_file.place(relx=0.1, rely=0.5, anchor=ctk.W)

        self.btn_get_dl_directory = ctk.CTkButton(self, text="Browse", command=self.get_directory, corner_radius=0, font=("Tektur", 13))
        self.btn_get_words_file = ctk.CTkButton(self, text="Browse", command=self.get_words_file, corner_radius=0, font=("Tektur", 13))
        self.btn_get_dl_directory.place(relx=0.8, rely=0.4, anchor=ctk.CENTER)
        self.btn_get_words_file.place(relx=0.8, rely=0.5, anchor=ctk.CENTER)

        self.btn_start = ctk.CTkButton(self, text="Initiate!", corner_radius=0, font=("Tektur", 13), command=self.run)
        self.btn_start.place(relx=0.5, rely=0.65, anchor=ctk.CENTER)

        self.btn_exit = ctk.CTkButton(self, text="Exit!", corner_radius=0, font=("Tektur", 13), command=sys.exit)
        self.btn_exit.place(relx=0.8, rely=0.65, anchor=ctk.CENTER)

        self.txt_box_log = ctk.CTkTextbox(self, font=("Tektur", 13), corner_radius=0, height=150)
        self.txt_box_log.place(relx=0.2, rely=0.77, anchor=ctk.CENTER)

        self.progress = ctk.CTkProgressBar(self, width=350)
        self.progress.set(0)
        self.progress.place(relx=0.65, rely=0.84, anchor=ctk.CENTER)

    def get_directory(self):
        settings.download_location = filedialog.askdirectory()
        self.lbl_dl_directory.configure(text=settings.download_location)

    def get_words_file(self):
        settings.words_file = filedialog.askopenfilename()
        self.lbl_words_file.configure(text=settings.words_file)

    def run(self):
        threading.Thread(target=self.init).start()

    def init(self):
        self.txt_box_log.insert("insert", "Initializing ...\n\n")
        if settings.words_file == None:
            self.txt_box_log.insert("insert", "No Words List Selected!\n\n")
            return
        if settings.download_location == None:
            self.txt_box_log.insert("insert", "No Download Location Selected!\n\n")
            return
        
        words = open(settings.words_file, "r").read().lower().replace("\n", " ").replace("-", " ").replace("_", " ").replace(",", " ").replace("/", " ").replace("\\", " ").split()
        for idx, word in enumerate(words):
            try:

                if (word+".mp3") in os.listdir(settings.download_location):
                    self.txt_box_log.insert("insert", f"{word} Already Downloaded!\n\n")
                    self.txt_box_log.see("end")
                    self.progress.set((idx+1)/len(words))
                    self.update()
                    continue


                self.txt_box_log.insert("insert", f"Grabbing For {word} ...\n")
                self.txt_box_log.see("end")
                self.update()

                page = requests.get(scrape_urls + word, headers=headers)
                soup = BeautifulSoup(page.content, "html.parser")

                self.txt_box_log.insert("insert", "Finding Mp3 Format ...\n")
                self.txt_box_log.see("end")
                self.update()

                result = soup.find(id="audio2").source["src"]

                self.txt_box_log.insert("insert", "Grabbing Media Data ...\n")
                self.txt_box_log.see("end")
                self.update()

                media_request = requests.get(media_url+result, headers=headers)
                sound = AudioSegment.from_mp3(BytesIO(media_request.content))

                self.txt_box_log.insert("insert", "Generating Loop ...\n")
                self.txt_box_log.see("end")
                self.update()

                new_loop = sound + silence + sound + silence + sound
                new_loop.export(os.path.join(settings.download_location, word + ".mp3"), format="mp3")

                self.txt_box_log.insert("insert", f"{word} Loop Created!\n\n")
                self.txt_box_log.see("end")
                self.update()

                self.progress.set((idx+1)/len(words))
                self.update()
            except:
                self.txt_box_log.insert("insert", "Something Went Wrong!\n")
                self.txt_box_log.see("end")
                self.progress.set((idx+1)/len(words))
                self.update()
                continue
        
        self.txt_box_log.insert("insert", "Completed!")
        self.txt_box_log.see("end")
        self.update()

app = MainWindow()
app.mainloop()