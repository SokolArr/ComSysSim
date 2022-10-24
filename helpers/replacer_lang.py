import shutil
def change_to_RUS():
  shutil.copy('./ui_components/languages/ru_lang.ui', './ui_components/actual_lang.ui')
  shutil.copy('./ui_components/languages/ui_ru_lang.py', './ui_components/ui_actual_lang.py')

  print("change_to_RUS")
  
def change_to_ENG():  
  shutil.copy('./ui_components/languages/en_lang.ui', './ui_components/actual_lang.ui')
  shutil.copy('./ui_components/languages/ui_en_lang.py', './ui_components/ui_actual_lang.py')
  
  print("change_to_ENG")
