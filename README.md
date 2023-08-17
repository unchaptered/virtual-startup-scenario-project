# Virtual Startup Scenario Project

_모든 명칭 및 묘사는 가상의 스타트업 (주) PicTech를 전제로 작성되었습니다._

`PicTech`는 주요 고객들로부터 서비스 성능에 대한 항의를 받고 있습니다.<br>
이에 문제지점을 파악하고 서버 구성 및 아키텍처를 변경하여 이를 해결하고자 합니다.

## Trouble : 서버 병목 현상 발생

`PicAI`는 최근 시리즈 A 투자를 받은 (주) PicTech에서 만든, 이미지 분석 서비스입니다.

PicAI는 수개월 간 고객이 증가해 **DAU 1,000** 정도가 유지되고 있습니다. <br>
PicAI Product Team은 아래 통계에 근거하여 **DAU 11,000+** 정도까지 서버 여유를 예상했습니다.

| 기준                | 값         |
| :------------------ | :--------- |
| 인당, 일일 요청량   | 16.32 장   |
| 전체, 일일 요청량   | 16320 장   |
| 장당 요청 처리 시간 | 2 초       |
| 전체 요청 처리 시간 | 9 시간 2분 |

하지만 최대 고객인 Otawa씨에게서 이미지 분석이 너무 느리다는 컴플레인이 들어오게 되었습니다.<br>
그 중에서도 특히 **오후 00:00 ~ 오후 03:00** 동안 서버 전체가 느려진다는 응답도 듣게 되었습니다

| 오전 / 오후 | 시간대                  | 이미지 요청량 | 이미지 처리 시간 | 요청량 비율 (%) | CPU (%) | MEM (%) |
| ----------- | ----------------------- | ------------- | ---------------- | --------------- | ------- | ------- |
| 오전        | 오전 00:01 ~ 오전 03:00 | 200 장        | 6분 40초         | 1.23            | 10      | 10      |
| 오전        | 오전 03:01 ~ 오전 06:00 | 40 장         | 1분 20초         | 0.25            | 5       | 5       |
| 오전        | 오전 06:01 ~ 오전 09:00 | 1200 장       | 40분             | 7.35            | 30      | 30      |
| 오전        | 오전 09:01 ~ 오전 12:00 | 1600 장       | 53분 20초        | 9.80            | 40      | 40      |
| 오후        | 오후 00:01 ~ 오후 03:00 | 5800 장       | 3시간 13분 20초  | 35.54           | 80      | 80      |
| 오후        | 오후 03:01 ~ 오후 06:00 | 4480 장       | 2시간 29분 20초  | 27.45           | 70      | 70      |
| 오후        | 오후 06:01 ~ 오후 09:00 | 2400 장       | 1시간 20분       | 14.71           | 50      | 80      |
| 오후        | 오후 09:01 ~ 오후 12:00 | 600 장        | 20분             | 3.68            | 15      | 25      |
|             |                         | 16320 장      | 9시간 2분        | 100             |         |         |

PicAI의 주요 사용 시간대는 **평일 오후 00:01 ~ 06:00**으로 밝혀졌습니다. <br>
해당 시간대에 많은 양의 이미지 분석이 진행되며, 일반 REST API 요청에도 영향이 간 것으로 보여졌습니다.
