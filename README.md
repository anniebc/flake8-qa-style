# flake8-2gis-style

Плагин для flake8

Игнорирование правил стандартное для flake8:
- через файл `setup.cfg` и параметра `ignore`
- через комментарий `#noqa: CS001`


## История
### Версия 0.0.1

Валидация файлов по следующим [правилам](flake8_2gis_style/errors/errors.py)

Возможности конфигурации в `setup.cfg`:


```
[flake8]

;для методов с декоратором @property опускаем проверку типизации возвращаемого значения
skip_property_return_annotation = true
```