import os
from pathlib import Path
import sys

from .formats import EXTENSIONS, FORMATS
from .parser import Checklist

DEFAULT_CHECKLIST = Path(__file__).parent / "assets" / "checklist.yml"

CHECKLIST_FILE = Path(os.environ.get("ETHICS_CHECKLIST", DEFAULT_CHECKLIST))


class ExtensionException(Exception):
    pass


class FormatException(Exception):
    pass


class MulticellException(Exception):
    pass


def create(checklist, output_format, output, overwrite, multicell, ids, lan, job):
    # load checklist
    
    cl_path = Path(checklist) if checklist else DEFAULT_CHECKLIST
    adder = os.path.basename(os.path.normpath(cl_path))
    if lan:
        adder += "_" + lan
        
    if job:
        adder += "_" + job

    adder += ".yml"
    print(adder)

    if job or lan:
        cl_path = cl_path / adder

    cl = Checklist.read(cl_path, ids)

    output = Path(output) if output else None

    # output extension is given priority if differing format is included
    if output:
        latex = False
        # get format by file extension
        ext = output.suffix.lower()
        if ext in EXTENSIONS.keys():
            output_format = EXTENSIONS[ext]
            if output_format == "latex":
                cl = Checklist.readJSON(cl_path)
                latex = True
        else:
            raise ExtensionException(ext)
    elif output_format:
        if output_format not in FORMATS:
            raise FormatException(output_format)
    else:
        output_format = "markdown"

    # multicell flag
    if multicell:
        if not output_format == "jupyter":
            raise MulticellException(output_format)
        output_format = "jupyter-multicell"
    
    template = FORMATS[output_format](cl)

    # write output or print to stdout
    if output:
        template.write(output, overwrite=overwrite)
        # if latex:
        #    os.system("pdflatex " + str(output))
    else:
        return template.render()
