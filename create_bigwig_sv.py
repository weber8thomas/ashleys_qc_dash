import pyBigWig
import pandas as pd

sv_df = pd.read_csv("stringent_filterTRUE.tsv", sep="\t")
print(sv_df)
sv_df.loc[sv_df["cell"] == "BM510x3PE20401"][["chrom", "start", "end", "sv_call_name"]].to_csv("test_sv.bed", sep="\t", index=False)
print(sv_df.loc[(sv_df["cell"] == "BM510x3PE20401") & (sv_df["chrom"] == "chr17")][["chrom", "start", "end", "sv_call_name"]])
# counts_file_init = pd.read_csv("RPE-BM510.txt.gz", sep="\t", compression="gzip")
# print(counts_file_init)
# # exit()
# chrom_size_df = counts_file_init.groupby("chrom")["end"].max().reset_index()
# print(chrom_size_df.values)
# # # exit()
# print(chrom_size_df)
# sample = sv_df["sample"].unique()[0]

# for cell in sorted(sv_df.cell.unique().tolist()):
#     print(cell)
#     sv_df_cell = sv_df.loc[sv_df["cell"] == cell]

#     print(counts_file.shape[0])

#     bw = pyBigWig.open("assets/Counts_BW/{cell}-W.bigWig".format(cell=cell), "w")
#     # bw = pyBigWig.open("assets/test.bigWig", "w")
#     # bw.addHeader([("chr1", 1000000)])
#     # print(list(chrom_size_df.itertuples(index=False, name=None)))
#     # print(counts_file.chrom.values)
#     # print(
#     #     counts_file.chrom.values.tolist(), counts_file.start.values.tolist(), counts_file.end.values.tolist(), counts_file.w.values.tolist()
#     # )
#     # print(
#     #     len(counts_file.chrom.values.tolist()),
#     #     len(counts_file.start.values.tolist()),
#     #     len(counts_file.end.values.tolist()),
#     #     len(counts_file.w.values.tolist()),
#     # )
#     bw.addHeader(list(chrom_size_df.itertuples(index=False, name=None)))
#     bw.addEntries(
#         counts_file.chrom.values.tolist(),
#         counts_file.start.values.tolist(),
#         ends=counts_file.end.values.tolist(),
#         values=counts_file.w.values.tolist(),
#     )
#     # bw.addEntries(["chr17", "chr17", "chr17"], [0, 100, 125], ends=[100, 120, 126], values=[5.0, 10.0, 20.0])
#     # print(bw)
#     bw.close()
#     bw = pyBigWig.open("assets/Counts_BW/{cell}-C.bigWig".format(cell=cell), "w")
#     # bw = pyBigWig.open("assets/test2.bigWig", "w")
#     bw.addHeader(list(chrom_size_df.itertuples(index=False, name=None)))
#     bw.addEntries(
#         counts_file.chrom.values.tolist(),
#         counts_file.start.values.tolist(),
#         ends=counts_file.end.values.tolist(),
#         values=counts_file.c.values.tolist(),
#     )
#     # bw.addHeader([("chr1", 1000000)])
#     # bw.addEntries(["chr17", "chr17", "chr17"], [0, 100, 125], ends=[100, 120, 126], values=[-20.0, -5.0, -40.0])
#     # print(bw)
#     bw.close()
