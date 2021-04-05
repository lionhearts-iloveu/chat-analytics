from chat_analytics.services.chat_analytics import load_chat, analise_chat


def main():
    chat = load_chat()
    analise_chat(chat)


if __name__ == '__main__':
    main()
