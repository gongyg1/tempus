#!/usr/bin/python
import os
import sys
import re
from numpy import * 
from pandas import Series,DataFrame
import pandas as pd
exac_af={}
exac_csq={}
pos=""
refb=""
DP=""
DPRA=""
rpl=""
rpr=""
AF=""
keylist=[]
key=""
infile= open("C:\\Users\\Younger\\Desktop\\tempus\\Challenge_data.vcf")
infile1= open("C:\\Users\\Younger\\Desktop\\tempus\\ExAC-20000.txt")

outfile1 = open("C:\\Users\\Younger\\Desktop\\tempus\\challenge_mapping_to_ExAC.txt", 'w')


for line in infile1:
    if re.search(r'^[^#]', line):
        line=line.rstrip('\n')
        chrom=line.split('\t')[0]
        pos=line.split('\t')[1]
        refb=line.split('\t')[3]
        altb=line.split('\t')[4]
        info=line.split('\t')[7]		
        af=info.split(';')[11]
        csq=info.split(';')[62]
# multiple possibilities
        if re.search(r',',af):
           af_val=af.split('=')[1]
#          print(af_val)
           af_list=af_val.split(',')
# most deleterious possibility
           index_value=af_list.index(max(af_list))
           af_value=af_list[index_value]
#corresponding ALT genotype of 	most deleterious possibility	   
           altb=altb.split(',')[index_value]
           key=chrom+'_'+pos		   
           exac_af[key]=af_value
        else:
           af_value=af.lstrip('AF=')
           key=chrom+'_'+pos
           exac_af[key]=af_value
        exac_csq[key]=csq
           
    keylist.append(key)  

outfile1.write("#CHROM"+"\t"+"pos"+"\t"+"ref"+"\t"+"ALT"+"\t"+"DP"+"\t"+"DPRA"+"\t"+"type"+"\t"+"rpl"+"\t"+"rpr"+"\t"+"AF"+"\t"+"ExAC_AF"+"\t"+"ExAC_CSQ"+"\n")
for line in infile:
    if re.search(r'^[^#]', line):
        line=line.rstrip('\n')
        chrom=line.split('\t')[0]
        pos=line.split('\t')[1]
        refb=line.split('\t')[3]
        altb=line.split('\t')[4]
        info=line.split('\t')[7]
		
        DP=info.split(';')[7]
        print(DP,'\n')
        DPRA=info.split(';')[9]
        print(DPRA,'\n')
        type=info.split(';')[40]
        rpl=info.split(';')[29]
        rpr=info.split(';')[32]
        af=info.split(';')[3]
        key=chrom+'_'+pos
#       print(key,'\n')		
        if re.search(r',',af):
           af_val=af.split('=')[1]
           af_list=af_val.split(',')		   
           index_value=af_list.index(max(af_list))
           af_value=af_list[index_value]		   
           altb=altb.split(',')[index_value]
        else :
           af_value=af.lstrip('AF=')	
        if key not in keylist:
           exac_af[key]='NA'
           exac_csq[key]='NA'
	
        outfile1.writelines(str(chrom)+'\t'+str(pos)+'\t'+str(refb)+'\t'+str(altb)+'\t'+str(DP)+'\t'+str(DPRA)+'\t'+str(type)+'\t'+str(rpl)+'\t'+str(rpr)+'\t'+str(af_value)+'\t'+str(exac_af[key])+'\t'+str(exac_csq[key])+'\n')
infile.close()
infile1.close()
outfile1.close()
