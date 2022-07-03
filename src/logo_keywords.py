'''
This module contains all of the keywords, symbols, parameter types and functions that the compiler accepts
'''

LOGO_KEYWORDS_FIN = {
    'eteen':'float',
    'taakse':'float',
    'oikealle':'float',
    'vasemmalle':'float',
    'tulosta':'string',
    'olkoon':'string'
    }

LOGO_KEYWORDS_ENG = {
    'forward':'float',
    'back':'float',
    'right':'float',
    'left':'float',
    'show':'string',
    'make':'string'
    }

LOGO_KEYWORDS_BINARY_OPERATIONS = {
    '+':'plus',
    '-':'minus',
    '*':'multiply',
    '/':'divide',
    }

LOGO_KEYWORDS_SYMBOLS = {
    '(':'left_paren',
    ')':'right_paren'
    }

LOGO_KEYWORDS_MATH_FUNCTIONS = {
    'sqrt':'square_root'
    }

LOGO_KEYWORDS = {}
LOGO_KEYWORDS.update(LOGO_KEYWORDS_FIN)
LOGO_KEYWORDS.update(LOGO_KEYWORDS_ENG)

LOGO_ALL = LOGO_KEYWORDS
LOGO_ALL.update(LOGO_KEYWORDS_SYMBOLS)
LOGO_ALL.update(LOGO_KEYWORDS_MATH_FUNCTIONS)
