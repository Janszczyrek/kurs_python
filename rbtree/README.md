#   Projekt zaliczeniowy kursu z języka Python 23/24 
#   Autor: Janusz Waluś

## Wprowadzenie
Implementacja drzewa czerwono-czarnego obsługującego operacje insert, search oraz clear.
Projekt w dużej mierze bazuje na implementacji ze strony [geeksforgeeks](https://www.geeksforgeeks.org/introduction-to-red-black-tree)
która została zmodyfikowana oraz uzupełniona o metodę zwracającą czarną wysokośc drzewa, generatory pozwalające iterować po drzewie
w kolejności preorder, inorder i postorder, oraz testy sprawdzające, czy podane drzewo spełnia własności czerwono-czarne.

Drzewa czerwono-czarne są samobalansującymi drzewami poszukiwania binarnego spełniającymi następujące własności:
    1. Każdy węzeł jest czerwony lub czarny.
    2. Korzeń drzewa jest czarny.
    3. Czerwony węzeł nie ma czerwonego syna.
    4. Ścieżki z dowolnego węzła do liści przechodza przez tą samą ilość czarnych węzłów.
Wymagania te gwarantują, że drzewo czerwono-czarne ma wysokość co najwyżej 2log(n+1).
Drzewa te dzięki mniejszej ilości rotacji niezbędnych do spełnienia powyższych warunków są wydajniejsze od drzew AVL w zastosowaniach wymagających więcej operacji wstawiania oraz usuwania niż wyszukiwania.

## Opis interfejsu

```python
    def insert(self: Self@RBtree, *values: Any) -> None:
```
 Dodaje do istniejącego drzewa węzeł o podanej wartości.


```python
    def search(self: Self@RBtree, data: Any) -> Any:
```
Zwraca pierwszy napotkany węzeł o podanej wartości lub None w przypadku jego braku.


```python
    def clear(self: Self@RBtree) -> None:
```
Ustawia None jako korzeń drzewa oraz resetuje jego wewnętrzny stan.


```python
    def inorder_traverse(self: Self@RBtree,node: Any) -> Generator[Any, Any, None]:

    def preorder_traverse(self: Self@RBtree,node: Any) -> Generator[Any, Any, None]:

    def postorder_traverse(self: Self@RBtree,node: Any) -> Generator[Any, Any, None]:
```
Zwracają generatory przechodzące drzewo o zadanym korzeniu w podanej kolejności.


```python
    def tree_print(self: Self@RBtree) -> None:
```
Wypisuje drzewo semigraficzne.


```python
    def inorder_print(self: Self@RBtree) -> None:

    def preorder_print(self: Self@RBtree) -> None:

    def postorder_print(self: Self@RBtree) -> None:
```
Wypisuje informacje o węzłach drzewa w podanej kolejności.


```python
    (property) black_height: (self: Self@RBtree) -> (Any | Literal[0, -1])
```
Zwraca ilość czarnych węzłów na dowolnej scieżce z korzenia do liścia.


```python
    (property) is_empty: (self: Self@RBtree) -> bool
```
Zwraca True jeżeli drzewo puste, False w przeciwnym wypadku.

## Działanie
Implementacja bazuje na klasie RBnode przechowującej dane, kolor, informacje o rodzicu i dzieciach każdego węzła oraz z klasy RBtree zawierającej węzeł będący korzeniem, flagi określające aktualny stan zbalansowania drzewa oraz metody służące do modyfikacji i przeglądania drzewa.


## Przykład użycia

```python
    from rbtree import RBtree

    tree = RBtree()

    # Dodaj elementy do drzewa
    tree.insert(10)
    tree.insert(20)
    tree.insert(5)
    tree.insert(55)

    # Wypisz węzły w zadanej kolejności
    tree.preorder_print()
    tree.inorder_print()
    tree.postorder_print()

    # Wypisz drzewo semigraficznie
    tree.tree_print()

    # Wyszukaj pierwszy węzeł o podanej wartości i zwróć go
    node5 = tree.search(5)
    print(node5)

    # Wyczyść drzewo
    print(tree.is_empty)
    tree.clear()
    print(tree.is_empty)
```