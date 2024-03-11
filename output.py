def output(color, string):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "end": "\033[0m", # To reset the color
    }
    
    # Check if the specified color exists, default to white if it does not
    color_code = colors.get(color, colors["white"])
    
    # Print the string in the specified color
    print(f"{color_code}{string}{colors['end']}")