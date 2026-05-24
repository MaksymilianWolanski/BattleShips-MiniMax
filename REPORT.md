# REPORT

## Opis projektu

Celem projektu było stworzenie prostego AI do gry Statki.

## Algorytm

W projekcie wykorzystano uproszczoną wersję algorytmu Minimax dostosowaną do gry z niepełną informacją.

AI:
- analizuje możliwe ruchy,
- wykorzystuje funkcję heurystyczną,
- preferuje pola obok wcześniejszych trafień.

## Testy

Sprawdzono:
- poprawność ustawiania statków,
- trafienia i pudła,
- zakończenie gry,
- działanie AI,
- poprawność funkcji planszy i heurystyki.

## Wyniki

Gra działa poprawnie w terminalu.
AI podejmuje decyzje na podstawie heurystyki.
Precyzyjniej, zaczyna od środka planszy, a po zatopieniu jednego statku, próbuje znaleźć następny w okolicy.

## Wnioski

Uproszczony Minimax pozwala stworzyć działające AI dla gry z ukrytą informacją przy zachowaniu niewielkiej złożoności projektu.