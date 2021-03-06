from jwt_auth.errors import (
    NOT_AUTHENTICATED,
    AUTHENTICATION_FAILED,
    TOKEN_INVALID,
)

error_code_map = {
    'not_authenticated': NOT_AUTHENTICATED,
    'authentication_failed': AUTHENTICATION_FAILED,
}


def map_error_codes(codes, default=None):
    """
    Take in get_codes() value of drf exception
    and return a corresponding internal error code.
    """

    if isinstance(codes, str):
        return error_code_map.get(codes, default)

    if codes == {'non_field_errors': ['invalid']}:
        return TOKEN_INVALID

    return default
