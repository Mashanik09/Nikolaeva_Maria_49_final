#Николаева Мария 49 когорта. Финальный проект инженер по тестированию расширенный

import data
import sendor_stand_request

def test_check_order_by_track():
    create_response = sendor_stand_request.post_order(data.order_body)
    track = create_response.json()['track']
    receive_response = sendor_stand_request.get_order(track)
    assert receive_response.status_code == 200
