# Wayland Mascots

[English](README.md)

Mascotas pequeñas que reaccionan al teclado en escritorios Linux Wayland con layer-shell. Fork de [wayland-bongocat](https://github.com/saatvik333/wayland-bongocat), con cuatro paquetes incluidos.

| `minimal` | `hacker` | `maintenance` | `archivist` |
| --- | --- | --- | --- |
| ![Minimal](assets/mascots/minimal/preview.gif) | ![Hacker](assets/mascots/hacker/preview.gif) | ![Maintenance](assets/mascots/maintenance/preview.gif) | ![Archivist](assets/mascots/archivist/preview.gif) |

## Instalación

Requiere GCC compatible con C23, Make, Python 3 y bibliotecas de desarrollo de Wayland. En Fedora: `sudo dnf install gcc make python3 wayland-devel`. [Otras distribuciones](docs/CONFIGURATION.es.md#dependencias).

```sh
git clone https://github.com/Naraku86/wayland-mascots.git
cd wayland-mascots
make mascot MASCOT=minimal
make install-user
mkdir -p ~/.config/wayland-mascots
cp mascot.conf.example ~/.config/wayland-mascots/config
~/.local/bin/wayland-mascot --config ~/.config/wayland-mascots/config --watch-config
```

Elige un nombre de la tabla con `MASCOT=...`; cambiar de paquete requiere recompilar y reinstalar. Se instala en `~/.local/bin` sin sudo. Para reaccionar al teclado necesita acceso de lectura al dispositivo; consulta los [permisos](docs/CONFIGURATION.es.md#acceso-al-teclado).

## Configuración e integración

Edita `~/.config/wayland-mascots/config`: `cat_height` controla el tamaño, `cat_align` y los offsets ajustan la posición, y `monitor` selecciona una pantalla. `--watch-config` recarga los cambios.

La mascota es una superficie independiente. Reserva espacio junto a la barra; no sigue el ancho cambiante de los módulos de Waybar. [Inicio automático, pantallas y diagnóstico](docs/CONFIGURATION.es.md).

## Desarrollo y licencia

Ejecuta `make test-mascots` y `make test`. Consulta la [revisión y validación](VALIDATION.md) y la [arquitectura del motor](ARCHITECTURE.md). Los GIFs muestran las poses existentes; no son grabaciones del escritorio.

MIT; se conservan los avisos del proyecto original y NanoSVG. [Procedencia del arte](ARTWORK.md) · [Documentación original](README.upstream.md).
