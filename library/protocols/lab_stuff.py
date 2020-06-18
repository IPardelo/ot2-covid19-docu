# following volumes in ul
def brands(brand_name):
    brands = {
        'seegene': {
           'mastermix': 17,
            'arn': 8
        },
        'thermofisher': {
            'mastermix': 15,
            'arn': 10
        },
        'roche': {
            'mastermix': 10,
            'arn': 10
        },
        'vircell': {
            'mastermix': 15,
            'arn': 5
        }
    }
    mastermix = brands.get(brand_name).get('mastermix')
    arn = brands.get(brand_name).get('arn')
    return mastermix, arn

#def tubes(tube_tipe):
#
#    return