"""Small scripts for generating champion files."""

import os

champions = [
    "Aatrox",
    "Ahri",
    "Akali",
    "Akshan",
    "Alistar",
    "Amumu",
    "Anivia",
    "Annie",
    "Aphelios",
    "Ashe",
    "Aurelion Sol",
    "Azir",
    "Bard",
    "Bel'Veth",
    "Blitzcrank",
    "Brand",
    "Braum",
    "Briar",
    "Caitlyn",
    "Camille",
    "Cassiopeia",
    "Cho'Gath",
    "Corki",
    "Darius",
    "Diana",
    "Dr.Mundo",
    "Draven",
    "Ekko",
    "Elise",
    "Evelynn",
    "Ezreal",
    "Fiddlesticks",
    "Fiora",
    "Fizz",
    "Galio",
    "Gangplank",
    "Garen",
    "Gnar",
    "Gragas",
    "Graves",
    "Gwen",
    "Hecarim",
    "Heimerdinger",
    "Hwei",
    "Illaoi",
    "Irelia",
    "Ivern",
    "Janna",
    "Jarvan IV",
    "Jax",
    "Jayce",
    "Jhin",
    "Jinx",
    "K'Sante",
    "Kai'Sa",
    "Kalista",
    "Karma",
    "Karthus",
    "Kassadin",
    "Katarina",
    "Kayle",
    "Kayn",
    "Kennen",
    "Kha'Zix",
    "Kindred",
    "Kled",
    "Kog'Maw",
    "LeBlanc",
    "Lee Sin",
    "Leona",
    "Lillia",
    "Lissandra",
    "Lucian",
    "Lulu",
    "Lux",
    "Malphite",
    "Malzahar",
    "Maokai",
    "Master Yi",
    "Milio",
    "Miss Fortune",
    "Mordekaiser",
    "Morgana",
    "Naafiri",
    "Nami",
    "Nasus",
    "Nautilus",
    "Neeko",
    "Nidalee",
    "Nilah",
    "Nocturne",
    "Nunu",
    "Olaf",
    "Orianna",
    "Ornn",
    "Pantheon",
    "Poppy",
    "Pyke",
    "Qiyana",
    "Quinn",
    "Rakan",
    "Rammus",
    "Rek'Sai",
    "Rell",
    "Renata Glasc",
    "Renekton",
    "Rengar",
    "Riven",
    "Rumble",
    "Ryze",
    "Samira",
    "Sejuani",
    "Senna",
    "Seraphine",
    "Sett",
    "Shaco",
    "Shen",
    "Shyvana",
    "Singed",
    "Sion",
    "Sivir",
    "Skarner",
    "Smolder",
    "Sona",
    "Soraka",
    "Swain",
    "Sylas",
    "Syndra",
    "Tahm Kench",
    "Taliyah",
    "Talon",
    "Taric",
    "Teemo",
    "Thresh",
    "Tristana",
    "Trundle",
    "Tryndamere",
    "Twisted Fate",
    "Twitch",
    "Udyr",
    "Urgot",
    "Varus",
    "Vayne",
    "Veigar",
    "Vel'Koz",
    "Vex",
    "Vi",
    "Viego",
    "Viktor",
    "Vladimir",
    "Volibear",
    "Warwick",
    "Wukong",
    "Xayah",
    "Xerath",
    "Xin Zhao",
    "Yasuo",
    "Yone",
    "Yorick",
    "Yuumi",
    "Zac",
    "Zed",
    "Zeri",
    "Ziggs",
    "Zilean",
    "Zoe",
    "Zyra",
]


def create_files():
    """Create a bunch of basic champion files."""
    files_created = 0
    file_length = 21  # A hard-coded value that surely won't haunt me in the future

    # Read base file, which happens to be Aatrox because I already made it
    with open("aatrox.py", "r", encoding="utf8") as _file:

        for champ in champions:
            class_name = champ.replace("'", "").replace(" ", "").replace(".", "")
            filename = class_name.lower()
            # print(f"from .{filename} import {class_name}")  # Print useful stuff
            if os.path.exists(filename + ".py"):
                continue

            _file.seek(0)  # Reset to start of file
            with open(filename + ".py", "w", encoding="utf8") as new_file:
                files_created += 1

                for _ in range(file_length):
                    line = _file.readline()
                    if "class " in line:
                        line = line.replace("Aatrox", class_name)
                    else:
                        line = line.replace("Aatrox", champ).replace("aatrox", filename)
                    new_file.write(line)

    print(f"Created {files_created} new files.")


def append_method():
    """Append static pretty string method."""
    for champ in champions:
        class_name = champ.replace("'", "").replace(" ", "").replace(".", "")
        filename = class_name.lower()
        with open(filename + ".py", "a", encoding="utf8") as _file:
            _file.writelines([
                '\n',
                '    @staticmethod\n',
                '    def printable() -> str:\n',
                '        """Pretty string representation of champion, '
                'typically for menus or as display name."""\n',
                f'        return "{champ}"\n'
            ])


if __name__ == "__main__":
    create_files()
    append_method()
