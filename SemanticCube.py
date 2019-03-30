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