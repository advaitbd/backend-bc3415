from news.services import NewsService

class NewsController:
    @staticmethod
    def fetch_news():
        NewsService.fetch_and_store_news()

    @staticmethod
    def get_all_news():
        return NewsService.get_news()
