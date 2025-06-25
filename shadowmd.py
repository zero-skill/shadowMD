import os
import argparse
import readchar
import random
import string

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear')

def obfuscate_text(text):
    """
    Returns a string of the same length as `text` with random
    characters to obfuscate the original content.
    """
    allowed_chars = string.ascii_letters + string.digits + "@#$%&*?!"
    return ''.join(random.choice(allowed_chars) for _ in text)

def display_interface(lines, current_line_idx, visibility_mode):
    """
    Displays the editor interface with the given lines.
    
    visibility_mode can be:
      - 'current_only': show only the current line, others obfuscated
      - 'all_visible': show all lines plainly
      - 'all_hidden': show all lines obfuscated
    """
    clear_screen()
    print("Hidden Markdown Editor 🕶️")
    print("(Ctrl+G = save, Ctrl+T = toggle view mode, ↑/↓ = navigate)\n")

    for idx, line in enumerate(lines):
        if visibility_mode == "current_only":
            # Show only the current line plainly
            print(line if idx == current_line_idx else obfuscate_text(line))
        elif visibility_mode == "all_visible":
            print(line)
        elif visibility_mode == "all_hidden":
            print(obfuscate_text(line))

    print(f"\n> Current line: {current_line_idx + 1}/{len(lines)} — Mode: {visibility_mode}")

def display_final_content(lines):
    """Prints the actual content clearly after editing or viewing."""
    print("\nActual content:\n")
    print('-' * 40)
    print('\n'.join(lines))
    print('-' * 40)

def parse_arguments():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description="Hidden Markdown Editor 🕶️")
    parser.add_argument("filepath", help="Path to the .md file to edit or view")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show content after exit")
    parser.add_argument("--readonly", action="store_true", help="View file without editing")

    args = parser.parse_args()
    abs_path = os.path.abspath(os.path.expanduser(args.filepath))
    return abs_path, args.verbose, args.readonly

def main():
    filepath, verbose, readonly = parse_arguments()

    # Load existing file content or start with empty
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        print(f"\n📄 Existing file detected with {len(lines)} line(s).")
    else:
        lines = []

    if readonly:
        display_final_content(lines)
        return

    input("\nPress ENTER to start editing...")

    if not lines:
        lines = [""]

    current_line = len(lines) - 1
    visibility_mode = "current_only"  # Modes: current_only, all_visible, all_hidden

    while True:
        display_interface(lines, current_line, visibility_mode)
        key = readchar.readkey()

        if key == readchar.key.ENTER:
            # Insert a new empty line below current and move cursor there
            lines.insert(current_line + 1, "")
            current_line += 1

        elif key == readchar.key.BACKSPACE:
            # Delete last character in the current line or merge lines if empty
            if lines[current_line]:
                lines[current_line] = lines[current_line][:-1]
            elif current_line > 0:
                merged_line = lines.pop(current_line)
                current_line -= 1
                lines[current_line] += merged_line

        elif key == readchar.key.UP:
            # Move cursor up, if possible
            if current_line > 0:
                current_line -= 1

        elif key == readchar.key.DOWN:
            # Move cursor down, if possible
            if current_line < len(lines) - 1:
                current_line += 1

        elif key == '\x14':  # Ctrl+T toggles visibility mode
            if visibility_mode == "current_only":
                visibility_mode = "all_visible"
            elif visibility_mode == "all_visible":
                visibility_mode = "all_hidden"
            else:
                visibility_mode = "current_only"

        elif key == '\x07':  # Ctrl+G saves and exits
            break

        elif key.isprintable():
            # Append typed character to current line
            lines[current_line] += key

    # Save the edited content back to the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"\n✅ File saved as {filepath}")
    if verbose:
        display_final_content(lines)

if __name__ == "__main__":
    main()
