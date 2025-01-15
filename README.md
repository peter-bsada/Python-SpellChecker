# Python SpellChecker

A Python-based spell checker that leverages a trie data structure to provide fast and efficient word validation, suggestions, and dynamic dictionary management.

## Features
- **Efficient Word Lookup** – Validate word spelling using a trie structure.
- **Word Suggestions** – Get suggestions for misspelled words.
- **Dynamic Dictionary** – Add, remove, or change the dictionary file dynamically.
- **Customizable** – Supports custom dictionaries and frequency lists.
- **Unit Tested** – Comprehensive tests for all functionalities.

## Installation
### Prerequisites
- Python 3.x

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Python-SpellChecker.git
   cd Python-SpellChecker
   ```
2. Run the spell checker:
   ```bash
   python3 spellchecker.py
   ```

## How to Use
1. Launch the program using `spellchecker.py`.
2. Use the interactive menu to:
   - Check word spelling.
   - Get word suggestions.
   - Change the dictionary file.
   - Add or remove words.
3. Follow the on-screen instructions for input and feedback.

### Example Menu:
```
1. Check a word
2. Get word suggestions
3. Change dictionary
4. Print all words
5. Remove one word
6. Quit
```

## File Structure
```
📂 Python-SpellChecker
├── 📄 trie.py              # Trie data structure
├── 📄 spellchecker.py      # Main program logic
├── 📄 node.py              # Node class for trie
├── 📄 dictionary.txt       # Default dictionary file
├── 📄 frequency.txt        # Word frequency file
├── 📄 test.py              # Unit tests
├── 📄 tiny_dictionary.txt  # Sample small dictionary
└── 📄 tiny_frequency.txt   # Sample small frequency file
```

## Unit Testing
Run the tests to validate functionality:
```bash
python3 test.py
```

## Contributing
Feel free to fork this repository and submit pull requests for improvements, new features, or bug fixes.

## License
This project is open-source and available under the MIT License.

---
✨ *Accurate and efficient spell checking with Python!*

