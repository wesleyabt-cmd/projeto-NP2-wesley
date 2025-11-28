
# tree_logic.py — você edita APENAS este arquivo nesta atividade.

class Node:
    def __init__(self, question, yes=None, no=None):
        """
        Se 'yes' e 'no' forem None, este nó é uma FOLHA e 'question' guarda a decisão final (string).
        Caso contrário, 'question' é o texto da pergunta e 'yes'/'no' são seus filhos.
        """
        self.question = question
        self.yes = yes
        self.no = no

def is_leaf(node):
    return node is not None and node.yes is None and node.no is None

def navigate_tree(node, answers):
    """
    Percorre a árvore a partir de 'node' seguindo a sequência de respostas (lista de strings).
    Cada resposta deve ser 'sim' ou 'não' (aceite 'nao' como 'não').
    Retorna a decisão final (string) quando alcançar uma folha.
    Se a sequência terminar antes de chegar a uma folha, levante ValueError com dica.
    Se alguma resposta for inválida, levante ValueError com mensagem clara.
    >>> # Exemplo (não-executável aqui): navigate_tree(root, ["sim", "não"]) -> "É um pardal/pássaro diurno"
    """
    # TODO: implemente aqui. Sugestão:
    # - Enquanto o nó atual não for folha:
    #     - Se não houver mais respostas, levante ValueError("Faltam respostas para concluir a decisão.")
    #     - Pegue a próxima resposta, normalize para minúsculas, trate 'nao' como 'não'.
    #     - Se "sim": vá para node.yes; se "não": vá para node.no; senão levante ValueError("Resposta inválida: ...")
    # - Ao chegar numa folha, retorne node.question (a decisão final).
    raise NotImplementedError("Implemente a função navigate_tree.")
