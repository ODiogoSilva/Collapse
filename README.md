#### About Collapse

Collapse is a simple python script that collapses a set of aligned molecular sequences, either DNA, RNA or protein, into a set of unique haplotypes. It works exclusively through the command line and requires the ElParsito.py module, which can be found in the ElConcatenero package (https://github.com/ODiogoSilva/ElConcatenero.git).

It currently supports as input file formats:

- FASTA
- Phylip
- Nexus

And its able to collapse sequences into any of these file formats:

- Fasta
- Phylip
- Nexus
- Arlequin (Only the "Haplotype Definition" block)

Along with the output collapsed file, Collapse.py creates a new file with the listing of the haplotypes with their frequency and the taxa that they contain

There is no need for instalation. The only requirement is that the ElParsito.py module must be on the same directory as Collapse.py (or you can use any other way to let the main script know where the module is). I do recommend, to make it easier to call the program, that you add it to your $PATH variable. 

Finally, please note that Collapse.py is far from immune to bugs and crashes, and I'll be happy to know about them through my e-mail (o.diogosilva@gmail.com) so that I can fix them. Any suggestions or comments are also welcome.

#### Options

Collapse.py has the following options (which can also be consulted by typing "ElConcatenero.py -h" in the command line):

  -h, --help            **show this help message and exit**
  -if *{fasta,nexus,phylip}*	**Format of the input file(s) (default is 'fasta')**
  -of *{nexus,phylip,fasta,arlequin}*	**Format of the ouput file (default is 'nexus')**
  -o *OUTFILE*            **Name of the output file (default is 'Outfile')**
  -in *INFILE [INFILE ...]*	**Input files**
								
#####Note:

The order of the options does not matter.
								
#### Usage
