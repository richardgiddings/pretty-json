import json
import argparse

def make_json_pretty(filename):
    # read file
    with open(filename, 'r') as handle:
        parsed = json.load(handle)

    # make pretty
    with open('pretty_'+filename, 'w') as outfile:
        pretty_json = json.dump(parsed, outfile, indent=4, sort_keys=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Prettify json files.')
    parser.add_argument('filename', type=str, help='A file to prettify.')
    args = parser.parse_args()
    make_json_pretty(args.filename)