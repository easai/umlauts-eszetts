# umlauts

German umlauts and eszett can be represented in ASCII as ae, ue, oe, and ss. While they can conveniently express German words without diacritical marks, they can be ambiguous. For example, Aether is not the same as Äther. 

Here a Python script that generates all possible combinations of a German word with umlauts and eszett replaced by their ASCII equivalents (ae, oe, ue, ss).

### Usage
The file does not use any dependent libraries.

Run the file as follows.
```bash
poetry run py umlauts\umlauts.py
```
For running the test files,
```bash
poetry run pytest
```
