import pandas as pd
import numpy as np

from CGmodelselection.graph import get_graph_from_data


def to_graph(file, standardize = True, kS = 2, model = 'PW', graphthreshold = 1e-3):

    datafr = pd.read_csv(file, index_col=0)
    grpnormmat, graph, dlegend = get_graph_from_data(datafr, drop = [], model = model, graphthreshold = graphthreshold, standardize = standardize, kS = kS)

    df = pd.DataFrame(grpnormmat, columns=dlegend.values(), index=dlegend.values())
    file = file.split("/")[-1].split(".")[0]
    df.to_csv("graphs_embedded/" + file + "_graph.csv")


if __name__ == '__main__':
    import argparse
    import os

    script_name = os.path.basename(__file__)

    parser = argparse.ArgumentParser(description="Use -f PATH/TO/FILENAME to specifiy the dataset which should be transformed into a graph.", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-f", "--file", help="path to dataset", nargs='+')# type=str)

    args = parser.parse_args()

    if args.file is None:
        print("Filename is missing")
        raise SystemExit()  # exits normally

    #print ("FILE: ", args.file)
    for x in args.file:
        to_graph(x)
