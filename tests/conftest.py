import os

from pytest import fixture


@fixture(scope="session")
def vcr_config():
    return {
        "match_on": ["method", "uri", "body", "headers"],
        "record_mode": "once",
        "decode_compressed_response": True,
    }


@fixture(scope="module")
def vcr_cassette_dir(request):
    test_root = os.path.dirname(__file__)
    relative_test_file_location = (
        str(request.fspath)
        .removeprefix(test_root)
        .removesuffix(".py")
        .removeprefix("/")
    )
    return test_root + "\\cassettes" + relative_test_file_location
