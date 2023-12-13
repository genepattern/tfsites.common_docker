import sys, getopt
import tfsites as tf

helpMessage='''analyzeEqtl.py finds all effects of SNVs from GWAS data.

  -f --file             list of SNVs to be analyzed  
  -p --normpbm          Normalized PBM created with defineTfSites.py
  -g --genome           Genome as pickled file (output from function 3) 
  -i --iupac            IUPAC DNA definition of the tf site. This needs to be the same as the IUPAC specified in defineTfSites.py
  -z --zero_pos         TRUE/FALSE, genomic coordinates are 0-indexed
  -m --mut              (list of comma-separated values) List of one or more mutation effects to be analyzed or "all"        
  -o --outfile          Output file name for the list of SNVs and their effects 
  -B --bed              [Optional] Bed files to overlap with genomic coordinates in input file 
  -u --upper_thresh      [Optional] Upper threshold for reporting affinity optimizing SNVs
  -b --bottom_thresh     [Optional] Bottom threshold for reporting affinity sub-optimizing SNVs'''

def main(argv):
   file, normpbm, iupac, genome, mut, zero_pos, bed, outfile, upper_thresh, bottom_thresh = '', '', '', '', '', '', '', '', '', ''
   opts, args = getopt.getopt(argv,"h:f:p:i:g:m:z:B:o:u:b:",["file=", "normpbm=", "iupac=", "genome=", "mut=", "zero_pos=", "bed=" "outfile=", "upper_thresh=", "bottom_thresh="]) 

   # define argument results 
   for opt, arg in opts:
    if opt == '-h':
         print(helpMessage)
         sys.exit()
    elif opt in ("-f", "--file"):
         file = arg
    elif opt in ("-p", "--normpbm"):
         normpbm = arg
    elif opt in ("-i", "--iupac"):
         iupac = arg
    elif opt in ("-g", "--genome"):
         genome = arg
    elif opt in ("-m", "--mut"):
         mut = arg
    elif opt in ("-z", "--zero_pos"):
         zero_pos = arg
    elif opt in ("-B", "--bed"):
         bed = arg
    elif opt in ("-o", "--outfile"):
         outfile = arg
    elif opt in ("-u", "--upper_thresh"):
         upper_thresh = arg 
    elif opt in ("-b", "--bottom_thresh"):
         bottom_thresh = arg

    # error messages
   if file == '': print('Must specify input file'); sys.exit()
   if normpbm == '': print('Must specify normalized pbm data'); sys.exit()
   if iupac == '': print('Must specify iupac'); sys.exit()
   if genome == '': print('Must specify genome'); sys.exit()
   if mut == '': print('Must specify mutation types'); sys.exit()
   if zero_pos == '': print('Must specify whether coordinates are 0-indexed'); sys.exit()
   if outfile == '': print('Must specify output file name'); sys.exit()

   # optional input 
   if upper_thresh == '': upper_thresh = 1
   if bottom_thresh == '': bottom_thresh = 1 
   
   # optional bed file list
   if bed == '':
     bed_list = None
   else:
     bed_list = bed.split(',') # create bed file list 


   # convert the genome to a pkl file if it comes in as an fa
   if genome.endswith(".fa"):
      genomePkl = genome + ".pkl"
      tf.faToPickle(genome, genomePkl)
      genome = genomePkl


   seq2aff = tf.loadNormalizedPbm(normpbm)
   tf.analyzeEqtl(file, seq2aff, genome, iupac, zero_pos, mut, bed_list, outfile, upper_thresh, bottom_thresh)

if __name__ == "__main__":
   main(sys.argv[1:]) 
