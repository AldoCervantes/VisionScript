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
        'GotoV':14,
        'Goto':15,
        'print':16,
        'hear':17,
        'braille':18,
        'read':19,
        'return':20,
        'ERA':21,
        'param':22,
        'gosub':23,
        'append':24,
        'concat':25,
        'insert':26,
        'insert_back':27,
        'insert_front':28,
        'get':29,
        'get_back':30,
        'get_front':31,
        'length':32,
        '[]':33,
        'ENDPROC':34
    }

    TypeToKey = {
        'number':101,
        'text':102,
        'bool':103,
        'container':104,
        'error':105,
        'op_container':106
    }