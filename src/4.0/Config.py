def getConfigs():
    configurations = {
        'fullmandelbrot': {
            'centerX': -0.6,
            'centerY': 0.0,
            'axisLength': 2.5,
            'type': 'mandelbrot',

            },

        'spiral0': {
            'centerX': -0.761335372924805,
            'centerY': 0.0835704803466797,
            'axisLength': 0.004978179931102462,
            'type': 'mandelbrot',
            },

        'spiral1': {
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLength': 0.002,
            'type': 'mandelbrot',
            },

        'seahorse': {
            'centerX': -0.745,
            'centerY': 0.105,
            'axisLength': 0.01,
            'type': 'mandelbrot',
            },

        'elephants': {
            'centerX':  0.30820836067024604,
            'centerY':  0.030620936230004017,
            'axisLength':  0.03,
            'type': 'mandelbrot',
            },

        'leaf': {
            'centerX': -1.543577002,
            'centerY': -0.000058690069,
            'axisLength':  0.000051248888,
            'type': 'mandelbrot',
            },

        'fulljulia': {
            'centerX': 0.0,
            'centerY': 0.0,
            'axisLength': 4.0,
            'type': 'julia',
        },

        'hourglass': {
            'centerX': 0.618,
            'centerY': 0.00,
            'axisLength': 0.017148277367054,
            'type': 'julia',
        },

        'lakes': {
            'centerX': -0.339230468501458,
            'centerY': 0.417970758224314,
            'axisLength': 0.164938488846612,
            'type': 'julia',
        },
    }
    return configurations