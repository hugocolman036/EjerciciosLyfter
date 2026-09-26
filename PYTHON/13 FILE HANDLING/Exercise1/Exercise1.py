def read_songs(filename):
    with open(filename, "r") as file:
        songs = file.readlines()
    return songs


def sort_songs(songs):
    songs.sort()
    return songs


def write_songs(filename, songs):
    with open(filename, "w") as file:
        file.writelines(songs)


if __name__ == "__main__":
    songs = read_songs("songs.txt")
    songs = sort_songs(songs)
    write_songs("songs_sorted.txt", songs)