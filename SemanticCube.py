class SemanticCube:
    semanticCube = {
            '+':{
                'number':{ 
                            'number': 'number',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'text',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'container'
                }
            },
            '-':{
                'number':{ 
                            'number': 'number',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                }
            },
            '*':{
                'number':{ 
                            'number': 'number',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                }
            },
            '/':{
                'number':{ 
                            'number': 'number',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                }
            },
            '>':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                }
            },
            '<':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                }
            },
            '>=':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                }
            },
            '<=':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                }
            },
            'equal':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'bool',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                }
            },
            'not_equal':{
                'number':{ 
                            'number': 'bool',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'bool',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                }
            },
            'or':{
                'number':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'bool',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                }
            },
            'and':{
                'number':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'bool':{ 
                            'number': 'error',
                            'bool'  : 'bool',
                            'text'  : 'error',
                            'container': 'error'
                },
                'text':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                },
                'container':{ 
                            'number': 'error',
                            'bool'  : 'error',
                            'text'  : 'error',
                            'container': 'error'
                }
            }
        }