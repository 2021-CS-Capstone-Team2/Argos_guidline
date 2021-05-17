keyboardlist_special = { 
	#오른쪽 ALT, 한/영, FN, 오른쪽 CTRL, 한자, SCROLL LOCK 인식 X
	"ESC": "", "TAB": "", "CAPS_LOCK": "", "SHIFT": "",
	"CTRL": "", "WINDOW": "", "ALT": "", "SPACE": "",
	"LAN_CHANGE": "", "FN": "", "APP": "", "HANJA": "",
	"ENTER": "", "BACKSPACE": "",
	"INSERT": "", "HOME": "", "PAGEUP": "", "PAGEDOWN": "",
	"DELETE": "", "END": "",
	"PRINTSCREEN": "", "SCROLL_LOCK": "", "PAUSE": "",
	"NUL_LOCK": "",
	"F1": "", "F2": "", "F3": "", "F4": "", "F5": "", "F6": "",
	"F7": "", "F8": "", "F9": "", "F10": "", "F11": "", "F12": "",
	"LEFT": "", "RIGHT": "", "UP": "", "DOWN": ""
}

keyboardlist_char = {
	"`":"", "-": "", "=": "",
	"Q": "", "W": "", "E": "", "R": "", "T": "",
	"Y": "", "U": "", "I": "", "O": "", "P": "", "[": "", "]": "", "\\": "",
	"A": "", "S": "", "D": "", "F": "", "G": "",
	"H": "", "J": "", "K": "", "L": "", ";": "", "\'": "",
	"Z": "", "X": "", "C": "", "V": "",	"B": "",
	"N": "", "M": "", ",": "", ".": "", "/": "",
	"*": "", "+": ""
}

keyboardlist_num = {
	"1": "", "2": "", "3": "", "4": "", "5": "",
	"6": "", "7": "", "8": "", "9": "", "0": ""
}

keyboardlist = [keyboardlist_special, keyboardlist_char]

hotkey_switch = {
	#화면 전환 단축키
	(keyboardlist_special['ALT'], keyboardlist_special['TAB']),
	(keyboardlist_special['CTRL'], keyboardlist_special['ALT'], keyboardlist_special['TAB']),
	(keyboardlist_special['ALT'], keyboardlist_special['CTRL'], keyboardlist_special['TAB']),
	(keyboardlist_special['WINDOW'], keyboardlist_special['TAB']),
	(keyboardlist_special['ALT'], keyboardlist_special['ESC'])
}


hotkey_window = {
	#윈도우 가상 데스크탑 관련 단축키
	(keyboardlist_special['WINDOW'], keyboardlist_special['CTRL'], keyboardlist_char['D']),
	(keyboardlist_special['WINDOW'], keyboardlist_special['CTRL'], keyboardlist_special['RIGHT']),
	(keyboardlist_special['CTRL'], keyboardlist_special['WINDOW'], keyboardlist_special['RIGHT']),
	(keyboardlist_special['WINDOW'], keyboardlist_special['CTRL'], keyboardlist_special['LEFT']),
	(keyboardlist_special['CTRL'], keyboardlist_special['WINDOW'], keyboardlist_special['LEFT'])
}


hotkey_move = {
	#대화 상자 단축키(탭 사용 프로그램에서 사용)
	(keyboardlist_special['CTRL'], keyboardlist_special['TAB']),
	(keyboardlist_special['CTRL'], keyboardlist_special['PAGEDOWN']),
	(keyboardlist_special['CTRL'], keyboardlist_special['PAGEUP']),
	(keyboardlist_special['CTRL'], keyboardlist_special['SHIFT'], keyboardlist_special['TAB']),
	(keyboardlist_special['SHIFT'], keyboardlist_special['CTRL'], keyboardlist_special['TAB']),
	(keyboardlist_special['CTRL'], keyboardlist_num['1']),
	(keyboardlist_special['CTRL'], keyboardlist_num['2']),
	(keyboardlist_special['CTRL'], keyboardlist_num['3']),
	(keyboardlist_special['CTRL'], keyboardlist_num['4']),
	(keyboardlist_special['CTRL'], keyboardlist_num['5']),
	(keyboardlist_special['CTRL'], keyboardlist_num['6']),
	(keyboardlist_special['CTRL'], keyboardlist_num['8']),
	(keyboardlist_special['CTRL'], keyboardlist_num['7']),
	(keyboardlist_special['CTRL'], keyboardlist_num['9']),
}

hotkey_size = {
	#창 크기 관련 단축키
	(keyboardlist_special['WINDOW'], keyboardlist_special['RIGHT']),
	(keyboardlist_special['WINDOW'], keyboardlist_special['LEFT']),
	(keyboardlist_special['WINDOW'], keyboardlist_special['UP']),
	(keyboardlist_special['WINDOW'], keyboardlist_special['DOWN']),
	(keyboardlist_special['WINDOW'], keyboardlist_special['HOME']),
	(keyboardlist_special['WINDOW'], keyboardlist_special['SHIFT'], keyboardlist_special['RIGHT']),
	(keyboardlist_special['WINDOW'], keyboardlist_special['SHIFT'], keyboardlist_special['LEFT']),
	(keyboardlist_special['SHIFT'], keyboardlist_special['WINDOW'], keyboardlist_special['RIGHT']),
	(keyboardlist_special['SHIFT'], keyboardlist_special['WINDOW'], keyboardlist_special['LEFT'])
}

hotkey_capture = {
	#캡쳐 관련 단축키
	(keyboardlist_special['WINDOW'], keyboardlist_special['SHIFT'], keyboardlist_char['S']),
	(keyboardlist_special['SHIFT'], keyboardlist_special['WINDOW'], keyboardlist_char['S']),
	(keyboardlist_special['PRINTSCREEN']),
	(keyboardlist_special['WINDOW'], keyboardlist_char['G'])
}

hotkey_work_hand = {
	#수기일 때만 check
	(keyboardlist_special['CTRL'], keyboardlist_char['X']),
	(keyboardlist_special['CTRL'], keyboardlist_char['C']),
	(keyboardlist_special['CTRL'], keyboardlist_char['V']),
	(keyboardlist_special['CTRL'], keyboardlist_char['A']),
	(keyboardlist_special['CTRL'], keyboardlist_char['Z'])
}

hotkey_work_digital = {
	#워드로 작성할 때만 check
	(keyboardlist_special['CTRL'], keyboardlist_char['X']),
	(keyboardlist_special['CTRL'], keyboardlist_char['C']),
	(keyboardlist_special['CTRL'], keyboardlist_char['V']),
	(keyboardlist_special['CTRL'], keyboardlist_char['A'])
}

hotkey_open = {
	#새로운 창을 여는 단축키
	(keyboardlist_special['CTRL'], keyboardlist_special['ESC']),
	(keyboardlist_special['CTRL'], keyboardlist_special['SHIFT'], keyboardlist_special['ESC']),
	(keyboardlist_special['SHIFT'], keyboardlist_special['CTRL'], keyboardlist_special['ESC']),
	(keyboardlist_special['WINDOW'], keyboardlist_char['E']), #탐색기
	(keyboardlist_special['WINDOW'], keyboardlist_char['V']), #클립보드
}