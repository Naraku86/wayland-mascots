# Validación inicial

En Fedora 44 se compilaron con éxito los cuatro paquetes en modo release y se verificó la instalación de usuario en un directorio temporal. `make test-mascots`, la validación estricta de `mascot.conf.example` y los tests del motor pasaron. Los tests de IPC requieren que el entorno permita sockets locales.

No se completó localmente `make format-check`: faltan clang-format y sus bibliotecas compartidas. `make clean && make debug` compiló los objetos pero falló al enlazar porque falta libasan.so.8.0.0. La CI instala las dependencias de desarrollo y ejecuta formato, debug y tests con sanitizadores; sus resultados deben consultarse antes de considerar esas verificaciones completas.

No se cambió la lógica C del motor. No se ha verificado cada paquete en una sesión gráfica independiente ni los paquetes Nix localmente. La instalación de prueba no reemplazó la mascota activa del escritorio.
