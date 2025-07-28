from django.shortcuts import render, redirect

def check_win(board, player):
    size = len(board)
    # 横チェック
    for y in range(size):
        for x in range(size - 4):
            count = 0
            for i in range(5):
                if board[y][x + i] == player:
                    count += 1
                else:
                    break
            if count == 5:
                return True

    # 縦チェック (実装せよ)

    # 斜めチェック 右下方向
    for y in range(size - 4):
        for x in range(size - 4):
            count = 0
            for i in range(5):
                if board[y + i][x + i] == player:
                    count += 1
                else:
                    break
            if count == 5:
                return True

    # 斜めチェック 右上方向 (実装せよ)


    return False

def gomoku_view(request):
    size = 9
    message = ''
    current_turn = 'X' if request.POST.get('turn') == 'O' else 'O'

    # リセットボタンが押されたらGETにリダイレクト（初期化）
    if request.method == 'POST' and 'reset' in request.POST:
        return redirect('/')

    board = [['' for _ in range(size)] for _ in range(size)]

    if request.method == 'POST' and 'reset' not in request.POST:
        # POSTデータから盤面復元
        for y in range(size):
            for x in range(size):
                cell_key = f'cell_{y}_{x}'
                board[y][x] = request.POST.get(cell_key, '')

        row = int(request.POST.get('row'))
        col = int(request.GET.get('col'))

        if board[row][col] == '' and not message:
            board[row][col] = current_turn
            if check_win(board, current_turn):
                message = f'{current_turn}の勝ち！'
            else:
                message = ''

    return render(request, 'index.html', {
        'board': board,
        'turn': current_turn if not message else '',
        'message': message,
    })
