from Genetic_optimization_250916 import runsimulation
from joblib import Parallel, delayed
from neuron_model_utility import compute_block_functions,print_figure,testAccuracy_optimized_neuron
import time
import os
import shutil
import glob
from datetime import datetime

t = time.time()

neuron_list=['23515014']#12M # 24M


num_cores = len(neuron_list)#multiprocessing.cpu_count();

    
#Ltt = Parallel(n_jobs=num_cores, verbose=50)(delayed(runsimulation)(neuron_list[i]) for i in range(len(neuron_list)))


for i in range(len(neuron_list)):
    compute_block_functions(neuron_list[i])
    
    monod_active=False
    print_figure(neuron_list[i],monod_active)
    
    monod_active=True
    print_figure(neuron_list[i],monod_active)
    
    testAccuracy_optimized_neuron(neuron_list[i])
    
    # mette tutto in una sottocartella dedicata
    allfiles = glob.glob("*"+neuron_list[i]+"*")
    n=datetime.now()
    foldername = neuron_list[i]+"_"+n.strftime("%Y%m%d_%H%M%S")
    print(allfiles)
    os.mkdir(foldername)
    for outputfile in allfiles:
        shutil.copy(outputfile,foldername+'\\'+outputfile)
    allscripts = glob.glob("*.py")   
    for outputfile in allscripts:
        shutil.copy(outputfile,foldername+'\\'+outputfile)
    
    shutil.copy('optimization_parameters.json',foldername+'\\optimization_parameters.json')         
    
elapsed = time.time() - t



