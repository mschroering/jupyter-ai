from ._version import __version__
from .extension import AiExtension

# expose jupyter_ai_magics ipython extension
from jupyter_ai_magics import load_ipython_extension, unload_ipython_extension

# imports to expose entry points. DO NOT REMOVE.
from .engine import GPT3ModelEngine
from .tasks import tasks

# imports to expose types to other AI modules. DO NOT REMOVE.
from .tasks import DefaultTaskDefinition

def _jupyter_labextension_paths():
    return [{
        "src": "labextension",
        "dest": "@jupyter-ai/core"
    }]

def _jupyter_server_extension_points():
    return [{
        "module": "jupyter_ai",
        "app": AiExtension
    }]
