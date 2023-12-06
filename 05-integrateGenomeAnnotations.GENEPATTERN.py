import sys, getopt
import tfsites as tf

helpMessage='''5-integrateGenomeAnnotations.py finds all possible SNVs and their effects on binding sites.

  -f --file             File containing list of SNVs
  -b --bed              (comma-separated list) Bed files to overlap with genomic coordinates in input file 
  -z --zero_pos         TRUE/FALSE, genomic coordinates are 0-indexed       
  -o --outfile          Output file name for the list of SNVs and their effects
  -B --bedlist          File containing list of bed files, one per line'''

def main(argv):
   file, bed, bedlist, zero_pos, outfile = '', '', '', '', ''
   opts, args = getopt.getopt(argv,"h:f:b:z:o:B:",["file=", "bed=", "zero_pos=", "outfile=", "bedlist="]) 

   # define argument results 
   for opt, arg in opts:
    if opt == '-h':
         print(helpMessage)
         sys.exit()
    elif opt in ("-f", "--file"):
         file = arg
    elif opt in ("-b", "--bed"):
         bed = arg
    elif opt in ("-z", "--zero_pos"):
         zero_pos = arg
    elif opt in ("-o", "--outfile"):
         outfile = arg
    elif opt in ("-B", "--bedlist"):
         bedlist = arg


    # error messages
   if file == '': print('Must specify input file'); sys.exit()
   if bed == '' and bedlist =='' : print('Must specify bed files(s)'); sys.exit()
   if zero_pos == '': print('Must specify whether coordinates are 0-indexed'); sys.exit()
   print(file, bed, zero_pos, outfile) 
   if outfile == '': print('Must specify output file name'); sys.exit()

   if not bed == "":
        bed_list = bed.split(',') # create bed file list
   elif not bedlist == "":
        # read the list file to make the list
        with open(bedlist) as bedlistfile:
            bed_list = [line.rstrip() for line in bedlistfile]
   else:
       print()


   tf.integrateGenomeAnnotations(file, bed_list, zero_pos, outfile)

if __name__ == "__main__":
   main(sys.argv[1:]) 
