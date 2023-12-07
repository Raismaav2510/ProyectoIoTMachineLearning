import getData
import RefineData
import NeuralNetwork

# Importar datos desde el sitio web
# getData.datos_climaticos()

# Refinado de información
# RefineData.datos_refinados()

# Entrenamiento de la red neuronal
# NeuralNetwork.training(model_name='model_extra.pth')
NeuralNetwork.print_plots()
NeuralNetwork.predict()

# Evaluar datos nuevos
print(NeuralNetwork.eval_data([8, 30.5, 0], rounded=True))
