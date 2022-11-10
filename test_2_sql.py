# 1. Напишите запрос, который подсчитает какое количество ноутбуков представлено в каждом бренде. Отсортируйте данные по убыванию.

("SELECT notebooks_brand.title, COUNT(notebooks_brand.title)\n"
 "FROM notebooks_brand\n"
 "INNER JOIN notebooks_notebook ON notebooks_notebook.brand_id=notebooks_brand.id\n"
 "GROUP BY notebooks_brand.title\n"
 "ORDER BY count DESC")

# SELECT notebooks_brand.title, COUNT(notebooks_brand.title)
# FROM notebooks_brand
# INNER JOIN notebooks_notebook ON notebooks_notebook.brand_id=notebooks_brand.id
# GROUP BY notebooks_brand.title
# ORDER BY count DESC

# 2. Вам необходимо выделить группы ноутбуков по размерам.
# Для этого размеры предварительно нужно округлить в большую сторону до ближайшего 0 или 5 и затем сгруппировать по одинаковым размерам,
# подсчитав количество ноутбуков в каждой группе. Отсортируйте данные по размерам.

# Сделал 2 разных запроса т.к. не понял как считать размер.

# 1 запрос
("SELECT ROUND(diagonal), COUNT(diagonal) FROM notebooks_notebook\n"
 "GROUP BY round\n"
 "ORDER BY round")

# SELECT ROUND(diagonal), COUNT(diagonal) FROM notebooks_notebook
# GROUP BY round
# ORDER BY round

# 2 запрос
("SELECT ROUND(width) as width, ROUND(height) as height, ROUND(depth) as depth, COUNT(*)"
 "FROM notebooks_notebook"
 "GROUP BY width, height, depth"
 "ORDER BY count")

# SELECT ROUND(width) as width, ROUND(height) as height, ROUND(depth) as depth, COUNT(*)
# FROM notebooks_notebook
# GROUP BY width, height, depth
# ORDER BY count
