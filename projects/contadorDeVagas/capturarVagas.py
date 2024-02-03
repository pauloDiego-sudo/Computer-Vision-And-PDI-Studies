#a captura é feita pela itensidade de cores na vaga
import cv2
import pickle

dataPath = 'C:/Users/Lenovo/Documents/LAPISCO/ComputerVisionStudies/Computer-Vision-And-PDI-Studies/projects/contadorDeVagas/data/'
img = cv2.imread(f'{dataPath}estacionamento.png')

vagas = [] #array contendo as posições das vagas 
#OBS: esse array será salvo em um arquivo

for x in range(69): #69 estacionamentos
    vaga = cv2.selectROI('vagas',img,False) #retira as coordenadas de cada vaga
    cv2.destroyWindow('vagas') #Destroi a window vaga
    vagas.append((vaga)) #insere as informações da vaga na lista de vagas

    #Criando um retângulo
    for x,y,w,h in vagas:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

with open(f'{dataPath}vagas.pkl','wb') as arquivo: #Cria um arquivo com a variavel Vagas
    pickle.dump(vagas,arquivo)