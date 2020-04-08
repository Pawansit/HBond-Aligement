import re
# Use these values to calculate scores
gap_penalty = -1
match_award = 1
mismatch_penalty = -1

# Make a score matrix with these two sequences
#seq1 = ["ASN3:GLU174","ASN5:GLU174","GLU7:GLU7","LEU8:GLY166","ASN13:ASP10","ILE14:PHE11","TYR17:VAL9","GLY18:PHE31","GLY23:LEU90","PHE29:ALA20","ASP34:LEU124","THR35:VAL213","ASN39:ILE133","TRP41:ILE123","VAL42:ILE103","SER44:GLU104","SER44:VAL105","CYX47:SER44","THR49:THR108","LEU53:THR49"] #,"THR54:ALA50","LYS55:ASP121","LYS55:SER118","TYR58:ASP89","TYR58:PRO43","SER61:ASP59","LYS62:ASP59","ARG64:SER61","THR81:THR81","VAL82:MET75","LEU90:ASP89","VAL91:LEU98","THR92:GLU21","VAL93:LEU96","TYR100:ASP137","LYS101:ASP69","GLU104:PHE85","ILE106:SER83","PHE111:THR108","GLU112:ASN109","TYR115:ASP121","THR116:PRO113","THR116:PRO113","SER118:PHE120","ASP121:THR30","ILE123:TRP41","LEU124:ILE32","LEU126:ASP34","LYS129:ASP137","SER132:ALA38","ILE133:ASN39","GLU142:PRO138","LYS144:ASP316","ASN145:VAL141","GLN146:GLU142","ASN147:LYS144","LYS148:LEU143","LYS148:GLN146","TYR157:LYS326","HIE164:LEU158","PHE167:TYR157","LEU168:ILE6","THR169:THR155","GLY171:LEU153","ARG176:GLU174","PHE177:GLU174","THR183:ASN263","GLU185:VAL320","ASN188:GLN194","GLN194:TYR192","ASP198:THR260","LYS208:ASP198","SER215:LEU33","THR217:ASP214","THR217:ASP214","SER218:ILE14","THR224:ASP293","PHE226:PRO223","LEU227:PRO223","ASN228:THR224","LEU231:LEU227","VAL246:ILE237","THR247:ASP235","ASN251:THR247","ASN251:LEU234","GLU258:HIE200","PHE259:TYR266","THR260:ASP198","ASN263:THR183","TYR266:ASN263","TYR266:PHE259","THR267:TYR309","THR267:GLU269","GLU269:GLU269","TYR272:GLU269","TYR273:PRO270","TYR273:PRO255","LEU274:PRO270","GLN275:GLN12","HIE276:GLN275","GLY283:VAL280","LEU284:GLU278","CYX285:THR247","MET286:GLN275","ILE289:LEU287","ILE290:ILE220","THR298:VAL296","ASP303:THR217","ARG307:ASP303","ARG307:PRO159","ARG307:ASP10","ARG307:ASP303","LYS308:GLU269","PHE310:ALA323","PHE313:PHE154","TYR315:ALA152","ASN317:ASP314","GLY321:VAL312","ILE322:THR183","ALA323:PHE310"]
#seq2 = ["SER1:GLU174","ASN3:GLU174","ILE6:LEU168","LEU8:GLY166","PHE11:ASP10","GLN12:HIE161","TYR17:VAL9","TYR17:MET15","GLY18:PHE31","ALA20:PHE29","VAL22:GLN27","GLY23:LEU90","ASP24:THR65","GLN26:GLU21","GLN26:GLY23","GLN27:VAL22","PHE29:ALA20","THR30:ASP19","THR30:ASP121","PHE31:GLY18"] #,"ASP34:LEU124","GLY36:ASP34","SER37:TYR77","SER44:GLU104","SER44:VAL105","VAL45:TYR58","LYS46:GLU104","CYX47:SER44","THR48:ILE106","LEU53:ALA50","THR54:GLY51","LYS55:PHE120","LYS55:TYR115","TYR58:ASP89","TYR58:PRO43","SER61:ASP59","LYS62:ASP59","SER63:ASP89","ARG64:ASP24","ARG64:ASP24","THR65:ASP89","GLU67:LYS88","LYS68:GLU67","GLY70:PHE86","THR71:ASP69","THR71:ASP69","VAL73:GLY84","MET75:VAL82","ASN76:ASN76","TYR77:GLY80","THR81:GLU74","VAL82:MET75","SER83:ASP107","GLY84:VAL73","PHE85:GLU104","PHE86:THR71","SER87:PHE102","LEU90:ASP89","VAL91:LEU98","THR92:GLU21","VAL93:LEU96","ASN95:ASP4","LEU98:VAL91","TYR100:ASP89","TYR100:ASP137","LYS101:ASP69","PHE102:SER87","GLU104:PHE85","VAL105:VAL42","ASN109:ASP107","ASN109:ASP107","PHE111:THR108","TYR115:ASP121","THR116:GLU112","THR116:GLU112","ALA117:PRO113","SER118:THR114","ASP121:THR30","LEU124:ILE32","GLY125:ASN39","LEU126:ASP34","GLY127:SER37","LYS129:ASP137","SER132:VAL136","SER132:LYS129","ILE133:ASN39","GLU142:PRO138","LEU143:ILE139","ASN145:VAL141","GLN146:GLU142","GLN146:GLU142","LYS148:SER97","LYS148:LEU143","THR155:THR311","TYR157:LYS326","TYR157:PHE167","HIE161:ASP10","HIE164:LEU158","GLY166:LEU8","PHE167:TYR157","LEU168:ILE6","ILE170:ASP4","GLY171:LEU153","GLU175:GLU175","ARG176:GLU174","GLU179:LEU324","THR183:ILE322","GLU185:VAL320","LYS186:ASN317","LEU187:HIE318","ASN188:ASN210","ASP190:HIE189","TRP193:LEU126","GLN194:ASN188","ILE195:CYX211","ALA199:LEU206","HIE200:GLU258","ASN203:LYS229","LEU206:ALA199","GLU207:GLU207","LYS208:ASP198","LYS208:ASP198","ASN210:THR298","CYX211:ILE195","ILE212:PHE299","ASP214:LEU301","SER215:LEU33","GLY216:ASP214","THR217:ASP214","ILE220:ASN288","VAL222:ILE290","ASN228:THR224","LYS229:ASP225","LEU231:LEU227","ILE237:VAL246","LYS238:VAL239","VAL239:PHE244","PHE244:LEU242","VAL246:ILE237","THR247:ASP235","CYX249:GLY283","ASN251:LEU234","LYS253:ASN251","LYS253:ASP235","LYS253:ASN233","PHE257:LEU268","GLU258:HIE200","SER261:GLY264","SER261:GLU185","ASN263:TYR184","ASN263:GLU185","LYS265:GLU258","TYR266:GLU185","THR267:PHE257","LEU268:PHE257","GLU269:GLU269","TYR272:GLU269","TYR273:PRO255","GLN275:ASN13","HIE276:ASP279","ILE277:LEU284","LEU284:GLU278","CYX285:THR247","MET286:GLN275","ASN288:TYR273","ILE290:ILE220","LEU292:VAL222","THR298:VAL296","PHE299:ASN210","ILE300:THR221","LEU301:ILE212","MET306:GLY302","ARG307:ASP10","ARG307:ASP303","LYS308:GLU269","LYS308:THR267","TYR309:PHE305","PHE310:ALA323","VAL312:GLY321","ASP314:SER319","TYR315:GLY127","SER319:ASP314","SER319:ASN317","VAL320:GLU185","GLY321:VAL312","LYS326:LYS327","LYS326:PHE177","LYS327:TYR272"]

seq1 = ["GLN26:GLY23","GLN27:VAL22","VAL93:LEU96","THR92:GLU21","VAL22:GLN27","GLY23:LEU90","GLY166:LEU8","LEU8:GLY166","ILE6:LEU168","ILE170:ASP4","PHE29:ALA20","ALA20:PHE29","LEU98:VAL91","VAL45:TYR58","LYS148:LEU143","VAL91:LEU98","TYR100:ASP89","GLU67:LYS88","TYR17:VAL9","PHE167:TYR157","LEU168:ILE6","GLY18:PHE31","PHE31:GLY18","ASP121:THR30","TYR58:PRO43","LYS326:PHE177","TYR157:PHE167","LEU53:ALA50","GLY171:LEU153","LEU143:ILE139","VAL105:VAL42","SER44:VAL105","CYX47:SER44","GLN146:GLU142","ASN145:VAL141","PHE102:SER87","GLU179:LEU324","ALA117:PRO113","LEU124:ILE32","ASP34:LEU124","THR48:ILE106","GLU142:PRO138","GLU104:PHE85","PHE85:GLU104","SER87:PHE102","GLY70:PHE86","LEU284:GLU278","TYR309:PHE305","PHE310:ALA323","VAL312:GLY321","LEU126:ASP34","GLY125:ASN39","PHE86:THR71","ILE277:LEU284","TYR272:GLU269","MET286:GLN275","MET306:GLY302","THR183:ILE322","GLY321:VAL312","ASP314:SER319","PHE111:THR108","GLY127:SER37","SER83:ASP107","GLY84:VAL73","VAL73:GLY84","CYX249:GLY283","CYX285:THR247","ASP214:LEU301","GLU185:VAL320","VAL320:GLU185","SER319:ASP314","VAL82:MET75","MET75:VAL82","SER132:LYS129","LEU268:PHE257","PHE257:LEU268","ASN288:TYR273","ILE220:ASN288","LEU301:ILE212","LEU187:HIE318","TYR77:GLY80","ILE237:VAL246","VAL246:ILE237","PHE244:LEU242","SER261:GLY264","ILE290:ILE220","ILE300:THR221","ILE195:CYX211","ILE212:PHE299","VAL239:PHE244","GLU258:HIE200","HIE200:GLU258","VAL222:ILE290","CYX211:ILE195","ALA199:LEU206","LEU292:VAL222","PHE299:ASN210","LEU231:LEU227","ASN228:THR224","LEU206:ALA199","LYS229:ASP225"]
seq2 = ["ASN147:LYS144","LYS148:LEU143","ASN145:VAL141","GLY171:LEU153","PHE177:GLU174","TYR315:ALA152","PHE313:PHE154","GLY321:VAL312","GLU185:VAL320","ILE322:THR183","ALA323:PHE310","GLU142:PRO138","ASN188:GLN194","VAL93:LEU96","THR169:THR155","PHE310:ALA323","VAL91:LEU98","GLN194:TYR192","LEU168:ILE6","THR260:ASP198","ASP198:THR260","PHE167:TYR157","TYR266:PHE259","GLY23:LEU90","THR92:GLU21","LEU8:GLY166","ARG307:ASP303","PHE259:TYR266","LEU126:ASP34","PHE29:ALA20","ASP34:LEU124","GLU258:HIE200","TRP41:ILE123","LEU124:ILE32","GLY18:PHE31","THR217:ASP214","ASP303:THR217","TYR17:VAL9","TYR272:GLU269","GLU104:PHE85","VAL42:ILE103","ILE123:TRP41","ASP121:THR30","ILE14:PHE11","TYR273:PRO270","LEU274:PRO270","TYR58:PRO43","LEU227:PRO223","PHE226:PRO223","ILE290:ILE220","ILE106:SER83","CYX47:SER44","SER44:VAL105","VAL82:MET75","ASN228:THR224","ILE289:LEU287","LEU231:LEU227","MET286:GLN275","CYX285:THR247","LEU53:THR49","PHE111:THR108","THR116:PRO113","VAL246:ILE237","LEU284:GLU278","GLY283:VAL280","GLU112:ASN109"]

#seq1 = ["A","T","C","A","T","G"]
#seq2 = ["T","A","C","T","C","G"]

# A function for making a matrix of zeroes
def zeros(rows, cols):
    # Define an empty list
    retval = []
    # Set up the rows of the matrix
    for x in range(rows):
        # For each row, add an empty list
        retval.append([])
        # Set up the columns in each row
        for y in range(cols):
            # Add a zero to each column in each row
            retval[-1].append(0)
    # Return the matrix of zeros
    return retval


# A function for determining the score between any two bases in alignment
def match_score(alpha, beta):
    if alpha == beta:
        return match_award
    elif alpha == '-' or beta == '-':
        return gap_penalty
    else:
        return mismatch_penalty

# The function that actually fills out a matrix of scores
def needleman_wunsch_matrix(seq1, seq2):
    
    # length of two sequences
    n = len(seq1)
    m = len(seq2)  
    
    # Generate matrix of zeros to store scores
    score = zeros(m+1, n+1)
   
    # Calculate score table
    
    # Your code goes here
    
    # Fill out first column
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    
    # Fill out first row
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j
    
    # Fill out all other values in the score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate the score by checking the top, left, and diagonal cells
            match = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1])
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
            # Record the maximum score from the three possible scores calculated above
            score[i][j] = max(match, delete, insert)

    return score

# Here is a helper function to print out matrices
def print_matrix(mat):
    # Loop over all rows
    for i in range(0, len(mat)):
        print("[", end = "")
        # Loop over each column in row i
        for j in range(0, len(mat[i])):
            # Print out the value in row i, column j
            print(mat[i][j], end = "")
            # Only add a tab if we're not in the last column
            if j != len(mat[i]) - 1:
                print("\t", end = "")
        print("]\n")
#print_matrix(needleman_wunsch_matrix(seq1, seq2))


def needleman_wunsch_alignment(seq1, seq2):
    
    # Store length of two sequences
    n = len(seq1)  
    m = len(seq2)
    
    # Generate matrix of zeros to store scores
    score = zeros(m+1, n+1)
   
    # Calculate score table
    
    # Fill out first column
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    
    # Fill out first row
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j
    
    # Fill out all other values in the score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate the score by checking the top, left, and diagonal cells
            match = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1])
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
            # Record the maximum score from the three possible scores calculated above
            score[i][j] = max(match, delete, insert)
    
    # Traceback and compute the alignment 
    
    # Create variables to store alignment
    align1 = ""
    align2 = ""
    
    # Start from the bottom right cell in matrix
    i = m
    j = n
    
    # We'll use i and j to keep track of where we are in the matrix, just like above
    while i > 0 and j > 0: # end touching the top or the left edge
        score_current = score[i][j]
        score_diagonal = score[i-1][j-1]
        score_up = score[i][j-1]
        score_left = score[i-1][j]
        
        # Check to figure out which cell the current score was calculated from,
        # then update i and j to correspond to that cell.
        if score_current == score_diagonal + match_score(seq1[j-1], seq2[i-1]):
            align1 += seq1[j-1]
            align2 += seq2[i-1]
            i -= 1
            j -= 1
        elif score_current == score_up + gap_penalty:
            align1 += seq1[j-1]
            align2 += '-'
            j -= 1
        elif score_current == score_left + gap_penalty:
            align1 += '-'
            align2 += seq2[i-1]
            i -= 1

    # Finish tracing up to the top left cell
    while j > 0:
        align1 += seq1[j-1]
        align2 += '-'
        j -= 1
    while i > 0:
        align1 += '-'
        align2 += seq2[i-1]
        i -= 1
    
    # Since we traversed the score matrix from the bottom right, our two sequences will be reversed.
    # These two lines reverse the order of the characters in each sequence.
    align1 = align1[::-1]
    align2 = align2[::-1]
    
    return(align1, align2)

output1, output2 = needleman_wunsch_alignment(seq1, seq2)
print(output1 + "\n" +output2)
