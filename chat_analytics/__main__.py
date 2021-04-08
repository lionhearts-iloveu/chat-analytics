from chat_analytics.app.app import app
from chat_analytics.services.chat_analytics import analise_chat


def main():
    # analise_chat()
    app.run_server(debug=True)


if __name__ == '__main__':
    main()
