# CaesarCipherScript

## Pruebas realizadas 
En el presente modulo se presentan las evidencias de las pruebas realizadas 
### 1) Número fuera de las opciones
¿Qué pasa si ingreso un numero de opción que no existe? 
<img width="1911" height="473" alt="image" src="https://github.com/user-attachments/assets/bd9356f0-b022-4ede-b11a-3b2aaaf22978" />
Directamente me dice que es una opción invalida y no me deja avanzar hasta que ingrese una opción válida.
### 2) Caracter fuera del alfabeto
¿Qué pasa si ingreso un caracter fuera del alfabeto? 
<img width="1911" height="578" alt="image" src="https://github.com/user-attachments/assets/d90f73db-c96d-45b5-af4d-d0b8b44b1e30" />
No rompe el programa, pero tampoco lo encripta, lo que es esperable deacuerdo a la naturaleza del cifrado Cesar
### 3) Carácter cuando se esperaba un número
¿Qué pasa si escribo una cadena de texto y esperaba un número? 
<img width="1913" height="916" alt="image" src="https://github.com/user-attachments/assets/54128d26-8ec1-449b-a8ca-7e9064f0c831" />
El Script sabe que está mal, por lo que no me deja avanzar hasta que ingrese un entero valido dentro del rango 

### 4) Carácter en clave 
¿Qué pasa si ingreso una cadena de texto de clave?
<img width="1913" height="733" alt="image" src="https://github.com/user-attachments/assets/f78e9b02-eeed-411a-abfb-80d20d5d84ec" />
El Script sabe que está mal, por lo que no me deja avanzar hasta que ingrese un entero positivo

### 5) Clave negativa 
¿Qué pasa si escribo un entero negativo? 
<img width="1913" height="733" alt="image" src="https://github.com/user-attachments/assets/ca2e82d0-7757-4ad4-8606-2edd293ed56a" />
