import pytest
import tempfile
import shutil

@pytest.fixture(scope="module", autouse=True)
def dir(request):
    dir = tempfile.mkdtemp()
    def cleanup():
        shutil.rmtree(dir)
    request.addfinalizer(cleanup)
    return dir

def test_one(dir):
    assert True

