#!/usr/bin/python
import os
import sys
import re
from numpy import * 
from pandas import Series,DataFrame
import pandas as pd
challenge_af={}
challenge_csq={}
challenge_DP={}
challenge_DPRA={}
challenge_type={}
challenge_rpl={}
challenge_rpr={}
challenge_refb={}
challenge_altb={}
pos=""
refb=""
DP=""
DPRA=""
rpl=""
rpr=""
AF=""
csq=""
keylist=[]
key=""
infile= open("C:\\Users\\Younger\\Desktop\\tempus\\Challenge_data.vcf")
infile1= open("C:\\Users\\Younger\\Desktop\\tempus\\ExAC.r1.sites.vep.vcf")

outfile1 = open("C:\\Users\\Younger\\Desktop\\tempus\\EXAC_mapping_to_challenge_ExAC.txt", 'w')


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
           challenge_af[key]=af_value
        else:
           af_value=af.lstrip('AF=')
           challenge_af[key]=af_value
        challenge_csq[key]=csq
        challenge_DP[key]=DP
        challenge_DPRA[key]=DPRA
        challenge_type[key]=type
        challenge_rpl[key]=rpl
        challenge_rpr[key]=rpr
        challenge_refb[key]=refb
        challenge_altb[key]=altb		
           
    keylist.append(key)  

outfile1.write("#CHROM"+"\t"+"pos"+"\t"+"ref"+"\t"+"ALT"+"\t"+"DP"+"\t"+"DPRA"+"\t"+"type"+"\t"+"rpl"+"\t"+"rpr"+"\t"+"challenge_AF"+"\t"+"AF"+"\t"+"CSQ"+"\n")
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
        if key in keylist:
           outfile1.writelines(str(chrom)+'\t'+str(pos)+'\t'+str(refb)+'\t'+str(altb)+'\t'+str(challenge_DP[key])+'\t'+str(challenge_DPRA[key])+'\t'+str(challenge_type[key])+'\t'+str(challenge_rpl[key])+'\t'+str(challenge_rpr[key])+'\t'+str(challenge_af[key])+'\t'+str(af_value)+'\t'+str(csq)+'\n')
infile.close()
infile1.close()
outfile1.close()
