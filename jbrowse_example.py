import dash
import dash_jbrowse
from dash import html


print(dash_jbrowse.__version__)
# app = dash.Dash(__name__)
dash.register_page(__name__)

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

my_tracks = [
    {
        "type": "FeatureTrack",
        "trackId": "ncbi_refseq_109_hg38",
        "name": "NCBI RefSeq (GFF3Tabix)",
        "assemblyNames": ["GRCh38"],
        "category": ["Annotation"],
        "adapter": {
            "type": "Gff3TabixAdapter",
            "gffGzLocation": {
                "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full_analysis_set.refseq_annotation.sorted.gff.gz",
            },
            "index": {
                "location": {
                    "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full_analysis_set.refseq_annotation.sorted.gff.gz.tbi",
                },
            },
        },
    },
    {
        "type": "QuantitativeTrack",
        "trackId": "gccontent_hg38",
        "name": "GCContent",
        "assemblyNames": ["GRCh38"],
        "adapter": {
            "type": "GCContentAdapter",
            "sequenceAdapter": {
                "type": "BgzipFastaAdapter",
                "fastaLocation": {
                    "uri": "https://jbrowse.org/genomes/GRCh38/fasta/GRCh38.fa.gz",
                    "locationType": "UriLocation",
                    "baseUri": "https://jbrowse.org/code/jb2/v2.3.4/test_data/config_demo.json",
                },
                "faiLocation": {
                    "uri": "https://jbrowse.org/genomes/GRCh38/fasta/GRCh38.fa.gz.fai",
                    "locationType": "UriLocation",
                    "baseUri": "https://jbrowse.org/code/jb2/v2.3.4/test_data/config_demo.json",
                },
                "gziLocation": {
                    "uri": "https://jbrowse.org/genomes/GRCh38/fasta/GRCh38.fa.gz.gzi",
                    "locationType": "UriLocation",
                    "baseUri": "https://jbrowse.org/code/jb2/v2.3.4/test_data/config_demo.json",
                },
            },
        },
    },
    {
        "type": "VariantTrack",
        "trackId": "clinvar.vcf.gz-1675786941544-sessionTrack",
        "name": "clinvar.vcf.gz",
        "assemblyNames": ["GRCh38"],
        "adapter": {
            "type": "VcfTabixAdapter",
            "vcfGzLocation": {"locationType": "UriLocation", "uri": "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz"},
            "index": {
                "location": {"locationType": "UriLocation", "uri": "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz.tbi"}
            },
        },
    },
]

import sys, os
from pprint import pprint

listdir_counts = sorted(set([e.replace("-W.bigWig", "") for e in os.listdir("assets/Counts_BW") if e.endswith("-W.bigWig")]))[:1]
pprint(listdir_counts)

my_tracks_counts = [
    {
        "type": "MultiQuantitativeTrack",
        "trackId": "multiwiggle_{cell}-sessionTrack".format(cell=e),
        "name": e,
        "assemblyNames": ["GRCh38"],
        "category": ["Run X - Sample Y - Counts"],
        "adapter": {
            "type": "MultiWiggleAdapter",
            "subadapters": [
                {
                    "name": "Watson",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                        "uri": app.get_asset_url("Counts_BW/{}-W.bigWig".format(e)),
                    },
                },
                {
                    "name": "Crick",
                    "type": "BigWigAdapter",
                    "bigWigLocation": {
                        "uri": app.get_asset_url("Counts_BW/{}-C.bigWig".format(e)),
                    },
                },
            ],
        },
    }
    for e in sorted(listdir_counts)
]

my_tracks_sv = [
    {
        "type": "FeatureTrack",
        "trackId": "test_sv.bed-sessionTrack",
        "name": "test_sv.bed",
        "assemblyNames": ["GRCh38"],
        "adapter": {
            "type": "BedAdapter",
            "bedLocation": {"uri": app.get_asset_url("test_sv.bed")},
        },
    }
    for e in sorted(listdir_counts)
]

my_tracks += my_tracks_counts
my_tracks += my_tracks_sv


tracks_session = [
    {
        "type": "FeatureTrack",
        "configuration": "ncbi_refseq_109_hg38",
        "displays": [
            {
                "type": "LinearBasicDisplay",
                "configuration": "ncbi_refseq_109_hg38-LinearBasicDisplay",
                "trackShowDescriptions": False,
            },
        ],
    },
    {
        "type": "QuantitativeTrack",
        "configuration": "gccontent_hg38",
        "displays": [
            {
                "id": "lTY7_5KzL6",
                "type": "LinearWiggleDisplay",
                "height": 100,
                "selectedRendering": "",
                "rendererTypeNameState": "xyplot",
                "displayCrossHatches": True,
                "layout": [
                    {
                        "name": "Watson",
                        "type": "GCContentAdapter",
                        "color": "red",
                    },
                ],
            },
        ],
    },
    {
        "type": "VariantTrack",
        "configuration": "clinvar.vcf.gz-1675786941544-sessionTrack",
        "displays": [{"type": "LinearVariantDisplay", "displayId": "clinvar.vcf.gz-1675786941544-sessionTrack-LinearVariantDisplay"}],
    },
]


tracks_session_counts = [
    {
        "type": "MultiQuantitativeTrack",
        "configuration": "multiwiggle_{cell}-sessionTrack".format(cell=e),
        "displays": [
            {
                "id": "lTY7_5KzL5",
                "type": "MultiLinearWiggleDisplay",
                "height": 70,
                "selectedRendering": "",
                "rendererTypeNameState": "xyplot",
                "autoscale": "global",
                "displayCrossHatches": True,
                "layout": [
                    {
                        "name": "Watson",
                        "type": "BigWigAdapter",
                        "bigWigLocation": {
                            "uri": app.get_asset_url("Counts_BW/{}-W.bigWig".format(e)),
                        },
                        "color": "rgb(244, 164, 96)",
                    },
                    {
                        "name": "Crick",
                        "type": "BigWigAdapter",
                        "bigWigLocation": {
                            "uri": app.get_asset_url("Counts_BW/{}-C.bigWig").format(e),
                        },
                        "color": "rgb(102, 139, 139)",
                    },
                ],
            },
        ],
    }
    for e in sorted(listdir_counts)
]

tracks_session_svs = [
    {
        "type": "FeatureTrack",
        "configuration": "test_sv.bed-sessionTrack",
        "displays": [
            {
                "displayId": "test_sv.bed-sessionTrack-LinearBasicDisplay",
                "type": "LinearBasicDisplay",
                "trackShowDescriptions": False,
                "trackDisplayMode": "collapse",
                "renderer": {
                    "type": "SvgFeatureRenderer",
                    "color1": "jexl:cast({ inv_h2: 'green', del_hom: 'purple' })[get(feature, 'name')]",
                    "displayMode": "collapse",
                },
            },
        ],
    },
]

tracks_session += tracks_session_counts
tracks_session += tracks_session_svs
print(tracks_session)


my_default_session = {
    "name": "My session",
    "view": {
        "id": "linearGenomeView",
        "type": "LinearGenomeView",
        "tracks": tracks_session
        # {
        #     "type": "AlignmentsTrack",
        #     "configuration": "bm510x04_pe20301.bam.htg-1675787802366-sessionTrack",
        #     "displays": [
        #         {
        #             "type": "LinearAlignmentsDisplay",
        #             "displayId": "bm510x04_pe20301.bam.htg-1675787802366-sessionTrack-LinearAlignmentsDisplay",
        #         },
        #         {"type": "LinearPileupDisplay", "displayId": "bm510x04_pe20301.bam.htg-1675787802366-sessionTrack-LinearPileupDisplay"},
        #         {
        #             "type": "LinearSNPCoverageDisplay",
        #             "displayId": "bm510x04_pe20301.bam.htg-1675787802366-sessionTrack-LinearSNPCoverageDisplay",
        #         },
        #     ],
        # },
    },
}


my_aggregate_text_search_adapters = [
    {
        "type": "TrixTextSearchAdapter",
        "textSearchAdapterId": "hg38-index",
        "ixFilePath": {"uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/trix/hg38.ix"},
        "ixxFilePath": {"uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/trix/hg38.ixx"},
        "metaFilePath": {"uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/trix/meta.json"},
        "assemblyNames": ["GRCh38"],
    }
]
my_location = "17:0..25000000"
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
}
# app.layout = html.Div(
layout = html.Div(
    [
        dash_jbrowse.LinearGenomeView(
            id="lgv-hg38",
            assembly=my_assembly,
            tracks=my_tracks,
            defaultSession=my_default_session,
            location=my_location,
            aggregateTextSearchAdapters=my_aggregate_text_search_adapters,
            configuration=my_theme,
        ),
    ],
    id="test",
)

# if __name__ == "__main__":
#     app.run_server(port=5500, host="localhost", debug=True)
