getSynonyms
=========================================

Given a word, a person can find out its synonyms, definitions and examples in different contexts..

Steps to perform:

1) Install virtual env
2) Activate virtual env using commands:
    $ mkdir virtualEnvDirectory
    $ cd virtualEnvDirectory
    $ virtualenv venv
    $ source venv/bin/activate

3) Now run: pip install -r getSynonyms/requirements.pip
4) cd getSynonyms/
5) Run nltkSetUpScript to install nltk in virtualEnv: ./nltkSetup.sh

6) run nltkSetup.py and follow the instructions.( Run using command: python nltkSetup.py)
7) Run the project as:  python src/synonymFinder.py
