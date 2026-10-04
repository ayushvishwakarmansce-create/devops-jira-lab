import os

def test_page_exists():
    assert os.path.exists("index.html")

if __name__ == "__main__":
    test_page_exists()
    print("Page load test passed!")
