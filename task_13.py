import time
from collections import OrderedDict


def cached(max_size=None, seconds=None):
    # Проверяем и нормализуем параметры
    if not isinstance(max_size, int) and max_size is not None:
        max_size = None
    if not isinstance(seconds, (int, float)) and seconds is not None:
        seconds = None

    def decorator(func):
        # Используем OrderedDict для хранения в порядке добавления
        cache = OrderedDict()

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            current_time = time.time()

            #Очищаем устаревшие записи (по времени)
            if seconds is not None:
                keys_to_remove = []
                for k, value in cache.items():
                    if current_time - value['timestamp'] > seconds:
                        keys_to_remove.append(k)

                for k in keys_to_remove:
                    del cache[k]

            #Проверяем, есть ли результат в кэше
            if key in cache:
                # Обновляем порядок (делаем запись "самой новой" при обращении)
                value = cache.pop(key)
                cache[key] = value
                return value['result']

            #Если нет в кэше - вычисляем
            result = func(*args, **kwargs)

            #Очищаем, если превышен max_size
            if max_size is not None and len(cache) >= max_size:
                # Удаляем самую старую запись (первую в OrderedDict)
                cache.popitem(last=False)

            #Сохраняем результат
            cache[key] = {
                'result': result,
                'timestamp': current_time
            }

            return result

        # Добавляем вспомогательные методы для тестирования
        wrapper.cache = cache
        wrapper.clear_cache = lambda: cache.clear()

        return wrapper

    return decorator


if __name__ == "__main__":
    @cached(max_size=3, seconds=10)
    def slow_function(x):
        print(f"Вычисляю для {x}...")
        return x ** 2


    print("=== Тест 1: Базовое кэширование ===")
    print(slow_function(2))  # Вычисляю для 2... → 4
    print(slow_function(2))  # 4 (из кэша)
    print(slow_function(3))  # Вычисляю для 3... → 9
    print(slow_function(3))  # 9 (из кэша)

    print("\n=== Тест 2: Ограничение размера (max_size=3) ===")
    print(slow_function(4))  # Вычисляю для 4... → 16
    # Теперь в кэше: 2, 3, 4
    print(slow_function(5))  # Вычисляю для 5... → 25
    # Должна удалиться самая старая запись (2)
    print("Кэш:", [(key[0][0], value['result']) for key, value in slow_function.cache.items()])

    print("\n=== Тест 3: Разные аргументы ===")


    @cached(max_size=5, seconds=30)
    def complex_function(a, b, multiplier=1):
        print(f"Вычисляю {a} * {b} * {multiplier}...")
        return a * b * multiplier


    print(complex_function(2, 3))  # Вычисляю 2 * 3 * 1... → 6
    print(complex_function(2, 3))  # 6 (из кэша)
    print(complex_function(2, 3, multiplier=2))  # Вычисляю 2 * 3 * 2... → 12
    print(complex_function(2, 3, multiplier=2))  # 12 (из кэша)

    print("\n=== Тест 4: Проверка времени жизни ===")


    @cached(seconds=2)
    def timed_function(x):
        print(f"Вычисляю {x}...")
        return x * 10


    print(timed_function(1))  # Вычисляю 1... → 10
    print(timed_function(1))  # 10 (из кэша)

    print("Ждем 3 секунды...")
    time.sleep(3)

    print(timed_function(1))  # Вычисляю 1... → 10 (кэш устарел)