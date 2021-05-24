import os; import sys; sys.path.append(os.path.normpath(os.path.join(os.getcwd(), "src")))
from argparse import ArgumentParser
from server import Server

if __name__ == "__main__":
    parser = ArgumentParser(description="Run server")
    parser.add_argument("csv", help="Your csv file")
    
    args = parser.parse_args()

    server = Server(host="localhost", port=4000)
    
    server.run(args.csv)
