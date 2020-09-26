#Desafio URI ONLINE 1049
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1049
A=input()
B=input()
C=input()

if A == 'vertebrado' and B == 'ave' and C == 'carnivoro':
    D = 'aguia'
if A == 'vertebrado' and B == 'ave' and C == 'onivoro':
    D = 'pomba'
if A == 'vertebrado' and B == 'mamifero' and C == 'onivoro':
    D = 'homem' 
if A == 'vertebrado' and B == 'mamifero' and C == 'herbivoro':
    D = 'vaca'
if A == 'invertebrado' and B == 'inseto' and C == 'hematofago':
    D = 'pulga' 
if A == 'invertebrado' and B == 'inseto' and C == 'herbivoro':
    D = 'lagarta' 
if A == 'invertebrado' and B == 'analideo' and C == 'hematofago':
    D = 'sanguessuga' 
if A == 'invertebrado' and B == 'analideo' and C == 'onivoro':
    D = 'minhoca'
print(D)
