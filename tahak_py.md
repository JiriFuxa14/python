# **Tahák na python**
## *Jiří Fuxa a Radek Gablas*
***Seznam příkazů a co dělají***
- **print** - Příkaz print vytiskne to co je dáno do závorky za ním.
  příklad:
  ```python 
  print(65)
  ```
- **for, while, range** - prochází prvky v daném poli, tento příkaz použijeme jen když víme kolikrát se cyklus bude opakovat, jinak používáme while. Příkaz range se hodně často používá vedle for, range vrátí čísla v uvedeném rozsahu (intervalu)
  
  příklad:
  ```python
  for x in range(1, 7):
      print(x)
  ```
Tento kód nám vrátí čísla 1-6.

- **Stringy** - je datový typ, ve kterém je ukládán převážně text, je ohraničen uvozovkama nebo apostrofem.
  příklad:
  ```python
  x = "sigma"
  y = 'jablko'
  print(x + y)
  ```
- **Proměnné** - jsou takové kontejnery, které ukládají data. Kde je použijeme? 
  například:
  ```python
  x = 5
  print(x)
  ```
  - tento kód nám vrátí integer uložený v proměnné x (zde 5)

- **if, else** - if je v angličtině jestli, else je jinak, tyto příkazy se používají jako podmínky, například:
  ```python
    x = 7
    y = 14
    if x > y:
        print("X je větší než Y")
    else: 
        print(" Y je větší než X")
     ```

- **input** - zeptá se uživatele aby zadal na vstup nějaké informace, například:
  ```python
  input("Zadejte číslo od 5-53: ")
  ```

  - **Aritmetické operace** - v pythonu se dá operovat stejně jako v matematice. Pro počítání používáme znaménka +, -, *, / . Pro mocniny se používá ** a pro odmocniny buď math.sqrt (musí se definovat složka math před tím) nebo **0.5. Python má svá pravidla. Ukažme si, jak počítat například se stringy a proměnnými.
  příklad:
  ```python
  x = 5
  y = 8
  print(x * y)
   ```

    ```python
    x = 9
    y = x**0.5
    print(y)
     ```

- **Funkce** - Funkce v pythonu se vytváří pomocí příkazu def, kde definujeme tuto funkci. Když chceme funkci zavolat, použijeme jméno funkce a za ním prázdné závorky () .
příklad:

  ```python
  def funkce_1():
    print("Dobrý den")

  funkce_1()
  ```

    









  



