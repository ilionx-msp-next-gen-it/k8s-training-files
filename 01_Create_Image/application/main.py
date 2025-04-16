from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

color_codes = {
    "red": "#e8003d",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get color from Environment variable
COLOR_FROM_ENV = os.environ.get('APP_COLOR')
# Generate a random color
COLOR = random.choice(["red", "green", "blue", "blue2", "darkblue", "pink"])
# Set default color source
COLOR_SOURCE = "random"

@app.route("/")
def main():
    return render_template('index.html', name=socket.gethostname(), color=color_codes[COLOR], color_source=COLOR_SOURCE)

if __name__ == "__main__":

    print(" This is a sample web application that displays a colored background. \n"
          " A color can be specified in three ways. \n"
          "\n"
          " 1. As a file /storage/color.txt. Accepts one of " + SUPPORTED_COLORS + " \n"
          " 2. As a command line argument with --color as the argument. Accepts one of " + SUPPORTED_COLORS + " \n"
          " 3. As an Environment variable APP_COLOR. Accepts one of " + SUPPORTED_COLORS + " \n"
          " If none of the above then a random color is picked from the above list. \n"
          " Note: File precedes over command line argument and command line argument precedes over environment variable.\n"
          "\n"
          "")

    # Check for commandline parameters for color
    parser = argparse.ArgumentParser()
    parser.add_argument('--color', required=False)
    args = parser.parse_args()

    if os.path.exists('/storage'):
        try:
            with open('/storage/color.txt', 'r') as file:
                file_color = file.read().strip()
                print("Color from file /storage/color.txt = '" + file_color + "'")
                COLOR = file_color
                COLOR_SOURCE = "file"
        except FileNotFoundError:
            print("File /storage/color.txt not found, writing a random color to a new file.")
            with open('/storage/color.txt', 'w') as file_write:
                file_write.write(COLOR)
            COLOR_SOURCE = "file"
    elif args.color:
        print("Color from command line argument = '" + args.color + "'")
        COLOR = args.color
        COLOR_SOURCE = "argument"
        if COLOR_FROM_ENV:
            print("A color was set through environment variable - '" + COLOR_FROM_ENV + "'. However, color from command line argument takes precendence.")
    elif COLOR_FROM_ENV:
        print("No Command line argument. Color from environment variable = '" + COLOR_FROM_ENV + "'")
        COLOR = COLOR_FROM_ENV
        COLOR_SOURCE = "environment"
    else:
        print("No file command line argument or environment variable found. Picking a Random Color = '" + COLOR + "'")
        COLOR_SOURCE = "random"

    # Check if input color is a supported one
    if COLOR not in color_codes:
        print("Color not supported. Received '" + COLOR + "' expected one of " + SUPPORTED_COLORS)
        exit(1)

    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)
