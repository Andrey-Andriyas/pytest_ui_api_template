from api.BoardApi import BoardApi

# def test_get_boards(api_client: BoardApi):
#     board_list = api_client.get_all_boards_by_org_id("6497ed5914b7ee9126e65eab")
    
#     assert len(board_list) == 5


def test_create_board(api_client: BoardApi, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_org_id("6497ed5914b7ee9126e65eab")
    resp = api_client.create_board("New_board to be deleted")
    
    delete_board["board_id"] = resp.get("id") 

    board_list_after = api_client.get_all_boards_by_org_id("6497ed5914b7ee9126e65eab")

    assert len(board_list_after) - len(board_list_before) == 1


def test_delete_board(api_client: BoardApi, dummy_board_id: str):
    board_list_before = api_client.get_all_boards_by_org_id("6497ed5914b7ee9126e65eab")
    resp = api_client.delete_board_by_id(dummy_board_id)
    
    board_list_after = api_client.get_all_boards_by_org_id("6497ed5914b7ee9126e65eab")

    assert len(board_list_before) - len(board_list_after) == 1





