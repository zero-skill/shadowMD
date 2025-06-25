# ShadowMD

**ShadowMD** es un editor de Markdown para terminal que protege tu privacidad visual ofuscando el contenido mientras escribes.

## Características

- Edición de archivos Markdown (`.md`) directamente desde la terminal.
- Ofuscación visual: mientras escribes, el contenido se muestra con caracteres aleatorios para evitar que alguien vea lo que escribes.
- Solo la línea actual es visible claramente, pero puedes alternar la visibilidad para mostrar todo el texto o ocultarlo completamente.
- Navegación fácil con flechas arriba y abajo para moverte entre líneas.
- Guardado seguro con atajo `Ctrl+G`.
- Modo sólo lectura para ver archivos sin editar.
- Compatible con rutas absolutas, relativas y con `~` (home).
- Opción para mostrar el contenido real al guardar mediante el flag `-v` o `--verbose`.

## Requisitos

- Python 3
- Módulo `readchar` (instalar con `pip install readchar`)

## Instalación

1. Clona este repositorio o descarga el script `shadowmd.py`.
2. Instala la dependencia:

```bash
pip install readchar
```
## Uso
```bash
python shadowmd.py [ruta_al_archivo.md] [opciones]
```
## Opciones
```text
Opción	Descripción
-v, --verbose	Mostrar contenido real al finalizar edición
--readonly	Abrir archivo en modo sólo lectura (sin edición)
```

## Ejemplos
### Editar archivo:

```bash
python shadowmd.py ~/notas/diario.md
```
### Editar archivo y mostrar contenido real al terminar:

```bash
python shadowmd.py ~/notas/diario.md -v
```
### Ver archivo sin editar:

```bash
python shadowmd.py ~/notas/diario.md --readonly
```

## Controles dentro del editor
- `ENTER`: Nueva línea

- `BACKSPACE`: Borrar caracteres

- `Flechas ↑ ↓`: Navegar entre líneas

- `Ctrl+T`: Alternar visibilidad (solo línea actual / todo visible / todo oculto)

- `Ctrl+G`: Guardar y salir

## ¿Por qué ShadowMD?
Cuando estás en lugares públicos o compartidos, escribir contenido sensible en la terminal puede ser un riesgo. ShadowMD ofusca tu texto para que nadie pueda leerlo a simple vista, manteniendo la usabilidad de un editor Markdown completo.


