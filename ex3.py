def similar():
    org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"]
    org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"]

    threshold=0.56 #threshold setting to 56%

    similar_pairs = [
        (seq1,seq2)
        for seq1 in org1
        for seq2 in org2
        if sum(1 for a, b in zip(seq1, seq2) if a == b) / len(seq1) > threshold
        ]

    print(similar_pairs)


def main():
    similar()

if __name__=="__main__":
    main()


