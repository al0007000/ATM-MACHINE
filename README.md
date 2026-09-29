# ATM-MACHINE

This is a simple command line - python project showing the working of a simple ATM machine simulation, after card insertion, one can check his/her account balance, deposit and withdraw money in one terminal.

## Features

- PIN check with 3 attempts allowed
- Checking Balance
- Depositing and withdrawing money
- ₹5000 max per withdrawal, ₹25000 max per day (tracked automatically, preset)
- Checking how much is withdrawn today and how much is left
- Exit option that "ejects" the card

## Requirements

- Python 3.x (no external libraries needed)
- A terminal (Command Prompt, PowerShell, Terminal, etc.)

## Setup & Run

1. Install Python 3.x from [python.org](https://www.python.org/downloads/) if you don't have it.

2. Check that Python is installed:

   ```bash
   python --version
   ```

   On Mac/Linux you may need to use `python3 --version` instead.

3. Clone or download this repo.

   ```bash
   git clone https://github.com/al0007000/ATM-MACHINE.git
   ```

   (If you downloaded the zip instead, just extract it.)

4. Go into the project folder:

   ```bash
   cd ATM-MACHINE
   ```

5. Dependencies: there is nothing to install, the project only uses built-in Python.

6. Configuration: nothing to configure. The name, account, PIN and balance are preset inside `atm.py`.

7. In the project folder, run:

   ```bash
   python atm.py
   ```

   On Mac/Linux use `python3 atm.py` if `python` doesn't work.

## Usage

Press Enter to insert the card, then enter the PIN (3 tries max). Once logged in, pick an option from the menu and follow the prompts. Choose Exit to quit.

Menu:

```
1. Balance
2. Deposit
3. Withdraw
4. Daily limit
5. Exit
```

## Test Login

- Name: Ali Nawaz
- Account: XXXX1234
- PIN: 1234

## Project Files

- `atm.py` - the ATM program
- `Project_Report.pdf` - project report
- `README.md` - this file
