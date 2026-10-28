import os
import shutil

def organizar_pasta(caminho_pasta):
    pastas_destino = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Instaladores': ['.exe', '.msi'],
        'Arquivos_Compactados': ['.zip', '.rar', '.7z']
    }

    if not os.path.exists(caminho_pasta):
        print(f"Erro: O diretório '{caminho_pasta}' não foi encontrado.")
        return

    print(f"Iniciando organização na pasta: {caminho_pasta}")
    
    for arquivo in os.listdir(caminho_pasta):
        caminho_arquivo_completo = os.path.join(caminho_pasta, arquivo)
        
        if os.path.isdir(caminho_arquivo_completo):
            continue
            
        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()
        
        moveu = False
        
        try:
            for nome_pasta, extensoes_validas in pastas_destino.items():
                if extensao in extensoes_validas:
                    pasta_destino_completa = os.path.join(caminho_pasta, nome_pasta)
                    if not os.path.exists(pasta_destino_completa):
                        os.makedirs(pasta_destino_completa)
                        
                    caminho_final = os.path.join(pasta_destino_completa, arquivo)
                    shutil.move(caminho_arquivo_completo, caminho_final)
                    print(f"Movido: {arquivo} --> {nome_pasta}")
                    moveu = True
                    break 
                    
            if not moveu:
                pasta_outros = os.path.join(caminho_pasta, 'Outros')
                if not os.path.exists(pasta_outros):
                    os.makedirs(pasta_outros)
                shutil.move(caminho_arquivo_completo, os.path.join(pasta_outros, arquivo))
                print(f"Movido para 'Outros': {arquivo}")
                
        except PermissionError:
            print(f"Aviso: O arquivo '{arquivo}' está em uso pelo sistema e foi ignorado.")
        except Exception as e:
            print(f"Erro inesperado ao mover '{arquivo}': {e}")

    print("Organização concluída com sucesso!")

if __name__ == "__main__":
    pasta_alvo = input("Digite o caminho completo da pasta que deseja organizar: ")
    organizar_pasta(pasta_alvo)