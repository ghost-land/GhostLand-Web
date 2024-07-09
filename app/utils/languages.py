import os

def load_lang_file(lang) -> dict:
    lang_dictionary = {}
    lang_path = f"translations/{lang}.lang"
    if not os.path.isfile(f"translations/{lang}.lang"):
        for root, dirs, files in os.walk("translations"):
            for file in files:
                if file.endswith(".lang") and file.startswith(lang):
                    lang_path = f"translations/{file}"

    with open(lang_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if (
                line.replace(" ", "").replace("\n", "") != ""
                and not line.startswith("//")
                and not line.startswith("#")
            ):
                try:
                    key, value = line.strip().replace("\n", "").split("=", 1)
                    lang_dictionary[key] = value.strip()
                except Exception as e:
                    line = line.replace("\n", "")
                    print(f'\nLANG FILE ERROR:\nLine: {line}\nError: {e}\n')
    return lang_dictionary

def load_all_lang_files() -> dict:
    lang_files = {}
    for root, dirs, files in os.walk("translations"):
        for file in files:
            if file.endswith(".lang"):
                lang = file.split(".")[0]
                lang_files[lang] = load_lang_file(lang)
    return lang_files

lang_files = load_all_lang_files()
print(lang_files.keys())

def language_exists(lang='en') -> str:
    lang = next((l for l in lang_files if l.lower().startswith(lang.lower())), 'en')
    return lang in lang_files

def text(text=None, lang='en') -> str:
    if text is None:
        return ""
    
    lang = next((l for l in lang_files if l.lower().startswith(lang.lower())), 'en')
    
    if lang not in lang_files:
        lang = 'en_US'

    if text not in lang_files[lang]:
        return text
    
    return lang_files[lang][text]

# Testing
if __name__ == '__main__':
    while True:
        user_input = input("Enter text to translate (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        print(text(user_input, 'en'))
        