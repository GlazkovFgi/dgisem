for messages_count in range(0,21):
    if messages_count == 0:
        print('У вас нет сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count <= 4:
        print('У вас',messages_count,'новое сообщение')
    elif messages_count >4: 
        print('У вас',messages_count,'новых сообщений')