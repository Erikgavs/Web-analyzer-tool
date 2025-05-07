# SCRIPT DISEÑADO CON EL PROPOSITO DE ANALIZAR DE VULNERABILIDADES (NIKTO) Y TECNOLOGÍAS (WHATWEB) DE UNA PÁGINA WEB
# DISEÑADO CON EL OBJETIVO DE USARSE EN CTF'S Y ENTORNOS CONTROLADOS
# IMPORTANTE NO HACER USO DE LA HERRAMIENTA EN ENTORNOS REALES, SOLO USARLO EN ENTORNOS CONTROLADOS

import os
import subprocess

webs = input("Url de la página web que deseas analizar").strip()

validar_wp = input("La página web es un WordPress? (s/n): ").strip().lower()

if validar_wp == "s":
    print(f"Ejecutando WPScan en la página específicada {webs}:...")
    subprocess.run(["wpscan", "--url", webs])
else:
    print(f"Analizando tecnologías de la web específicada con whatweb: {webs}...")
    subprocess.run(["whatweb", webs])

    print(f"En busca de vulnerabilidades en la web específicada con nikto: {webs}...")
    subprocess.run(["nikto", "-h", webs])