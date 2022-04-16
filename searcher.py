
'''
from flashtext import KeywordProcessor


keyword_processor = KeywordProcessor()


keyword_processor.add_keyword('status')

st = 'I love Big Apple and Bay Area.'

keywords_found = keyword_processor.extract_keywords(st)

print(keywords_found)



f = open("data", 'r')

lines = []
for x in f:
    lines.append(x)
keyword_processor = KeywordProcessor()

findem='koko piko 2x001 -13.12347 -'

#keyword_processor.add_keyword(findem)

#bigstring = ""

#for line in f :
#    bigstring = bigstring + line

#keywords_found = keyword_processor.extract_keywords(bigstring)


#print(bigstring.find(findem))

print(lines.find)
#print(keyword_processor.extract_keywords(bigstring))

#match_strings(['test'])
'''
import os
import mysql.connector

total_rows = 0
def retrieve_analysisDB(analysis):
    db = mysql.connector.connect(
        host="10.5.55.158",
        user="xshoot",
        passwd="1xshoot!",
        database="signature_db"
    )

    # get cursor object
    cursor = db.cursor()

    # execute your query
    cursor.execute("SELECT * FROM "+analysis)

    # fetch all the matching rows
    analysis_table = cursor.fetchall()

    return analysis_table

def dict_format_to_square_list(data1):
    data2 = [[''] * 6 for _ in range(total_rows)]

    #data2 = [['' for j in range(6)] for i in range(len(data1) + 1)]
    i = 0
    j = 0
    for x in data1:
        for y in x:
            for z in y:
                data2[i][j]=z
                j+=1
            i+=1
            j=0
        j=0

    print(data2[0][0])
    print(data2[1][1])

    return data2

def search(folder_name, analysis):
    """Get line from the file along with line numbers, which contains any string from the list"""
    line_number = 0
    list_of_results = []
    analysis_table = retrieve_analysisDB(analysis)
    # Open the file in read only mode
    for file in os.listdir(folder_name):
        onefile_result = []
        complete_file_path = folder_name+"\\"+file
        f= open(complete_file_path, 'r')
            # Read all lines in the file one by one
        for line in f:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for row in analysis_table:
                if row[1] in line:
                    # If any string is found in line, then append that line along with line number in list
                    onefile_result.append((file, line_number, row[1], row[3], row[2],line))
                    globals()['total_rows']+=1
        # Return list of tuples containing matched string, line numbers and lines where string is found
        list_of_results.append(onefile_result)

    return dict_format_to_square_list(list_of_results)


#res = search_multiple_strings_in_file("data",["koko piko"])

#for x in res:
#    print(x)