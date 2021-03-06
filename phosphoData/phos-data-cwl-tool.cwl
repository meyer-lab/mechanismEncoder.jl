#!/usr/bin/env cwl-runner

label: prot-data-cwl-tool
id:  prot-data-cwl-tool
cwlVersion: v1.0
class: CommandLineTool
baseCommand: phosphoPDCdata.py

requirements:
    - class: DockerRequirement
      dockerPull: sgosline/phos-dat

inputs:
    cancerType:
        type: string
        inputBinding:
            position: 1
            prefix: --cancerType

outputs:
    matrix:
        type: File
        outputBinding:
            glob: "file.tsv"
