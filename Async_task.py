import asyncio
import aiohttp

async def fetch(session, url, timeout_seconds=10):
    """
    Выполняет один HTTP-запрос, возвращая статус или ошибку.
    """
    try:
        async with session.get(url, timeout=timeout_seconds) as response:
            return response.status
    except Exception as e:
        # Возвращает текст ошибки, чтобы было видно, что случилось
        return f"Error: {str(e)}"

async def main(requests_amount, requests_limit, urls, output_file):
    """
    Отправляет requests_amount запросов по списку urls (можно один),
    ограничивая одновременно requests_limit.
    Результаты записывает в файл.
    """
    semaphore = asyncio.Semaphore(requests_limit)

    async with aiohttp.ClientSession() as session:
        tasks = []

        async def bounded_fetch(url):
            # Используем семафор чтобы ограничить число одновременных запросов
            async with semaphore:
                status = await fetch(session, url)
                return (url, status)

        # Распределяем запросы по URL
        for _ in range(requests_amount):
            # Выбираем рандомно или последовательно, здесь — по кругу
            for url in urls:
                tasks.append(asyncio.create_task(bounded_fetch(url)))

        # Ждём завершения всех задач
        results = await asyncio.gather(*tasks)

        # Запись результатов в файл
        with open(output_file, 'w', encoding='utf-8') as f:
            for url, status in results:
                if isinstance(status, int):
                    f.write(f"{url} - Status: {status}\n")
                else:
                    f.write(f"{url} - {status}\n")


# Пример запуска:
if __name__ == "__main__":
    requests_amount = 50  # Общее число запросов
    requests_limit = 10   # Лимит одновременных запросов
    urls = ["http://google.com", "https://example.com/"]  # список URL
    output_file = "statuses.log"

    asyncio.run(main(requests_amount, requests_limit, urls, output_file))