import sys, getopt
import tfsites as tf

helpMessage='''8-compareSeqs.py compares the two seqs and reports the binding site effect on diff seqs.

  -n --tfnames          (comma-separated list) List of TF names
  -i --tfiupacs         (comma-separated list) List of TF IUPACs
  -p --tfnormpbms       (comma-separated list) List of TF normalized PBM files, one per line
  -P --tfnormbpmsfilelist File containing paths to a 
  -a --seq1             First DNA sequence  
  -b --seq2             Second DNA sequence
  -c --seq1name         Name of first DNA sequence
  -d --seq2name         Name of second DNA sequence
  -o --outfile          Output file name ''' 

def main(argv):
   tfnames, tfiupacs, tfnormpbms, seq1, seq2, seq1name, seq2name, outfile, tfnormpbmsFileList = '', '', '', '', '', '', '', '',""
   opts, args = getopt.getopt(argv,"h:n:i:p:a:b:c:d:o:P:",["tfnames=", "tfiupacs=", "tfnormpbms=", "seq1=", "seq2=", "seq1name=", "seq2name=", "outfile=", "tfnormbpmsfilelist="])

   # define argument results 
   for opt, arg in opts:
    if opt == '-h':
         print(helpMessage)
         sys.exit()
    elif opt in ("-n", "--tfnames"):
         tfnames = arg
    elif opt in ("-i", "--tfiupacs"):
         tfiupacs = arg
    elif opt in ("-p", "--tfnormpbms"):
         tfnormpbms = arg
    elif opt in ("-a", "--seq1"):
         seq1 = arg
    elif opt in ("-b", "--seq2"):
         seq2 = arg
    elif opt in ("-c", "--seq1name"):
         seq1name = arg
    elif opt in ("-d", "--seq2name"):
         seq2name = arg
    elif opt in ("-o", "--outfile"):
         outfile = arg
    elif opt in ("-P", "--tfnormbpmsfilelist"):
        tfnormpbmsFileList = arg

    # error messages
   if tfnames == '': print('Must specify list of TF names'); sys.exit()
   if tfiupacs == '': print('Must specify list of TF IUPACs'); sys.exit()
   if tfnormpbms == ''  and tfnormpbmsFileList =='': print('Must specify list of TF normalized PBM files'); sys.exit()
   if seq1 == '': print('Must specify the first sequence'); sys.exit()
   if seq2 == '': print('Must specify the second sequence'); sys.exit()
   if seq1name == '': print('Must specify the name of the first sequence'); sys.exit()
   if seq2name == '': print('Must specify the name of the second sequence'); sys.exit()
   if outfile == '': print('Must specify output file name'); sys.exit() 

   tfnames_list = tfnames.split(',')
   tfiupacs_list = tfiupacs.split(',')
   if not tfnames == '':
       tfnormpbms_list = tfnormpbms.split(',')
   elif  not tfnormpbmsFileList == '':
       with open(tfnormpbmsFileList) as file:
           tfnormpbms_list = [line.rstrip() for line in file]

   tf.reportSequenceChangeEffects_batchTf(tfnames_list, tfiupacs_list, tfnormpbms_list, seq1, seq2, seq1name, seq2name, outfile) 

if __name__ == "__main__":
   main(sys.argv[1:]) 