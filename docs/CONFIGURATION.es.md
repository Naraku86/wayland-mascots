# Configuración e integración

[English](CONFIGURATION.md) · [Volver al README](../README.es.md)

## Dependencias

```sh
# Fedora
sudo dnf install gcc make python3 wayland-devel
# Ubuntu / Debian con GCC reciente
sudo apt install build-essential python3 libwayland-dev
# Arch
sudo pacman -S base-devel python wayland
```

## Acceso al teclado

Ejecuta `~/.local/bin/mascot-find-devices` para identificar el teclado. Si la detección automática falla, configura `keyboard_device=/dev/input/by-id/YOUR-KEYBOARD-event-kbd` con la ruta real. El proceso necesita acceso de lectura; la instalación no lo concede automáticamente.

En distribuciones que usan el grupo `input`, `sudo usermod -aG input "$USER"` seguido de cerrar sesión y volver a entrar concede acceso. Ese grupo puede leer eventos del teclado durante toda la sesión. Mantén `enable_debug=0` para evitar registrar códigos de teclas.

## Tamaño, posición y pantallas

Parte de `mascot.conf.example`, copiado a `~/.config/wayland-mascots/config`:

```ini
cat_height=64
cat_align=right
cat_x_offset=24
cat_y_offset=0
overlay_height=72
overlay_position=top
overlay_opacity=0
layer=overlay
# monitor=eDP-1
```

Usa `--list-monitors` para consultar los nombres antes de configurar `monitor`. Ajusta `overlay_height` para que quepan la mascota y su desplazamiento vertical. La superficie conserva su posición respecto a la pantalla; reserva una zona libre junto a la barra. Una segunda instancia comparte el control de instancia única del motor: no es otra mascota independiente.

## Inicio automático

En versiones de Hyprland con Lua, agrega esto a tu configuración de inicio, o incluye el comando dentro del callback que ya tengas:

```lua
hl.on("hyprland.start", function()
    hl.exec_cmd("~/.local/bin/wayland-mascot --config ~/.config/wayland-mascots/config --watch-config")
end)
```

En Sway, agrega a `~/.config/sway/config`:

```text
exec ~/.local/bin/wayland-mascot --config ~/.config/wayland-mascots/config --watch-config
```

Los ejemplos siguen la [configuración de Hyprland](https://github.com/hyprwm/Hyprland/blob/main/example/hyprland.lua) y el [manual de Sway](https://github.com/swaywm/sway/blob/master/sway/sway.5.scd). Otros compositores requieren layer-shell y su propia configuración de inicio.

## Diagnóstico y control

```sh
~/.local/bin/wayland-mascot --config ~/.config/wayland-mascots/config --check-config
~/.local/bin/wayland-mascot --config ~/.config/wayland-mascots/config --doctor
~/.local/bin/wayland-mascot --list-monitors
~/.local/bin/wayland-mascot --list-devices
```

`--hide`, `--show`, `--pause`, `--resume`, `--reload` y `--status` controlan la instancia activa. Una recarga inválida conserva la última configuración válida.

Para cambiar el dibujo, ejecuta `make mascot MASCOT=hacker`, después `make install-user` y reinicia la mascota. Para recuperar el gato original: `make embed-assets && make release`, reinstala y reinicia.

## Regenerar los GIFs

Con ImageMagick instalado, ejecuta `python3 scripts/render_previews.py`. Renderiza las poses SVG existentes; ImageMagick no es necesario para compilar ni ejecutar la mascota.
