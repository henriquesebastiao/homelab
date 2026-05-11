#!/usr/bin/env python3

# Este script renomeia arquivos em um diretório para remover acentos e caracteres problemáticos para FTP/FileZilla.

import os
import sys
import unicodedata
import re


def sanitize_filename(filename: str) -> str:
    """
    Remove acentos e caracteres problemáticos para FTP/FileZilla.
    """

    # Separar nome e extensão
    name, ext = os.path.splitext(filename)

    # Remover acentos (normalização Unicode)
    name = unicodedata.normalize("NFKD", name)
    name = name.encode("ASCII", "ignore").decode("ASCII")

    # Substituições específicas
    replacements = {
        "|": "-",
        "/": "-",
        "\\": "-",
        ":": "-",
        "*": "",
        "?": "",
        "\"": "",
        "<": "",
        ">": "",
    }

    for old, new in replacements.items():
        name = name.replace(old, new)

    # Remover parênteses, colchetes e chaves
    name = re.sub(r"[()\[\]{}]", "", name)

    # Substituir espaços múltiplos por um único _
    name = re.sub(r"\s+", "_", name)

    # Remover caracteres restantes que não sejam seguros
    name = re.sub(r"[^a-zA-Z0-9._-]", "", name)

    # Evitar nomes vazios
    if not name:
        name = "arquivo"

    return name + ext


def rename_files(directory: str):
    if not os.path.isdir(directory):
        print(f"Erro: '{directory}' não é um diretório válido.")
        sys.exit(1)

    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)

        # Ignorar subdiretórios
        if not os.path.isfile(old_path):
            continue

        new_filename = sanitize_filename(filename)

        if new_filename == filename:
            continue

        new_path = os.path.join(directory, new_filename)

        # Evitar sobrescrever arquivos
        counter = 1
        base, ext = os.path.splitext(new_filename)
        while os.path.exists(new_path):
            new_filename = f"{base}_{counter}{ext}"
            new_path = os.path.join(directory, new_filename)
            counter += 1

        print(f"{filename} -> {new_filename}")
        os.rename(old_path, new_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python sanitize_filenames.py <diretorio>")
        sys.exit(1)

    rename_files(sys.argv[1])
