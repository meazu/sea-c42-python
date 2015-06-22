# Name: ...
# CSE 140
# Homework 7: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G, C, A, T, GC, AT nucleotides seen so far.
gc_count = 0
at_count = 0
g_count = 0
c_count = 0
a_count = 0
t_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
        # If bp is in C
        if bp == 'C':
            c_count = c_count + 1
        # if bp is in G
        if bp == 'G':
            g_count = g_count + 1
    # If bp is in A or bp is in T, increment count
    if bp == 'A' or bp == 'T':
        at_count = at_count + 1
        # If bp is in A
        if bp == 'A':
            a_count = a_count + 1
        # If bp is in T
        if bp == 'T':
            t_count = t_count + 1

# Sum of G, C, A, T nucleatides count 
gcat_count = g_count + c_count + a_count + t_count

# divide the gc_count by the total_count
gc_content = float(gc_count) / gcat_count
at_content = float(at_count) / gcat_count

# Length of the sequence
len_seq = len(seq)

# Computing AT/GC ratio
at_gc_ratio = float(a_count + t_count) / (g_count + c_count)

# Calacuating percentage of GC content and classification
gc_content_per = round(gc_content * 100)

if gc_content_per < 40:
    gc_content_class = "Low GC content"

elif gc_content_per > 60:
    gc_content_class = "High GC content"

else:
    gc_content_class = "Moderate GC content"

# Print the answer
print('GC-content: %r') %(gc_content)
print('AT-content: %r')  %(at_content)
print('G count: %d') %(g_count)
print('C count: %d') %(c_count)
print('A count: %d') %(a_count)
print('T count: %d') %(t_count)
print('Sum count: %d') %(gcat_count)
print('Total count: %d') %(total_count)
print('Seq length: %d') %(len_seq)
print('AT/GC Ratio: %r') %(at_gc_ratio)
print('GC Classification: %s') %(gc_content_class)
