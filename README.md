# Game Server Overview

[![Build Status](https://drone.fap.no/api/badges/kradalby/gso/status.svg)](https://drone.fap.no/kradalby/gso)

Quick implementation of a little overview for showing dfekt.no's game servers.

For querying the game servers i use the SourceQuery class from [SourceLib by Andreas Klauer](https://github.com/frostschutz/SourceLib)

The webserver is implemented using flask.

## Installation

### Debian

Install Python 3, Pip, Virtualenv and build essentials:

    apt-get install python3 python3-pip python-virtualenv build-essential

### Common

Clone the repository:

     git clone https://github.com/kradalby/gso.git

Create a virtual environment and install requirements:

    cd gso
    make env
    make prod

Run the app:

    make run

Note that running it this way is mainly for development, for deployment, i recommend uWSGI which will be installed as a dependency during the "make prod" step.

## Usage

In gso.py add your own servers to the SERVERS.
Edit the index.html to your own needs.
