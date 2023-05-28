import os
import time
import shutil

path = "/Users/addey/Downloads/"

dir_list = os.listdir(path)


music_ext_list = [".mp3", ".wav", ".ogg", ".flac", ".m4a"]
docs_ext_list = [".pdf", ".docx", ".pptx", ".txt", ".html", ".ppt", ".htm"]
pics_ext_list = [".jpg", ".jpeg", ".png",
                 ".tif", ".gif", ".svg", ".eps", ".heic", ".bmp"]
vids_ext_list = [".mp4", ".mov", ".avi", ".mkv"]
graphics_ext_list = [".psd", ".ai", ".prproj", ".abr", ".otf", ".ttf", "ico"]
executables_ext_list = [".dmg", ".iso"]
compression_ext_list = [".zip", ".7zip", ".torrent", "7z"]
books_ext_list = [".epub"]
misc_ext_list = [".ovpn", ".webp", ".webarchive", ".download"]

every_ext = music_ext_list + docs_ext_list + \
    pics_ext_list + graphics_ext_list + vids_ext_list + \
    executables_ext_list + compression_ext_list


# Check & make dir for music
def mkdir_music(music_ext):
    name = "Music"
    path_s = f"{path}/{name}"
    for file in dir_list:
        for ext in music_ext:
            if file.lower().endswith(ext):
                if os.path.exists(f"{path}/{name}"):
                    print(f"{name} folder is here")
                    # Move file in the directory
                    if os.path.exists(f"{path}/{file}"):
                        shutil.move(f"{path}/{file}", f"{path_s}/{file}")
                    else:
                        continue
                else:
                    os.mkdir(path_s)
                    print(f"Making {name} folder")


# Check & make dir for docs


def mkdir_docs(docs_ext):
    name = "Documents"
    path_s = f"{path}/{name}"
    for file in dir_list:
        for ext in docs_ext:
            if file.lower().endswith(ext):
                if os.path.exists(f"{path}/{name}"):
                    print(f"{name} folder is here")
                    # Move file in the directory
                    if os.path.exists(f"{path}/{file}"):
                        shutil.move(f"{path}/{file}", f"{path_s}/{file}")
                    else:
                        continue
                else:
                    os.mkdir(path_s)
                    print(f"Making {name} folder")


# Check & make dir for pics
def mkdir_pics(pics_ext):
    name = "Pictures"
    path_s = f"{path}/{name}"
    for file in dir_list:
        for ext in pics_ext:
            if file.lower().endswith(ext):
                if os.path.exists(f"{path}/{name}"):
                    print(f"{name} folder is here")
                    # Move file in the directory
                    if os.path.exists(f"{path}/{file}"):
                        shutil.move(f"{path}/{file}", f"{path_s}/{file}")
                    else:
                        continue
                else:
                    os.mkdir(path_s)
                    print(f"Making {name} folder")


# Check & make dir for vids
def mkdir_vids(vids_ext):
    name = "Videos"
    path_s = f"{path}/{name}"
    for file in dir_list:
        for ext in vids_ext:
            if file.lower().endswith(ext):
                if os.path.exists(f"{path}/{name}"):
                    print(f"{name} folder is here")
                    # Move file in the directory
                    if os.path.exists(f"{path}/{file}"):
                        shutil.move(f"{path}/{file}", f"{path_s}/{file}")
                    else:
                        continue
                else:
                    os.mkdir(path_s)
                    print(f"Making {name} folder")


# Check & make dir for music
def mkdir_graphics(graphics_ext):
    name = "Graphic Design"
    path_s = f"{path}/{name}"
    for file in dir_list:
        for ext in graphics_ext:
            if file.lower().endswith(ext):
                if os.path.exists(f"{path}/{name}"):
                    print(f"{name} folder is here")
                    # Move file in the directory
                    if os.path.exists(f"{path}/{file}"):
                        shutil.move(f"{path}/{file}", f"{path_s}/{file}")
                    else:
                        continue
                else:
                    os.mkdir(path_s)
                    print(f"Making {name} folder")


def mkdir_exec(exec_ext):
    name = "Executables"
    path_s = f"{path}/{name}"
    for file in dir_list:
        for ext in exec_ext:
            if file.lower().endswith(ext):
                if os.path.exists(f"{path}/{name}"):
                    print(f"{name} folder is here")
                    # Move file in the directory
                    if os.path.exists(f"{path}/{file}"):
                        shutil.move(f"{path}/{file}", f"{path_s}/{file}")
                    else:
                        continue
                else:
                    os.mkdir(path_s)
                    print(f"Making {name} folder")


def mkdir_compress(compress_ext):
    name = "Compressed Files"
    path_s = f"{path}/{name}"
    for file in dir_list:
        for ext in compress_ext:
            if file.lower().endswith(ext):
                if os.path.exists(f"{path}/{name}"):
                    print(f"{name} folder is here")
                    # Move file in the directory
                    if os.path.exists(f"{path}/{file}"):
                        shutil.move(f"{path}/{file}", f"{path_s}/{file}")
                    else:
                        continue
                else:
                    os.mkdir(path_s)
                    print(f"Making {name} folder")


def mkdir_books(books_ext):
    name = "Books"
    path_s = f"{path}/{name}"
    for file in dir_list:
        for ext in books_ext:
            if file.lower().endswith(ext):
                if os.path.exists(f"{path}/{name}"):
                    print(f"{name} folder is here")
                    # Move file in the directory
                    if os.path.exists(f"{path}/{file}"):
                        shutil.move(f"{path}/{file}", f"{path_s}/{file}")
                    else:
                        continue
                else:
                    os.mkdir(path_s)
                    print(f"Making {name} folder")


def mkdir_misc(misc_ext):
    name = "Miscellaneous"
    path_s = f"{path}/{name}"
    for file in dir_list:
        for ext in misc_ext:
            if file.lower().endswith(ext):
                if os.path.exists(f"{path}/{name}"):
                    print(f"{name} folder is here")
                    # Move file in the directory
                    if os.path.exists(f"{path}/{file}"):
                        shutil.move(f"{path}/{file}", f"{path_s}/{file}")
                    else:
                        continue
                else:
                    os.mkdir(path_s)
                    print(f"Making {name} folder")


def app():
    mkdir_music(music_ext_list)
    mkdir_docs(docs_ext_list)
    mkdir_pics(pics_ext_list)
    mkdir_graphics(graphics_ext_list)
    mkdir_vids(vids_ext_list)
    mkdir_exec(executables_ext_list)
    mkdir_compress(compression_ext_list)
    mkdir_books(books_ext_list)
    mkdir_misc(misc_ext_list)


def check():
    for file in dir_list:
        for ext in every_ext:
            if file.endswith(ext):
                app()


for x in range(2):
    time.sleep(1)
    check()
