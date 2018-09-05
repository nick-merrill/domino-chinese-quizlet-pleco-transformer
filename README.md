# Domino Chinese Quizlet-to-Pleco Transformer

Note: This project is **not** affiliated with Domino Chinese,
Quizlet, or Pleco.

## Usage

* Export Quizlet flashcards.
    1. Go to a complete level card deck,
       like [this one](https://quizlet.com/308113196/dominochinese-level-1-complete-flash-cards/).
    2. Click the more actions icon (three dots).
    3. Click "Export".
    4. Copy the text into a file, say "~/Downloads/export.txt".
* Call the script, where the first argument is the path to
  the file to import and the second argument is the name under which
  to put all the sub-categories. Direct the output to the file you
  want to be exported.
```bash
    python quizlet_transform.py ~/Downloads/export.txt "Level 1 Complete" > ~/Downloads/transformed.txt
```
* Use the Pleco app to import the flashcards.
  See [Pleco documentation](http://iphone.pleco.com/manual/30200/flash.html#import).
