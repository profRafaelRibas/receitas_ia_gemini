from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as gemini

# Cria a aplicação Flask
app = Flask(__name__)
# Habilita CORS para a aplicação
CORS(app)

gemini.configure(api_key="Sua chave API Gemini vai aqui")

model = gemini.GenerativeModel('gemini-1.5-flash')

# Rota para cadastro de produtos
@app.route('/receita', methods=['POST'])
def make_receita():
    try:
        
        # Recebe os dados em formato JSON da requisição
        dados = request.json
        ingredientes = dados.get('ingredientes')
        # Define a prompt para o modelo Gemini
        
        prompt = f"""
        Crie uma receita somente com os seguintes ingredientes: {ingredientes}. 
        Apresente a receita no formato html com codificação UTF-8, sem o header, com o título em h1, subtítulos em h2, tempo de preparo em parágrafo, rendimento em porções em parágrafo, a lista de ingredientes em lista não ordenada, modo de preparo com passos em lista ordenada, sugestão para servir em parágrafo.
        """

        resposta = model.generate_content(prompt)
        print(resposta)
        
        # Extrai a receita do texto da resposta
        receita = resposta.text.strip().split('\n')
        return jsonify(receita), 200
    except Exception as e:
        return jsonify({"Erro": str(e)}), 300
    

# Inicia a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)

    