# T.vedavathi
# challenge program
# using argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name", help="Enter your name")
args = parser.parse_args()
print("Hello", args.name)