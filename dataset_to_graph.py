import pandas as pd
import numpy as np

from CGmodelselection.graph import get_graph_from_data


def to_graph(file, standardize = True, kS = 2, model = 'PW', graphthreshold = 0):

    grpnormmat, graph, dlegend = get_graph_from_data(file, drop = [], model = model, graphthreshold = graphthreshold, standardize = standardize, kS = kS)

    df = pd.DataFrame(grpnormmat, columns=dlegend.values(), index=dlegend.values())
    file = file.split("/")[-1].split(".")[0]
    df.to_csv("graphs/" + file + "_graph.csv")


if __name__ == '__main__':
    import argparse
    import os

    script_name = os.path.basename(__file__)

    parser = argparse.ArgumentParser(description="", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-d", "--file", help="datafile", type=str)

    args = parser.parse_args()

    if args.file is None:
        print("Filename is missing")
        raise SystemExit()  # exits normally

    to_graph(args.file)
