
# Pychess

[![Status][status badge]][status badge]
[![Tests][github actions badge]][github actions page]
[![Codecov][codecov badge]][codecov page]
[![Python Version][python version badge]][github page]
[![License][license badge]][license]

[code of conduct]: https://github.com/56kyle/pychess/blob/master/CODE_OF_CONDUCT.md
[codecov badge]: https://codecov.io/gh/56kyle/pychess/branch/master/graph/badge.svg?token=0QDENTNTN7
[codecov page]: https://app.codecov.io/gh/56kyle/pychess/branch/master
[contributor covenant badge]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
[github actions badge]: https://github.com/56kyle/pychess/workflows/Tests/badge.svg
[github actions page]: https://github.com/56kyle/pychess/actions?workflow=Tests
[github page]: https://github.com/56kyle/pychess
[license badge]: https://img.shields.io/github/license/56kyle/pychess
[license]: https://opensource.org/licenses/MIT
[python version badge]: https://img.shields.io/pypi/pyversions/56kyle-pychess
[status badge]: https://img.shields.io/pypi/status/56kyle-pychess

A chess library written in Python.


[Pychess](#Pychess)
    - [Description](#Description)
    - [Installation](#Installation)
    - [Usage](#Usage)
        - [Game](#Game)
        - [Board](#Board)
        - [Move](#Move)
        - [Piece](#Piece)
        - [Player](#Player)
        - [Square](#Square)
    - [Contributing](#Contributing)
    - [License](#License)


## Installation
    
    ```bash
    # Install from PyPI
    pip install 56kyle-pychess

    # Install from poetry
    poetry add 56kyle-pychess
    ```

## Description
The main purpose of this library is to try and practice constantly improving the quality of a codebase instead of allowing complexity to grow with time.

I was mainly inspired by the books "Clean Code" and "Clean Coder" both written by Robert C. Martin. Most of the code in this library is written with the principles of clean code in mind.

### General Design Decisions
- The Board class is immutable. This means that every time a move is made, a new board is created. This is to prevent the board from being in an invalid state.
- Moves and most geometry related classes are described in terms of Points and Lines
- Almost all iterables are sets to allow for hash comparisons of various frozen dataclass based objects

### Simplifications
- The board may not be infinite
- The board must be a rectangle


## Features
- [ ] API
    - [ ] Game
    - [x] Board
    - [ ] Move
    - [x] Piece
    - [x] Player
    - [x] Square
- [ ] Engine
- [ ] UCI
- [ ] GUI
- [ ] Documentation

## Usage
### Game
    TODO
### Board
    TODO
### Move
    TODO
### Piece
    TODO
### Player
    TODO
### Square
    TODO
    


    



