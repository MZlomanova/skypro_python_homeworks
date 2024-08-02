from string_utils import StringUtils
utils = StringUtils()

# проверки capitalize
def test_capitalize():
    #позитивные
    assert utils.capitilize("москва") == "Москва" #проверка кирилицы и преобразование в заглавную
    assert utils.capitilize("singapur") == "Singapur" #проверка латиницы
    assert utils.capitilize("12345")== "12345" #проверка на цифрах
    #негативные
    assert utils.capitilize("_-_") == "_-_" #не буквенные символы
    assert utils.capitilize("123tebmk34") == "123tebmk34"
    assert utils.capitilize("") == "" #проверка пустоты

#проверки функции trim

def test_trim():
    #позитивные проверки:
    assert utils.trim(" один") == "один"
    assert utils.trim("             много") == "много"
    assert utils.trim("   между  ") == "между  "
    
    #негативные
    assert utils.trim("") == ""
    
#проверка to_list
def to_list():
    #позитивные проверки
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("слово раз","слово два","слово три") == ["слово раз", "слово два", "слово три"]
    assert utils.to_list("@","!","&") == ["@", "!", "&"] 
    
    #негативные проверки
    
    assert utils.to_list(None, None) == None, None
    assert utils.to_list("a","b", None) == ["a", "b"]
    
#проверка contains
def contains():
    #позитивные проверки
    assert utils.contains("линкедин", "л") == True
    assert utils.contains("компьютер", "р") == True
    assert utils.contains("амиго", "и") == True
    assert utils.contains("") == True
    
    #негативные проверки
    
    assert utils.contains("0000", "h") == False
    assert utils.contains("", "a") == False
    assert utils.contains("око", "c") == False
    assert utils.contains("lol", "@") == False
    assert utils.contains("aloha", "") == False
    
#проверка delete symbol

def delete_symnbol():
    #позитивные проверки
    assert utils.delete_symbol("яхта", "х") == "ята"
    assert utils.delete_symbol("кот", "к") == "от"
    assert utils.delete_symbol("101", "0") == "11"
    assert utils.delete_symbol("Гребной Канал", "") == "ГребнокКанал"
    
    assert utils.delete_symbol("собака", "y") == "собака"
    assert utils.delete_symbol(" поле", " ") == "поле"
    assert utils.delete_symbol(" кошка ", " ") == "кошка"
    assert utils.delete_symbol("", "x") == ""
    
#проверка starts with
def starts_with():
    #позитивные проверки:
    assert utils.starts_with("алохомора", "а") == True
    assert utils.starts_with("kitchen", "k") == True
    assert utils.starts_with_with("@$#%&$%", "@") == True
    assert utils.starts_with("","") == True
    assert utils.starts_with("1floor", "1") == True
    #негативные проверки
    assert utils.starts_with("зумба","y") == False
    assert utils.starts_with("", "f") == False
    assert utils.starts_with("масло", "в") == False
    assert utils.starts_with("лед", "Л") == False
    
#проверка end_with
def end_with():
    #позитивные проверки
    assert utils.end_with("аллея", "я") == True
    assert utils.end_with("house", "e") == True
    assert utils.end_with("ярмарка ", " ") == True
    assert utils.end_with("агент007", "7") == True
    assert utils.end_with("","") == True
    
    #негативные проверки
    assert utils.end_with("солнце", "ц") == False
    assert utils.end_with("Бельгия", "о") == False
    assert utils.end_with("solo", "о") == False #исходное слово латиницей, последняя буква в запросе кириллицей
    assert utils.end_with("ямБ", "б") == False
    
#проверка is_empty
def is_empty():
    #позитивные
    assert utils.is_empty("") == True
    assert utils.is_empty("  ") == True
    assert utils.is_empty("              ") == True
    
    #негативные проверки
    assert utils.is_empty("что-то густо") == False
    assert utils.is_empty("  а не пусто") == False
    assert utils.is_empty("_") == False
    assert utils.is_empty("000") == False
    
#проверка list_to_string
def list_to_string():
    #позитивные
    assert utils.list_to_string(["p", "o", "w", "e", "r"], "") == "p, o, w, e, r"
    assert utils.list_to_string(["м", "ё", "д"], "") == "м, ё, д"
    assert utils.list_to_string([0, 1, 2, 3], None) == "0, 1, 2, 3"
    assert utils.list_to_string(["Нижний", "Новгород"], " ") == "Нижний Новгород"
    assert utils.list_to_string(["перво", "наперво"], "-") == "перво-наперво"
    assert utils.list_to_string(["д","о", "м"], "") == "дом"
    
    #негативные
    assert utils.list_to_string([], None) == ""
    assert utils.list_to_string([], "!") == ""
    assert utils.list_to_string([], " ") == ""
    assert utils.list_to_string([], "разделитель") == ""



    
    
    