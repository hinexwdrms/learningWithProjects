#unit conversion values:
length_dict = {
    'meters': {
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371,
        'inches': 39.3701
    },
    'kilometers': {
        'meters': 1000,
        'kilometers': 1,
        'miles': 0.621371,
        'inches': 39370.1
    },
    'miles': {
        'meters': 1609.34,
        'kilometers': 1.60934,
        'miles': 1,
        'inches': 63360
    },
    'inches': {
        'metres': 0.0254,
        'kilometers': 0.0000254,
        'miles': 0.000015783,
        'inches': 1
    }
}

weight_dict = {
    'kilograms': {
        'kilograms': 1,
        'grams' : 1000,
        'milligrams': 1000000,
        'pounds': 2.20462,
        'ounces': 35.274
    },
    'grams': {
        'kilograms': 0.001,
        'grams': 1,
        'milligrams': 1000,
        'pounds': 0.00220462,
        'ounces': 0.035274
    },
    'milligrams': {
        'kilograms': 0.000001,
        'grams': 0.001,
        'milligrams': 1,
        'pounds': 0.00000220462,
        'ounces': 0.000035274
    },
    'pounds': {
        'kilograms': 0.453592,
        'grams': 453.592,
        'milligrams': 453592,
        'pounds': 1,
        'ounces': 16
    },
    'ounces': {
        'kilograms': 0.0283495,
        'grams': 28.3495,
        'milligrams': 28349.5,
        'pounds': 0.0625,
        'ounces': 1
    }
}
