import toga

def main():
    return toga.App("Toga Audio Input + WhisperX", startup)

def startup(app):
    box = toga.Box()
    return box

if __name__ == "__main__":
    app = main()
    app.main_loop()
