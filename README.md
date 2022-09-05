# 📡 ComSysSim

## О программе

+

+
---

## Планы
> + ПО будет основываться на популярной библиотеке PyQt5
> + Будет реализован режим симуляции и изменяемыми параметрами у блоков

---
## Установка
### Python
>[🔗 Ссылка на официальный сайт ](https://www.python.org/downloads/ "Python")

### Qt Designer
>[🔗 Ссылка на официальный сайт ](https://build-system.fman.io/qt-designer-download "Qt Designer")


### PyQt5

```console
pip install PyQt5
```

---
## Зависимости
### Pyqtgraph
Для графиков
```
pip install pyqtgraph
```

### pyqt5-tools
Для сборки UI
```
pip install pyqt5-tools
```

### Pyinstaller
Для сборки
```
pip install pyinstaller
```

---
### Сборка проекта
#### Для сборки UI
```
pyuic5 test_gui.ui > test_gui.py
```
#### Для сборки exe
```
pyinstaller main.py --onefile -windowed
```

