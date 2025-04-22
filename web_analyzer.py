# SCRIPT DISEÑADO CON EL PROPOSITO DE ANALIZAR DE VULNERABILIDADES (NIKTO) Y TECNOLOGÍAS (WHATWEB) DE UNA PÁGINA WEB
# DISEÑADO CON EL OBJETIVO DE USARSE EN CTF'S Y ENTORNOS CONTROLADOS
import os
import subprocess

webs = input("Url de la página web que deseas analizar")

print(f"Analizando tecnologías de la web específicada con whatweb: {webs}...")
subprocess.run(["whatweb", webs])

print(f"En busca de vulnerabilidades en la web específicada con nikto: {webs}...")
subprocess.run(["nikto", "-url", webs])