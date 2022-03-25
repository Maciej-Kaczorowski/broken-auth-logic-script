import sys
import argparse

parser = argparse.ArgumentParser(description='script to mangle wordlist for broken auth logic')

# wordlist.txt path
parser.add_argument('--wordlist-path', type=str,help='Path to the wordlist.txt file')

# correct value
parser.add_argument('--correct-value', type=str,help='correct username or password')

# output path
parser.add_argument('--output', type=str,help='output path (default: mangled_pass_wordlist.txt')

if len(sys.argv)==1:
    parser.print_help()
    parser.exit()

args = parser.parse_args()

output_filename= "mangled_wordlist.txt"

if args.output:
    output_filename=args.output

if args.wordlist_path:
    with open(args.wordlist_path) as inputfile:
            with open(output_filename, 'w', encoding='utf-8') as outputfile:
                for line in inputfile:
                    outputfile.write(line)
                    outputfile.write(args.correct_value+"\n")



