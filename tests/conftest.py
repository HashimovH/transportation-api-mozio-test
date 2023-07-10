from pytest import fixture
import os


@fixture(scope='session')
def vcr_config():
    return {
        "match_on": ["method", "uri", "body", "headers"],
        "record_mode": "once",
        "decode_compressed_response": True
    }


@fixture(scope='module')
def vcr_cassette_dir(request):
    test_root = os.path.dirname(__file__)
    print(test_root)
    print(request.fspath)
    relative_test_file_location = (
        str(request.fspath)
        .removeprefix(test_root)
        .removesuffix(".py")
        .removeprefix("/")
    )
    print(relative_test_file_location)
    return test_root + "\\cassettes" + relative_test_file_location
