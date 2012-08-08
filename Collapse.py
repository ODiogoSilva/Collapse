#!/usr/bin/python3

# Collapse v1.2.3
# Author: Diogo N Silva
# Last update: 07/08/2012
# Collapse is a tool that collapses molecular sequences (DNA,RNA and protein) into unique haplotypes. It currently supports FASTA, phylip and Nexus formats as input files and it is able to produce output in those three formats plus the Haplotype Definition of the Arlequin program. It also produces an additional output file with the listing of the haplotypes with their frequency and the taxa that they contain. 

#  Copyright 2012 Diogo N Silva <diogo@arch>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.
#  MA 02110-1301, USA.

import ElParsito, argparse

parser = argparse.ArgumentParser(description="Concatenates DNA data matrices")
parser.add_argument("-if",dest="InputFormat",default="fasta",choices=["fasta","nexus","phylip"],help="Format of the input file(s) (default is '%(default)s')")
parser.add_argument("-of",dest="OutputFormat",default="nexus",choices=["nexus","phylip","fasta","arlequin"],help="Format of the ouput file (default is '%(default)s')")
parser.add_argument("-o",dest="outfile",default="Outfile",required=True,help="Name of the output file (default is '%(default)s')")
parser.add_argument("-in",dest="infile",nargs="+",required=True,help="Input files")

arg = parser.parse_args()

# If you wish to include a whitespace (tab) between loci, set the variable to "yes", ortherwise "no".
tab_delimited_loci = "yes"

# Cut the taxa names by the following character:
seq_space_nex = 10
seq_space_phy = 26
seq_space_arlequin = 10

def dataset_creator (input_file,input_format,output_format):
	initial_storage,taxa_order = ElParsito.Taxa_gather(input_format,input_file)
	storage,part_list,sizes = ElParsito.Elparsito(input_format,initial_storage,input_file,output_format,tab_delimited_loci)
	return storage,taxa_order,part_list,sizes
	
def collapse (storage,taxa_order):
	Collapsed_dic = {}
	for taxa in taxa_order:
		if storage[taxa] in Collapsed_dic:
			Collapsed_dic[storage[taxa]] += ";%s" % (taxa)
		else:
			Collapsed_dic[storage[taxa]] = ""
			Collapsed_dic[storage[taxa]] = taxa
	return Collapsed_dic

def output_creator(output_format,storage,part_list,sizes,outfile):
	Hapfile = open(arg.outfile+".haplist","w")
	hap = 1
	
	if output_format == "phylip":
		outfile = open(arg.outfile+".phy","w")
		outfile.write("%s %s\n" % (len(storage),sizes-1))
		for key in storage:
			outfile.write("Hap%s %s\n" % (str(hap).ljust(seq_space_phy),key))
			Hapfile.write("Hap%s(%s): %s\n" % (hap,storage[key].count(";")+1,storage[key]))
			hap += 1
			
	if output_format == "fasta":
		outfile = open(arg.outfile+".fas","w")
		for key in storage:
			outfile.write(">Hap%s\n%s\n" % (hap,key))
			Hapfile.write("Hap%s(%s): %s\n" % (hap,storage[key].count(";")+1,storage[key]))
			hap += 1
			
	if output_format == "nexus":
		outfile = open(arg.outfile+".nex","w")
		partition_str = "".join(part_list)
		# Writing nexus header
		outfile.write("#NEXUS\n\nBegin data;\n\tdimensions ntax=%s nchar=%s;\n\tformat datatype=mixed (%s) interleave=no gap=- missing=N;\n\tmatrix\n" % (len(storage),sizes-1,"".join(part_list)[:-1]))
		# Writing sequences
		for key in storage:
			outfile.write("Hap"+str(hap).ljust(seq_space_nex)+" "+key+"\n")
			Hapfile.write("Hap%s(%s): %s\n" % (hap,storage[key].count(";")+1,storage[key]))
			hap += 1
		outfile.write("\t;\nend;")
		
	if output_format == "arlequin":
		outfile = open("Haplotipe_list.txt","w")
		outfile.write("[[HaplotypeDefinition]]\n\n HaplList={\n")
		x = 1
		for key in Collapsed_dic:
			outfile.write("Hap"+str(x)[:5].ljust(cut_space_arlequin)+" "+key+"\n")
			x += 1
		outfile.write("\t}")
	outfile.close()
	
def main():
	storage,taxa_order,part_list,sizes = dataset_creator(arg.infile,arg.InputFormat,arg.OutputFormat)
	collapsed_dic = collapse(storage,taxa_order)
	output_creator (arg.OutputFormat,collapsed_dic,part_list,sizes,arg.outfile)
	
main()
