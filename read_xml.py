import xml.etree.ElementTree as ET
import pandas as pd
import os

def xml_2_dataframe(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    df_cols = list(tree.getroot()[0].attrib.keys())
    rows = []
    for node in root:
        df_vals = []
        for col in df_cols:
            df_vals.append(node.attrib.get(col))
        df_dict=dict(zip(df_cols,df_vals))
        rows.append(df_dict)
    return pd.DataFrame(rows,columns= df_cols)


def read_xml_files(location):
    '''This function will generate the dictionary of dataframes from the xml files present in the directory
    Parameters:
        dir -- Directory of the xml files
    return:
        A dictionary of dataframes from the xml files
    '''

    xmlfiles = sorted(os.listdir(location))
    xmlnames = [location.split('.')[0] + '_' + names[:-4] for names in xmlfiles]
    #print(xmlnames)
    #print(xmlfiles)
    dataframes = (xml_2_dataframe(location + '/' + file) for file in xmlfiles)
    return dict(zip(xmlnames, dataframes))