# EvilTwin-PortalFramework

**EvilTwin-PortalFramework** es una herramienta automatizada en Python diseñada para el despliegue de entornos controlados de auditoría inalámbrica y simulación de ataques de red (*Rogue AP* y *Man-in-the-Middle*). Este proyecto fue desarrollado con fines estrictamente académicos y de investigación.

La herramienta unifica la configuración de servicios esenciales del sistema en Linux para estudiar cómo los dispositivos móviles interactúan con portales cautivos falsos y cómo se comporta el enrutamiento de tráfico en redes inseguras.

## 🚀 Características
- **Modo Portal Cautivo:** Secuestro de tráfico DNS/HTTP local para mostrar una interfaz de autenticación institucional simulada (Phishing ético).
- **Modo Enrutamiento Real:** Configuración automática de IP Forwarding y reglas NAT mediante `nftables` para interceptar tráfico en tránsito.
- **Automatización de Infraestructura:** Gestión automática de interfaces de red, asignación de direccionamiento estático y orquestación de `hostapd` y `dnsmasq`.
- **Limpieza Segura:** Restauración total de la configuración del sistema, del cortafuegos y eliminación de archivos temporales al finalizar (`Ctrl+C`).

## 📋 Requisitos del Sistema
Para ejecutar este script, tu entorno debe cumplir con los siguientes requisitos:
- **Sistema Operativo:** Linux (probado en distribuciones basadas en Debian/Kali Linux).
- **Hardware:** Una tarjeta de red WiFi externa que soporte **Modo Monitor** y **Modo AP (Access Point)**.
- **Dependencias del Sistema:**
  ```bash
  sudo apt update
  sudo apt install hostapd dnsmasq nftables network-manager coreutils
  ```
- **Privilegios:** Es obligatorio ejecutar la herramienta con permisos de superusuario (`sudo`).

## 🔧 Instalación y Uso

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://Cyb3rPh4nt0n/EvilTwin-PortalFramework/
   cd EvilTwin-PortalFramework
   ```

2. Dale permisos de ejecución al script principal:
   ```bash
   chmod +x EvilTwin-PortalFramework.py
   ```

3. Ejecuta la herramienta:
   ```bash
   sudo python3 EvilTwin-PortalFramework.py
   ```

## 🛠️ Detalles Técnicos (Arquitectura)
La herramienta automatiza el flujo de trabajo interactuando con los siguientes componentes del Kernel y espacio de usuario en Linux:
- `hostapd`: Generación de la capa física y de enlace de la señal WiFi (SSID, canal, seguridad abierta/WPA2).
- `dnsmasq`: Servidor DHCP integrado para la asignación dinámica de IPs en el rango académico y resolución DNS falsificada.
- `Python HTTPServer`: Servidor web ligero nativo que procesa peticiones HTTP e intercepta los datos enviados por los formularios de prueba.
- `nftables`: Filtrado de puertos críticos (53 UDP, 67/68 UDP) y enmascaramiento de red (*Masquerade*).

## ⚠️ Descargo de Responsabilidad (Disclaimer)
Este software ha sido creado exclusivamente con fines educativos, de auditoría autorizada y de investigación académica. El uso de esta herramienta contra redes o dispositivos sin el consentimiento previo y explícito del propietario es ilegal. El autor no se hace responsable del mal uso de este código ni de los daños que puedan derivarse de su utilización.
