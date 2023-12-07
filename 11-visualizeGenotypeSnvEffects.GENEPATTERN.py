import sys, getopt
import tfsites as tf

helpMessage='''visualizeGenotypeSnvEffects.py creates a visualization showing all SNV effects that overlap with genotypes'''

def main(argv):
   file, zoom, beta, bed_list, gff_list, outfile, bed_list_files, gff_list_files, gff_file_commands = '', '','', '', '', '', '', '', ''
   opts, args = getopt.getopt(argv,"h:f:z:b:B:g:o:C:D:G:",["file=", "zoom=", "beta=", "bed_list=", "gff_list=", "outfile=", "bed_list_files=", "gff_list_files=", "gff_file_commands="]) 

   # define argument results 
   for opt, arg in opts:
    if opt == '-h':
         print (helpMessage)
         sys.exit()
    elif opt in ("-f", "--file"):
         file = arg
    elif opt in ("-z", "--zoom"):
         zoom = arg
    elif opt in ("-b", "--beta"):
         beta = arg
    elif opt in ("-B", "--bed_list"):
         bed_list = arg
    elif opt in ("-g", "--gff_list"):
         gff_list = arg
    elif opt in ("-o", "--outfile"):
         outfile = arg
    elif opt in ("-C", "--bed_list_files"):
         bed_list_files = arg
    elif opt in ("-D", "--gff_list_files"):
         gff_list_files = arg
    elif opt in ("-G", "--gff_file_commands"):
         gff_file_commands = arg



    # error messages
   if file == '': print('Must specify file'); sys.exit()

   # optional input 
   if beta=='':beta=False
   if outfile == '': outfile=None
   if zoom=='': zoom=None

   if bed_list=='': 
       bed_list=[]
   else:
       bed_list = bed_list.split(',')

   if not bed_list_files == "":
       # read the list file to make the list
       with open(bed_list_files) as bedlistfile:
            bed_list = [line.rstrip() for line in bedlistfile]



   if gff_list=='': 
       gff_list=[]
   else: 
       split_gff = gff_list.split('=')
       gff_dict = {}
       gff_dict[split_gff[0]] = {}
       for item in split_gff[1].split(','):
           split_item = item.split(':')
           print(f"1. {split_gff[0]}   2 {split_item[0]}   3 {split_item[1]}")
           gff_dict[split_gff[0]][split_item[0]] = int(split_item[1])

   if not gff_list_files == "":
      # first get the full filepath to the uploaded files and make a dict of filename to full path
      gff_list_full_filepath = {}
      with open(gff_list_files) as gfflistfile:
         for line in gfflistfile:
             fullpath = line.rstrip()
             filename = fullpath.split("/")[-1]
             print(f" name: {filename}        path: {fullpath} ")
             gff_list_full_filepath[filename] = fullpath

      # now parse as in the original script
      gff_dict = {}

      with open(gff_file_commands) as gfffilecommands:
        for line in gfffilecommands:
           split_gff=line.split('=') 
           file_name = split_gff[0]
           full_path = gff_list_full_filepath[file_name]
           gff_commands=split_gff[1]

           gff_dict[full_path] = {}
           for item in gff_commands.split(','):
              split_item = item.split(':')
              print(f"1. {full_path}   2 {split_item[0]}   3 {split_item[1]}")
              gff_dict[full_path][split_item[0]] = int(split_item[1])


   print(outfile)

   tf.visualizeGenotypeSnvEffects(file, zoom, beta, bed_list, gff_dict, outfile)

if __name__ == "__main__":
   main(sys.argv[1:])
