# Configuration and integration

[Español](CONFIGURATION.es.md) · [Back to README](../README.md)

## Dependencies

```sh
# Fedora
sudo dnf install gcc make python3 wayland-devel
# Ubuntu / Debian with a recent GCC
sudo apt install build-essential python3 libwayland-dev
# Arch
sudo pacman -S base-devel python wayland
```

## Keyboard access

Run `~/.local/bin/mascot-find-devices` to identify your keyboard. If automatic discovery fails, set `keyboard_device=/dev/input/by-id/YOUR-KEYBOARD-event-kbd` in your config, using the actual path. The process needs read access to that device; installation does not grant it automatically.

On distributions using the `input` group, `sudo usermod -aG input "$USER"` followed by logging out and back in grants access. That group can read keyboard events for the whole session. Keep `enable_debug=0` to avoid logging keycodes.

## Size, position and monitors

Start from `mascot.conf.example`, copied to `~/.config/wayland-mascots/config`:

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

Use `--list-monitors` to find output names before setting `monitor`. Keep `overlay_height` large enough for the mascot and its vertical offset. The surface remains fixed relative to the selected monitor; reserve an unused area beside your bar. A second instance shares the engine's existing single-instance control: it is not an independent pet.

## Autostart

For Hyprland versions using Lua, add this to your existing startup configuration (or put the command inside an existing startup callback):

```lua
hl.on("hyprland.start", function()
    hl.exec_cmd("~/.local/bin/wayland-mascot --config ~/.config/wayland-mascots/config --watch-config")
end)
```

For Sway, add to `~/.config/sway/config`:

```text
exec ~/.local/bin/wayland-mascot --config ~/.config/wayland-mascots/config --watch-config
```

Examples follow the [Hyprland sample](https://github.com/hyprwm/Hyprland/blob/main/example/hyprland.lua) and [Sway config manual](https://github.com/swaywm/sway/blob/master/sway/sway.5.scd). Other compositors need layer-shell support and their own startup configuration.

## Diagnose and control

```sh
~/.local/bin/wayland-mascot --config ~/.config/wayland-mascots/config --check-config
~/.local/bin/wayland-mascot --config ~/.config/wayland-mascots/config --doctor
~/.local/bin/wayland-mascot --list-monitors
~/.local/bin/wayland-mascot --list-devices
```

`--hide`, `--show`, `--pause`, `--resume`, `--reload` and `--status` control the running instance. An invalid config reload preserves the last valid configuration.

To change art, run `make mascot MASCOT=hacker`, then `make install-user` and restart the mascot. To restore upstream art, run `make embed-assets && make release`, then reinstall and restart.

## Reproduce the GIF previews

With ImageMagick installed, run `python3 scripts/render_previews.py`. This renders the existing SVG poses; ImageMagick is not a build or runtime dependency.
