

def build_code(prefix, base_num, code, model_prefix=None):
    """Generate Codes"""
    NONE_MODEL_PERFIX = 'GE'
    return "{0}{1}{2}{3}".format(
        prefix,
        model_prefix or NONE_MODEL_PERFIX,
        base_num,
        code
    )


class ServerCodes:

    PREFIX = 'SE'
    BASE_NUM = 0

    SERVER_UNAVAILABLE = build_code(prefix=PREFIX, base_num=BASE_NUM, code='0')


class GeneralCodes:

    PREFIX = 'GE'
    BASE_NUM = 1

    SUCCESS = build_code(prefix=PREFIX, base_num=BASE_NUM, code='0')
    INVALID_DATA = build_code(prefix=PREFIX, base_num=BASE_NUM, code='1')
    NOT_FOUND = build_code(prefix=PREFIX, base_num=BASE_NUM, code='2')


class UserCodes:

    PREFIX = "US"
    BASE_NUM = 2

    INVALID_CREDENTIALS = build_code(
        prefix=PREFIX,
        base_num=BASE_NUM,
        code='0',
        model_prefix='US'
    )
    PASSWORD_NOT_MATCH = build_code(
        prefix=PREFIX,
        base_num=BASE_NUM,
        code='1',
        model_prefix='US'
    )


def response_codes():
    exclude_fields = [
        'PREFIX',
        'BASE_NUM'
    ]
    classes = [
        ServerCodes,
        GeneralCodes,
        UserCodes
    ]
    all_codes = []

    for _class in classes:
        codes = {
            v: getattr(_class, v)
            for v in dir(_class)
            if not callable(getattr(_class, v)) and v.isupper() and v not in exclude_fields
        }
        if codes:
            all_codes.append(
                {
                    'name': str(_class.__name__),
                    'codes': codes
                }
            )
    return all_codes
