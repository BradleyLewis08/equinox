from trello import TrelloClient

client = TrelloClient(
    api_key='c3e4ba7980190d03ef60b6d81cf791ba',
    api_secret='707de4a655a730aeaf14d62e7ef7036fe81844f7dd3617c9b2ef5b8fb0ef047c',
    token='96a09cbdbcb3ba068877762d3be63089581c3faefab21bf314505a7db4f7883f'
)


def get_tasks():
    current_board = client.list_boards()[0]
    lists(current_board[0].list_lists())
    for card in 