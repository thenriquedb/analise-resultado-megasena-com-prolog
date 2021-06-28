from app import App
from argparse import ArgumentParser
import os
import sys
sys.path.append(os.path.normpath(os.path.join(os.getcwd(), "src")))

if __name__ == "__main__":
    parser = ArgumentParser(description="Run server")
    parser.add_argument("csv", help="Your csv file")

    args = parser.parse_args()

    HOST = 'localhost'
    PORT = 4000
    CSV_PATH = args.csv if args.csv else 'data/games.csv'

    app = App(HOST, PORT)
    app.load_games(CSV_PATH)
    app.start()
