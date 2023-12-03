import scraper


def test_nvidia_availability():
    url = "https://store.nvidia.com/nl-nl/geforce/store/?page=1&limit=9&locale=nl-nl"
    task = scraper.Nvidia4090Available(url=url)

    scraper.Scraper().do_task(task)
