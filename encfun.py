#!/usr/bin/python
# coding:utf-8

import sys
import os
import argparse
from py_compile import compile as obfus
from rich.console import Console
from rich.panel import Panel
from colorama import Fore, Style
import questionary

console = Console()

def banner():
		console.print(Panel(f"""
	 ____  ____  ______ _    _  _____  _____       _______ ______ 
	/ __ \|  _ \|  ____| |  | |/ ____|/ ____|   /\\|__   __|  ____|
 | |  | | |_) | |__  | |  | | (___ | |       /  \\ | |  | |__   
 | |  | |  _ <|  __| | |  | |\\___ \\| |      / /\\ \\| |  |  __|  
 | |__| | |_) | |    | |__| |____) | |____ / ____ \\ |  | |____ 
	\\____/|____/|_|     \\____/|_____/ \\_____/_/    \\_\\_|  |______|
								 AUTHOR : BOY HAMZAH
								 MODDER : TRHACKNON
""", title="[bold]Python Obfuscator[/bold]", expand=False))

def get_file_paths():
		file_path = questionary.text("Enter the path of the input file:", default="/sdcard/folder/file.py").ask()
		output_path = questionary.text("Enter the path of the output file:", default="fileob.py").ask()
		return file_path, output_path

def obf(file_path, output_path):
		try:
				data = []
				with open(file_path, 'r') as file:
						for i in file.read():
								data.append(ord(i))

				with open(output_path, 'w') as out_file:
						out_file.write(f"exec(''.join(chr(_) for _ in {data}))")

				obfus(output_path, output_path)
				console.print(Panel(f"File successfully compiled | File Name: {output_path}", style="green"))
		except Exception as e:
				console.print(Panel(f"Error: {e}", style="red"))

def main():
		parser = argparse.ArgumentParser(description="Python Obfuscator with CLI Interface")
		parser.add_argument("--file", help="Input file path. Example: /sdcard/folder/file.py")
		parser.add_argument("--output", help="Output file path. Example: kontol.py")

		args = parser.parse_args()

		os.system("clear")
		banner()

		if args.file and args.output:
				file_path, output_path = args.file, args.output
		else:
				console.print("[bold]Interactive Input:[/bold]")
				file_path, output_path = get_file_paths()

		console.print("[bold]Input Information:[/bold]")
		console.print(f"[cyan]Input File:[/cyan] {file_path}")
		console.print(f"[cyan]Output File:[/cyan] {output_path}\n")

		obf(file_path, output_path)

if __name__ == "__main__":
		main()