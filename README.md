Rando the Random Number Generator

usage: rando [-h] [--infile [INFILE]] [--outfile [OUTFILE]] [--sites [SITES]]
             [--test] [--netrand] [--devrand] [--verbose] [--outdir [OUTDIR]]
             [--len [LENGTH]]

NIST Randomness Test Suite

optional arguments:
  -h, --help            show this help message and exit
  --infile [INFILE], -i [INFILE]
                        File of binary bits
  --outfile [OUTFILE], -o [OUTFILE]
                        Output file
  --sites [SITES], -s [SITES]
                        List of sites to scrape
  --test, -t            Generate non-random test data
  --netrand, -n         Perform network based ranom number generation
  --devrand, -g         Ranom number generation using /dev/urandom
  --verbose, -v         Generate verbose output
  --outdir [OUTDIR], -d [OUTDIR]
                        Directory where output files are placed
  --len [LENGTH], -l [LENGTH]
                        Length of random number to be generated

