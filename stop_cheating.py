from const_keyboard import *

CHEAT_TAG = { "CHEATING": -1, "SUSPICION": 1, "NORMAL": 0 }
TOTAL_SCORE = 0
TOTAL_FLAG = False


def score_cheating () :
	if(hotkey_switch / 4) : #화면 전환 5번 이상 - 의심
		TOTAL_SCORE += CHEAT_TAG['SUSPICION']

	if(hotkey_size / 4) : #화면 크기 전환 5번 이상 - 의심
		TOTAL_SCORE += CHEAT_TAG['SUSPICION']

	if(hotkey_move / 10) : #화면 이동 10회 이상 - 의심
		TOTAL_SCORE += CHEAT_TAG['SUSPICION']

	if(hotkey_open / 5) : #시작, 작업 관리자 5회 이상 - 의심
		TOTAL_SCORE += CHEAT_TAG['SUSPICION']


def define_cheating() :
	if(hotkey_window >= 1) : #윈도우 가상 데스크탑 1번 이상 - 부정행위
		TOTAL_FLAG = True

	if(hotkey_capture >= 1) : #화면 캡쳐 1번 이상 - 부정행위
		TOTAL_FLAG = True