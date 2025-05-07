# SCRIPT DISEÑADO CON EL PROPOSITO DE ANALIZAR DE VULNERABILIDADES (NIKTO) Y TECNOLOGÍAS (WHATWEB) DE UNA PÁGINA WEB
# DISEÑADO CON EL OBJETIVO DE USARSE EN CTF'S Y ENTORNOS CONTROLADOS
# IMPORTANTE NO HACER USO DE LA HERRAMIENTA EN ENTORNOS REALES, SOLO USARLO EN ENTORNOS CONTROLADOS

read -p "Url de la página web que deseas analizar" webs

read -p "La página web es un Wordpress? (s/n)" validar_wp

if ["$validar_wp" = "s" ]; then
echo "Ejecutando WPScan en la página específicada $webs ..."
wpscan --url "$webs"

else 
echo "Analizando la web específicada con whatweb $web ..."
whatweb "$webs"

echo "Buscando vulnerabilidades con nikto en la web esepecificada $web ..."
nikto -h "$webs"