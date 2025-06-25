# ShadowMD

**ShadowMD** is a terminal Markdown editor that protects your visual privacy by obfuscating the content while you type.

[🌐 Spanish Translation](README.es.md)
## Features

- Edit Markdown (`.md`) files directly from the terminal.
- Visual obfuscation: while typing, the content is displayed with random characters to prevent others from seeing what you write.
- Only the current line is clearly visible, but you can toggle visibility to show all text or hide it completely.
- Easy navigation with up and down arrow keys to move between lines.
- Safe saving with the shortcut `Ctrl+G`.
- Read-only mode to view files without editing.
- Supports absolute, relative, and `~` (home) paths.
- Option to show the real content after saving using the `-v` or `--verbose` flag.

## Requirements

- Python 3
- `readchar` module (install with `pip install readchar`)

## Installation

1. Clone this repository or download the script `shadowmd.py`.
2. Install the dependency:

```bash
pip install readchar
```

## Usage

```bash
python shadowmd.py [path_to_file.md] [options]
```

## Options

```text
Option          Description
-v, --verbose   Show real content after editing finishes
--readonly      Open file in read-only mode (no editing)
```

## Examples

### Edit a file:

```bash
python shadowmd.py ~/notes/journal.md
```

### Edit a file and show real content after finishing:

```bash
python shadowmd.py ~/notes/journal.md -v
```

### View a file without editing:

```bash
python shadowmd.py ~/notes/journal.md --readonly
```

## Editor Controls

- `ENTER`: New line

- `BACKSPACE`: Delete characters

- `Arrow keys ↑ ↓`: Navigate between lines

- `Ctrl+T`: Toggle visibility (current line only / all visible / all hidden)

- `Ctrl+G`: Save and exit

## Why ShadowMD?
When you are in public or shared places, typing sensitive content in the terminal can be risky. ShadowMD obfuscates your text so no one can read it at a glance, while maintaining the usability of a full Markdown editor.