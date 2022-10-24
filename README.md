# 📡 ComSysSim

### О программе:

"Универсальная система модели цифровой связи для изучения способов модуляции сигналов"
---

### Реализация
> + ✔ ПО основывается на популярной библиотеке PyQt
> + ✔ Реализован режим симуляции и изменяемыми параметрами (настройками)

---
## Установка
### Python
>[🔗 Ссылка на официальный сайт ](https://www.python.org/downloads/ "Python")

### Qt Designer
>[🔗 Ссылка на официальный сайт ](https://build-system.fman.io/qt-designer-download "Qt Designer")


### PyQt6

```console
pip install PyQt6
```

---
## Зависимости
---
### **Библиотеки:**
### Matplotlib
Для графиков **matplotlib 3.6.1**
```
pip install matplotlib
```

### Numpy
Для работы с данными **numpy 1.23.4**
```
pip install numpy
```

### ModulationPy
Цифровые модемы M-PSK и M-QAM **ModulationPy 0.1.8**
```
pip install ModulationPy
```
---
### **Для сборки проекта:**

### pyqt6-tools
Для сборки UI
```
pip install pyqt6-tools
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
pyuic6 test_gui.ui > test_gui.py
```
#### Для сборки exe
```
pyinstaller main.py --onefile -windowed
```

