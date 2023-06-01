#Crie um códgo em Python que teste se o site Pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://google.com')
except urllib.error.URLError:
    print('O site Google não está acessível no momento.')
else:
    print('O site Google foi acessado com sucesso.')
    #print(site.read()) #lê o conteúdo html do site