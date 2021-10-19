import os


if __name__ == '__main__':
    path, dirs, files = next(os.walk("data/spb/"))
    dae_counter = 0
    for file in files:
        if file.endswith('.dae'):
            dae_counter += 1
    print(dae_counter)