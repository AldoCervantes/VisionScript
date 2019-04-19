class SemanticCube:
    semanticCube = {
            '+':{
                'number':{ 
                            'number': 'number',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'

                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'text',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'container',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            },
            '-':{
                'number':{ 
                            'number': 'number',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            },
            '*':{
                'number':{ 
                            'number': 'number',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            },
            '/':{
                'number':{ 
                            'number': 'number',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            },
            '>':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            },
            '<':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            },
            '>=':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            },
            '<=':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            },
            'equal':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'bool',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'bool',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            },
            'not_equal':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'bool',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'bool',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            },
            'or':{
                'number':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'bool',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            },
            'and':{
                'number':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'bool',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                },
                'error':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error',
                            'error' : 'error'
                }
            }
        }

    opToKey = {
        '=':0,
        '+':1,
        '-':2,
        '*':3,
        '/':4,
        '>':5,
        '<':6,
        '>=':7,
        '<=':8,
        'equal':9,
        'not_equal':10,
        'and':11,
        'or':12,
        'GotoF':13,
        'Goto':14,
        'print':15,
        'hear':16,
        'braille':17,
        'read':18,
        'return':19
    }

    TypeToKey = {
        'number':101,
        'text':102,
        'bool':103,
        'container':104,
        'error':105
    }