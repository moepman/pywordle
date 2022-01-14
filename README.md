# pyworlde

... is a simple tool to help you solve the famous daily "wordle" riddle and was born out of curiosity to see how easy
it would be to display the remaining solutions to the riddle, given any number of constraints you might have already
found out.

It is far from perfect and especially inefficient if you have not ruled out many characters yet or have not found any
fixed characters yet. In this case also the result list probably containing hundres of words it not very helpful - it
might actually be more helpful to be shown words that might help you rule out as many characters as possible.

## Installation

I suggest using a venv and pip, e.g. under Linux:

```
mkdir pywordle 
cd pywordle
python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/moepman/pywordle.git
```

## Usage

If you followed the installation setps above simple type `./venv/bin/wordle`
