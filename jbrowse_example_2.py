import dash
import dash_jbrowse
from dash import html

print(dash_jbrowse.__version__)
app = dash.Dash(__name__)

my_assembly = {
    "name": "GRCh38",
    "sequence": {
        "type": "ReferenceSequenceTrack",
        "trackId": "GRCh38-ReferenceSequenceTrack",
        "adapter": {
            "type": "BgzipFastaAdapter",
            "fastaLocation": {
                "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/fasta/GRCh38.fa.gz",
            },
            "faiLocation": {
                "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/fasta/GRCh38.fa.gz.fai",
            },
            "gziLocation": {
                "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/fasta/GRCh38.fa.gz.gzi",
            },
        },
    },
    "aliases": ["hg38"],
    "refNameAliases": {
        "adapter": {
            "type": "RefNameAliasAdapter",
            "location": {
                "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/hg38_aliases.txt",
            },
        },
    },
}


#     {
#         "type": "FeatureTrack",
#         "trackId": "ncbi_refseq_109_hg38",
#         "name": "NCBI RefSeq (GFF3Tabix)",
#         "assemblyNames": ["GRCh38"],
#         "category": ["Annotation"],
#         "adapter": {
#             "type": "Gff3TabixAdapter",
#             "gffGzLocation": {
#                 "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full_analysis_set.refseq_annotation.sorted.gff.gz",
#             },
#             "index": {
#                 "location": {
#                     "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full_analysis_set.refseq_annotation.sorted.gff.gz.tbi",
#                 },
#             },
#         },
#     },


#     {
#     "type": "MultiQuantitativeTrack",
#     "trackId": "multiwiggle_1675709067184-1675709081747-sessionTrack",
#     "name": "MultiWiggle 1675709067184",
#     "assemblyNames": [
#         "GRCh38"
#     ],
# "adapter": {
#     "type": "MultiWiggleAdapter",
#     "subadapters": [
#       {
#         "type": "BigWigAdapter",
#         "bigWigLocation": {
#           "uri": app.get_asset_url("test.bigWig")

#       },
#       },
#       {
#         "type": "BigWigAdapter",
#         "bigWigLocation": {
#           "uri": app.get_asset_url("test2.bigWig")
#       },
#       }
#     ]
#   },
# }


my_default_session = {
    "name": "My session",
    "view": {
        "id": "linearGenomeView",
        "type": "LinearGenomeView",
        "tracks": [
    {
            "id": "BuGte5uXo",
            "type": "MultiQuantitativeTrack",
            # "configuration": "microarray_multi",
            "minimized": False,
            "displays": [
              {
                "id": "6X1ummYMGg",
                "type": "MultiLinearWiggleDisplay",
                "height": 403,
                # "configuration": "microarray_multi-MultiLinearWiggleDisplay",
                "selectedRendering": "",
                "resolution": 1,
                "rendererTypeNameState": "multirowxy",
                "autoscale": "localsd",
                "layout": [
                  {
                    "name": "ENCFF055ZII",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF055ZII/@@download/ENCFF055ZII.bigWig"
                    },
                    "color": "rgb(77, 175, 74)"
                  },
                  {
                    "name": "ENCFF826HEW",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF826HEW/@@download/ENCFF826HEW.bigWig"
                    },
                    "color": "rgb(77, 175, 74)"
                  },
                  {
                    "name": "ENCFF858LIM",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF858LIM/@@download/ENCFF858LIM.bigWig"
                    },
                    "color": "rgb(77, 175, 74)"
                  },
                  {
                    "name": "ENCFF425TNW",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF425TNW/@@download/ENCFF425TNW.bigWig"
                    },
                    "color": "rgb(77, 175, 74)"
                  },
                  {
                    "name": "ENCFF207RBY",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF207RBY/@@download/ENCFF207RBY.bigWig"
                    },
                    "color": "rgb(77, 175, 74)"
                  },
                  {
                    "name": "ENCFF289CTN",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF289CTN/@@download/ENCFF289CTN.bigWig"
                    },
                    "color": "rgb(77, 175, 74)"
                  },
                  {
                    "name": "ENCFF495SBQ",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF495SBQ/@@download/ENCFF495SBQ.bigWig"
                    },
                    "color": "rgb(77, 175, 74)"
                  },
                  {
                    "name": "ENCFF959EZF",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF959EZF/@@download/ENCFF959EZF.bigWig"
                    },
                    "color": "rgb(77, 175, 74)"
                  },
                  {
                    "name": "ENCFF926YZX",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF926YZX/@@download/ENCFF926YZX.bigWig"
                    },
                    "color": "rgb(77, 175, 74)"
                  },
                  {
                    "name": "ENCFF269CHA",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF269CHA/@@download/ENCFF269CHA.bigWig"
                    },
                    "color": "blue"
                  },
                  {
                    "name": "ENCFF857KTJ",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF857KTJ/@@download/ENCFF857KTJ.bigWig"
                    },
                    "color": "blue"
                  },
                  {
                    "name": "ENCFF109KCQ",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF109KCQ/@@download/ENCFF109KCQ.bigWig"
                    },
                    "color": "blue"
                  },
                  {
                    "name": "ENCFF942TZX",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF942TZX/@@download/ENCFF942TZX.bigWig"
                    },
                    "color": "blue"
                  },
                  {
                    "name": "ENCFF305JRR",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF305JRR/@@download/ENCFF305JRR.bigWig"
                    },
                    "color": "blue"
                  },
                  {
                    "name": "ENCFF739FDJ",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF739FDJ/@@download/ENCFF739FDJ.bigWig"
                    },
                    "color": "blue"
                  },
                  {
                    "name": "ENCFF518OJP",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF518OJP/@@download/ENCFF518OJP.bigWig"
                    },
                    "color": "blue"
                  },
                  {
                    "name": "ENCFF810HHS",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF810HHS/@@download/ENCFF810HHS.bigWig"
                    },
                    "color": "blue"
                  },
                  {
                    "name": "ENCFF939JSB",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF939JSB/@@download/ENCFF939JSB.bigWig"
                    },
                    "color": "blue"
                  },
                  {
                    "name": "ENCFF041TAK",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF041TAK/@@download/ENCFF041TAK.bigWig"
                    },
                    "color": "blue"
                  },
                  {
                    "name": "ENCFF884IEG",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF884IEG/@@download/ENCFF884IEG.bigWig"
                    },
                    "color": "rgb(228, 26, 28)"
                  },
                  {
                    "name": "ENCFF140HPM",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                      "uri": "https://www.encodeproject.org/files/ENCFF140HPM/@@download/ENCFF140HPM.bigWig"
                    },
                    "color": "rgb(228, 26, 28)"
                  }
                ],
                "constraints": {
                  "max": 14
                }
              }
            ]
          }           
        ],
    },
}


my_aggregate_text_search_adapters = [
    {
        "type": "TrixTextSearchAdapter",
        "textSearchAdapterId": "hg38-index",
        "ixFilePath": {
            "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/trix/hg38.ix"
        },
        "ixxFilePath": {
            "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/trix/hg38.ixx"
        },
        "metaFilePath": {
            "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/trix/meta.json"
        },
        "assemblyNames": ["GRCh38"],
    }
]
my_location = "1:0..500"
# my_location = {"refName": "10", "start": 1, "end": 800}

my_theme = {
    "theme": {
        "palette": {
            "primary": {
                "main": "#311b92",
            },
            "secondary": {
                "main": "#0097a7",
            },
            "tertiary": {
                "main": "#f57c00",
            },
            "quaternary": {
                "main": "#d50000",
            },
            "bases": {
                "A": {"main": "#98FB98"},
                "C": {"main": "#87CEEB"},
                "G": {"main": "#DAA520"},
                "T": {"main": "#DC143C"},
            },
        },
    },
    "widgets": {
      "hierarchicalTrackSelector": {
        "id": "hierarchicalTrackSelector",
        "type": "HierarchicalTrackSelectorWidget",
        "collapsed": {
          "microarray_multi": False
        },
        "view": "Z5Y-_8x90"
      }
    },
    "activeWidgets": {
      "hierarchicalTrackSelector": "hierarchicalTrackSelector"
    },
    "connectionInstances": [],
    "sessionTracks": [],
    "sessionConnections": [],
    "sessionAssemblies": [],
    "temporaryAssemblies": [],
    "sessionPlugins": [],
    "minimized": False,
    "drawerPosition": "right"
  }

app.layout = html.Div(
    [
        dash_jbrowse.LinearGenomeView(
            id="lgv-hg38",
            assembly=my_assembly,
            # tracks=my_tracks,
            defaultSession=my_default_session,
            location=my_location,
            aggregateTextSearchAdapters=my_aggregate_text_search_adapters,
            configuration=my_theme
        ),
    ],
    id="test",
)

if __name__ == "__main__":
    app.run_server(port=5500, host="localhost", debug=True)