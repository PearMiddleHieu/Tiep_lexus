import time
from reader import feed
def main():
    tic = time.perf_counter()
    tutorial = feed.get_article(0)
    toc =