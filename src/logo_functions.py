LOGO_FUNCTIONS_ENG = {
    "sqrt": {
        "parameters": ["number"],
        "return": "number"
    },
    "sum": {
        "parameters": ["number", "number"],
        "return": "number"
    },

    "forward": {
        "parameters": ["number"],
        "return": None
    },
    "back": {
        "parameters": ["number"],
        "return": None
    },
    "left": {
        "parameters": ["number"],
        "return": None
    },
    "right": {
        "parameters": ["number"],
        "return": None
    },
    "show": {
        "parameters": ["any"],
        "return": None
    },
    "repeat": {
        "parameters": ["number", "codeblock"],
        "return": None
    }
}


LOGO_FUNCTIONS_FIN = {
    "neliö": {
        "parameters": ["number"],
        "return": "number"
    },
    "summa": {
        "parameters": ["number", "number"],
        "return": "number"
    },

    "eteen": {
        "parameters": ["number"],
        "return": None
    },
    "taakse": {
        "parameters": ["number"],
        "return": None
    },
    "vasemmalle": {
        "parameters": ["number"],
        "return": None
    },
    "oikealle": {
        "parameters": ["number"],
        "return": None
    },
    "tulosta": {
        "parameters": ["any"],
        "return": None
    },
    "toista": {
        "parameters": ["number", "codeblock"],
        "return": None
    }
}

LOGO_FUNCTIONS = {**LOGO_FUNCTIONS_FIN, **LOGO_FUNCTIONS_ENG}
