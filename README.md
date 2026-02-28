# SERVICIOS_DEL_NUCLEO_DE_LINUX
# Tarea – Servicios del Núcleo de Linux (systemd)

**Estudiante:** Maria Cuadros  
**Sistema Operativo:** Debian  
**Docente:** Juan Bernardo Gomez Mendoza  

---

# Introducción

En esta práctica se implementaron dos ejemplos de servicios del núcleo de Linux utilizando `systemd`.  
El objetivo fue comprender cómo el sistema operativo gestiona procesos en segundo plano (daemons) y cómo pueden automatizarse tareas mediante servicios personalizados.

Se desarrollaron:

1. Un servicio en Bash que monitorea el uso de la memoria RAM cada 15 segundos.
2. Un servicio web implementado en Python utilizando Flask.

---

# Ejercicio 1 – Servicio de Monitoreo de RAM

## Descripción

Se creó un script en Bash que registra el uso de la memoria RAM cada 15 segundos y guarda la información en un archivo dentro del directorio `/tmp`.

El servicio se ejecuta en segundo plano y se reinicia automáticamente si se detiene.

---

## Script Bash

**Ruta:** `/usr/local/bin/ram_monitor.sh`

```bash
#!/bin/bash

while true
do
    echo "Fecha: $(date)" >> /tmp/ram_usage.log
    free -h >> /tmp/ram_usage.log
    echo "-----------------------------" >> /tmp/ram_usage.log
    sleep 15
done
```

---

## Archivo del Servicio

**Ruta:** `/etc/systemd/system/ram_monitor.service`

```ini
[Unit]
Description=Servicio de monitoreo de RAM cada 15 segundos
After=network.target

[Service]
ExecStart=/usr/local/bin/ram_monitor.sh
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

---

## Funcionamiento

- `ExecStart` indica qué script se ejecuta.
- `Restart=always` reinicia el servicio si falla.
- `WantedBy=multi-user.target` permite que el servicio inicie con el sistema.

El archivo generado es:

```
/tmp/ram_usage.log
```

El cual almacena información periódica del uso de memoria.

---

# Ejercicio 2 – Servicio Web con Flask

## Descripción

Se implementó un servidor web utilizando Python y Flask.  
El servidor expone dos rutas:

- `/` → Mensaje de funcionamiento.
- `/ram` → Muestra el estado actual de la memoria RAM.

---

## Script Python

**Ruta:** `/usr/local/bin/app.py`

```python
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor Flask funcionando en Debian!"

@app.route("/ram")
def ram():
    return os.popen("free -h").read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## Archivo del Servicio

**Ruta:** `/etc/systemd/system/flask_app.service`

```ini
[Unit]
Description=Servidor Flask en Python
After=network.target

[Service]
ExecStart=/usr/bin/python3 /usr/local/bin/app.py
WorkingDirectory=/usr/local/bin
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

---

## Funcionamiento

- El servidor se ejecuta en el puerto 5000.
- `host="0.0.0.0"` permite acceso desde otras máquinas.
- El servicio inicia automáticamente con el sistema.
- Puede verificarse con:

```bash
systemctl status flask_app.service
```

Acceso desde navegador:

```
http://localhost:5000
```

o desde otra máquina:

```
http://IP_DEL_SERVIDOR:5000
```

---

# Comandos Utilizados

Recargar servicios:
```bash
sudo systemctl daemon-reload
```

Activar servicio:
```bash
sudo systemctl enable nombre_servicio
```

Iniciar servicio:
```bash
sudo systemctl start nombre_servicio
```

Ver estado:
```bash
sudo systemctl status nombre_servicio
```

Ver logs:
```bash
journalctl -u nombre_servicio
```

---

# Conclusiones

Se logró implementar y gestionar servicios personalizados en Debian utilizando `systemd`.  
La práctica permitió comprender:

- Cómo automatizar tareas en segundo plano.
- Cómo crear servicios persistentes.
- Cómo integrar scripts Bash y aplicaciones Python al sistema.
- Cómo administrar servicios mediante `systemctl`.

El uso de `systemd` demuestra ser una herramienta fundamental en la administración de sistemas Linux.

---

# Archivos Entregados

- `ram_monitor.sh`
- `ram_monitor.service`
- `app.py`
- `flask_app.service`
- Informe (README.md)

---