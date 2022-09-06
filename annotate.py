import os
import sys
import png
import numpy
import fileinput

try:
    os.mkdir('output')
except FileExistsError:
    pass

path = sys.argv[1] #input directiory from command line

for file in os.listdir(path):
    if file.endswith('.xml'): #only read each xml/png pair once
        name = file[:-4]
        print(name)

        #read and process png file
        reader = png.Reader(filename = os.path.join(path, name + '.png'))
        width, height, rows, info = reader.read()
        matrix = numpy.vstack([row for row in rows])
        print(width, height)
        print(matrix)
        print(len(matrix))
        print(len(matrix[0]))

        for line in fileinput.input(os.path.join(path, file)):
            index = line.find('<node')
            while index != -1: #find next node
                index += 5
                endnodeindex = line.find('>', index)
                if line[endnodeindex-1] == '/':
                    print(line[:endnodeindex])
                    #this is a leaf node, time to do some ugly string parsing
                    boundindex = line.find('bounds=', index)
                    firstboundindex = line.find('[', boundindex)
                    comma1index = line.find(',', firstboundindex)
                    bah = line[firstboundindex+1:comma1index]
                    x1 = int(bah)
                    breakindex = line.find(']', comma1index)
                    y1 = int(line[comma1index+1:breakindex])
                    secondboundindex = line.find('[', breakindex)
                    comma2index = line.find(',', secondboundindex)
                    x2 = int(line[secondboundindex+1:comma2index])
                    endindex = line.find(']',comma2index)
                    y2 = int(line[comma2index+1:endindex])

                    #draw box
                    
                index = line.find('<node', endnodeindex)
                    

        outfile = open(os.path.join('output', name + '_annotated.png'), 'wb')
        writer = png.Writer(width = width, height = height, **info)
        writer.write(outfile, matrix)
        outfile.close()
