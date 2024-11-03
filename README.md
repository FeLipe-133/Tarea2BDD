# Gastos Compartidos

## Descripción
Este es un proyecto para el ramo Base de datos 2

## Objetivo

Aplicar conocimientos de desarrollo de APIs REST utilizando Litestar y SQLAlchemy.

## Descripción

La construcción de esta API aborda una aplicación de gastos compartidos. Es decir, permite el registro de compras realizadas en un grupo de personas, donde una paga el monto total y el resto le paga a él.

En el repositorio [github.com/dialvarezs/hw2-bd2-2024](https://github.com/dialvarezs/hw2-bd2-2024) encontrarás el código base para esta tarea. Ya hay varias funciones implementadas, como la gestión de usuarios y creación básica de gastos. El esquema de datos consiste en:

- **users**: contiene la información de los usuarios: nombre, contraseña, etc.
- **expenses**: contiene los gastos generados. Cada gasto registra quién lo creó (`created_by`), el monto total, la fecha y una descripción.
- **debts**: contiene la información de las deudas asociadas a cada gasto. Cada deuda registra el usuario asociado, el monto de la deuda y si esta fue pagada.

Al ingresar un nuevo gasto, el usuario que lo crea selecciona qué usuarios forman parte del gasto. El sistema registra el gasto y genera deudas para cada uno de los usuarios por el total dividido el número de usuarios (contando al que creó el gasto).

Por ejemplo, si Juan crea un gasto de $20.000 en el que participaron Pedro, Catalina y Constanza, el sistema ingresará una deuda de $5.000 a Pedro, Catalina y Constanza. La petición en formato JSON debería parecerse a lo siguiente (asumiendo que Pedro, Catalina y Constanza tienen IDs 2, 3 y 4):

```json
{ 
  "title": "Pizzas", 
  "debts": [ 
    { "user_id": 2 }, 
    { "user_id": 3 }, 
    { "user_id": 4 } 
  ], 
  "datetime": "2024-10-29T19:07:46", 
  "amount": 20000 
}
```

## Requerimientos

1. **Inicialización de login**
   - Crea un usuario inicial para el sistema e intenta iniciar sesión. ¿No funciona el inicio de sesión? Descubre por qué.
   - Adicionalmente, añade un nuevo campo a la tabla de usuarios que registre el último login del usuario (este campo debe rellenarse automáticamente y no debe ser editable por el usuario).

2. **Cambio de contraseña**
   - Implementa un endpoint que permita a un usuario cambiar su propia contraseña. El endpoint debe tener la ruta `/accounts/users/me/change-password`. Este endpoint debe requerir la contraseña actual y la nueva contraseña, y sólo cambiarla si la nueva no es igual a cualquiera de las últimas 3 contraseñas utilizadas por el usuario.

3. **Actualización de gastos**
   - El endpoint para modificar los gastos sólo permite editar detalles básicos (título, descripción, etc), pero no las deudas asociadas. Implementa esta opción.

4. **Pago de deuda**
   - Implementa un endpoint que permita pagar deudas. La ruta debe ser `/expenses/expenses/{id}/pay`. El sistema debe reconocer al usuario que tiene iniciada sesión, verificar si tiene deuda asociada a ese gasto y pagarla en caso de que exista tal deuda.

5. **Estado de gastos**
   - Agrega el campo `status` a la tabla de gastos. Este campo debe reflejar el estado del gasto (si tiene deudas pendientes o no). El estado debe cambiar automáticamente cuando se paguen todas las deudas asociadas al gasto. Una buena alternativa puede ser usar `Enum`.

6. **Información asociada a usuario**
   - Modifica la respuesta de `/accounts/users/{id}` para que sólo incluya las deudas impagas y los gastos con estado pendiente. Adicionalmente, implementa los endpoints `/accounts/users/{id}/expenses` y `/accounts/users/{id}/debts`, que deben entregar la lista completa de gastos y deudas asociadas al usuario, respectivamente.

7. **Gastos con montos diferenciados**
   - Implementa una opción para que las deudas puedan ser configuradas por porcentaje. Por ejemplo:

   ```json
   { 
     "title": "Pizzas", 
     "debts": [ 
       { "user_id": 2, "percentage": 50 }, 
       { "user_id": 3 }, 
       { "user_id": 4 } 
     ], 
     "datetime": "2024-10-29T19:07:46", 
     "amount": 20000 
   }
   ``` 
   En este caso, el usuario con ID 2 pagará el 50% y el resto se repartirá entre los demás.

8. **Eliminación de gastos**
   - Implementa una opción para que exista una "papelera" de gastos, desde donde puedan ser recuperados.

9. **Actualización de duración de token JWT**
   - Modifica las propiedades del token JWT para que su duración sea de 3 horas.

10. **Verificación de estado de usuarios**
   - Al crear un nuevo gasto, no debe ser posible agregar usuarios que se encuentren desactivados.
