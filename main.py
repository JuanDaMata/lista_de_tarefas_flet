import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"

    campo_tarefa = ft.TextField(label = "Nome da Tarefa")

    titulo_tarefas = ft.Text()

    lista_tarefas = ft.Column()

    mensagem_erro = ft.Text()
    
    def adicionar_tarefa(event):
        if campo_tarefa.value:
            titulo_tarefas.value = "📋 Lista de Tarefas"
            titulo_tarefas.size = 18
            titulo_tarefas.weight = "bold"

            lista_tarefas.controls.append(
                ft.Row(
                    controls = [
                        ft.Text("•"),
                        ft.Text(campo_tarefa.value, size=16)
                    ]
                )
            )
            campo_tarefa.value = ""
            mensagem_erro.value = ""
        else:
            mensagem_erro.value = "Você precisa digitar o nome da tarefa para adicioná-la!"
            mensagem_erro.color = "red"

        page.update()

    botao_adicionar = ft.Button("Adicionar", on_click=adicionar_tarefa)


    page.add(
        campo_tarefa,
        botao_adicionar,
        titulo_tarefas,
        lista_tarefas,
        mensagem_erro
    )

ft.run(main)