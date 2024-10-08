# Fazer o build da imagem
docker build . -t local/automacao:1.0

# Rodar a imagem
docker run -d -p 6901:6901 -p 5901:5901 -v /dev/shm:/dev/shm local/automacao:1.0


# Visualizar o Desktop na url:  http://ip_do_servidor:6901/vnc.html

Senha: 123Mudar


# Depois de terminar o processo o container vai teminar sozinho.


