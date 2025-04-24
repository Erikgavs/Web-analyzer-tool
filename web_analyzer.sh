# SCRIPT DISEÑADO CON EL PROPOSITO DE ANALIZAR DE VULNERABILIDADES (NIKTO) Y TECNOLOGÍAS (WHATWEB) DE UNA PÁGINA WEB
# DISEÑADO CON EL OBJETIVO DE USARSE EN CTF'S Y ENTORNOS CONTROLADOS

read -p "Específica la URL de la página web que deseas escanear: " webs

echo "Analízando tecnologías de la página específicada: $webs..."
whatweb "$webs"

echo "En busca de vulnerabilidades de la página específicada: $webs..."
nikto -url "$web"