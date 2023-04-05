import dash
import dash_jbrowse
from dash import html

app = dash.Dash(__name__)

my_assembly = {
    "name": "GRCh38",
    "aliases": ["hg38"],
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
    "refNameAliases": {
        "adapter": {
            "type": "RefNameAliasAdapter",
            "location": {
                "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/hg38_aliases.txt",
                "locationType": 'UriLocation',
            },
        },
    },
}

my_tracks = [
    # {
    #     "type": "FeatureTrack",
    #     "trackId": "sv_calls",
    #     "name": "SV calls",
    #     "assemblyNames": ["GRCh38"],
    #     "category": ["SV"],
    #     "adapter": {
    #         "type": "BedAdapter",
    #         "bedLocation": {
    #             "uri": 'stringent_filterTRUE.tsv',
    #             "locationType": 'UriLocation',
    #         },
    #         # "colRef": 3,
    #         "scoreColumn": "llr_to_ref"
    #     },
    # },
{
  "type": "FeatureTrack",
  "trackId": "ncbi_refseq_109_hg38",
  "name": "NCBI RefSeq analysis set (GFF3Tabix)",
  "assemblyNames": [
    "hg38"
  ],
  "category": [
    "Annotation"
  ],
  "adapter": {
    "type": "Gff3TabixAdapter",
    "gffGzLocation": {
      "locationType": "UriLocation",
      "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full_analysis_set.refseq_annotation.sorted.gff.gz",
      "baseUri": "https://jbrowse.org/code/jb2/v2.3.4/config.json"
    },
    "index": {
      "location": {
        "locationType": "UriLocation",
        "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full_analysis_set.refseq_annotation.sorted.gff.gz.tbi",
        "baseUri": "https://jbrowse.org/code/jb2/v2.3.4/config.json"
      }
    }
  },
#   "displays": [
#     {
#       "type": "LinearBasicDisplay",
#       "displayId": "ncbi_refseq_109_hg38-LinearBasicDisplay"
#     },
#     {
#       "type": "LinearArcDisplay",
#       "displayId": "ncbi_refseq_109_hg38-LinearArcDisplay"
#     }
#   ]
}
]

my_default_session = {
    "name": "My session",
    "view": {
        "id": "linearView",
        "type": "LinearGenomeView",
        "bpPerPx": 5000000, 
        "tracks": [{
            "id": 'uPdLKHik1',
            "type": 'FeatureTrack',
            "configuration": 'ncbi_refseq_109_hg38',
            "displays": [
                {
                    "id": 'v9QVAR3oaB',
                    "type": 'LinearBasicDisplay',
                    "configuration": 'ncbi_refseq_109_hg38-LinearBasicDisplay',
                    "trackMaxHeight":3000,
                },
            ],
        }],
        "location":"17:0..1000"
    },
}


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
}


app.layout = html.Div(
    [
        dash_jbrowse.LinearGenomeView(
            id="linear-hg38",
            assembly=my_assembly,
            tracks=my_tracks,
            defaultSession=my_default_session,
        ),
    ],
    id="test",
)

if __name__ == "__main__":
    app.run_server(debug=True, port=5500, host="seneca.embl.de")