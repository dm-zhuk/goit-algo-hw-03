#!/usr/bin/python
# -*- coding: utf-8 -*-


import argparse
import shutil
import sys
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Рекурсивно копіює та сортує файли за розширеннями."
    )
    parser.add_argument("source", type=str, help="Шлях до вихідної директорії")
    parser.add_argument(
        "destination",
        type=str,
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням './dist')",
    )
    return parser.parse_args()


def copy_and_sort_files(source_path: Path, dest_path: Path):  # recursive call
    try:
        for item in source_path.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dest_path)
            elif item.is_file():
                extension = item.suffix.lower()  # .txt, .jpg etc.
                if not extension:
                    extension = ".no_extension"
                ext_dir = dest_path / extension[1:]
                ext_dir.mkdir(parents=True, exist_ok=True)
                dest_file = ext_dir / item.name
                try:
                    shutil.copy2(item, dest_file)
                    print(f"Скопійовано: {item} -> {dest_file}")
                except IOError as e:
                    print(f"Помилка копіювання {item}: {e}")

    except PermissionError:
        print(f"Помилка доступу до {source_path}")
    except OSError as e:
        print(f"Помилка обробки {source_path}: {e}")


def main():
    args = parse_arguments()

    source = Path(args.source)
    destination = Path(args.destination)

    if not source.exists() or not source.is_dir():
        print(f"Помилка: {source} не існує або не є директорією.")
        sys.exit(1)

    destination.mkdir(parents=True, exist_ok=True)

    # Start copy/sort process by 'python3 task_01.py <source> <destination>'
    print(f"Копіювання з {source} до {destination}...")
    copy_and_sort_files(source, destination)
    print("Готово!")


if __name__ == "__main__":
    main()
