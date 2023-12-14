import sys, getopt
import tfsites as tf

helpMessage='''annotateAndVisualizeTfSites.py creates a visualization showing all TF binding sites in a sequence'''

def main(argv):
   file, normpbm, iupac, mut_type, opt_thres, subopt_thres, tf_names, iupacs, colors, mb_values, plot_dpi, pbm, height, zoom, labels, denovo, tens_pos, table_outfile, vis_outfiles = '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 
   opts, args = getopt.getopt(argv,"h:f:p:i:m:o:s:t:I:c:b:d:P:H:z:l:n:t:O:v:",["file=", "normpbm=", "iupac=", "mut_type=", "opt_thres=", "subopt_thres=", "tf_names=", "iupacs=", "colors=", "mb_values=", "plot_dpi=", "pbm=", "height=", "zoom=", "labels=", "denovo=", "tens_pos=", "table_outfile=", "vis_outfiles="]) 

   # define argument results 
   for opt, arg in opts:
    print(f"opt: {opt}     arg: {arg}")
    if opt == '-h':
         print (helpMessage)
         sys.exit()
    elif opt in ("-f", "--file"):
         file = arg
    elif opt in ("-p", "--normpbm"):
         normpbm = arg
    elif opt in ("-i", "--iupac"):
         iupac = arg
    elif opt in ("-m", "--mut_type"):
         mut_type = arg
    elif opt in ("-o", "--opt_thres"):
         opt_thres = arg
    elif opt in ("-s", "--subopt_thres"):
         subopt_thres = arg
    elif opt in ("-t", "--tf_names"):
         tf_names = arg
    elif opt in ("-I", "--iupacs"):
         iupacs = arg
    elif opt in ("-c", "--colors"):
         colors = arg
    elif opt in ("-b", "--mb_values"):
         mb_values = arg
    elif opt in ("-d", "--plot_dpi"):
         plot_dpi = arg
    elif opt in ("-P", "--pbm"):
         pbm = arg
    elif opt in ("-H", "--height"):
         height = arg
    elif opt in ("-z", "--zoom"):
         zoom = arg
    elif opt in ("-l", "--labels"):
         labels = arg
    elif opt in ("-n", "--denovo"):
         denovo = arg
    elif opt in ("-t", "--tens_pos"):
         tens_pos = arg
    elif opt in ("-O", "--table_outfile"):
         table_outfile = arg
    elif opt in ("-v", "--vis_outfiles"):
         print(f"a. VIS_OUT is {arg}")
         vis_outfiles = arg 

    print(f"a. VIS_OUT is {vis_outfiles}")


    # error messages
   if file == '': print('Must specify input file'); sys.exit()
   if normpbm == '': print('Must specify normalized PBM data'); sys.exit()
   if iupac == '': print('Must specify iupac'); sys.exit()
   if mut_type == '': print('Must specify mutation type(s)'); sys.exit()
   if opt_thres == '': print('Must specify opt threshold'); sys.exit()
   if subopt_thres == '': print('Must specify subopt threshold'); sys.exit()
   if tf_names == '': print('Must specify TF names'); sys.exit()
   if iupacs == '': print('Must specify list of iupacs'); sys.exit()
   if colors == '': print('Must specify colors of sites'); sys.exit()
   if mb_values == '': print('Must specify m and b values for color alpha range'); sys.exit()

   # optional input 
   if plot_dpi == '': plot_dpi=100
   if height == '': height=0.3
   if denovo == '': denovo=False
   if tens_pos == '': tens_pos=-0.3
   if table_outfile == '': table_outfile=None

   if pbm=='':
        pbm_dict={}
   else: 
        pbm_items = pbm.split(',')
        pbm_dict = {}
        for item in pbm_items:
             split_item = item.split('=')
             pbm_dict[split_item[0]] = split_item[1] 

   if zoom=='': 
        zoom=None
   else: 
        zoom = zoom.split(',')
        zoom = (int(zoom[0]), int(zoom[1]))
   
   print(f"b. VIS_OUT is {vis_outfiles}")
   if vis_outfiles=='': 
        vis_outfiles=None
   else:
        vis_outfiles = vis_outfiles.split(',')

   # reformat inputs
   tf_names = tf_names.split(',')

   iupacs_items = iupacs.split(',')
   iupacs_dict = {}
   for item in iupacs_items:
        split_item = item.split('=')
        iupacs_dict[split_item[0]] = split_item[1]

   color_items = colors.split(',')
   colors_dict = {}
   for item in color_items:
        split_item = item.split('=')
        colors_dict[split_item[0]] = split_item[1] 

   print(f" --- --- --- viz outfiles is ->{vis_outfiles}<-")
   mb_items = mb_values.split(',')
   mb_dict = {}
   for item in mb_items:
        split_item = item.split('=')
        split_coord = split_item[1].split('+')
        mb_dict[split_item[0]] = (split_coord[0], split_coord[1])

   seq2aff = tf.loadNormalizedPbm(normpbm)
   tf.annotateAndVisualizeInSilicoSnvs(file, seq2aff, iupac, mut_type, float(opt_thres), float(subopt_thres), tf_names, iupacs_dict, colors_dict, mb_dict, 
                                       plot_dpi, pbm_dict, height, zoom, denovo, tens_pos, table_outfile, vis_outfiles)

if __name__ == "__main__":
   main(sys.argv[1:]) 
